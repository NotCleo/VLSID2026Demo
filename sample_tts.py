import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Change voice rate (default ~200)
engine.setProperty('rate', 150)

# Change volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# List available voices
voices = engine.getProperty('voices')
for idx, voice in enumerate(voices):
    print(f"{idx}: {voice.name}")

# Select a voice (example: female voice if available)
engine.setProperty('voice', voices[0].id)  

# Speak text
engine.say("Hello! This is an offline text to speech demo in Python.")
engine.runAndWait()
