from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

from .xpath import xpath
from .browser import explicit_wait_visibility_of_element_located

MODE_FACEBOOK = "mode=facebook"

def go_to_facebook_Tab(browser):
    """Go to facebook mode"""

    if MODE_FACEBOOK in browser.current_url:
        print("Already in Facebook Mode")
        return
    
    try:
        facebook_button = browser.find_element_by_xpath(xpath[go_to_facebook_Tab.__name__]["facebook_button"])
    except:
        print("Unable to find Facebook Button")
    
    ActionChains(browser).move_to_element(facebook_button).click().perform()

    if MODE_FACEBOOK in browser.current_url:
        print("Switched to Facebook Mode")
        return


def create_post(browser, page, message, file, schedule_options=None):
    """Create a post."""

    explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["create_post_button"])
    create_post_button = browser.find_element_by_xpath(xpath["facebook"][create_post.__name__]["create_post_button"])
    ActionChains(browser).move_to_element(create_post_button).click().perform()
    sleep(2)

    explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["create_post_button_2"])
    create_post_button_2 = browser.find_element_by_xpath(xpath["facebook"][create_post.__name__]["create_post_button_2"])
    ActionChains(browser).move_to_element(create_post_button_2).click().perform()
    sleep(1)

    explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["input_page"])
    input_page = browser.find_element_by_xpath(xpath["facebook"][create_post.__name__]["input_page"])
    for character in page:
        ActionChains(browser).move_to_element(input_page).click().send_keys(character).perform()
        sleep(1)
        list_page = explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["list_page"].format(page), timeout=2)
        if list_page is not None:
            ActionChains(browser).move_to_element(list_page).click().perform()
            sleep(1)
            break
    sleep(2)

    input_message = explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["input_message"])
    ActionChains(browser).move_to_element(input_message).click().send_keys(message).perform()
    sleep(1)
    input_file = browser.find_element_by_xpath(xpath["facebook"][create_post.__name__]["input_file"])
    input_file.send_keys(file)
    sleep(1)



    if schedule_options is not None:

        schedule_options_hour, schedule_options_minutes, schedule_options_am_pm, = schedule_options["time"].replace(":", " ").split()
        options_publish_button = browser.find_element_by_xpath(xpath["facebook"][create_post.__name__]["options_publish_button"])
        ActionChains(browser).move_to_element(options_publish_button).click().perform()
        sleep(1)

        schedule_option = explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["schedule_option"])
        ActionChains(browser).move_to_element(schedule_option).click().perform()
        sleep(1)

        input_date = browser.find_element_by_xpath(xpath["facebook"][create_post.__name__]["input_date"])
        input_date.clear()
        input_date.send_keys(schedule_options["date"])
        sleep(1)

        hour, minutes, am_pm = browser.find_elements_by_xpath(xpath["facebook"][create_post.__name__]["input_time"])
        hour.send_keys(schedule_options_hour)
        sleep(1)
        minutes.send_keys(schedule_options_minutes)
        sleep(1)
        am_pm.send_keys(schedule_options_am_pm)
        sleep(1)

        schedule_button = explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["schedule_button"])
        ActionChains(browser).move_to_element(schedule_button).click().perform()
        sleep(1)

    publish_button = explicit_wait_visibility_of_element_located(browser, xpath["facebook"][create_post.__name__]["publish_button"])
    ActionChains(browser).move_to_element(publish_button).click().perform()
    sleep(1)

    success_message = explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["success_message"])
    if success_message is None:
        print("Error Creating Post")
        return False
    
    print("Post Created.")
    browser.refresh()
    return True
