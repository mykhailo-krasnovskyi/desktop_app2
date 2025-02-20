import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image

APP_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCREENSHOT_PATH = "screenshot.png"
WINAPPDRIVER_URL = "http://127.0.0.1:4723"

def is_winappdriver_running():
    try:
        response = requests.get(WINAPPDRIVER_URL, timeout=3)
        if response.status_code == 200:
            print("✅ WinAppDriver is running")
            return True
    except requests.exceptions.ConnectionError:
        print("❌ WinAppDriver is NOT running")
    return False

if not is_winappdriver_running():
    print("🔄 Starting WinAppDriver...")
    os.system("start /B C:\\Program Files (x86)\\Windows Application Driver\\WinAppDriver.exe")
    time.sleep(3)  # Ждем, чтобы драйвер успел запуститься

    if not is_winappdriver_running():
        print("❌ WinAppDriver failed to start! Exiting.")
        exit(1)

if not os.path.exists(APP_PATH):
    print(f"❌ Chrome not found at {APP_PATH}")
    exit(1)

print("✅ Chrome found at:", APP_PATH)

caps = {
    "app": APP_PATH,
    "platformName": "Windows",
    "deviceName": "WindowsPC"
}

try:
    print("🔄 Connecting to WinAppDriver...")
    driver = webdriver.Remote(WINAPPDRIVER_URL, caps)
    print("✅ Successfully connected to WinAppDriver")
except Exception as e:
    print(f"❌ Failed to connect to WinAppDriver: {e}")
    exit(1)

time.sleep(3)

print("📸 Taking screenshot...")
driver.save_screenshot(SCREENSHOT_PATH)
print(f"✅ Screenshot saved to {SCREENSHOT_PATH}")

print("🔍 Running processes:")
os.system("tasklist | findstr /I chrome")

print("🔄 Closing Chrome...")
driver.quit()
print("✅ Test finished successfully!")
