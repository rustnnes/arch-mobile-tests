import json, logging, os, sys, yaml
from pathlib import Path

from appium import webdriver
from dotenv import load_dotenv

sys.path.append("/helpers")
from helpers.appiumService import AppiumServiceWrapper

load_dotenv()
AppiumServiceWrapper()

logger = logging.getLogger(__name__)
service_url = f'http://{os.getenv("HOST")}:{os.getenv("PORT")}/wd/hub'


class DriverProvider:
    @staticmethod
    def get(caps_file):
        with open(f"caps/{caps_file}.yaml", "r") as f:
            caps = yaml.safe_load(f.read())["caps"]

        logger.info(
            f"Providing Driver with the following capabilities\n{json.dumps(caps, indent=4)}"
        )
        driver = webdriver.Remote(service_url, caps)
        driver.implicitly_wait(15)
        return driver
