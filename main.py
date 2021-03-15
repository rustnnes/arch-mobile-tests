import os
from pathlib import Path

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.mobileby import MobileBy as By
from dotenv import load_dotenv
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clickable,
    presence_of_element_located as is_present,
    visibility_of as is_visible,
    invisibility_of_element as is_hidden,
)
from selenium.webdriver.support.ui import WebDriverWait as wdw


def wait(driver, timeout=30):
    return wdw(driver, timeout)


if __name__ == "__main__":
    driver = appium_service = None

    try:
        load_dotenv()

        caps = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "version": "9.0",
            "app": f'{Path(__file__).parent.absolute()}/app_under_test/{os.getenv("APP")}',
            "realDevice": False,
        }

        appium_service = AppiumService()

        appium_service.start(
            args=["--address", os.getenv("HOST"), "-p", os.getenv("PORT")]
        )

        driver = webdriver.Remote(
            f'http://{os.getenv("HOST")}:{os.getenv("PORT")}/wd/hub', caps
        )

        inputA = wait(driver).until(is_clickable((By.ACCESSIBILITY_ID, "inputA")))
        inputA.send_keys("10")

        inputB = wait(driver).until(is_clickable((By.ACCESSIBILITY_ID, "inputB")))
        inputB.send_keys("5")

        sum = wait(driver).until(is_clickable((By.ACCESSIBILITY_ID, "sum")))

        assert sum != None and sum.text == "15"

    except Exception as e:
        print(e)
    finally:
        if driver != None:
            driver.quit()
        appium_service.stop()