import os
import time
from datetime import datetime
from PiPocketGeiger import RadiationWatch

import pyrealsense_test as prt
import cv2
import time
from numpy import False_, True_
os.system('clear')

#Libraries

import RPi.GPIO as GPIO
#Filesimport board
from enviro_test import init_environ, run_environ
from co_sensor import init_co, run_co
from EM_Sensor import init_EM, run_EM
#from radiation2 import run_radiation2
from communication import publish_data


CO_PATH = "CO"
ENVIRONMENT_PATH = "ENVIRONMENT"
RADIATION_PATH = "RADIATION"
ELECTROMAGNETIC_PATH = "ELECTROMAGNETIC"
DEPTH_PATH = "DEPTH"
RGB_PATH = "RGB"

LATENCY_PATH = "LATENCY"


#--------------------------------
config = {
    'select_co': False,
    'select_environ': False,
    'select_radiation': False,
    'select_EM': False
}
#--------------------------------



GPIO.setmode(GPIO.BCM)

#--------------------------------
print('\nModule Selection Menu: \n')
print("1: CO\n2: Environment\n3: Radiation\n4: Electromagnetic\n5: Depth Camera\n6: RGB Camera\n7: Test Latency\n7")
choice = input("Select Module With Number Keys: \n")
choice = int(choice)
print('\n\nChoice Selected -  ',choice)
#--------------------------------

'''
#--------------------------------
def sle_menu(sel):
    if sel == 1:
        #run_co()
        config = {'select_co': True}
    elif sel == 2:
        #run_environ()
        config = {'select_environ': True}
    elif sel == 3:co
        config = {'select_radiation': True}
#--------------------------------
'''

#-------------channel1.voltage-------------------
if choice == 1:
    #run_co()
    config['select_co']=True
    config['select_environ']=False
    config['select_radiation']=False
    config['select_EM']=False
elif choice == 2:
    GPIO.setmode(GPIO.BCM)
    #run_environ()
    config['select_co']=False
    config['select_environ']=True
    config['select_radiation']=False
    config['select_EM']=False
elif choice == 3:
    #run_radiation()
    config['sechannel1.voltagelect_co']=False
    config['select_environ']=False
    config['select_radiation']=True
    config['select_EM']=False
elif choice == 4:
    #run_EM()
    config['select_co']=False
    config['select_environ']=False
    config['select_radiation']=False
    config['select_EM']=True

elif choice ==5:#Lidar
    x=10
    y=10
    print("Pixel at location")
    prt.main(x,y)
    #depth_frame = prt.get_depth_frame()
    while True:
        image = prt.colorize_lidar(prt.get_depth_frame())
    #cv2.imshow("test",image)
        cv2.imwrite("depth.jpg",image)
        print("Captured depth image at finalfiles/depth.jpg")
        time.sleep(5)
elif choice == 6:#Camera
    
    frame_width = 640
    frame_height = 480
    

        #camera_no = 0
    cap = cv2.VideoCapture(-1,cv2.CAP_V4L)#-1 to auto search.  Camera no 6 seems to work.
    cap.set(3,frame_height)
    cap.set(4,frame_width)
            
    while True:
        success,image = cap.read()
        publish_data(RGB_PATH,str(image))
        #cv2.imshow("Image RGB",image)
        cv2.imwrite("rgb.jpg",image)
        print("Captured RGB image at finalfiles/rgb.jpg")
        time.sleep(5)
    cap.release()
#--------------------------------
elif choice == 7:
    publish_data(LATENCY_PATH,str(datetime.now()))
#sle_menu(choice)

#--------------------------------
if config['select_co']:
    channel = init_co()
    while True:
        co_data = run_co(channel)
        publish_data(CO_PATH,str(co_data))
        
        
#Set Select pins to run_bme ead from CO censor.
elif config['select_environ']:
    #Select BME
    bme = init_environ()
    while True:
        environ_data = run_environ(bme)
        publish_data(ENVIRONMENT_PATH,str(environ_data))
        time.sleep(1)
elif config['select_radiation']:
    #Select radiation
    if __name__ == "__main__":
        # Create the RadiationWatch object, specifying the used GPIO pins ...
        with RadiationWatch(24, 23) as radiationWatch:
            while 1:
                # ... and simply print readings each 5 seconds.
                
                data = radiationWatch.status()
                print(data)
                #What data do we need?  duration,cpm,uSvh,uSvhError
                publish_data(RADIATION_PATH,str(data))
                
                time.sleep(1)
                # That's all.
elif config['select_EM']:
    #Select EM Sensor
    EM_sensor = init_EM()
    run_EM(EM_sensor)
#--------------------------------

