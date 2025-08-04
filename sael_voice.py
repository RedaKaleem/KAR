from gtts import gTTS
import os

def speak_sael(text):
    print("🔊 Sael is speaking...")
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("sael_output.mp3")
    os.system("afplay sael_output.mp3")  # macOS built-in audio player