
import time
import board
from adafruit_bme280 import basic as adafruit_bme280

def init_environ():
    # Create sensor object, using the board's default I2C bus.
    i2c = board.I2C()  # uses board.SCL and board.SDA
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    # change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1021.67
    # OR create sensor object, using the board's default SPI bus.
    # spi = board.SPI()
    # bme_cs = digitalio.DigitalInOut(board.D10)
    # bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)
    return bme280

def run_environ(bme280,time_seconds):

    return_val = {}
    return_val["seconds"]=time_seconds
    return_val["temp"] = bme280.temperature
    return_val["rel_humidity"] = bme280.relative_humidity
    return_val["pressure"] = bme280.pressure
    return_val["altitude"] = bme280.altitude
    return return_val
    '''
    while True:
        print("\nTemperature: %0.1f C" % bme280.temperature)
        print("Humidity: %0.1f %%" % bme280.relative_humidity)
        print("Pressure: %0.1f hPa" % bme280.pressure)
        print("Altitude = %0.2f meters" % bme280.altitude)
        time.sleep(1)
        '''