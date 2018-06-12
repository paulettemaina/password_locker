#!/usr/bin/env python3.6
import pyperclip
import string
import random
from user_credentials import User, Credentials

def create_user(login, pword):
    '''
    Function to create a new user
    '''
    new_user = User(login,pword)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def find_user(login):
    '''
    Funtion that finds a user by a login and returns the user
    '''
    return User.find_by_login(login_name)

def check_existing_users(login):
    '''
    Function that checks if a user exists with that login and return a boolean
    '''
    return User.user_exist(login)

def create_credentials(website,username,p_key):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(website,username,p_key)
    return new_credentials

def generate_password(self):
    return generated_passwords

def save_credential(credentials):
    '''
    Function to save Credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(user_id):
    '''
    Funtion that finds a credentials by a user_id and returns the credentials
    '''
    return Credentials.find_by_user_id(user_id)

def check_existing_credential(user_id):
    '''
    Function that checks if a credentials exists with that user_id and return a boolean
    '''
    return Credentials.credentials_exist(user_id)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def copy_credentials_pass_key(user_id):
    '''
    Function that copies email to clipboard
    '''
    return Credentials.copy_pass_key(user_id)

def main():
    print("WELCOME TO PASSWORD LOCKER. ")
    print('\n')

    while True:
        print("Use these short codes :")
        print("\n log - To login into your password_locker account, \n cu - To create a new password_locker account, \n fu - To find user account, \n ex -exit account ")
        short_code = input().lower()


        if short_code == 'cu':
            print('\n')
            print("To create a password_locker account kindly fill in the information below")
            print("Enter your desired password_locker  login name")
            login = input()
            print("Enter your desired password_locker password")
            pword = input()

            save_users(create_user(login,pword))
            print('\n')
            print(f"Welcome {login}. \n")
            print("You have succesfully created a password locker account. You can now log in and save, display, delete or copy youe credentials.")
       

        elif short_code == 'fu':
            print(" \n Enter the login username to find the user account \n")
            search_login = find_user(search_login)
            print(f"Account {search_login.login} exists")
      


        elif short_code == 'log':
            print('\n')
            print("Enter you password_locker login id  ...")
            login = input()
            print("Enter you password_locker login password ...")
            pword = input()

            if check_existing_users(login):             
                logged_user = find_user(login)

                if logged_user == pword:
                    print(f"Welcome {login}")

        while True:
            print('\n')
            print("Please use the following short codes \n    cc-To create a new credential, \n    cpass- To generate a new password, \n    fc - To find a credential, \n    dc- To display credentials, \n    del- to delete a credential, \n    cp- To copy a credential's password \n    ex- to exit")
            log_shortcode=input()

         #   credential_user =logged_user

            if log_shortcode == 'cc':
                print('\n')
                print("Fill in the information below to create a new credential")
                print('\n')
                print("Enter the website")
                website=input()
                print("Enter your username for the website")
                username=input()
                print("Enter your password for the website")
                p_key=input()

                save_credential(create_credentials(website,username,p_key))
                print('\n')
                print(f"You have created a new credential for {website}.")
                print('\n')

            elif log_shortcode == 'cpass':
                print('\n')
                print("Generate a new random password \n")
                print(generate_password)

            elif log_shortcode == 'dc':
                print('/n')
                if display_credentials():
                    for credentials in display_credentials():
                        print(f"{credentials.site}, {credentials.user_id}, {credentials.pass_key}")
                        print('\n')
                else:
                    print("\n Nothing to display")
                    
            elif log_shortcode == 'fc':
                print('/n')
                print("Enter your username for the website you want to find your stored credentials")
                search_username = input()
                if check_existing_credential(search_username):
                    search_credential = find_credentials(search_username) 
                    print(f"{search_username.username} ,  {search_contact.website}")
                    print('-' *20)
                else:
                    print(" \n That credential does not exist")

            elif log_shortcode == 'del':
                print('/n')
                print("Enter the username of the credentials you want to delete")
                del_username = input()
                if check_existing_credential(del_username):
                    search_del_credentials = find_credentials(del_username)
                    del_credential = del_credentials(search_del_credentials)
                    print(f"Deleted credentials of {website} with the {del_username} username ")
                else:
                    print(" \n That credential does not exist")

            elif log_shortcode == 'cp':
                print('/n')
                print("Enter the username of the credential you want to copy")
                copy_user = input()
                if check_existing_credential(copy_user):
                    search_copy_user = find_credentials(copy_user)
                    pyperclip.copy(search_copy_user.pass_key)
                    #copy_search_pass_key = copy_credentials_pass_key(search_copy_user)
                   # print("Copy: {copy_search_pass_key}")

                    print(f"Password has been copied {search_copy_user.pass_key} ")
                else:
                    print(" \n Those credentials don't exist.")
    
            elif log_shortcode =='ex' :
                print("Bye...")
                break

            else:
                print("I really didn't get that. Please use shortcode, Thank you.")                    

if __name__ == '__main__':
    main()
