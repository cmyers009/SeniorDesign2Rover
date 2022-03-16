#https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython
#Created with help from above website.

#Libraries
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

#Files
from enviro_test import run_bme 

import RPi.GPIO as GPIO

config = {
    'select_co2': True
}

GPIO.setmode(GPIO.BCM)


if config['select_co2']:
#Set Select pins to read from CO2 censor.
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, config['select_co2'])
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, False)
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
#board.D24 = 0import run_bme 
    cs = digitalio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)
    channel = AnalogIn(mcp, MCP.P0)
    while True:
        print('Raw ADC Value: ', channel.value)
        print('ADC Voltage: ' + str(channel.voltage) + 'V')
        time.sleep(1)

else:
    #Select BME
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, False)
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, True)
    #Run Bme
    run_bme()


