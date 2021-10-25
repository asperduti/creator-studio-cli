# Based on https://github.com/timgrossmann/InstaPy/blob/c3ad0c869bcaa402a738804b9a20f55a82c12edb/instapy/browser.py
import os
import pickle
import zipfile
from os.path import sep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException


def create_firefox_extension():
    ext_path = os.path.abspath(os.path.dirname(__file__) + sep + "firefox_extension")
    # safe into assets folder
    zip_file = os.path.abspath(os.path.dirname(__file__) + sep) +"extension.xpi"

    files = ["manifest.json", "content.js", "arrive.js"]
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED, False) as zipf:
        for file in files:
            zipf.write(ext_path + sep + file, file)

    return zip_file


def get_browser(browser_profile_path=None):
    """Start the driver and retur it."""
    if browser_profile_path is not None:
        firefox_profile = webdriver.FirefoxProfile(browser_profile_path)
    else:
        firefox_profile = webdriver.FirefoxProfile()

    browser = webdriver.Firefox(firefox_profile)
    browser.implicitly_wait(10) # seconds
    # add extenions to hide selenium
    browser.install_addon(create_firefox_extension(), temporary=True)

    return browser


def explicit_wait_visibility_of_element_located(browser, xpath, timeout=35):
    """Explicitly wait until visibility on element."""
    locator = (By.XPATH, xpath)
    condition = expected_conditions.visibility_of_element_located(locator)

    try:
        wait = WebDriverWait(browser, timeout)
        result = wait.until(condition)
    except TimeoutException:
        print("Timeout Exception in explicit wait")
        return False
    
    return result


def save_cookies(browser, path):
    """Save the current session's cookies."""
    with open(path, 'wb') as file:
        pickle.dump(browser.get_cookies(), file)


def load_cookies(browser, path):
    """Load cookies from file."""
    with open(path, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            browser.add_cookie(cookie)