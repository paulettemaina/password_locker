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
             Credentials of person that matched the login_name.
        '''

        for user in cls.user_list:
            if user.login_name == login_name:
                return user

    @classmethod
    def user_exist(cls,login_name):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for user in cls.user_list:
            if user.login_name == login_name:
                    return True

        return False






class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__(self,site,user_id,pass_key):
        self.site = site
        self.user_id = user_id
        self.pass_key = pass_key

    def save_credentials(self):
        '''
        save_credentials method saves credentials object into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
    
