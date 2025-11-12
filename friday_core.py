import os, time

class FridayCore:
    def __init__(self):
        self.active = True

    def speak(self, text):
        print(f"🎤 Friday: {text}")
        os.system(f'termux-tts-speak "{text}" > /dev/null 2>&1')

    def intro(self):
        self.speak("नमस्ते sir, मैं Friday हूँ — सिस्टम एक्टिव है।")

    def listen_loop(self):
        while self.active:
            cmd = input("🧠 Command: ").lower().strip()

            if "youtube" in cmd and ("open" in cmd or "खोल" in cmd):
                self.speak("यूट्यूब खोल रही हूँ सर।")
                os.system("am start -a android.intent.action.VIEW -d https://youtube.com")

            elif "youtube" in cmd and ("close" in cmd or "बंद" in cmd):
                self.speak("यूट्यूब बंद कर रही हूँ सर।")
                os.system("am start -a android.intent.action.MAIN -c android.intent.category.HOME")

            elif "exit" in cmd or "फ्राइडे बंद" in cmd:
                self.speak("फ्राइडे बंद हो रही है सर। आपका दिन शुभ हो।")
                self.active = False
            else:
                self.speak("सर, यह कमांड समझ नहीं आई।")
