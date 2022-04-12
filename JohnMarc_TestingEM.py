from array import array
from audioop import add
import RPi.GPIO as GPIO
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#from numpy import mean


def run_EM():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, False)
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
#board.D24 = 0import run_bme 
    cs = digitalio.DigitalInOut(board.D5)
    mcp = MCP.MCP3008(spi, cs)
    channel1 = AnalogIn(mcp, MCP.P1)
    channel2 = AnalogIn(mcp, MCP.P3)
    channel3 = AnalogIn(mcp, MCP.P2)
    
    while True:
        
        ArrayEM = [float(channel1.voltage),float(channel2.voltage),float(channel3.voltage)]
        AverageField = sum(ArrayEM)/3
        PrintAvg = str(AverageField)


        #Averages not currently working

        #print('Raw ADC Value: ', channel.value)
        print('X Field: ' + str(ArrayEM[0]) + 'V')
        print('Y Field: ' + str(ArrayEM[1]) + 'V')
        print('Z Field: ' + str(ArrayEM[2]) + 'V\n')
        print('Average Field: ' + PrintAvg + 'V\n')

        time.sleep(1)