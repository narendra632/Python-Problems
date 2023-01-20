import pyttsx3


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine=pyttsx3.speak('Hello, I am Na-rendra, hi')

def gotdate():
    import datetime
    print(datetime.datetime.now())
gotdate()

 