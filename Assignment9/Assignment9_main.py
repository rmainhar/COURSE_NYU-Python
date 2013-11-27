'''
Assignment 9: main function
'''
import uservalidation

# get a username from the user
username = input("Username: ")

# validate username
result, reason = uservalidation.valid_username(username)

# if it isn't valid we should tell them why
if not(result):
    print (reason)

# otherwise the username is good - ask them for a password
else:
    # get a password from the user
    password = input("Password: ")

    # determine if the password is valid
    pwresult, pwreason = uservalidation.valid_password(password, username)

    # if the password isn't valid we should tell them why
    if not(pwresult):
        print (pwreason)
    else:
        print ("Username and Password combination is valid!")
