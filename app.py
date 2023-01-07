 # localhost/phpmyadmin
 # create   retrieve   update    delete  (crud)
import sys
from dbhelper import DBHelper


class Pritush:

    def __init__(self):
        # this is the correct time to connect to database
        self.db = DBHelper() # this for the connection with the other class

        self.menu()  # ye line se iss class ka sara code execute hone lagjaega

    def menu(self):


        user_input = input("""
        1. Enter 1 to Sign Up
        2. Enter 2 to login
        3. Enter anything else to leave : """)

        if user_input == "1":
            self.Sign_Up()

        elif user_input == "2":
            self.login()

        else:
            sys.exit(1000)

    def login_menu(self):

        input("""
        1. Enter 1 to see the profile 
        2. Enter 2 to edit th profile
        3. Enter 3 to delete the profile 
        4. Enter 4 to logout 
        """)



    def Sign_Up(self):
        name = input("Enter the Name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")


        u = self.db.Sign_Up(name,email,password)
        if u:
            print("Signed up successfully")

        else:
            print("There was an error please try again later")
        self.menu()

    def login(self):
        email = input("Enter your email : ")
        password = input("Enter password : ")

        data = self.db.search(email,password)
        if len(data) == 0:
            print(" Incorrect email or password please try again ")
            self.login()
        else:
            print("Hello ",data[0][1])
            self.login_menu()



obj = Pritush()