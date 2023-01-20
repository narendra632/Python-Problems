from pygame import init, mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while True:
            a=input()
            if a==stopper:
                mixer.music.stop()
                break
        
def log_now(msg):
    with open ("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
#musiconloop("Sleep Away.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watertime =30 * 60
    eyestime=35 * 60
    exercisetime=40 * 60
    
while True:
    
    if time() - init_water >  watertime:
        print("Water Drinking time. Enter 'drank' to stop the alarm")
        musiconloop("Sleep Away.mp3","drank")
        init_water=time()
        log_now("Drank Water at ")
            
    if time() - init_eyes >  eyestime:
        print("Eye Exercise time. Enter 'done' to stop the alarm")
        musiconloop("Sleep Away.mp3","done")
        init_eyes=time()
        log_now("Eye exercise done at ")
            
    if time() - init_exercise >  exercisetime:
        print("Body Exercise time. Enter 'done' to stop the alarm")
        musiconloop("Sleep Away.mp3","done")
        init_exercise=time()
        log_now("Body Exercise done at ")
    

