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
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def check_existing_users(name):
    '''
    Function that checks if a user exists with that name and return boolean
    '''
    return User.user_exist(name)