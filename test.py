from gitsearch import User

user = "rs9f"

if User()._user_valid(user):
    print(User()._get_user(user))