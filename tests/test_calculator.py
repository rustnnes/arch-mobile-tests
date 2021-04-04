import unittest
from appium.webdriver.common.mobileby import MobileBy as By

from helpers.driver import DriverProvider
from helpers.logger import LoggerProvider

logger = LoggerProvider.get_logger(__name__)


@unittest.skip("not implemented")
class Calculator(unittest.TestCase):
    """
    Teste para Calculadora do Android

    Params
        - digit_7: Número "7"
        - digit_8: Número "8"
        - opr_add: Operador Soma
        - opr_sub: Operador Subtração
        - eq: Sinal de Igual
        - txt_result: Campo que guarda o resultado da operação

    Curiosidade:
        Os asserts do método test_subtract_7_and_8_must_give_minus_1 verificam
        pelo caractere "−" (https://www.compart.com/en/unicode/U+2212),
        diferente do caractere "-" (https://www.compart.com/en/unicode/U+002D),
        que encontramos nos teclados.
    """

    digit_7 = (By.ID, "digit_7")
    digit_8 = (By.ID, "digit_8")
    opr_add = (By.ID, "op_add")
    opr_sub = (By.ID, "op_sub")
    eq = (By.ID, "eq")
    txt_result = (By.XPATH, ".//*[contains(@resource-id, 'result')]")

    def setUp(self) -> None:
        self.driver = DriverProvider.get(self.__class__.__name__.lower())

    def tearDown(self) -> None:
        if self.driver != None:
            logger.debug("Disposing Driver...")
            self.driver.quit()

    def test_add_7_and_8_must_give_15(self):
        self.driver.find_element(*self.digit_7).click()
        self.driver.find_element(*self.opr_add).click()
        self.driver.find_element(*self.digit_8).click()
        self.driver.find_element(*self.eq).click()

        txt_result = self.driver.find_element(*self.txt_result)
        self.assertEqual(txt_result.text, "15")

    def test_subtract_7_and_8_must_give_minus_1(self):
        self.driver.find_element(*self.digit_7).click()
        self.driver.find_element(*self.opr_sub).click()
        self.driver.find_element(*self.digit_8).click()
        self.driver.find_element(*self.eq).click()

        txt_result = self.driver.find_element(*self.txt_result)
        self.assertTrue(txt_result.text == "−1")
        self.assertEqual(txt_result.text.find("−"), 0)
        self.assertNotEqual(txt_result.text.find("-"), 0)


if __name__ == "__main__":
    unittest.main()
