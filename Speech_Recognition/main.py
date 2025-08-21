from speechfun import *

i = 1

if __name__ == '__main__':
    obj = SpeechRecognition()
    # obj.google_text_to_speech("សក់អ៊ុតសារ៉ូមមែន", to_lang="km")
    # # while i < 3:
    #     obj.text_to_speech('bro ')
    #     i += 1
    # obj.text_to_speach('What the fuck')
    # print("Please say something...!")
    # obj.text_to_speech("Please say something...!")
    # text = obj.speech_to_text(to_lang="km")

    # print(f"Your said: {text}")
    # obj.google_text_to_speech(f"{text}", "km")
    # obj.text_to_speech(f"Your said: {text}")

    # text = obj.speech_to_text_dual_language(lang1="km", lang2="en")
    # obj.google_text_to_speech(text, to_lang="km" if any(ord(c) > 128 for c in text) else "en")
    obj.answer_question("How old are you", "en")