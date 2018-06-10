import unittest
import pyperclip
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
        self.new_user = User("Ace","Ventura","1234")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Ace")
        self.assertEqual(self.new_user.last_name,"Ventura")
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
        test_user = User("Ace","Ventura","1234") #new Contact
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)



if __name__ == '__main__':
    unittest.main()

    

    



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
        self.new_Credentials = Credentials("fb","ace","1234")

    

    

    



