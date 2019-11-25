import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED, Button
import random
import datetime

def getTime():
    elapsedTime = datetime.datetime.now() - startTime
    total = elapsedTime.seconds + float(elapsedTime.microseconds / 1000000)
    print("Reaction Time: %.3f" % total) #Print out the elapsed time in seconds
    greenLED.off()

GPIO.setmode(GPIO.BCM)
    
button = Button(2)
redLED = LED(26)
greenLED = LED(16)

print("%s\n" % "-----Reaction Game-----")
sleep(2)
print("%s\n" % "Hit the BUTTON as soon as the RED LED turns off and the GREEN LED turns on!")
sleep(3)
print("%s\n" % "In 3 seconds the RED LED will turn on...")
sleep (3)

redLED.on()

time = random.uniform(4,9) #Random time between 4 and 9 seconds
sleep(time)
redLED.off()
greenLED.on()
startTime = datetime.datetime.now()

button.wait_for_press()
getTime()
