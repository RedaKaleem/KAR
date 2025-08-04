import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Listening... Speak now.")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Sorry, couldn't understand you.")
            return ""
        except sr.RequestError:
            print("⚠️ Error with the speech service.")
            return ""