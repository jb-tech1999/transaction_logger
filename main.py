import pyodbc
from easygui import passwordbox
from easygui import msgbox, enterbox
import os

#function to print login menu
def  login():
    os.system("cls")
    os.system("color a")

    print("\t==============================================")
    print("\t|            Rapoeli v0.1                    |")
    print("\t==============================================")
    print("\t| 1. Login                                   |")
    print("\t| 2. Add user                                |")
    print("\t| 3. Exit                                    |")
    print("\t==============================================")


#prints the main menu
def main_menu():
    os.system("cls")
    print("\t==============================================")
    print("\t|            Rapoeli v0.3                    |")
    print("\t==============================================")
    print("\t| 1. Enter Transaction                       |")
    print("\t| 2. Show transactions                       |")
    print("\t| 3. Search                                  |")
    print("\t==============================================")
    print("\t| x. Exit                                    |")
    print("\t==============================================")

#check login credentials
def check_login(username):
     cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=DESKTOP-PND5I06\SQLEXPRESS;"
                          "Database=rapoeli;"
                          "Trusted_Connection=yes;")
     cursor = cnxn.cursor()
     query = "SELECT * FROM users WHERE userName = "
     found = True
     while found:
         username = "'" + username + "'"
         tmp_query = query+username
         cursor.execute(tmp_query)
         user_data = cursor.fetchone()
         if user_data != "":
             found = False
             return user_data
         else:
             break

def add_user(username, password):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=DESKTOP-PND5I06\SQLEXPRESS;"
                          "Database=rapoeli;"
                          "Trusted_Connection=yes;")
    cursor = cnxn.cursor()
    query = ("INSERT INTO users VALUES(?, ?)")
    cursor.execute(query, [username, password])
    cnxn.commit()




login() # print the login menu
choice = int(input("Enter choice: ")) # asks for a choice
if choice == 1: # if choice = 1, user wil be prompt to enter username, if username is found, check for password
    username = enterbox("Enter username: ", "Username")
    print(check_login(username))
    if check_login(username) != "None":
        run = False
        i = 0
        while i < 3:
            password = passwordbox("Enter password","Password")
            if password in check_login(username):
                main_menu()
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
            add_user(username, password)
            run = False
            main_menu()
            ask = int(input("Enter choice"))
        else:
            print("Password doesn't match")





else:
    print("Goodbye")
    exit()




