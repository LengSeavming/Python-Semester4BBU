import time
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import json
import os


class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.data = open("data.json", "r", encoding="utf-8")
        self.json_data = json.load(self.data)

    def answer_question(self, question: "", lang):
        if question == "":
            self.text_to_speech("Sorry, I can't answer!")
            return
        question = str(question).lower().replace("?", "")
        for x in self.json_data["q_and_a"]:
            if question in str(x["q"]).lower().replace("?", ""):
                i = 0
                while i < len(str(x["a"])):
                    print(x["a"][i], end='')
                    time.sleep(.2)
                    i += 1
                self.google_text_to_speech(x["a"], lang)
            pass
        pass

    def google_text_to_speech(self, text, to_lang):
        tts = gTTS(text, lang=to_lang)
        tts.save("output.mp3")
        os.system("output.mp3")
        pass

    def text_to_speech(self, text):
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()

    def speech_to_text(self, to_lang):
        text = ""
        with sr.Microphone() as mic:
            try:
                self.recognizer.adjust_for_ambient_noise(mic)
                voice = self.recognizer.listen(mic, timeout=3, phrase_time_limit=3)
                print('Please wait!')
                text = self.recognizer.recognize_google(voice, language=to_lang)
                pass
            except sr.UnknownValueError as ex:
                print(ex)
            except sr.WaitTimeoutError as ex:
                print(ex)
            except Exception as ex:
                print(ex)
        return text

    def speech_to_text_dual_language(self, lang1="km", lang2="en"):
        text1 = text2 = ""
        with sr.Microphone() as mic:
            try:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(mic)
                audio = self.recognizer.listen(mic, timeout=3, phrase_time_limit=5)

                # Try language 1
                try:
                    text1 = self.recognizer.recognize_google(audio, language=lang1)
                    print(f"[{lang1}] Recognized: {text1}")
                except:
                    pass

                # Try language 2
                try:
                    text2 = self.recognizer.recognize_google(audio, language=lang2)
                    print(f"[{lang2}] Recognized: {text2}")
                except:
                    pass

            except Exception as e:
                print(f"Error: {e}")

        # Return the first successful one, or both if needed
        return text1 if text1 else text2
