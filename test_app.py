import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image


APP_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCREENSHOT_PATH = "screenshot.png"


os.system("start WinAppDriver")


caps = {
    "app": APP_PATH,
    "platformName": "Windows",
    "deviceName": "WindowsPC"
}


driver = webdriver.Remote("http://127.0.0.1:4723", caps)


time.sleep(3)


driver.save_screenshot(SCREENSHOT_PATH)
print(f"Screenshot saved to {SCREENSHOT_PATH}")


driver.quit()
