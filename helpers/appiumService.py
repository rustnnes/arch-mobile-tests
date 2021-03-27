import logging
import os
from appium.webdriver.appium_service import AppiumService
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()


class AppiumServiceWrapper:
    service = None

    def __init__(self) -> None:
        if AppiumServiceWrapper.service is None:
            AppiumServiceWrapper.service = AppiumService()

            logger.debug("Starting AppiumService...")
            AppiumServiceWrapper.service.start(
                args=["--address", os.getenv("HOST"), "-p", os.getenv("PORT")]
            )

    def is_started(self):
        return AppiumServiceWrapper.service is not None

    def __del__(self):
        AppiumServiceWrapper.service.stop()
