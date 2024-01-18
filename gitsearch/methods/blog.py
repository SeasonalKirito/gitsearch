from ..url_manager import url_manager

class Blog:
    def __init__(self) -> None:
        self.url_manager = url_manager()
        self.user_api = "https://api.github.com/users/"

    def _get_blog(self, username: str=None, blog: str=None):
        '''
        Gets a user's blog.

        Parameters:
            username (str): The username to get blog from.
            blog (str): The blog to get.

        Returns:
            str: The user's blog.
        '''

        if username is None:
            return "No username provided"

        if blog is None:
            return "No blog provided"

        response = self.url_manager._get(self.user_api + username + "/blog/" + blog)
        return response.json()
    
    def _get_blog_posts(self, username: str=None):
        '''
        Gets a user's blog posts.

        Parameters:
            username (str): The username to get blog posts from.

        Returns:
            list: The user's blog posts.
        '''

        if username is None:
            return "No username provided"

        response = self.url_manager._get(self.user_api + username + "/blog/posts")
        return response.json()
    
    def _get_blog_post(self, username: str=None, blog_post: str=None):
        '''
        Gets a user's blog post.

        Parameters:
            username (str): The username to get blog post from.
            blog_post (str): The blog post to get.

        Returns:
            str: The user's blog post.
        '''

        if username is None:
            return "No username provided"

        if blog_post is None:
            return "No blog post provided"

        response = self.url_manager._get(self.user_api + username + "/blog/" + blog_post)
        return response.json()
    
    def _get_blog_post_comments(self, username: str=None, blog_post: str=None):
        '''
        Gets a user's blog post comments.

        Parameters:
            username (str): The username to get blog post comments from.
            blog_post (str): The blog post to get comments from.

        Returns:
            list: The user's blog post comments.
        '''

        if username is None:
            return "No username provided"

        if blog_post is None:
            return "No blog post provided"

        response = self.url_manager._get(self.user_api + username + "/blog/" + blog_post + "/comments")
        return response.json()
    
    def _get_blog_post_comment(self, username: str=None, blog_post: str=None, comment: str=None):
        '''
        Gets a user's blog post comment.

        Parameters:
            username (str): The username to get blog post comment from.
            blog_post (str): The blog post to get comment from.
            comment (str): The comment to get.

        Returns:
            str: The user's blog post comment.
        '''

        if username is None:
            return "No username provided"

        if blog_post is None:
            return "No blog post provided"

        if comment is None:
            return "No comment provided"

        response = self.url_manager._get(self.user_api + username + "/blog/" + blog_post + "/comments/" + comment)
        return response.json()
    
    def _get_blog_post_comment_reactions(self, username: str=None, blog_post: str=None, comment: str=None):
        '''
        Gets a user's blog post comment reactions.

        Parameters:
            username (str): The username to get blog post comment reactions from.
            blog_post (str): The blog post to get comment reactions from.
            comment (str): The comment to get reactions from.

        Returns:
            list: The user's blog post comment reactions.
        '''

        if username is None:
            return "No username provided"

        if blog_post is None:
            return "No blog post provided"

        if comment is None:
            return "No comment provided"

        response = self.url_manager._get(self.user_api + username + "/blog/" + blog_post + "/comments/" + comment + "/reactions")
        return response.json()
    
    def _get_blog_post_comment_reaction(self, username: str=None, blog_post: str=None, comment: str=None, reaction: str=None):
        '''
        Gets a user's blog post comment reaction.

        Parameters:
            username (str): The username to get blog post comment reaction from.
            blog_post (str): The blog post to get comment reaction from.
            comment (str): The comment to get reaction from.
            reaction (str): The reaction to get.

        Returns:
            str: The user's blog post comment reaction.
        '''

        if username is None:
            return "No username provided"

        if blog_post is None:
            return "No blog post provided"

        if comment is None:
            return "No comment provided"

        if reaction is None:
            return "No reaction provided"

        response = self.url_manager._get(self.user_api + username + "/blog/" + blog_post + "/comments/" + comment + "/reactions/" + reaction)
        return response.json()