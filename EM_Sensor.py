from array import array
from audioop import add
from operator import truediv
import RPi.GPIO as GPIO
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#import matplotlib.pyplot as plt

#from numpy import mean

def init_EM():
        
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, False)
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
#board.D24 = 0import run_bme 
    cs = digitalio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)
    channel = AnalogIn(mcp, MCP.P1)
    return channel
'''def run_EM(channel):
    
        #spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        #board.D24 = 0import run_bme 
        #cs = digitalio.DigitalInOut(board.D5)
        #mcp = MCP.MCP3008(spi, cs)
    #channel1 = AnalogIn(mcp, MCP.P1) #update to fix traceback JM April 13th
        
            
    EM_data = str(channel1.voltage)
    return EM_data
    print('Average EM Field: ' + EM_data + ' V\n')'''
            