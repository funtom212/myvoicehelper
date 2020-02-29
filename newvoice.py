import pyttsx3
import speech_recognition as sr

rec = sr.Recognizer()


class Voice:
    def __init__(self):
        self.jvoice = pyttsx3.init()

    def say(self, stext):
        self.jvoice.say(stext)
        self.jvoice.runAndWait()

        voices = self.jvoice.getProperty('voices')
        self.jvoice.setProperty('voice', voices[3].id)

    def hear(self, htext="", say_mode=True):
        if say_mode:
            self.say(htext)
        try:
            with sr.Microphone(device_index=0) as source:
                audio = rec.listen(source)
            query = rec.recognize_google(audio, language="ru-RU")
            return query.lower()
        except Exception as error:
            print('Voice error: {}'.format(error))
            return ""