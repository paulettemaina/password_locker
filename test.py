import unittest
import pyperclip
from random import randint
from user_credentials import User, Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_user = User("Ace","1234")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.login_name,"Ace")
        self.assertEqual(self.new_user.password,"1234")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user 
        object is saved into the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test-save_multiple_user to check if we can save multiple 
        user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Ace","1234") #new User
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_find_user_by_login_name(self):
        '''
        test to check if we can find a credentials by login_name and display information
        '''

        self.new_user.save_user()
        test_user = User("Ace","1234") #new user
        test_user.save_user()

        found_user = User.find_by_login_name("Ace")
        self.assertEqual(found_user.login_name,test_user.login_name)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_user.save_user()
        test_user = User("Ace","1234") # new credentials
        test_user.save_user()

        user_exists = User.user_exist("Ace")

        self.assertTrue(user_exists)


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_credentials = Credentials("fb","Ventura","0000")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.site,"fb")
        self.assertEqual(self.new_credentials.user_id,"Ventura")
        self.assertEqual(self.new_credentials.pass_key,"0000")




    
    
    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials 
        object is saved into the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test-save_multiple_user to check if we can save multiple 
        user objects to our user_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("fb","Ventura","0000") #new User
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("fb","Ventura","0000") #new credentials
        test_credentials.save_credentials

        self.new_credentials.delete_credentials()# Deleting a credentials object
        self.assertEqual(len(Credentials.credentials_list),0)

    def test_find_credentials_by_user_id(self):
        '''
        test to check if we can find a credentials by phone user_id and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("fb","Ventura","0000") #new credentials
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_user_id("Ventura")
        self.assertEqual(found_credentials.user_id,test_credentials.user_id)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("fb","Ventura","0000") # new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Ventura")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_pass_key(self):
        '''
        Test to confirm that we are copying the pass_key address from a found credentials
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_pass_key("Ventura")

        self.assertEqual(self.new_credentials.pass_key,pyperclip.paste())





if __name__ == '__main__':
    unittest.main()

    

    



