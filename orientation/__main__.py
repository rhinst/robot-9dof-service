import os
from itertools import cycle
from time import sleep
from typing import Dict

from redis import Redis

from orientation.config import load_config
from orientation.logging import logger, initialize_logger
import orientation.device


def main():
    environment: str = os.getenv("ENVIRONMENT", "dev")
    config: Dict = load_config(environment)
    initialize_logger(config["logging"]["level"], config["logging"]["filename"])
    redis_host = config["redis"]["host"]
    redis_port = config["redis"]["port"]
    logger.debug(f"Connecting to redis at {redis_host}:{redis_port}")
    redis_client: Redis = Redis(host=redis_host, port=redis_port)

    orientation.device.initialize(config["device"]["name"], config["device"]["options"])
    try:
        while cycle([True]):
            measurement = orientation.device.get_distance()
            redis_client.publish("subsystem.orientation.measurement", measurement)
            sleep(0.1)
    finally:
        redis_client.close()
        orientation.device.cleanup()


if __name__ == "__main__":
    main()
