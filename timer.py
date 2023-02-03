import time 
from playsound import playsound
seconds = int(input("enter the time in seconds"))
def countdown(seconds):
    min = int(seconds/60)
    seconds = seconds%60
    while seconds>0:
       
        print(f"{min}:{seconds}")
        time.sleep(1)
        seconds = seconds-1
    print("timeup")
    playsound("beep.wav")

countdown(seconds)

    