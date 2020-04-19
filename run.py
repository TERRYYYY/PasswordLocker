#!/usr/bin/python3.7 
from user import User
from credential import Credential 

#==== create user account ======
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

#===== save the newly created account ====
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

#===== delete an existing user ====
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

#==== verify existing user ==============
def check_existing_users(name):
    '''
    Function that checks if a user exists with that name and return boolean
    '''

    return User.user_exist(name)

#====== create a credential =====
def create_credential(account,acc_username,acc_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account,acc_username,acc_password)
    return new_credential

#===== save the newly created credential =======
def save_credential(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential()

def generate_password():
    '''
    Function that generates a password
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

#===== delete an obsolete credential =======
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

#======= finding a saved credential =======
def find_credential(acc_name):
    '''
    Function that finds a credential
    '''
    return Credential.find_by_username(acc_name)


#======= checking for existing credential =======
def check_existing_credentials(acc_name):
    '''
    Function that checks if a credential exists
    '''
    return Credential.credential_user(acc_name)

#======= view/display all credentials =======
def display_credential():
    '''
    Function that returns all saved credentials
    '''
    return Credential.display_credential()

def main():
    print("Hello.Please Input your name")
    your_name = input()
    print(f "Hey there! {your_name}. Welcome to Password Locker. ")
    print(' ')
    print('\n')

    while True:
        print('Hey {your_name} !')
        print(' ')
        print('''Let's explore these Password Locker Options: - Select from: 
              1 - Create a password Locker account
              2 - Log into an existing password locker account
              3 - Create new credential
              4 - Display credential
              5 - Find a credential
              6 - Delete credential
              x - Exit the credential display mode''')


            short_code = input()

            if short_code == '1':
                print("New Password locker account")
                print("-" * 10)

                print("Username:")
                username = input()

                print("Password:")
                password = input()

                save_user(create_user(username,password)) #create and save new user
                print('\n')
                print( "New Password Locker account")
                print (' ')
                print (f "{username} created")
                print('\n')

            elif short_code == '2':
                print ("-" *40)
                print(' ')
                print(f "Fill in your details to log into your account")
                print("Your Username")
                username = input()
                print ("Your password")
                password = input()

                for user in User.user_list:
                    if user == username:
                        print ("You are already registered")
                    else :
                        print("You are already logged in to the account")
                    break 
                    print('\n')
            
            elif short_code == '3':
                print("Create new credential")
                print("-"*100)

                print(" Enter your Account name")
                account= input()

                print(" Enter your prefered Account username")
                acc_username = input()

                while True:
                    print(' ')
                    print("-" *60)
                    print("Please choose one of these:")
                    print("a - Enter password")
                    print("b - Generate password")
                    password_choice = input()
                    print("-"*60)
                    if password_choice == 'a':
                        print(" ")
                        acc_password = input("Enter your password")
                        break
                    elif password_choice == 'b':
                        acc_password = generate_password()
                        break
                    else:
                        print("Please try again")
                save_credential(create_credential(account,acc_username,acc_password)) #create and save new credentials
                print ('\n')
                print(f"New Credential is {account}, *{acc_username}* **{acc_password}**")
                print('\n')
            
            elif short_code == '4':
                if display_credential():
                    print("Here is a list of all your credentials")
                    print('\n')

                    for credential in display_credential():
                        print(f"Account: {credential.account} Account Username{credential.acc_username} Account Password:{credential.acc_password}")
                        print(' ')
                else:
                    print(' ')
                    print("There are no credentials saved")
                    print(' ')
            
            elif short_code == '5':
                print("Enter your account username")

                search_accountusername = input()
                if check_existing_credentials (search_accountusername):
                    found_username = find_credential(search_accountusername)
                    print(' ')
                    print("Here are your saved credentials")
                    print(f'Account:{found_username.account}, Account username:{found_username.acc_username}, Account Password: {found_username.acc_password}')
                    print(' ')
                else:
                    print("That username does not exist")
                    print(' ')
            elif short_code == '6':
                print( 'Delete a credential you no longer need')
                print( ' ')
                to_delete = input('Search for the account to delete:')
                if check_existing_credentials(to_delete):
                    search_accountusername = find_credential(to_delete)
                    print(' ')
                    confirm = input("Confirm delete: yes or no").lower()
                    if confirm == 'yes':
                        delete_credential(search_accountusername)
                        print('Delete successful')
                        print(' ')
                        break
                    elif confirm == 'no':
                        continue
                    else:
                        print('Credential does not exist')
                        print(' ')
                        break 
            elif short_code == 'x':
                print(' ')
                print("Thank you for your time.Goodbye!")
                print(' ')
                break
            else:
                print("Sorry,I didn't quite catch that, Please use the given short codes.")

if __name__ == '__main__':

    main()



                

                

                








