from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
INPUTPIN = 4
BUZZER = 17
GPIO.setup(INPUTPIN, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

while True:
           if (GPIO.input(INPUTPIN) == False):
                GPIO.output(BUZZER,GPIO.HIGH)     
    	   else:
		GPIO.output(BUZZER,GPIO.LOW)    
	   sleep(1);


