import os
import base64
import time
from datetime import datetime
from PiPocketGeiger import RadiationWatch
import pyrealsense_test as prt
import cv2
import time
import threading
from playsound import playsound 



#Libraries
import RPi.GPIO as GPIO
from Environment_Sensor import init_environ, run_environ
from co_sensor import init_co
from EM_Sensor import init_EM
import rover_movement
#Connect to mqtt server
import paho.mqtt.client as mqtt

play_startup=0
play_co=0
play_rad=0

os.system('clear')

#Sleep for half a second to give computer time to load.
time.sleep(.5)


CO_PATH = "CO"
ENVIRONMENT_PATH = "ENVIRONMENT"
RADIATION_PATH = "RADIATION"
ELECTROMAGNETIC_PATH = "ELECTROMAGNETIC"
DEPTH_PATH = "DEPTH"
RGB_PATH = "RGB"

time_seconds=0

#RGB Camera Settings
frame_width = 640
frame_height = 480
cap = cv2.VideoCapture(-1,cv2.CAP_V4L)#-1 to auto search.  Camera no 6 seems to work.
cap.set(3,frame_height)
cap.set(4,frame_width)     

#CO Settings
channel = init_co()
#Environmental Settings
bme = init_environ()

#EM Settings
EM_sensor = init_EM()


BROKER_HOST = "test.mosquitto.org"
BROKER_PORT = 1883

def on_connect(client,userdata,flags,rc):
    global connected
    print("Connected with result code "+str(rc))
    client.subscribe(DRIVETRAIN_PATH)
    client.subscribe(TOGGLE_DEPTH_PATH)
    client.subscribe(TOGGLE_RGB_PATH)
    client.subscribe(TOGGLE_CO_PATH)
    client.subscribe(TOGGLE_ENVIRONMENTAL_PATH)
    client.subscribe(TOGGLE_RADIATION_PATH)
    client.subscribe(TOGGLE_ELECTROMAGNETIC_PATH)
    connected=rc
    
def on_publish(client,user_data,mid):
    print("Message "+str(mid)+" published.")
    print(str(user_data))

def on_message(client,userdata,msg):
    data = str(msg.payload)[2:-1]
    if msg.topic == DRIVETRAIN_PATH:
        print(data)
        rover_movement.move_rover(data)
    elif msg.topic == TOGGLE_DEPTH_PATH:
        global toggle_depth
        toggle_depth = int(data)
        print("toggle depth: ",data)
    elif msg.topic == TOGGLE_RGB_PATH:
        global toggle_rgb
        toggle_rgb = int(data)
        print("toggle rgb: ",data)
    elif msg.topic == TOGGLE_CO_PATH:
        global toggle_co
        toggle_co = int(data)
        print("toggle co: ",data)
    elif msg.topic == TOGGLE_ENVIRONMENTAL_PATH:
        global toggle_environmental
        toggle_environmental = int(data)
        print("toggle environmental: ",data)
    elif msg.topic == TOGGLE_RADIATION_PATH:
        global toggle_radiation
        toggle_radiation = int(data)
        print("toggle radiation: ",data)
    elif msg.topic == TOGGLE_ELECTROMAGNETIC_PATH:
        global toggle_electromagnetic
        toggle_electromagnetic = int(data)
        print("toggle electromagnetic: ",data)

client = mqtt.Client()
client.on_connect=on_connect
client.on_publish=on_publish
client.on_message = on_message
connected=1
while(connected):
    try:
        client.connect(BROKER_HOST,BROKER_PORT)
        print("connected:",connected)
    except Exception as e:
        print(e)
        time.sleep(4)
    else:
        connected=0


#mqttclient.publish(TOPIC,"Communication")
#mqttclient.publish(TOPIC,"Is")
#mqttclient.publish(TOPIC,"Working!!!!")

def publish_data(data_code,data):
    global client
    client.publish(data_code,data)

