import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

GPIO.output(22, True)

print("SENIOR DEISGN 2:")
print("Tripp Herlong, JohnMarc Bryan, Nicole D'amato, Graham Hyman, Cooper Meyers")


print(" \r\n")
print("------------------------------------")
print("| Welcome, please input a direction:  |")
print("------------------------------------")
print(" \r\n")



while (1):
    
    ''' this stuff is old, probably delete later
    keyboard.on_press_key("w",forward)
    keyboard.on_press_key("a",left)
    keyboard.on_press_key("s",right)
    keyboard.on_press_key("d",back)
    keyboard.on_press_key("q",stop)
    '''
    
    if keyboard.read_key() == "w":
        GPIO.output(23, True)
        GPIO.output(24, False)
        GPIO.output(5, False)
        GPIO.output(6, True)
        print("     Forward")
        
    elif keyboard.read_key() == "d":
        GPIO.output(23, True)
        GPIO.output(24, False)
        GPIO.output(5, True)
        GPIO.output(6, False)
        print("     Right")
    
    elif keyboard.read_key() == "s":
        GPIO.output(23, False)
        GPIO.output(24, True)
        GPIO.output(5, True)
        GPIO.output(6, False)
        print("     Backward")
        
        
    elif keyboard.read_key() == "a":
        GPIO.output(23, False)
        GPIO.output(24, True)
        GPIO.output(5, False)
        GPIO.output(6, True)
        print("       Left")
    
    elif keyboard.read_key() == "q":
        GPIO.output(23, True)
        GPIO.output(24, True)
        GPIO.output(5, False)
        GPIO.output(6, False)
        print("      Stopping")
