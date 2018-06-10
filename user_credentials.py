import pyperclip
class User:
    '''
    Class that generates new instances of users
    '''
    user_list = [] # Empty user list

    def __init__(self,login_name,password):
        self.login_name = login_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user object into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def find_by_login_name(cls,login_name):
        '''
        Method that takes in a login_name and returns a user that matched that login_name.

        Args:
            login_name: Phone login_name to search for
        Returns:
             Contact of person that matched the login_name.
        '''

        for user in cls.user_list:
            if user.login_name == login_name:
                return user





class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    Credentials_list = []

    def __init__(self,website_name,user_name,pass_key):
        self.website_name = website_name
        self.user_name = user_name
        self.pass_key = pass_key
    
