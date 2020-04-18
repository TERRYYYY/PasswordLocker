import string
import random
import pyperclip

class Credential:
    """
    Class that generates new instances of user.
    """
    credential_list = [] # Empty contact list

    def __init__(self,account,acc_username,acc_password):
        self.account = account
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_credential (self):
        '''
        save credential method saves credentials
        '''
        Credential.credential_list.append(self)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_user to check if we can save multiple users
        '''
        self.new_credential.save_credential()
        test_credential  = Credential("Account","acc_username","acc_password") #new contact
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),5)

if __name__ == '__main__':
    unittest.main()

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
    
    @classmethod
    def find_by_username(cls,name):
        '''
        Method that takes in a  account username and returns an account that matches that account username
        '''
        for credential in cls.credential_list:
            if credential.acc_username == name:
                return credential

    @classmethod
    def credential_exist(cls,acc_name):
        '''
        Method that checks if a credential exists from credential list
        '''
        for credential in cls.credential_list:
            if credential.acc_username == acc_name:
                return True

        return False

    @classmethod
    def display_credential(cls,acc_name):
        '''
        Method that returns the credential list
        '''
        return cls.credential_list

    
