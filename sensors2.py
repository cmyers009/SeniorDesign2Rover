import os

from numpy import True_
os.system('clear')

#Libraries

import RPi.GPIO as GPIO
#Filesimport board
from enviro_test import run_environ
from co2_sensor import run_co2
from radiation import run_radiation


#--------------------------------
config = {
    #'select_co2': False
    'select_co2': True
}
#--------------------------------


GPIO.setmode(GPIO.BCM)

#--------------------------------
if config['select_co2']:
    run_co2()
#Set Select pins to run_bme ead from CO2 censor.
elif config['select_environ']:
    #Select BME
    run_environ()
#--------------------------------