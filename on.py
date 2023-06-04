#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 

buzzer=4
led=17

GPIO.setup(buzzer,GPIO.OUT) 
GPIO.setup(led, GPIO.OUT)

try:
	while True: 
		GPIO.output(led,GPIO.HIGH)
		GPIO.output(buzzer,GPIO.HIGH) 
		print ("Beep") 
		sleep(0.5)
		GPIO.output(buzzer, GPIO.LOW)
		sleep(0.5)
except:
	GPIO.cleanup()	
