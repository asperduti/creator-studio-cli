xpath = {}

xpath["is_user_loged"] = {
    "login_button": "//div[text()='Facebook login']",
}

xpath["login_user"] = {
    "input_email": "//input[@name='email']",
    "input_password": "//input[@name='pass']",
    "login_button": "//div[text()='Facebook Login']",
}

xpath["go_to_instagram_Tab"] = {
    "instagram_button": "//div[@id='media_manager_chrome_bar_instagram_icon']",
}


xpath["instagram"] = {
}

xpath["instagram"]["create_post"] = {
    "create_post_button": "//div[text()='Create post']",
    "instagram_feed_button": "//strong[text()='Instagram Feed']",
    "input_account": "//input[@class='_4b7k _4b7k_media-manager-instagram-composer _53rs']",
    "list_account": "//div[text()='{}']",
    "input_message": "//div[@aria-autocomplete='list']",
    "add_content_button": "//span[text()='Add content' and not(@role='heading')]",
    "input_file": "//input[@class='_n _5f0v']",
    "send_post_button": "//button[@class='_271k _271m _1qjd']",
    "options_publish_button": "//button[@class='_271k _271l _1o4e _271m _1qjd']",
    "schedule_option": "//span[text()='Schedule']",
    "publish_now_option": "//span[text()='Publish Now']",
    "draft_option": "//span[text()='Draft']",
    "input_date": "//input[@placeholder='mm/dd/yyyy']",
    "input_time": "//input[@role='spinbutton']",
    "load_complete": "//div[text()='100%']",
    "success_message": "//span[text()='Your post has been successfully scheduled.']",
}

xpath["go_to_facebook_Tab"] = {
    "facebook_button": "//div[@id='media_manager_chrome_bar_facebook_icon']",
}

xpath["facebook"] = {
}

xpath["facebook"]["create_post"] = {
    "create_post_button": "//div[text()='Create new']",
    "create_post_button_2": "//span[text()='Create Post']",
    "input_page": "//input[@class='_4b7k _4b7k_media-manager-composer-search _53rs']",
    "list_page": "//span[@class='_4lq7']/div[text()='{}']",
    "input_message": "//div[@role='combobox']",
    "input_file": "//input[@accept='image/*, image/heic, image/heif']",
    "publish_button": "//button[@class='_1mf7  _8bma _4jy0 _4jy3 _4jy1 _51sy selected _42ft']",
    "options_publish_button": "//div[@class='_43rm' and text()='Share Now']",
    "schedule_option": "//span[text()='Schedule']",
    "publish_now_option": "//span[text()='Now']",
    "Backdate_option": "//span[text()='Backdate']",
    "draft_option": "//span[text()='Save Draft']",
    "input_date": "//input[@placeholder='mm/dd/yyyy']",
    "input_time": "//input[@role='spinbutton']",
    "schedule_button": "//button[@class='layerConfirm _4jy0 _4jy3 _4jy1 _51sy selected _42ft' and text()='Schedule']",
    "success_message": "//span[text()='Success! Find published posts in the Published tab, and scheduled or drafted posts in the Pre-Published tab.']",
}

xpath["facebook"]["create_story"] = {
    "add_story_button": "//span[text()='Add story']",
    "add_button": "//span[text()='Add button']",
    "share_to_story": "//span[text()='Share to story']",
    "input_file": "//input[@class='plzdoh0l']",
    "option_url": "//input[@aria-labelledby='jsc_c_4']",
    "input_url": "//input[@id='jsc_c_9']",
    "success_message": "//span[text()='Your story has been published.']",
}

