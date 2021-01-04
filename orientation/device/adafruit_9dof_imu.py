from typing import Dict
from time import sleep
from itertools import cycle

from smbus2 import SMBus

from ..gpio import GPIO
from ..logging import logger


bus = SMBus(1)
gyro_addr: int
accel_addr: int
compass_addr: int


def initialize(options: Dict):
    global gyro_addr, accel_addr, compass_addr
    GPIO.setmode(GPIO.BCM)
    gyro_addr = options['gyro_addr']
    accel_addr = options['accel_addr']
    compass_addr = options['compass_addr']
    # wait for sensor to settle
    sleep(2)


def get_distance():
    while cycle([True]):
        try:
            offset = 0
            block_size = 16
            measurement = bus.read_i2c_block_data(gyro_addr, offset, block_size)
            print("GYRO:")
            print(measurement)
            measurement = bus.read_i2c_block_data(accel_addr, offset, block_size)
            print("ACCEL:")
            print(measurement)
            measurement = bus.read_i2c_block_data(compass_addr, offset, block_size)
            print("COMPASS:")
            print(measurement)
        except IOError:
            logger.warning("I2C bus error")
        sleep(0.05)


def cleanup():
    GPIO.cleanup()
