#main_helper.py module
import os
import pyodbc

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

#adds user to database
def add_user(username, password):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=DESKTOP-PND5I06\SQLEXPRESS;"
                          "Database=rapoeli;"
                          "Trusted_Connection=yes;")
    cursor = cnxn.cursor()
    query = ("INSERT INTO users VALUES(?, ?)")
    cursor.execute(query, [username, password])
    cnxn.commit()