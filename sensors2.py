

#Libraries

import RPi.GPIO as GPIO
#Filesimport board
from enviro_test import run_environ
from co2_sensor import run_co2​
2
​
3
#Libraries
4
​
5
import RPi.GPIO as GPIO
6
#Filesimport board
7
from enviro_test import run_environ
8
from co2_sensor import run_co2
9
​
10
config = {
11
    'select_co2': False
12
}
13
​
14
GPIO.setmode(GPIO.BCM)
15
​
16
​
17
if config['select_co2']:
18
    run_co2()
19
#Set Select pins to run_bme ead from CO2 censor.
20
else:
21
    #Select BME
22
    run_environ()
23
​
24
​
25


config = {
    'select_co2': False
}

GPIO.setmode(GPIO.BCM)


if config['select_co2']:
    run_co2()
#Set Select pins to run_bme ead from CO2 censor.
else:
    #Select BME
    run_environ()


