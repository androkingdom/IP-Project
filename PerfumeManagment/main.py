# Library Used
import mysql.connector as sqLtor

# =================================================================================================================

def CreateDB(DBname):
    """Create a new database if it doesn't already exist"""
    try:
        query = f"CREATE DATABASE IF NOT EXISTS {DBname}"
        mydb = sqLtor.connect(host="localhost", user="root" ,password = "1234")  # Your MySQL username and password
        cursor = mydb.cursor()
        cursor.execute(query)
        print("Database created successfully ")
    except Exception as e:
        print("Error in creating database ", e)

def CreateTable(TBname):
    """Create a table within the DB"""
    try:
        query = f'''CREATE TABLE IF NOT EXISTS {TBname}(
            Brand_Name VARCHAR(30),
            Brand_Category VARCHAR(30) UNIQUE,
            Brand_Price_In_Dollar INT,
            Brand_Stock INT
        );'''
        TBconn = sqLtor.connect(host="localhost" , user="root" , password="1234" , database="Perfume_Management_System")
        Cursor = TBconn.cursor()
        Cursor.execute(query)
        TBconn.commit()
        print("Table Created Successfully!")
    except Exception as e:
        print("Error in creating Table",e)

def InsertData(TBname:str , Bname:str , BCategory:str , Bprice:int , Bstock:int):
    """Insert data into the table"""

    DataList = [Bname , BCategory , Bprice , Bstock]
    query = f'''INSERT INTO {TBname} VALUES (%s , %s , %s , %s)'''

    TBconn = sqLtor.connect(host="localhost" , user="root" , password="1234" , database="Perfume_Management_System")
    Cursor = TBconn.cursor()
    Cursor.execute(query,DataList)
    TBconn.commit()
    print("Data inserted!")

def result(rec):
    print("\n\n------------------------------SEARCH RESULTS-------------------------")
    Headers = ['Brand Name', 'Brand Category', 'Brand Price', 'Brand Stock']
    for rows in rec:
        i = 0
        for data in rows:
            print(f"{Headers[i]} : {data}")
            i += 1
        print("=====================================================")
    if len(rec)==0:
        print("No results found.")
        print("=====================================================================")

def searchByName(TBname , DBname , Bname:str):
    SearchConn = sqLtor.connect(host="localhost" , user="root" , password="1234" , database=DBname)
    Cursor = SearchConn.cursor()
    query = f"SELECT * FROM {TBname} WHERE Brand_Name LIKE '{Bname}' "
    Cursor.execute(query)
    records = Cursor.fetchall()
    result(records)

def searchByLessPrice(TBname , DBname , Price:int):
    SearchConn = sqLtor.connect(host="localhost" , user="root" , password="1234" , database=DBname)
    Cursor = SearchConn.cursor()
    query = f"SELECT * FROM {TBname} WHERE Brand_Price_In_Dollar <= {Price}"
    Cursor.execute(query)
    records = Cursor.fetchall()
    result(records)

def showTable(DBname , TBname):
    SearchConn = sqLtor.connect(host="localhost" , user="root" , password="1234" , database=DBname)
    Cursor = SearchConn.cursor()
    query = f"SELECT * FROM {TBname}"
    Cursor.execute(query)
    records = Cursor.fetchall()
    result(records)


def InsertDummyData(DBname:str , TBname:str):
    DummyConn = sqLtor.connect(host="localhost" , user="root" , password="1234" , database=DBname)
    Cursor = DummyConn.cursor()
    query = f"SELECT * FROM {TBname}"
    Cursor.execute(query)
    records = Cursor.fetchall()
    if len(records) == 0:
        query2 = f'''INSERT INTO {TBname} VALUES
        ("Dior" , "DIOR J’ADORE EDP" , "118" , "50"),
        ("Dior" , "DIOR VANILLA DIORAMA EDP" , "125" , "127"),
        ("Dior" , "DIOR EDEN-ROC EDP" , "125" , "100"),
        ("Dior" , "DIOR HYPNOTIC POISON EDP" , "102" , "122"),  
        ("Dior" , "DIOR ADDICT EDP" , "84" , "50"),
        ("Gucci" , "Gucci Bloom" , "155" , "50"),
        ("Gucci" , "Gucci Rush For Women" , "127" , "125"),
        ("Gucci" , "Gucci Flora For Women" , "105" , "100"),
        ("Gucci" , "Gucci Bamboo" , "108" , "111"),
        ("Gucci" , "Gucci Memoir D’Une Odeur" , "122" , "123"),
        ("Tom Ford" , "Tom Ford Eau de Soleil Blanc" , "215" , "100"),
        ("Tom Ford" , "Tom Ford Tobacco Vanille" , "180" , "123"),
        ("Tom Ford" , "Tom Ford Métallique" , "235" , "123"),
        ("Tom Ford" , "Tom Ford Tuscan Leather" , "400" , "70"),
        ("Tom Ford" , "Tom Ford Lost Cherry" , "250" , "123")        
        '''
        Cursor.execute(query2)
        DummyConn.commit()
        print("Data Inserted")
# ------------------------------------------------------------------------------------------------------------------------
print()
try:
    dbname = "Perfume_Management_System"
    tname = "AdminTable"

    CreateDB(dbname)
    CreateTable(tname)
    InsertDummyData(dbname , tname)
    print()
    print("-----------------------Perfume Managment System-----------------------")
    while True:
        print()
        print("1: Enter New Data")
        print("2: Retrieve Data")
        print("3: Exit")
        print()
        Administrator = int(input("Enter Choice : "))
        print('=================================')

        if Administrator == 1:
            try:
                Brand_Name = input("Enter Brand Name : ")
                Brand_Category = input("Enter Brand Category : ")
                Brand_Price = int(input("Enter Brand Price : $"))
                InStock = int(input("Enter Number of Items in Stock : "))
                InsertData(tname , Brand_Name , Brand_Category , Brand_Price , InStock)
                print("Data Entered Successfully !")
                showTable(dbname , tname)
            except Exception as e:
                print(e)

        elif Administrator == 2:
            print('1: Search By Brand Name')
            print('2: Search By Price Less Than')
            print('3: Show Table')
            print('4: Exit')
            print()
            Option = int(input("Enter Your Option : "))
            print('===============================')
            if Option == 1:
                BrandName = input("Enter Brand : ")
                searchByName(tname , dbname , BrandName)
            elif Option == 2:
                price = int(input("Enter Minimum Price : $"))
                searchByLessPrice(tname , dbname , price)
            elif Option == 3:
                showTable(dbname , tname)
            elif Option == 4:
                print("Byee !")
                break
            else:
                print("Invalid Command")

        elif Administrator == 3:
            print("Byee Byee !")
            break

        else:
            print("Invalid Command")

except Exception as e:
    print(e)