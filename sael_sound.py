from gtts import gTTS
import os

def speak_sael(text):
    print("🗣️ Sael is speaking...")
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("sael_output.mp3")

    # Play it using default macOS player
   os.system("afplay sael_output.mp3")