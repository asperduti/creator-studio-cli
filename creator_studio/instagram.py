from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

from .xpath import xpath
from .browser import explicit_wait_visibility_of_element_located

MODE_INSTAGRAM = "mode=instagram"

def go_to_instagram_Tab(browser):
    """Go to instragram mode"""

    if MODE_INSTAGRAM in browser.current_url:
        print("Already in Instragram Mode")
        return
    
    try:
        instagram_button = browser.find_element_by_xpath(xpath[go_to_instagram_Tab.__name__]["instagram_button"])
    except:
        print("Unable to find Instagram Button")
    
    ActionChains(browser).move_to_element(instagram_button).click().perform()

    if MODE_INSTAGRAM in browser.current_url:
        print("Switched to Instagram Mode")
        return


def create_post(browser, account, message, file, schedule_options=None):
    """Create a post."""

    explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["create_post_button"])
    create_post_button = browser.find_element_by_xpath(xpath["instagram"][create_post.__name__]["create_post_button"])
    ActionChains(browser).move_to_element(create_post_button).click().perform()
    sleep(2)

    explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["instagram_feed_button"])
    instagram_feed_button = browser.find_element_by_xpath(xpath["instagram"][create_post.__name__]["instagram_feed_button"])
    ActionChains(browser).move_to_element(instagram_feed_button).click().perform()
    sleep(1)

    explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["input_account"])
    input_account = browser.find_element_by_xpath(xpath["instagram"][create_post.__name__]["input_account"])
    for character in account:
        ActionChains(browser).move_to_element(input_account).click().send_keys(character).perform()
        sleep(1)
        list_account = explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["list_account"].format(account), timeout=1)
        if list_account is not None:
            ActionChains(browser).move_to_element(list_account).click().perform()
            sleep(1)
            break
    sleep(2)
    # First we load the content
    explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["add_content_button"])
    add_content_button = browser.find_element_by_xpath(xpath["instagram"][create_post.__name__]["add_content_button"])
    browser.execute_script("arguments[0].scrollIntoView();", add_content_button)
    ActionChains(browser).move_to_element(add_content_button).click().perform()
    sleep(2)    
    
    input_file = browser.find_element_by_xpath(xpath["instagram"][create_post.__name__]["input_file"])
    input_file.send_keys(file)
    sleep(1)


    input_message = explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["input_message"])
    browser.execute_script("arguments[0].scrollIntoView();", input_message)
    ActionChains(browser).move_to_element(input_message).click().send_keys(message).perform()
    sleep(1)



    if schedule_options is not None:

        schedule_options_hour, schedule_options_minutes, schedule_options_am_pm, = schedule_options["time"].replace(":", " ").split()
        options_publish_button = browser.find_element_by_xpath(xpath["instagram"][create_post.__name__]["options_publish_button"])
        ActionChains(browser).move_to_element(options_publish_button).click().perform()
        sleep(1)

        schedule_option = explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["schedule_option"])
        ActionChains(browser).move_to_element(schedule_option).click().perform()
        sleep(1)

        input_date = browser.find_element_by_xpath(xpath["instagram"][create_post.__name__]["input_date"])
        ActionChains(browser).move_to_element(input_date).click().send_keys(schedule_options["date"]).perform()
        sleep(1)

        hour, minutes, am_pm = browser.find_elements_by_xpath(xpath["instagram"][create_post.__name__]["input_time"])
        hour.send_keys(schedule_options_hour)
        sleep(1)
        minutes.send_keys(schedule_options_minutes)
        sleep(1)
        am_pm.send_keys(schedule_options_am_pm)
        sleep(1)

    print("Watting for load finish.")
    load_finished = explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["load_complete"])

    if load_finished is None:
        print("Load not finish. Aborting...")
        return

    send_post_button = explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["send_post_button"])
    browser.execute_script("arguments[0].scrollIntoView();", send_post_button)
    ActionChains(browser).move_to_element(send_post_button).click().perform()
    sleep(1)

    success_message = explicit_wait_visibility_of_element_located(browser, xpath["instagram"][create_post.__name__]["success_message"])
    if success_message is None:
        print("Error Creating Post")
        return False
    
    print("Post Created.")
    return True
