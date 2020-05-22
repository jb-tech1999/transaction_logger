import pyodbc
from easygui import passwordbox
from easygui import msgbox, enterbox
import os
import main_helper as mh


mh.login() # print the login menu
choice = int(input("Enter choice: ")) # asks for a choice
if choice == 1: # if choice = 1, user wil be prompt to enter username, if username is found, check for password
    username = enterbox("Enter username: ", "Username")
    if mh.check_login(username) != "None":
        run = False
        i = 0
        while i < 3:
            password = passwordbox("Enter password","Password")
            if password in mh.check_login(username):
                mh.main_menu()
                ask = int(input("Enter choice"))

            else:
                print("Please try again")
                i += 1
    else:
        login()

elif choice == 2:
    run = True
    username = enterbox("Enter username", "Username ")
    while run:
        password = passwordbox("Enter password ", "Password")
        password2 = passwordbox("Enter password again", "Password check")
        if password == password2:
            mh.add_user(username, password)
            run = False
            mh.main_menu()
            ask = int(input("Enter choice"))
        else:
            print("Password doesn't match")





else:
    print("Goodbye")
    exit()




