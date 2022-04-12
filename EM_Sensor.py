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
    channel1 = AnalogIn(mcp, MCP.P1)
    return channel1
def run_EM(EM):

    
    
        
    EM_data = str(channel1.voltage)

    print('Average EM Field: ' + EM_data + 'V\n')
    time.sleep(1)
    return EM_data
        