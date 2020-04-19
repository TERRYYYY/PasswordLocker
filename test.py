import unittest # Importing the unittest module
from user import User
from credential import Credential # Importing the user and credential class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class
    '''
    def setUp(self):
        '''Set up method to run before each test cases
        '''
        self.new_user = User("Terry", "hey123")

    def test_init (self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual (self.new_user.user_name,"Terry")
        self.assertEqual (self.new_user.password,"hey123")

if __name__ == '__main__':
    unittest.main ()

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class
    '''
    def setUp(self):
        '''Set up method to run before each test cases
        '''
        self.new_credential = Credential("Instagram", "terrykariuki","girlsrule")

    def test_init (self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual (self.new_credential.account,"Instagram")
        self.assertEqual (self.new_credential.acc_username,"terrykariuki")
        self.assertEqual (self.new_credential.acc_password,"girlsrule")

if __name__ == '__main__':
    unittest.main ()

