from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .browser import explicit_wait_visibility_of_element_located
from .xpath import xpath

CREATOR_STUDIO_HOMEPAGE = "https://business.facebook.com/creatorstudio/home"
FACEBOOK_LOGIN_PAGE = "https://www.facebook.com/login/"

def login_user(browser, email, password):
    """Logins the user with the given email and password."""
    assert email, "Email not provided"
    assert password, "Password not provided"

    current_url = browser.current_url
    if current_url == CREATOR_STUDIO_HOMEPAGE:
        button = browser.find_elements(by=By.XPATH, value=xpath[is_user_loged.__name__]["login_button"])
        if len(button):
            ActionChains(browser).move_to_element(button[0]).click().perform()
            sleep(2)
    
    explicit_wait_visibility_of_element_located(browser, xpath[login_user.__name__]["input_email"])
    input_email = browser.find_element(by=By.XPATH, value=xpath[login_user.__name__]["input_email"])
    ActionChains(browser).move_to_element(input_email).click().send_keys(email).perform()
    sleep(1)

    input_password = browser.find_element(by=By.XPATH, value=xpath[login_user.__name__]["input_password"])
    ActionChains(browser).move_to_element(input_password).click().send_keys(password).perform()
    sleep(1)

    ActionChains(browser).move_to_element(input_password).click().send_keys(Keys.ENTER).perform()
    sleep(30)
    # TODO: WAIT and promt user input for Two-Factor security


def is_user_loged(browser):

    if browser.current_url is not CREATOR_STUDIO_HOMEPAGE:
        browser.get(CREATOR_STUDIO_HOMEPAGE)

    button = browser.find_elements(by=By.XPATH, value=xpath[is_user_loged.__name__]["login_button"])

    if len(button) == 0:
        return True
    
    return False