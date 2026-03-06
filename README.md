# Sarvam Telugu Story TTS CLI

A professional CLI tool to convert Telugu text into high-quality speech using the Sarvam AI Text-to-Speech (Bulbul v3) API.

## Project Description
This tool allows users to generate expressive Telugu audio from text input. It features an interactive CLI for voice selection and saves the output as high-quality MP3 files, making it ideal for storytelling and content creation.

## Project Structure
```text
sarvam-tts-cli/
├── tts_cli.py
├── requirements.txt
├── .env
├── story1.mp3
├── story2.mp3
├── output.mp3
├── sample_story.txt
└── README.md
```

## Installation Steps
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd sarvam-tts-cli
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## API Key Setup
Before running the script, you must provide your Sarvam AI API key.
1. Create a `.env` file in the project root.
2. Add your API key: `SARVAM_API_KEY=your_actual_api_key_here`

## Running the Script
Run the application using Python:
```bash
python tts_cli.py
```

## CLI Usage Example
```text
--- Sarvam AI Telugu Text-to-Speech CLI ---

Enter or paste Telugu text for speech generation.
(Press Ctrl+D on Mac/Linux or Ctrl+Z on Windows followed by Enter to finish):
ఒక చిన్న గ్రామంలో రాము అనే బాలుడు ఉండేవాడు...

Available voices:
1. aditya
2. ritu
3. kavya
4. priya

Enter choice (1-4): 2

Generating audio for: output_audio.mp3...
Audio generated successfully.
Saved as output_audio.mp3
```

## Example Stories

### Example 1: The Thirsty Crow (తెలివైన కాకి)
**Text:**
ఒక ఊరిలో ఒక తెలివైన కాకి ఉండేది. దానికి ఒకరోజు చాలా దాహం వేసింది. నీళ్ల కోసం వెతుకుతుండగా ఒక కుండ కనిపించింది. కుండలో నీళ్లు చాలా తక్కువగా ఉన్నాయి. కాకి తన తెలివితేటలతో రాళ్లను కుండలో వేసి నీటిని పైకి తెచ్చి తాగి సంతోషించింది.

**Example 1 Audio:**
[Download Audio](story1.mp3)
<audio src="story1.mp3" controls="controls">
  Your browser does not support the audio element.
</audio>

---

### Example 2: Our Village (మా ఊరు)
**Text:**
మా ఊరు చాలా అందంగా ఉంటుంది. ఊరి చుట్టూ పచ్చని పొలాలు, ఎత్తైన కొండలు ఉన్నాయి. ఉదయాన్నే పక్షుల కిలకిలరావాలు వినడం చాలా ఆనందంగా ఉంటుంది. ఊరి ప్రజలందరూ ఒకరికొకరు సహాయం చేసుకుంటూ కలిసిమెలిసి ఉంటారు.

**Example 2 Audio:**
[Download Audio](story2.mp3)
<audio src="story2.mp3" controls="controls">
  Your browser does not support the audio element.
</audio>

## License
This project is open-source and available under the MIT License.
