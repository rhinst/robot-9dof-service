from typing import Dict
from time import sleep
from itertools import cycle
import busio
import adafruit_lsm303_accel
import adafruit_lsm303dlh_mag
from math import atan2, pi

from ..logging import logger


i2c: busio.I2C
mag: adafruit_lsm303dlh_mag.LSM303DLH_Mag
accel: adafruit_lsm303_accel.LSM303_Accel
gyro: object


SCL_PIN = 3
SDA_PIN = 2


def initialize(options: Dict):
    global i2c, gyro, mag, accel
    i2c = busio.I2C(SCL_PIN, SDA_PIN)
    logger.debug("Initializing magnetometer")
    mag = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
    logger.debug("Initializing accelerometer")
    accel = adafruit_lsm303_accel.LSM303_Accel(i2c)


def get_distance():
    while cycle([True]):
        #print("Acceleration (m/s^2): X=%0.3f Y=%0.3f Z=%0.3f"%accel.acceleration)
        #print("Magnetometer (micro-Teslas)): X=%0.3f Y=%0.3f Z=%0.3f"%mag.magnetic)
        heading = (atan2(mag.magnetic[1], mag.magnetic[0]) * 180) / pi
        if heading < 0:
            heading = 360 + heading
        print(f"Compass Heading: {heading}")
        sleep(0.5)


def cleanup():
    pass
