#!/usr/bin/python

import RPi.GPIO as GPIO
import time
BUZZ_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZ_PIN, GPIO.OUT)
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
    
GPIO.cleanup()
