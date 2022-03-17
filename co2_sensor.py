#https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython
#Created with help from above website.

import RPi.GPIO as GPIO
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def run_co2():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8,False)
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
#board.D24 = 0import run_bme 
    cs = digitalio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)
    channel = AnalogIn(mcp, MCP.P0)
    while True:
        print('Raw ADC Value: ', channel.value)
        print('ADC Voltage: ' + str(channel.voltage) + 'V')
        time.sleep(1)
