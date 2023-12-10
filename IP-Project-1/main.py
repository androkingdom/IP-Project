# Library Used
import pandas as pd
import mysql.connector as sqLtor
from sqlalchemy import create_engine
import function

# Variable Used
IsValidUser = False
DatabaseName = "IPProjectDB"
Working = True
Working2 = True

# Login Page
user_df = pd.read_csv("user.csv", names=["UserName", "LoginId"])
if user_df.empty:
    print("!!!No One Is Login!!!")
    print("!!!Please First Login!!!")

else:
    print("+-----------------+")
    print("|     Login       |")
    print("+-----------------+")
    username = input("Enter UserName : ").replace(" ","")
    login_code = input("Enter Login Code : ")
    for i in user_df.itertuples():
        if username == i[1] and login_code == i[2]:
            print("Successfully Logined")
            IsValidUser = True
            break
        else:
            print("Invaild Login ID or Username") 
            print("Not Allowed To Enter In System")

if IsValidUser:
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234')
        cursor = myconnection.cursor()
        table_create = '''
        CREATE TABLE IF NOT EXISTS Sales (OrderDate DATE,Region VARCHAR(30),Manager VARCHAR(30),SalesMan VARCHAR(30),Item VARCHAR(20),Units INT,Unit_price FLOAT,Sale_amt FLOAT);
        '''
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DatabaseName}')
        connection = sqLtor.connect(host = "localhost", user = "root", password = "1234", database = f"{DatabaseName}")

        db_cursor = connection.cursor()
        db_cursor.execute(table_create)

        print ("Database created successfully")
        print("Table created successfully.")
        myconnection.close()
        connection.close()

    except Exception as e:
        print(e)

    try:
        Query = 'SELECT * FROM SALES'
        dbengien = create_engine("mysql+pymysql://root:1234@localhost/IPProjectDB")
        
        alc_connection = dbengien.connect()
        ManagmentSystemDatabase = pd.read_sql(Query , alc_connection)
        if ManagmentSystemDatabase.empty:
            function.insert_data()
    except Exception as e:
        print(e)

# Managment System 
    print("Welcome to the Main Home Page")

    while Working:
        print(":--------- Sales Data Analysis Project---------:")
        print(":--------- Select Choice ---------:")
        dict_of_cho = {1 : "Dashboard" , 2 : "Insert Data",3 : "Delete Data" , 4 : "Exit"}
        for choice_number in dict_of_cho:
                print(f"{choice_number} : {dict_of_cho[choice_number]}")
        print(":--------- -------------- ---------:")
        choice = int(input('Enter Choice Number : '))
        print(":--------- -------------- ---------:")

        match choice:
            case 1 :
                while Working2:
                    print(":--------- DASHBOARD ---------:")
                    print(":--------- Select Choice ---------:")
                    dict_of_dashboard = {1 : "MONTH WISE SALES REVENUE" , 2 : "REIGIONWISE SALES REVENUE", 3 : "SALES PERSON REVENUE" , 4 : "EXIT"}
                    for choice_number in dict_of_dashboard:
                            print(f"{choice_number} : {dict_of_dashboard[choice_number]}")
                    print(":--------- ------------- ---------:")
                    choice_in = int(input('Enter Choice Number : '))
                    print(":--------- ------------- ---------:")

                    if choice_in == 1: 
                        print("========================")
                        print('MONTH WISE SALES REVENUE')
                        print("========================")
                        function.monthwise_sales_graph()
                        break

                    elif choice_in == 2: 
                        print("==========================")
                        print('REIGION WISE SALES REVENUE')
                        print("==========================")
                        function.region_sales_graph()
                        break

                    elif choice_in == 3:
                        print("====================")
                        print('SALES PERSON REVENUE')
                        print("====================")
                        function.sales_person_graph()
                        break

                    elif choice_in == 4:
                        print("Exit")
                        Working2 = False

            case 2 :
                lst = []
                dbeng = create_engine("mysql+pymysql://root:1234@localhost/IPProjectDB")
                conc = dbeng.connect()
                query = "SELECT * FROM Sales;"
                df = pd.read_sql(query, conc)
                for i in df.columns:
                    user = input(f"Enter {i} : ")
                    lst.append(user)
                function.insert_query(lst)
                pass

            case 3 :
                OrderOfDate = input("Enter Date : ")
                NoOFUnit = input("Enter no. of unit : ")
                ItemType = input("Enter item type : ")
                function.delete_query(OrderOfDate , NoOFUnit , ItemType)
                print("Data Deleted!!")

            case 4 :
                print("Exited") 
                Working = False
