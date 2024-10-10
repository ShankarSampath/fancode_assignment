from .base_page import BasePage

class TodosPage(BasePage):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_todos(self):
        return self.get_json("/todos")