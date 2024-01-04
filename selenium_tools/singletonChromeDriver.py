# Standard Library Modules
import os

# Third-Party Library Modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

# Specify the download folder path.
DOWNLOAD_FOLDER_PATH = os.path.join(os.path.expanduser("~"), "Downloads") + "\\"
cache_manager = DriverCacheManager(root_dir=DOWNLOAD_FOLDER_PATH)

class SingletonChromeDriver:
    _instance = None

    @classmethod
    def get_instance(cls) -> webdriver.Chrome:
        """
        Singleton Pattern 取得 ChromeDriver的實例

        Returns:
            - selenium.webdriver.Chrome: Chrome Driver
        """
        if cls._instance is None:
            # 使用 webdriver_manager 安裝或更新 ChromeDriver，並指定安裝路徑
            webdirver_path = ChromeDriverManager(cache_manager=cache_manager).install()

            # open Google Chrome Driver
            service = Service(webdirver_path)
            options = Options()
            options.add_argument("--start-maximized")
            options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
            cls._instance = webdriver.Chrome(service=service, options=options)

            # setting can't find elements timeout
            cls._instance.implicitly_wait(10)

        return cls._instance