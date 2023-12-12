import pandas as pd
import mysql.connector as sqLtor
from sqlalchemy import create_engine

print("!! Project Have Some Error To Fix !!")

def insert_query():
    global strnglst
    global lst_of_record
    global use_str
    tup_of_records = tuple(lst_of_record)
    mycursor = connection.cursor()
    query = f"insert into {table_name} values {use_str}"
    mycursor.execute(query, tup_of_records)
    connection.commit()
    print(f"-----------\n{mycursor.rowcount} record inserted.\n-----------")
    lst_of_record.clear()
    strnglst.clear()
 
def delete_query(primfield , primkey , tbname):
    mycursor = connection.cursor()
    query = f"delete from {tbname} where {primfield} = {primkey}"
    mycursor.execute(query)
    connection.commit()
    print(f"-----------\n{mycursor.rowcount } record deleted.\n-----------")

def create_database(DatabaseName = "class"):
    try:
        myconnection = sqLtor.connect( host = 'localhost' , user = 'root', password = '1234',port="3306")
        cursor = myconnection.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DatabaseName}')
        print ("Database created successfully")
        myconnection.close()
    except Exception as e:
        print(e)

def show_tables(database = 'class'):
    connection = sqLtor.connect(host = "localhost", user = "root", passwd = "1234" , database = database)
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES;")
    if cursor.fetchall() == []:
        return False

def create_table(database = 'class'):
    print("---------------------")
    print("Creating Table")
    print("---------------------")
    TableName = input("Enter Table Name : ")

    dict_of_constraints = {1 : "NOT NULL" , 2 : "UNIQUE" ,  3 : "DEFAUL" , 4 : "CHECK" , 5 : "PRIMARY KEY" , 6 : None}
    dict_of_datatype = {1 : "CHAR" , 2 : "VARCHAR" ,  3 : "INT" , 4 : "DECIMAL(N,F)"}
    dict_of_table = {}
    dict_of_type = {}

    connection = sqLtor.connect(host = "localhost", user = "root", passwd = "1234" , database = database)
    number_of_field = int(input("Enter Number Of Field : "))
    print()

    for fields in range(number_of_field):
        field_name = input(f"Enter Name of the field {fields+1} : ")
        print()

        for const in dict_of_constraints:
            print(f"{const} : {dict_of_constraints[const]}")
        constraints = int(input("Enter Constraints: "))
        dict_of_table[field_name] = dict_of_constraints[constraints]
        print()

        for TYPE in dict_of_datatype:
            print(f"{TYPE} : {dict_of_datatype[TYPE]}")
        data_type = int(input("Enter Data Type : "))
        match data_type:
            case 1:
                 length = int(input("Enter Length : "))
                 dict_of_type[dict_of_datatype[data_type]] = length
            case 2:
                 length = int(input("Enter Length : "))
                 dict_of_type[dict_of_datatype[data_type]] = length
            case 3:
                 length = int(input("Enter Length : "))
                 dict_of_type[dict_of_datatype[data_type]] = length
            case 4:
                N = int(input("Enter Total Digits : "))
                F = int(input("Enter Decimal Places : "))
                dict_of_type[dict_of_datatype[data_type]] = (N,F)
        print()
    print(f"{dict_of_table} : {dict_of_type}")
    field = list(dict_of_table.keys())
    constr = list(dict_of_table.values())

    data_typ = list(dict_of_type.keys())
    data_typ_size = list(dict_of_type.values())
    print("")
    create_table_string = f"create table if not exists {TableName} ("
    for fieldss in range(number_of_field):
        if None in constr:
            constr[constr.index(None)] = ""

        create_table_string += f"{field[fieldss]} {constr[fieldss]} {data_typ[fieldss]}({data_typ_size[fieldss]}) ,"
    create_table_string = create_table_string[:-1] + ");"
    print(create_table_string)

    cursor = connection.cursor()
    cursor.execute(create_table_string)
    connection.commit()
    print("Table Created Successfully!")
    df = pd.read_sql(f"Select * from table {TableName}" , connection)
    print(df)


# -----------------------------------------------------------------------------

try:
    create_database()
    connection = sqLtor.connect( host = 'localhost' , user = 'root' , passwd = '1234' , database = "class" )
    cursor = connection.cursor()
    cursor.execute("Show Tables ;")
    TablesDict = {}
    key = 1
    
    lst_of_record = []
    strnglst = []
 
    dbengine = create_engine("mysql+pymysql://root:1234@localhost/class")
    conn = dbengine.connect()
    print("1 : Use Table")
    print("2 : Create New Table")
    if show_tables() != False:
        choice_of_table_selection = int(input("Enter Choice : "))
        match choice_of_table_selection:
            case 1:
                print("-------------")
                print("Select Tables")
                print("-------------")

                for table_name in cursor.fetchall():
                    TablesDict[key] = table_name
                    key += 1
                for i in TablesDict:
                    print(f"{i} : {list(TablesDict[i])}")

                print("-----------------")
                table_no = int(input("Enter table name : "))
                for name in list(TablesDict[table_no]):
                    table_name_ = name
                print(table_name_)
                print("-----------------")
            
                df1 = pd.read_sql(f"select * from {table_name_} ;" , conn)
                column_of_df1 = df1.columns
                lst_of_column = list(column_of_df1)
                print(df1)

                while True:
                    
                    dic_of_choice = {1 : "Insert", 2 : "Revert", 3 : "Delete"}
                    print("---------------------")
                    for choices in dic_of_choice:
                        print(f"{choices} - {dic_of_choice[choices]}")
                    print("4 - close")
                    choice = int(input("Enter choice : "))
                    print("---------------------")

                    match choice:
                        case 1 :
                            for field in lst_of_column:
                                records = input(f"Enter {field} : ")
                                lst_of_record.append(records)
                                strnglst.append("%s")
                            tup = tuple(strnglst)
                            strg = ",".join(tup)
                            use_str = f"({strg})"
                            insert_query()
                        case 2 :
                            pass
                        case 3 : 
                            tbname = table_name_
                            primfield = input("Enter unique field name : ")
                            primkey = input("Enter field id : ")
                            delete_query(primfield , primkey , tbname)
                        case 4 :
                            print("Loop Exit")
                            break
                        case _ :
                            print("Wrong Input")
            
                    dbengine1 = create_engine("mysql+pymysql://root:1234@localhost/class")
                    connectiona= dbengine.connect()
                    df2 = pd.read_sql(f"select * from {table_name_}" , connectiona) 
                    print(df2)
            case 2:
                create_table()
                    

    else:
        print("-----------------")
        print("NO TABLE EXIST") 
        print("-----------------")
        create_table()
        
except Exception as e :
    print(e)
    print("Program Exit")