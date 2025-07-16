# voice_generator.py
from gtts import gTTS
import re

def clean_text(text):
    # Remove markdown symbols like *, _, #, etc.
    return re.sub(r'[*_`#>-]', '', text).strip()

def text_to_speech(text, filename='summary_en.mp3', lang='en', name='Yash'):
    # Clean and format final speech
    clean_summary = clean_text(text)
    final_text = f"Hi {name}, today’s top news is: {clean_summary}"
    
    tts = gTTS(text=final_text, lang=lang)
    tts.save(filename)
    return filename