MQTT_SERVER = "test.mosquitto.org"
DRIVETRAIN_PATH = "DRIVETRAIN"
TOGGLE_DEPTH_PATH = "TOGGLE_DEPTH"
TOGGLE_RGB_PATH = "TOGGLE_RGB"
TOGGLE_CO_PATH = "TOGGLE_CO"
TOGGLE_ENVIRONMENTAL_PATH = "TOGGLE_ENVIRONMENTAL"
TOGGLE_RADIATION_PATH = "TOGGLE_RADIATION"
TOGGLE_ELECTROMAGNETIC_PATH = "TOGGLE_ELECTROMAGNETIC"

#run thread for communication
def run_communication():
    global client
    client.loop_forever()

def send_lidar():
    global toggle_depth
    if toggle_depth:
        image = prt.colorize_lidar(prt.get_depth_frame())
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        publish_data(DEPTH_PATH,jpg_as_text)

def send_rgb():
    global toggle_rgb
    global cap
 
    if toggle_rgb:
        success,image = cap.read()
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        publish_data(RGB_PATH,jpg_as_text)

def send_co(time_seconds):
    global toggle_co
    global channel
    global play_co
    if toggle_co:
        print(channel.voltage)
        if channel.voltage > 1.8:
            play_co=1
        
        co_data = channel.voltage
        data = [time_seconds,channel.voltage]
        print(str(data))
        publish_data(CO_PATH,str(data))
        

def send_environmental(time_seconds):
    global bme
    global toggle_environmental
    if toggle_environmental:
        environ_data = run_environ(bme,time_seconds)
        print(environ_data)
        publish_data(ENVIRONMENT_PATH,str(environ_data))


def send_radiation():
    global play_rad
        #Select radiation

    global toggle_radiation
    with RadiationWatch(24, 23) as radiationWatch:
        while 1:
            if toggle_radiation:
            # ... and simply print readings each 5 seconds.  
                data = radiationWatch.status()
                if int(data['cpm']) > 50:
                    play_rad=1
                data = [data['duration'],data['cpm']]

                print(data)
                publish_data(RADIATION_PATH,str(data))
                
                #play_rad=1
                time.sleep(1)
def send_EM(time_seconds):
    global EM_sensor
    global toggle_electromagnetic
    if toggle_electromagnetic:
        voltage = EM_sensor.voltage
        print(voltage)
        publish_data(ELECTROMAGNETIC_PATH,str([time_seconds,voltage]))
def play_sound():
    #print("sound played")
    global play_startup
    global play_co
    global play_rad
    while 1:
        if play_startup:
            playsound('startup.mp3')
            print("Startup sound played.")
            play_startup=0
        if play_rad:
            playsound('fallout.mp3')
            print("Rad sound played.")
            time.sleep(60)
            play_rad=0
            
        if play_co:
            playsound('smoke.mp3')
            print("co sound played.")            
            time.sleep(10)
            play_co=0
            

#--------------------------------
GPIO.setmode(GPIO.BCM)
#
#Separate thread for communication
t1 = threading.Thread(target = run_communication)
#Run Drivetrain
t1.start()
#Variables to toggle sensors.
toggle_depth = 0
toggle_rgb = 0
toggle_co = 0
toggle_environmental = 0
toggle_radiation = 0
toggle_electromagnetic = 0

#Separate thread just for the radiation sensor.
t2 = threading.Thread(target = send_radiation)
t2.start()
#play sounds
t3 = threading.Thread(target = play_sound)
t3.start()

i=0

#Trigger the signal to play the startup sound once the rover has loaded in.
play_startup=1

while(1):
    send_EM(i/4)
    if i%2==0:
        send_lidar()
        send_rgb()

    if i%4==0:
        send_co(i//4)
        send_environmental(i//4)
        #send_radiation()
        
        #send_increment()
    i+=1
    time.sleep(.25)
