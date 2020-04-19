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

    def test_save_user(self):
        '''
        test_save_user test to test if the user object is saved into the user list
        '''
        self.new_user.save_user() #saving a new user
        self.assertEqual(len(User.user_list))

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("name" "hey123")
        test_user.save_user()

        self.new_user.delete_user() #deleting a user
        self.assertEqual(len(User.user_list),1)

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

    def tearDown(self):
        Credential.credential_list = []
    '''
    Method that cleans up after each test case has run
    '''


    def test_init (self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual (self.new_credential.account,"Instagram")
        self.assertEqual (self.new_credential.acc_username,"terrykariuki")
        self.assertEqual (self.new_credential.acc_password,"girlsrule")

    def test_save_credential(self):
        '''
        test_save_credential test to test if the credential object is saved into the credential list
        '''
        self.new_credential.save_credential() #saving a new user
        self.assertEqual(len(Credential.credential_list))

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our cr4edential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Instagram" "terrykariuki","hey123")
        test_credential.save_credential()

        self.new_credential.delete_credential() #deleting a user
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_username(self):
        '''
        test to check if we can find a credential by account username and display info
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Instagram" "terrykariuki","hey123")
        test_credential.save_credential()

        found_username = Credential.find_by_username("Instagram")

        self.assertEqual(found_username.account,test_credential.account)

    def test_display_credential(self):
        '''
        test whether one can view all the account credentials that they have created/saved
        '''
        self.new_credential.save_credential()
        account_2 = Credential("Facebook","Rihanna","mypassword")
        account_2.save_credential()
        self.assertEqual)(len(Credential.credential_list))


if __name__ == '__main__':
    unittest.main ()


