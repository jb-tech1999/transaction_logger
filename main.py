import pyodbc
import getpass
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

login()
choice = int(input("Enter choice: "))
if choice == 1:
    main_menu()
else:
    print("Goodbye")
    exit()




