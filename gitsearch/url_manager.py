import requests

class url_manager():
    def __init__(self) -> None:
        pass

    def _get(self, url: str):
        response = requests.get(url)
        return response