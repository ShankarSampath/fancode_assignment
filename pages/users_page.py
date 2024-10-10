from .base_page import BasePage

class UsersPage(BasePage):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_users(self):
        return self.get_json("/users")