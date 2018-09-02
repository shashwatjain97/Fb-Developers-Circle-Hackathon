import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

sensor = 4
buzzer = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print "IR Sensor ready...."
print "  "


try:
    while True:
        if GPIO.input(sensor):
            GPIO.output(buzzer,True)
            print "Object Detected"
            while GPIO.input(sensor):
                time.sleep(0.2)
        else:
            GPIO.output(buzzer,False)
             
except KeyboardInterrupt:
    GPIO.cleanup()