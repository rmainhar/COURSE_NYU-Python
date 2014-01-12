'''
Assignment 9

Jingxin Zhu

'''


# Function:   valid_username
# Input:      A username to check (string)
# Processing: Evaluates the username based on the following rules:
#             - at least 8 characters long
#             - can only contain alpha numeric characters
#             - must contain at least 1 uppercase character
#             - must contain at least 1 lowercase character
#             - must contain at least 1 numeric character (0-9)
# Output:     Returns two values
#             (1) whether the username provided is valid (Boolean)
#             (2) an error (if it failed) or confirmation (String)
def valid_username(username):
     
     # Mark whether username's length meets the requirement
     flag_length = False
     # Mark whether username contains at least 1 uppercase character
     flag_upper = False
     # Mark whether username contains at least 1 lowercase character
     flag_lower = False
     # Mark whether username contains at least 1 digit
     flag_num = False
     # Mark whether username contains space
     flag_space = False

     # check whether at least 8 characters
     if (len(username)<8):
         flag_length = True
         reason = "username must be greater than 8 characters"
         
     for c in username:
          # contains uppercase character? 
          if c.isupper():
               flag_upper = True
          # contains lowercase character?
          if c.lower():
               flag_lower = True
          # contains digit?
          if c.isdigit():
               flag_num = True
          # contains space?
          if c.isspace():
               flag_space = True
     
     # reason for invalid username         
     if (not flag_upper):
          reason = "username must contain at least one uppercase character"
          
     if (not flag_lower):
          reason = "username must contain at least one lowercase character"

     if (not flag_num):
          reason = "username must contain at least one number"

     if (flag_space):
          reason = "username must only contain alpha numeric characters"

     
     flag_username = (not flag_length) and flag_upper and flag_lower and flag_num and(not flag_space)

     # If valid, reason is empty
     if(flag_username):
          reason = ""
          
     return flag_username, reason



# Function:   valid_password
# Input:      A password to check (string)
#             A username (string)
# Processing: Evaluates the password based on the following rules:
#             - must not contain the username
#             - at least 8 characters long
#             - can only contain alpha numeric characters
#             - must contain at least 1 uppercase character
#             - must contain at least 1 lowercase character
#             - must contain at least 1 numeric character (0-9)
# Output:     Returns two values
#             (1) whether the password provided is valid (Boolean)
#             (2) an error (if it failed) or confirmation (String)
def valid_password(password, username):
     
     f_len = False
     f_cover = False
     f_upper = False
     f_lower = False
     f_num = False
     f_space = False

     # Make sure at least 8 characters
     if (len(username)<8):
         f_len = True
         pw_reason = "password must be greater than 8 characters"
     # Password must not contain username
     if username in password:
          f_cover = True
          pw_reason = "password cannot be used as part of your password"
         
     for c in password:
          if c.isupper():
               f_upper = True
          if c.lower():
               f_lower = True
          if c.isdigit():
               f_num = True
          if c.isspace():
               f_space = True
     
          
     if (not f_upper):
          pw_reason = "password must contain at least one uppercase character"
          
     if (not f_lower):
          pw_reason = "password must contain at least one lowercase character"

     if (not f_num):
          pw_reason = "password must contain at least one number"

     if (f_space):
          pw_reason = "password must only contain alpha numeric characters"

     flag_password = (not f_len) and (not f_cover) and (not f_space) \
                      and f_upper and f_lower and f_num
     
     # If valid, reason is empty
     if(flag_password):
          pw_reason = ""
     return flag_password, pw_reason
