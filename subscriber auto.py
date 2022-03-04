import speech_recognition as sr
import pyautogui

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say IT!")
    audio = r.listen(source)
    
text1 = r.recognize_google(audio)
def clickunia():
    if text1 == "subscribe" or "please subscribe" or "subscribe to my channel":
        cords = pyautogui.locateCenterOnScreen("subscribe.png")
        pyautogui.click(cords)
clickunia()


    