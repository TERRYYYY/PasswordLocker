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
