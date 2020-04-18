class User:
    """
    Class that generates new instances of user.
    """
    user_list = [] # Empty contact list

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
    
#     def save_user (self):
#         '''
#         save user method saves contact
#         '''
#         User.user_list.append(self)

#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run
#         '''
#     def test_save_multiple_user(self):
#         '''
#         test_save_multiple_user to check if we can save multiple users
#         '''
#         self.new_user.save_user()
#         test_user = User("Test","password") #new contact
#         test_user.save_user()
#         self.assertEqual(len(User.user_list),5)

# if __name__ == '__main__':
#     unittest.main()

#     def delete_user(self):

#         '''
#         delete_user method deletes a saved user from the user_list
#         '''

#         User.user_list.remove(self)




    