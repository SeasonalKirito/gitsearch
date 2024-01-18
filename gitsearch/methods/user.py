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
            dict: The user's information.
        '''

        if username is None:
            return "No username provided"

        response = self.url_manager._get(self.user_api + username)
        return response.json()
    
    def _get_user_repos(self, username: str=None):
        '''
        Gets a user's repositories.
        
        Parameters:
            username (str): The username to get repositories from.
            
        Returns:
            list: The user's repositories.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/repos")
        return response.json()
    
    def _get_user_followers(self, username: str=None):
        '''
        Gets a user's followers.
        
        Parameters:
            username (str): The username to get followers from.
            
        Returns:
            list: The user's followers.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/followers")
        return response.json()
    
    def _get_user_following(self, username: str=None):
        '''
        Gets a user's following.
        
        Parameters:
            username (str): The username to get following from.
            
        Returns:
            list: The user's following.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/following")
        return response.json()
    
    def _get_user_starred(self, username: str=None):
        '''
        Gets a user's starred repositories.
        
        Parameters:
            username (str): The username to get starred repositories from.
            
        Returns:
            list: The user's starred repositories.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/starred")
        return response.json()
    
    def _get_user_gists(self, username: str=None):
        '''
        Gets a user's gists.
        
        Parameters:
            username (str): The username to get gists from.
            
        Returns:
            list: The user's gists.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/gists")
        return response.json()
    
    def _get_user_orgs(self, username: str=None):
        '''
        Gets a user's organizations.
        
        Parameters:
            username (str): The username to get organizations from.
            
        Returns:
            list: The user's organizations.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/orgs")
        return response.json()
    
    def _get_user_events(self, username: str=None):
        '''
        Gets a user's events.
        
        Parameters:
            username (str): The username to get events from.
            
        Returns:
            list: The user's events.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/events")
        return response.json()
    
    def _get_user_received_events(self, username: str=None):
        '''
        Gets a user's received events.
        
        Parameters:
            username (str): The username to get received events from.
            
        Returns:
            list: The user's received events.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/received_events")
        return response.json()
    
    def _get_user_received_public_events(self, username: str=None):
        '''
        Gets a user's received public events.
        
        Parameters:
            username (str): The username to get received public events from.
            
        Returns:
            list: The user's received public events.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/received_events/public")
        return response.json()
    
    def _get_user_keys(self, username: str=None):
        '''
        Gets a user's keys.
        
        Parameters:
            username (str): The username to get keys from.
            
        Returns:
            list: The user's keys.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username + "/keys")
        return response.json()
    
    def _get_user_followers_count(self, username: str=None):
        '''
        Gets a user's followers count.
        
        Parameters:
            username (str): The username to get followers count from.
            
        Returns:
            int: The user's followers count.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username)
        return response.json()["followers"]
    
    def _get_user_following_count(self, username: str=None):
        '''
        Gets a user's following count.
        
        Parameters:
            username (str): The username to get following count from.
            
        Returns:
            int: The user's following count.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username)
        return response.json()["following"]
    
    def _get_user_public_repos_count(self, username: str=None):
        '''
        Gets a user's public repositories count.
        
        Parameters:
            username (str): The username to get public repositories count from.
            
        Returns:
            int: The user's public repositories count.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username)
        return response.json()["public_repos"]
    
    def _get_user_public_gists_count(self, username: str=None):
        '''
        Gets a user's public gists count.
        
        Parameters:
            username (str): The username to get public gists count from.
            
        Returns:
            int: The user's public gists count.
        '''

        if username is None:
            return "No username provided"
        
        response = self.url_manager._get(self.user_api + username)
        return response.json()["public_gists"]