import speech_recognition as sr
import pyttsx3
import pywhatkit

google = pyttsx3.init()
listener = sr.Recognizer()



google.say("how can i help you sir")
google.runAndWait()


try:
   with sr.Microphone() as source:
       print("listening...")
       print("must be said : Play")
       voice = listener.listen(source)
       command = listener.recognize_google(voice)
       print(command)

   if "play" in command:
       play_vedio = command.replace("play", "")
       print("playing" + play_vedio + "...")
       pywhatkit.playonyt(play_vedio)

except:
    pass
