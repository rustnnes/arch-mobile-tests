import logging
import os
import yaml

from appium import webdriver
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

service_url = f'http://{os.getenv("HOST")}:{os.getenv("PORT")}/wd/hub'


class DriverProvider:
    @staticmethod
    def get(caps_file):
        f = open(caps_file)
        caps = yaml.safe_load(f)["caps"]
        f.close()
        logger.debug("Returning Driver...")
        return webdriver.Remote(service_url, caps)
