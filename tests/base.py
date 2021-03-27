import logging
import sys
import unittest

from selenium.webdriver.support.ui import WebDriverWait as wdw

sys.path.append("/helpers")
from helpers.driver import DriverProvider
from helpers.appiumService import AppiumServiceWrapper

logger = logging.getLogger(__name__)


class BaseTest(unittest.TestCase):
    appium_service = AppiumServiceWrapper()

    def __init__(self, caps_file) -> None:
        self.driver = DriverProvider.get(caps_file)

    @classmethod
    def setUpClass(cls):
        logger.info("classmethod")

    @classmethod
    def tearDownClass(cls):
        logger.debug("Disposing AppiumServer...")
        del cls.appium_service

    def tearDown(self) -> None:
        if self.driver != None:
            logger.debug("Disposing Driver...")
            self.driver.quit()
        return super().tearDown()

    @staticmethod
    def wait(self, timeout=30):
        return wdw(self.driver, timeout)


if __name__ == "__main__":
    unittest.main()