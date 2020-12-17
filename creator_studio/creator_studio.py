from .login_util import is_user_loged
from .login_util import login_user
from .browser import get_browser
from . import instagram
from . import facebook

class CreatorStudio:
    """Class to be instantiated to use te script."""

    def __init__(self, email, password, browser_profile_path=None):
        self.email = email
        self.password = password
        self.browser = get_browser(browser_profile_path)

    def login(self):
        """Used to login the user."""
        
        if is_user_loged(self.browser):
            print("User is logged")
            return
        
        print("Tryin to perform loggin")
        login_user(self.browser, self.email, self.password)
    
    def create_post(self, account, message, file, schedule_options=None, social_network=None):
        if social_network == None:
            social_network = "instagram"
        
        if social_network == "instagram":
            instagram.go_to_instagram_Tab(self.browser)
            instagram.create_post(self.browser, account, message, file, schedule_options=schedule_options)
        
        if social_network == "facebook":
            facebook.go_to_facebook_Tab(self.browser)
            facebook.create_post(self.browser, account, message, file, schedule_options=schedule_options)

    def create_story(self, account, file, url=None):
        facebook.create_story(self.browser, account, file, url)