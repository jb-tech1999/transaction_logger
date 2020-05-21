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
     while True:
         tmp_query = query+username
         print(tmp_query)
         cursor.execute(tmp_query)
         for row in cursor:
             print(row)
             break
     cursor.close()





login()
choice = int(input("Enter choice: "))
if choice == 1:
    username = enterbox("Username:")
    check_login(username)
    #password = passwordbox("Password:")
    main_menu()
else:
    print("Goodbye")
    exit()




