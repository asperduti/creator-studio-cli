from .login_util import is_user_loged
from .login_util import login_user
from .browser import get_browser
from .instagram import go_to_instagram_Tab, create_post

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
    
    def create_post(self, account, message, file, schedule_options=None):
        go_to_instagram_Tab(self.browser)
        create_post(self.browser, account, message, file, schedule_options=schedule_options)