import string
import random

class Credential:
    """
    Class that generates new instances of user.
    """
    credential_list = [] # Empty contact list

    def __init__(self,account,acc_username,acc_password):
        self.account = account
        self.acc_username = acc_username
        self.acc_password = acc_password

#     def save_credential (self):
#         '''
#         save credential method saves credentials
#         '''
#         Credential.credential_list.append(self)

#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run
#         '''
#     def test_save_multiple_credential(self):
#         '''
#         test_save_multiple_user to check if we can save multiple users
#         '''
#         self.new_credential.save_credential()
#         test_credential  = Credential("Account","acc_username","acc_password") #new contact
#         test_credential.save_credential()
#         self.assertEqual(len(Credential.credential_list),5)

# if __name__ == '__main__':
#     unittest.main()

#     def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
#         '''
#         Function to generate an 8 character password
#         '''
#         gen_pass=''.join(random.choice(char) for _ in range(size))
#         return gen_pass

#     def delete_credential(self):

#         '''
#         delete_credential method deletes a saved credential from the credential_list
#         '''

#         User.user_list.remove(self)