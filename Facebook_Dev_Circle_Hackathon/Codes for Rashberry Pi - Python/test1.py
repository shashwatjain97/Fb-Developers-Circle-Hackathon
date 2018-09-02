import RPi.GPIO as GPIO
from time import sleep
import sys, tty, termios, time
 
GPIO.setmode(GPIO.BOARD)
 
Motor1 = 16    # Input Pin
Motor2 = 18    # Input Pin
Motor3 = 22    # Enable Pin

Motor4 = 13    # Input Pin
Motor5 = 11    # Input Pin
Motor6 = 15    # Enable Pin
 
GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor3,GPIO.OUT)

GPIO.setup(Motor4,GPIO.OUT)
GPIO.setup(Motor5,GPIO.OUT)
GPIO.setup(Motor6,GPIO.OUT)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
def motor1_forward():
            print "FORWARD MOTION"
            GPIO.output(Motor1,GPIO.HIGH)
            GPIO.output(Motor2,GPIO.LOW)
            GPIO.output(Motor3,GPIO.HIGH)
 
def motor1_backward(): 
            print "BACKWARD MOTION"
            GPIO.output(Motor1,GPIO.LOW)
            GPIO.output(Motor2,GPIO.HIGH)
            GPIO.output(Motor3,GPIO.HIGH)
            
            
def motor2_left():
            print "Left"
            GPIO.output(Motor4,GPIO.HIGH)
            GPIO.output(Motor5,GPIO.LOW)
            GPIO.output(Motor6,GPIO.HIGH)
 
def motor2_right(): 
            print "Right"
            GPIO.output(Motor4,GPIO.LOW)
            GPIO.output(Motor5,GPIO.HIGH)
            GPIO.output(Motor6,GPIO.HIGH)
 
while True:
    
        char = getch()
        
        if(char=="w"):
                motor1_forward()
                
        if(char=="a"):
                motor2_left()
        if(char=="d"):
                motor2_right()
        if(char=="s"):
                motor1_backward()        
                
        if(char=="x"):
                print("Program ended")
                GPIO.output(Motor3,GPIO.LOW)
                GPIO.output(Motor6,GPIO.LOW)
                break

 
# print "STOP"
# GPIO.output(Motor3,GPIO.LOW)
GPIO.output(Motor3,GPIO.LOW)
GPIO.cleanup()