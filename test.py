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

    

    

    



