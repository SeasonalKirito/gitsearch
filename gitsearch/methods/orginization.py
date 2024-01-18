from ..url_manager import url_manager

class Orginization:
    def __init__(self) -> None:
        self.url_manager = url_manager()
        self.orginization_api = self.url_manager.base_api + "orgs/"

    def _orginization_valid(self, orginization: str=None):
        '''
        Checks if an orginization is valid.

        Parameters:
            orginization (str): The orginization to check.

        Returns:
            bool: Whether the orginization is valid or not.
        '''

        if orginization is None:
            return False
        
        response = self.url_manager._get(self.orginization_api + orginization)
        if response.status_code != 404:
            return True
        else:
            return False

    def _get_orginization(self, orginization: str=None):
        '''
        Gets an orginization.

        Parameters:
            orginization (str): The orginization to get.

        Returns:
            dict: The orginization.
        '''

        if orginization is None:
            return "No orginization provided"

        response = self.url_manager._get(self.orginization_api + orginization)
        return response.json()
    
    def _get_orginization_repos(self, orginization: str=None):
        '''
        Gets an orginization's repositories.

        Parameters:
            orginization (str): The orginization to get repositories from.

        Returns:
            list: The orginization's repositories.
        '''

        if orginization is None:
            return "No orginization provided"
        
        response = self.url_manager._get(self.orginization_api + orginization + "/repos")
        return response.json()
    
    def _get_orginization_members(self, orginization: str=None):
        '''
        Gets an orginization's members.

        Parameters:
            orginization (str): The orginization to get members from.

        Returns:
            list: The orginization's members.
        '''

        if orginization is None:
            return "No orginization provided"
        
        response = self.url_manager._get(self.orginization_api + orginization + "/members")
        return response.json()
    
    def _get_orginization_public_members(self, orginization: str=None):
        '''
        Gets an orginization's public members.

        Parameters:
            orginization (str): The orginization to get public members from.

        Returns:
            list: The orginization's public members.
        '''

        if orginization is None:
            return "No orginization provided"
        
        response = self.url_manager._get(self.orginization_api + orginization + "/public_members")
        return response.json()
    
    def _get_orginization_issues(self, orginization: str=None):
        '''
        Gets an orginization's issues.

        Parameters:
            orginization (str): The orginization to get issues from.

        Returns:
            list: The orginization's issues.
        '''

        if orginization is None:
            return "No orginization provided"
        
        response = self.url_manager._get(self.orginization_api + orginization + "/issues")
        return response.json()
    
    def _get_orginization_memberships(self, orginization: str=None):
        '''
        Gets an orginization's memberships.

        Parameters:
            orginization (str): The orginization to get memberships from.

        Returns:
            list: The orginization's memberships.
        '''

        if orginization is None:
            return "No orginization provided"
        
        response = self.url_manager._get(self.orginization_api + orginization + "/memberships")
        return response.json()
    
    def _get_orginization_teams(self, orginization: str=None):
        '''
        Gets an orginization's teams.

        Parameters:
            orginization (str): The orginization to get teams from.

        Returns:
            list: The orginization's teams.
        '''

        if orginization is None:
            return "No orginization provided"
        
        response = self.url_manager._get(self.orginization_api + orginization + "/teams")
        return response.json()
    
    def _get_orginization_hooks(self, orginization: str=None):
        '''
        Gets an orginization's hooks.

        Parameters:
            orginization (str): The orginization to get hooks from.

        Returns:
            list: The orginization's hooks.
        '''

        if orginization is None:
            return "No orginization provided"
        
        response = self.url_manager._get(self.orginization_api + orginization + "/hooks")
        return response.json()