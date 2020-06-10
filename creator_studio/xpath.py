xpath = {}

xpath["is_user_loged"] = {
    "login_button": "//button[@class='_271k _1qjd']",
}

xpath["login_user"] = {
    "input_email": "//input[@name='email']",
    "input_password": "//input[@name='pass']",
    "login_button": "//button[@name='login']",
}

xpath["go_to_instagram_Tab"] = {
    "instagram_button": "//div[@id='media_manager_chrome_bar_instagram_icon']",
}

xpath["create_post"] = {
    "create_post_button": "//div[text()='Create Post']",
    "instagram_feed_button": "//strong[text()='Instagram Feed']",
    "input_account": "//input[@class='_4b7k _4b7k_media-manager-instagram-composer _53rs']",
    "list_account": "//div[text()='{}']",
    "input_message": "//div[@aria-autocomplete='list']",
    "add_content_button": "//span[@class='_3-99']",
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