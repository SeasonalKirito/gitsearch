from ..url_manager import url_manager

class Repository:
    def __init__(self) -> None:
        self.url_manager = url_manager()
        self.repository_api = "https://api.github.com/repos/"

    def _repository_valid(self, username: str=None, repository: str=None):
        '''
        Checks if a repository exists on GitHub.

        Parameters:
            username (str): The username to check.
            repository (str): The repository to check.

        Returns:
            bool: True if the repository exists, False if not.
        '''
        
        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"

        response = self.url_manager._get(self.repository_api + username + "/" + repository)
        if response.status_code != 404:
            return True
        else:
            return False
        
    def _get_repository(self, username: str=None, repository: str=None):
        '''
        Gets a repository's information.
        
        Parameters:
            username (str): The username to get information from.
            repository (str): The repository to get information from.
            
        Returns:
            dict: The repository's information.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"

        response = self.url_manager._get(self.repository_api + username + "/" + repository)
        return response.json()
    
    def _get_repository_commits(self, username: str=None, repository: str=None):
        '''
        Gets a repository's commits.
        
        Parameters:
            username (str): The username to get commits from.
            repository (str): The repository to get commits from.
            
        Returns:
            list: The repository's commits.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/commits")
        return response.json()
    
    def _get_repository_languages(self, username: str=None, repository: str=None):
        '''
        Gets a repository's languages.
        
        Parameters:
            username (str): The username to get languages from.
            repository (str): The repository to get languages from.
            
        Returns:
            dict: The repository's languages.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/languages")
        return response.json()
    
    def _get_repository_topics(self, username: str=None, repository: str=None):
        '''
        Gets a repository's topics.
        
        Parameters:
            username (str): The username to get topics from.
            repository (str): The repository to get topics from.
            
        Returns:
            dict: The repository's topics.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/topics")
        return response.json()
    
    def _get_repository_contributors(self, username: str=None, repository: str=None):
        '''
        Gets a repository's contributors.
        
        Parameters:
            username (str): The username to get contributors from.
            repository (str): The repository to get contributors from.
            
        Returns:
            list: The repository's contributors.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/contributors")
        return response.json()
    
    def _get_repository_branches(self, username: str=None, repository: str=None):
        '''
        Gets a repository's branches.
        
        Parameters:
            username (str): The username to get branches from.
            repository (str): The repository to get branches from.
            
        Returns:
            list: The repository's branches.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/branches")
        return response.json()
    
    def _get_repository_tags(self, username: str=None, repository: str=None):
        '''
        Gets a repository's tags.
        
        Parameters:
            username (str): The username to get tags from.
            repository (str): The repository to get tags from.
            
        Returns:
            list: The repository's tags.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/tags")
        return response.json()
    
    def _get_repository_releases(self, username: str=None, repository: str=None):
        '''
        Gets a repository's releases.
        
        Parameters:
            username (str): The username to get releases from.
            repository (str): The repository to get releases from.
            
        Returns:
            list: The repository's releases.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/releases")
        return response.json()
    
    def _get_repository_deployments(self, username: str=None, repository: str=None):
        '''
        Gets a repository's deployments.
        
        Parameters:
            username (str): The username to get deployments from.
            repository (str): The repository to get deployments from.
            
        Returns:
            list: The repository's deployments.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/deployments")
        return response.json()
    
    def _get_repository_downloads(self, username: str=None, repository: str=None):
        '''
        Gets a repository's downloads.
        
        Parameters:
            username (str): The username to get downloads from.
            repository (str): The repository to get downloads from.
            
        Returns:
            list: The repository's downloads.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        response = self.url_manager._get(self.repository_api + username + "/" + repository + "/downloads")
        return response.json()
    
    def _get_repository_forks(self, username: str=None, repository: str=None):
        '''
        Gets a repository's forks.
        
        Parameters:
            username (str): The username to get forks from.
            repository (str): The repository to get forks from.
            
        Returns:
            list: The repository's forks.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        if self._repository_valid(username, repository):
            response = self.url_manager._get(self.repository_api + username + "/" + repository + "/forks")
            return response.json()
        
        else:
            return "Repository does not exist"
        
    def _get_repository_merges(self, username: str=None, repository: str=None):
        '''
        Gets a repository's merges.
        
        Parameters:
            username (str): The username to get merges from.
            repository (str): The repository to get merges from.
            
        Returns:
            list: The repository's merges.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        if self._repository_valid(username, repository):
            response = self.url_manager._get(self.repository_api + username + "/" + repository + "/merges")
            return response.json()
        
        else:
            return "Repository does not exist"
        
    def _get_repository_milestones(self, username: str=None, repository: str=None):
        '''
        Gets a repository's milestones.
        
        Parameters:
            username (str): The username to get milestones from.
            repository (str): The repository to get milestones from.
            
        Returns:
            list: The repository's milestones.
        '''

        if username is None:
            return "No username provided"
        if repository is None:
            return "No repository provided"
        
        if self._repository_valid(username, repository):
            response = self.url_manager._get(self.repository_api + username + "/" + repository + "/milestones")
            return response.json()
        
        else:
            return "Repository does not exist"
        
    