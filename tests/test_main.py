from pathlib import Path
from unittest import skip

from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clickable,
)

from tests.base import BaseTest


@skip("showing class skipping")
class TestingBot(BaseTest):
    def __init__(self) -> None:
        caps_file = f"{Path().parent.absolute()}/caps/app.yaml"
        super().__init__(caps_file)

    def test_apk(self):
        input_a = BaseTest.wait(self.driver).until(
            is_clickable((By.ACCESSIBILITY_ID, "inputA"))
        )
        input_a.send_keys("10")

        input_b = BaseTest.wait(self.driver).until(
            is_clickable((By.ACCESSIBILITY_ID, "inputB"))
        )
        input_b.send_keys("5")

        input_sum = BaseTest.wait(self.driver).until(
            is_clickable((By.ACCESSIBILITY_ID, "sum"))
        )

        self.assertTrue((input_sum != None) and (input_sum.text == "15"))
