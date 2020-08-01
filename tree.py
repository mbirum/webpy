import RPi.GPIO as GPIO
import time

def turnTreeOn():
     GPIO.setmode(GPIO.BCM)
     GPIO.setwarnings(False)
     GPIO.setup(25, GPIO.OUT)
     try:
          GPIO.output(25, GPIO.HIGH)
          return 1
     except:
          return 0

def turnTreeOff():
     GPIO.setmode(GPIO.BCM)
     GPIO.setwarnings(False)
     GPIO.setup(25, GPIO.OUT)
     try:
          GPIO.output(25, GPIO.LOW)
          return 1
     except:
          return 0

def getTree():
     GPIO.setmode(GPIO.BCM)
     GPIO.setwarnings(False)
     GPIO.setup(25, GPIO.OUT)
     try:
          state = GPIO.input(25)
          return state
     except:
          return 7     
