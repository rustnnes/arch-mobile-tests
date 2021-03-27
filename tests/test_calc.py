from pathlib import Path

from appium.webdriver.common.mobileby import MobileBy as By
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clickable,
    visibility_of_element_located as is_visible,
)

from tests.base import BaseTest


class Calculator(BaseTest):
    def __init__(self, caps_file) -> None:
        caps_file = f"{Path().parent.absolute()}/caps/calc.yaml"
        super().__init__(caps_file=caps_file)
        self.id_path = "com.google.android.calculator:id/"

    def test_add_7_and_8_must_give_15(self):
        augend = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}digit_7"))
        )
        augend.click()

        operator = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}op_add"))
        )
        operator.click()

        addend = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}digit_8"))
        )
        addend.click()

        eq = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}eq"))
        )
        eq.click()

        input_sum = BaseTest.wait(self.driver).until(
            is_visible((By.ID, f"{self.id_path}result_final"))
        )

        self.assertTrue((input_sum != None) and (input_sum.text == "15"))

    def test_subtract_7_and_8_must_give_minus_1(self):
        minuend = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}digit_7"))
        )
        minuend.click()

        operator = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}op_"))
        )
        operator.click()

        subtrahend = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}digit_8"))
        )
        Subtrahend.click()

        eq = BaseTest.wait(self.driver).until(
            is_clickable((By.ID, f"{self.id_path}eq"))
        )
        eq.click()

        input_sum = BaseTest.wait(self.driver).until(
            is_visible((By.ID, f"{self.id_path}result_final"))
        )

        self.assertTrue((input_sum != None) and (input_sum.text == "15"))
