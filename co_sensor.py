#https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython
#Created with help from above website.

import RPi.GPIO as GPIO
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def init_co():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, False)
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
#board.D24 = 0import run_bme 
    cs = digitalio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)
    channel = AnalogIn(mcp, MCP.P0)
    return channel
'''    while True:
        if 0 < channel.voltage < 0.75:  #Determine 
            print('Safe CO Levels!')
            
        elif channel.voltage > 0.75:
            print('WARNING HIGH CO LEVELS!')

        #print('Raw ADC Value: ', channel.value)
        #print('ADC Voltage: ' + str(channel.voltage) + 'V')
        

        time.sleep(1)'''
def run_co(channel):
    if 0 < channel.voltage < 1.75:  #Determine
        time.sleep(1)
        return 'Safe CO Levels!'
    elif channel.voltage > 1.75:
        time.sleep(1)
        return 'WARNING HIGH CO LEVELS!'

def test():
    channel=init_co()
    out = run_co(channel)
    print(out)