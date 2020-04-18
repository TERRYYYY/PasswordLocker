#!/usr/bin/env python3.7
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

def create_credential(account,acc_username,acc_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account,acc_username,acc_password)
    return new_credential

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

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(acc_name):
    '''
    Function that finds a credential
    '''
    return Credential.find_by_username(acc_name)

def check_existing_credentials(acc_name):
    '''
    Function that checks if a credential exists
    '''
    return Credential.credential_user(acc_name)

# def display_credential():






