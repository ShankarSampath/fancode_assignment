import requests

class BasePage:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}")

    def get_json(self, endpoint):
        response = self.get(endpoint)
        response.raise_for_status()
        return response.json()