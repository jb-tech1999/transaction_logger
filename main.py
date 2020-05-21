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
    print("\t| 2. Exit                                    |")
    print("\t==============================================")


#prints the main menu
def main_menu():
    os.system("cls")
    print("\t==============================================")
    print("\t|            Rapoeli v0.1                    |")
    print("\t==============================================")
    print("\t| 1. Enter Transaction                       |")
    print("\t| 2. Show transactions                       |")
    print("\t| 3. Search                                  |")
    print("\t==============================================")
    print("\t| 4. Add users                               |")
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
         username = '''username'''
         tmp_query = query+username
         print(tmp_query)
         cursor.execute(tmp_query)
         user_data = cursor.fetchone()
         if user_data != "":
             found = False
             return user_data






login()
choice = int(input("Enter choice: "))
if choice == 1:
    username = enterbox("Username:")
    print(check_login(username))
    i = 0
    while i < 3:
        password = passwordbox("Password:")
        if password in check_login(username):
            main_menu()
            break
        else:
            print("Please try again")
            i += 1


else:
    print("Goodbye")
    exit()




