import os
from appium.webdriver.appium_service import AppiumService
from dotenv import load_dotenv

from helpers.logger import LoggerProvider

load_dotenv()
logger = LoggerProvider.get_logger(__name__)


class AppiumServiceWrapper:
    service = None

    def __init__(self) -> None:
        if AppiumServiceWrapper.service is None:
            AppiumServiceWrapper.service = AppiumService()

            logger.info("Starting AppiumService...")
            AppiumServiceWrapper.service.start(
                args=["--address", os.getenv("HOST"), "-p", os.getenv("PORT")],
            )
            assert AppiumServiceWrapper.service.is_running
            assert AppiumServiceWrapper.service.is_listening

    def __del__(self):
        AppiumServiceWrapper.service.stop()
        assert not AppiumServiceWrapper.service.is_listening
        assert not AppiumServiceWrapper.service.is_running