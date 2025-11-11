import os

def speak(text):
    print(f"🎤 Friday: {text}")
    os.system(f'termux-tts-speak "{text}"')

def main():
    speak("नमस्ते sir, मैं Friday हूँ — online sync mode में हूँ।")

if __name__ == "__main__":
    main()
