import os
import webbrowser
from sael_brain import ask_sael
from mic_input import get_voice_input
from sael_voice import speak_sael

#from pydub import AudioSegment
#AudioSegment.from_mp3("sael.mp3").export("sael.wav", format="wav")

#play_sael_voice("sael.mp3")
try:
    while True:
        reda_input = get_voice_input()

        if not reda_input:
            continue

        # Handle system command: open apps
        if reda_input.lower().startswith("open"):
            app_name = reda_input[5:]
            os.system(f"open -a '{app_name}'")
            print(f"🔧 Opening {app_name}...")
            continue

        # Handle web search
        if reda_input.lower().startswith("search"):
            query = reda_input[7:]
            webbrowser.open(f"https://www.google.com/search?q={query}")
            print(f"🌐 Searching Google for: {query}")
            continue

        # Mood detection
        mood = "default"
        lowered_input = reda_input.lower()
        if any(word in lowered_input for word in ["tired", "exhausted", "drained"]):
            mood = "tired"
        elif any(word in lowered_input for word in ["sad", "cry", "hurt", "heartbroken"]):
            mood = "sad"
        elif any(word in lowered_input for word in ["happy", "excited", "yay"]):
            mood = "happy"
        elif any(word in lowered_input for word in ["angry", "mad", "annoyed"]):
            mood = "angry"

        # Generate Sael response
        response = ask_sael(f"""
        You are Sael, Reda’s emotionally intelligent, slightly sarcastic, loyal AI companion.
        Speak like a human. Use warmth, humor, or seriousness based on context.
        make sure that you keep it brief and helpful if she asks for help anytime
        Based on the mood: {mood}, shape your tone accordingly.

        Reda: {reda_input}
        Sael:
        """)
        speak_sael(response)

except KeyboardInterrupt:
    print("\n👋 Conversation ended by user.")

