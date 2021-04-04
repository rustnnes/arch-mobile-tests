import unittest

from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clickable,
)
from selenium.webdriver.support.ui import WebDriverWait as wdw

from helpers.driver import DriverProvider
from helpers.logger import LoggerProvider

logger = LoggerProvider.get_logger(__name__)


def wait(driver, timeout=15):
    return wdw(driver, timeout)


class TestingBot(unittest.TestCase):
    """
    Teste para App TestingBot

    Params
        - txt_a: campo representando um operando
        - txt_b: campo representando outro operando
        - txt_result: Campo que guarda o resultado da operação
    """

    txt_a = (By.ACCESSIBILITY_ID, "inputA")
    txt_b = (By.ACCESSIBILITY_ID, "inputB")
    txt_result = (By.ACCESSIBILITY_ID, "sum")

    def setUp(self) -> None:
        self.driver = DriverProvider.get(self.__class__.__name__.lower())

    def tearDown(self) -> None:
        if self.driver != None:
            logger.debug("Disposing Driver...")
            self.driver.quit()

    def test_apk(self):
        wait(self.driver).until(is_clickable(self.txt_a)).send_keys("10")
        wait(self.driver).until(is_clickable(self.txt_b)).send_keys("5")

        txt_result = wait(self.driver).until(is_clickable(self.txt_result))
        self.assertEqual(txt_result.text, "15")


if __name__ == "__main__":
    unittest.main()
