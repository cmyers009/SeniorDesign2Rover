import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

GPIO.output(18, True)

print("Senior Design 2 - Team Genesis:")
print("Tripp Herlong, JohnMarc Bryan, Nicole D'amato, Graham Hyman, Cooper Myers")

previous_key=""
def move_rover(key):
    global previous_key
    if key == "w" or key =="W":
        if previous_key == "s":
            GPIO.output(16, True)
            GPIO.output(12, True)
            GPIO.output(5, False)
            GPIO.output(6, False)
            time.sleep(.5)
        previous_key = "w"
        GPIO.output(16, True)
        GPIO.output(12, False)
        GPIO.output(5, False)
        GPIO.output(6, True)
        print("     Forward")
        
    elif key == "d" or key == "D":
        if previous_key != "d" and previous_key!="q":
            GPIO.output(16, True)
            GPIO.output(12, True)
            GPIO.output(5, False)
            GPIO.output(6, False)
            time.sleep(.25)
        previous_key = "d"
        GPIO.output(16, True)
        GPIO.output(12, False)
        GPIO.output(5, True)
        GPIO.output(6, False)
        print("     Right")
    
    elif key == "s" or key == "S":
        if previous_key=="w":
            GPIO.output(16, True)
            GPIO.output(12, True)
            GPIO.output(5, False)
            GPIO.output(6, False)
            time.sleep(.5)
        previous_key = "s"
        GPIO.output(16, False)
        GPIO.output(12, True)
        GPIO.output(5, True)
        GPIO.output(6, False)
        print("     Backward")
        
        
    elif key == "a"or key == "A":
        if previous_key != "a" and previous_key!="q":
            GPIO.output(16, True)
            GPIO.output(12, True)
            GPIO.output(5, False)
            GPIO.output(6, False)
            time.sleep(.25)
        previous_key = "a"
        GPIO.output(16, False)
        GPIO.output(12, True)
        GPIO.output(5, False)
        GPIO.output(6, True)
        print("       Left")
    
    elif key == "q"or key == "Q":
        previous_key = "q"
        GPIO.output(16, True)
        GPIO.output(12, True)
        GPIO.output(5, False)
        GPIO.output(6, False)
        print("      Stopping Movement")
    else:
        print(key)


#On Start make sure it is stopped.
move_rover("q")