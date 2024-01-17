from ..url_manager import url_manager

class User:
    def __init__(self) -> None:
        self.url_manager = url_manager()
        self.user_api = "https://api.github.com/users/"

    def _user_valid(self, username: str=None):
            '''
            Checks if a user exists on GitHub.

            Parameters:
                username (str): The username to check.

            Returns:
                bool: True if the user exists, False if not.
            '''
            
            if username is None:
                return "No username provided"

            response = self.url_manager._get(self.user_api + username)
            if response.status_code != 404:
                return True
            else:
                return False
            
    def _get_user(self, username: str=None):
        '''
        Gets a user's information.
        
        Parameters:
            username (str): The username to get information from.
            
        Returns:
            dict: The user's information. Example: https://docs.github.com/en/rest/users/users#get-a-user
        '''

        if username is None:
            return "No username provided"

        response = self.url_manager._get(self.user_api + username)
        return response.json()