import time
import board
import digitalio
from adafruit_bme280 import basic as adafruit_bme280
import busio
from adafruit_bus_device.spi_device import SPIDevice
#import board
#import busio
#import digitalio
#import adafruit_bmp280
#spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
#cs = digitalio.DigitalInOut(board.D5)
#sensor = adafruit_bmp280.Adafruit_BMP280_SPI(spi, cs)

# Create sensfrom board import *or object, using the board's default I2C bus.
#i2c = board.I2C()  # uses board.SCL and board.SDA
#bme280 = adafruit_b me280.Adafruit_BME280_I2C(i2c)
from board import *
# OR create sensor object, using the board's default SPI bus.

#spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

def run_bme():
    spi = board.SPI()
    bme_cs = digitalio.DigitalInOut(board.D26)
    bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

    # change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1013.25

    while True:
        print("\nTemperature: %0.1f C" % bme280.temperature)
        print("Humidity: %0.1f %%" % bme280.relative_humidity)
        print("Pressure: %0.1f hPa" % bme280.pressure)
        print("Altitude = %0.2f meters" % bme280.altitude)
        time.sleep(2)