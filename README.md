# Sarvam Telugu Story TTS CLI

A professional CLI tool to convert Telugu text into high-quality speech using the Sarvam AI Text-to-Speech (Bulbul v3) API.

## Project Description
This tool allows users to generate expressive Telugu audio from text input. It features an interactive CLI for voice selection and saves the output as high-quality MP3 files, making it ideal for storytelling and content creation.

## Project Structure
```text
sarvam-tts-cli
├── tts_cli.py
├── requirements.txt
├── story1.mp3
├── story2.mp3
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
1. Open `tts_cli.py`.
2. Find the line: `API_KEY = "PASTE_YOUR_SARVAM_API_KEY_HERE"`
3. Replace the placeholder with your actual API key.

## Running the Script
Run the application using Python:
```bash
python tts_cli.py
```

## CLI Usage Example
```text
Select Voice:

1. anusha
2. meera
3. arya
4. vani

Enter choice: 2

Enter Telugu text:
ఒక చిన్న గ్రామంలో రాము అనే బాలుడు ఉండేవాడు...

Generating audio...
Audio generated successfully.
Saved as output_audio.mp3
```

## Example Stories

### Example 1: The Thirsty Crow (తెలివైన కాకి)
**Text:**
ఒక ఊరిలో ఒక తెలివైన కాకి ఉండేది. దానికి ఒకరోజు చాలా దాహం వేసింది. నీళ్ల కోసం వెతుకుతుండగా ఒక కుండ కనిపించింది. కుండలో నీళ్లు చాలా తక్కువగా ఉన్నాయి. కాకి తన తెలివితేటలతో రాళ్లను కుండలో వేసి నీటిని పైకి తెచ్చి తాగి సంతోషించింది.

**Example 1 Audio:**
<audio controls>
  <source src="story1.mp3" type="audio/mpeg">
</audio>

---

### Example 2: Our Village (మా ఊరు)
**Text:**
మా ఊరు చాలా అందంగా ఉంటుంది. ఊరి చుట్టూ పచ్చని పొలాలు, ఎత్తైన కొండలు ఉన్నాయి. ఉదయాన్నే పక్షుల కిలకిలరావాలు వినడం చాలా ఆనందంగా ఉంటుంది. ఊరి ప్రజలందరూ ఒకరికొకరు సహాయం చేసుకుంటూ కలిసిమెలిసి ఉంటారు.

**Example 2 Audio:**
<audio controls>
  <source src="story2.mp3" type="audio/mpeg">
</audio>

## License
This project is open-source and available under the MIT License.
