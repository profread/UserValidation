import webbrowser
import math
import string
import random
import re
import pprint

# Container for storing employees data
staffDetails = {'profread025@gmail.com': {'password': 'Omogbolahanxyz', 'first_name': 'Ridwan', 'last_name': 'Adeyemi'}}

# Email Verification Function to verify valid email address
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Generates Random Password for new users at during sign up
def passwordGenerator (first_name, last_name):
    password_length = 5
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase  # specifies the type of chracter needed through ASCII
    randomString = ''.join(random.choice(chars) for _ in range(password_length))
    generated_password = first_name[0:2] + last_name[-2:] + randomString
    return generated_password  # releases the output of the input

#Allow users to input a desired password
def user_preffered_password(newEmail, first_name, last_name):
    desired_password = input("Enter a valid password with 7 or more Character: ")
    if ((len(desired_password)) >= 7):
        confirmdesired_password = input("Confrim Password:")
        if (desired_password == confirmdesired_password):
            staffDetails[newEmail] = {'password': desired_password, 'first_name': first_name, 'last_name': last_name}
            print("Account Was created sucessfully")
            print("\nKindly Login to confirm your sign-up")
            authenticateUser()  # Log-in page function
        else:
            user_preffered_password(newEmail, first_name, last_name)
    else:
        print("\nInput a password that is above length 7")
        user_preffered_password(newEmail, first_name, last_name)

#Populates randomly generated password for 
def confirmPassWord(newEmail, first_name, last_name):
    password = passwordGenerator(first_name, last_name)
    print("Your password is " + password)
    reply = input("Are you okay with this custom password ? y/n")
    if (reply.lower() == 'y'):
        staffDetails[newEmail] = {'password': password, 'first_name': first_name, 'last_name': last_name}
        print("Registration Sucessful!\n")
        pprint.pprint(staffDetails[newEmail])
        print("\nLogin to confirm your sign-up")
        authenticateUser()
    elif (reply.lower() == 'n'):
        user_preffered_password(newEmail, first_name, last_name)
    else:
        createUserAcccount()
    return


#create new user account 

def createUserAcccount():
    print("\n-------------------------- WELCOME CREATE A NEW ACCOUNT --------------------------")
    print("\n----------EMAIL MUST CONTAIN domain 'hng.tech.com'-------------\n")
    print("\n----------Enter Your FIRST NAME, DOT(.) AND LAST NAME----------\n"
          "\n--Eg. xyz@hng.tech.com--\n")
    newEmail = input("Enter a valid email address: ").lower()
    if (re.search(regex, newEmail)):
        if verifyAccount(newEmail):
            print("User Exist!! Try again")
            homeAnyOther()
        else:
            domain = newEmail.split('@')[1]
            if domain == "hng.tech.com":
                first_name = input("Enter your first name: ").lower()
                last_name = input("Enter your last name: ").lower()
                confirmPassWord(newEmail, first_name, last_name)
            else:
                print("Invalid Email Address Domain\n Enter the company domain")
                createUserAcccount()
    else:
        print("Invalid Email Address")
        createUserAcccount()

# userUI interface


def homeAnyOther():
    print("\n-------------------------- KINDLY CHOOSE WHAT NEXT --------------------------\n")
    print("1. Do you want to return to home page?")
    print("2. Do you want to exit\n")
    ui_prompt = input("Reply: ")
    if (ui_prompt == '1'):
        userUI()
    elif (ui_prompt == '2'):
        exit()
    else:
        exit()


#check if user already exist"""
def verifyAccount(email):
    if email in staffDetails.keys():
        return email
    return False


"""This function handles the Log-In page"""


def authenticateUser():
    print("\n--------------------------LOG IN--------------------------")
    print("\n----------NOTE THAT YOUR EMAIL MUST HAVE THE DOMAIN 'hng.tech.com'----------\n")
    userEmail = input("Enter email address: ").lower()
    userPassword = input("Enter password: ")
    if userEmail in staffDetails.keys():
        if staffDetails[userEmail]['password'] == userPassword:
            print("You're logged in\n")
            pprint.pprint(staffDetails[userEmail])
            homeAnyOther()

    else:
        print("You are not authorized!\nWrong Email or password!!!")
        print("\n-------------KINDLY CHOOSE WHAT NEXT-------------\n")
        print("1. Do you want to attempt the log in again?")
        print("2. Do you want to return to home page?")
        print("3. Do you want to open an Account with us\n")
        ui_prompt = input("Reply: ")
        if (ui_prompt == '1'):
            authenticateUser()
        elif (ui_prompt == '2'):
            userUI()
        elif (ui_prompt == '3'):
            createUserAcccount()
        else:
            exit()

#User Interface
def userUI():
    print("\n-------------------------------------------------------WELCOME TO HNG TECH-------------------------------------------------------\n")
    print("------------------------------------- HOME PAGE -------------------------------------\n")
    print("\n----------NOTE: THAT YOUR EMAIL MUST HAVE THE DOMAIN 'hng.tech.com'=>=>=>=>=>\n")
    print("1. New Employee? Set up Your Account:")
    print("2. Log In")
    print("3. Exit\n")

    ui_prompt = int(input("Reply: "))
    if (ui_prompt == 1):
        createUserAcccount()
    elif (ui_prompt == 2):
        authenticateUser()
    elif (ui_prompt == 3):
        exit()
    else:
        print("Enter a valid option")
        homeAnyOther()


# Creates an infinite loop to run the program
# It also handles Task 5
var = 1
while var == 1:
    userUI()
