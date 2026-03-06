import os
import requests
import base64
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
API_ENDPOINT = "https://api.sarvam.ai/text-to-speech"
# Get API key from environment variable
API_KEY = os.getenv("SARVAM_API_KEY")

def generate_speech(text, voice, output_filename="output_audio.mp3"):
    """
    Sends text to Sarvam AI TTS API and saves the resulting audio.
    """
    if not API_KEY or API_KEY == "PASTE_YOUR_SARVAM_API_KEY_HERE":
        print("Error: SARVAM_API_KEY not found. Please set it in your .env file.")
        return False

    # Prepare headers and payload
    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "target_language_code": "te-IN",
        "speaker": voice,
        "model": "bulbul:v3",
        "output_format": "mp3"
    }

    try:
        print(f"\nGenerating audio for: {output_filename}...")
        response = requests.post(API_ENDPOINT, json=payload, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            audio_content = None
            
            if "audio_content" in data:
                audio_content = base64.b64decode(data["audio_content"])
            elif "audios" in data and isinstance(data["audios"], list) and len(data["audios"]) > 0:
                # Concatenate multiple audio chunks if returned
                audio_content = b"".join([base64.b64decode(a) for a in data["audios"]])
            
            if audio_content:
                # Save the audio
                with open(output_filename, "wb") as audio_file:
                    audio_file.write(audio_content)
                
                print("Audio generated successfully.")
                print(f"Saved as {output_filename}")
                return True
            else:
                print("Error: Invalid response format from API (missing audio content).")
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: Network issues occurred: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
    return False

def main():
    """
    Main function to handle user interaction or command line arguments.
    """
    # Check for command line arguments (usage: python tts_cli.py "text" "voice" "filename")
    if len(sys.argv) > 1:
        if len(sys.argv) >= 4:
            generate_speech(sys.argv[1], sys.argv[2], sys.argv[3])
            return
        else:
            print("Usage: python tts_cli.py \"text\" \"voice\" \"filename\"")
            return

    print("--- Sarvam AI Telugu Text-to-Speech CLI ---")
    
    # 1. Ask for Telugu text (Supporting multi-line input)
    print("\nEnter or paste Telugu text for speech generation.")
    print("(Press Ctrl+D on Mac/Linux or Ctrl+Z on Windows followed by Enter to finish):")
    
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    telugu_text = "\n".join(lines).strip()
    
    if not telugu_text:
        print("Error: Telugu text cannot be empty.")
        return

    # 2. Voice selection
    print("\nAvailable voices:")
    # Voices compatible with bulbul:v3 for Telugu
    voices = ["aditya", "ritu", "kavya", "priya"]
    for i, voice in enumerate(voices, 1):
        print(f"{i}. {voice}")

    try:
        choice = int(input("\nEnter choice (1-4): ").strip())
        if 1 <= choice <= 4:
            selected_voice = voices[choice - 1]
        else:
            print("Error: Invalid choice. Please select 1, 2, 3, or 4.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # 3. Call generate_speech
    generate_speech(telugu_text, selected_voice)

if __name__ == "__main__":
    main()
