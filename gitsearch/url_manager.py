import requests

class url_manager():
    def __init__(self) -> None:
        self.base_api = "https://api.github.com/"

    def _get(self, url: str):
        response = requests.get(url)
        return response