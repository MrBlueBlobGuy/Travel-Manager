import hashlib
from TravelManage.userdb import *


class User:
    def __init__(self, userid) -> None:
        self.userid = userid


def login(userid, password) -> User:
    match = get_user_hashed_password(userid)[0] == hashlib.sha1(password.encode()).hexdigest()
    return User(userid) if match else User('NOUSER')
