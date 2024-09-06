# Library Used
import pandas as pd
import mysql.connector as sqLtor
from matplotlib import pyplot
from sqlalchemy import create_engine

# DataFrame Of Graph
monthwise_sales_df = {}
region_sales_df = {}
sales_person_df = {}

# UDF To Be Used
def insert_data():
    try:
        db_connection = sqLtor.connect(host='localhost',user='root',password='1234',database='IPProjectDB')
        cursor = db_connection.cursor()
        insert_query = '''
        INSERT INTO Sales (Orderdate, Region, Manager, salesMan, Item, Units, Unit_price, Sale_amt)
        VALUES
        ('2018-01-06', 'East', 'Martha', 'Alexander', 'Television', 95, 1198.00, 113810.00),
        ('2018-01-23', 'Central', 'Hermann', 'Shelli', 'Home Theater', 50, 500.00, 25000.00),
        ('2018-02-09', 'Central', 'Hermann', 'Luis', 'Television', 36, 1198.00, 43128.00),
        ('2018-02-26', 'Central', 'Timothy', 'David', 'Cell Phone', 27, 225.00, 6075.00),
        ('2018-03-15', 'West', 'Timothy', 'Stephen', 'Television', 56, 1198.00, 67088.00),
        ('2018-04-01', 'East', 'Martha', 'Alexander', 'Home Theater', 60, 500.00, 30000.00),
        ('2018-04-18', 'Central', 'Martha', 'Steven', 'Television', 75, 1198.00, 89850.00),
        ('2018-05-05', 'Central', 'Hermann', 'Luis', 'Television', 90, 1198.00, 107820.00),
        ('2018-05-22', 'West', 'Douglas', 'Michael', 'Television', 32, 1198.00, 38336.00),
        ('2018-06-08', 'East', 'Martha', 'Alexander', 'Home Theater', 60, 500.00, 30000.00),
        ('2018-06-25', 'Central', 'Hermann', 'Sigal', 'Television', 90, 1198.00, 107820.00),
        ('2018-07-12', 'East', 'Martha', 'Diana', 'Home Theater', 29, 500.00, 14500.00),
        ('2018-07-29', 'East', 'Douglas', 'Karen', 'Home Theater', 81, 500.00, 40500.00),
        ('2018-08-15', 'East', 'Martha', 'Alexander', 'Television', 35, 1198.00, 41930.00),
        ('2018-09-01', 'Central', 'Douglas', 'John', 'Desk', 2, 125.00, 250.00),
        ('2018-09-18', 'East', 'Martha', 'Alexander', 'Video Games', 16, 58.50, 936.00),
        ('2018-10-05', 'Central', 'Hermann', 'Sigal', 'Home Theater', 28, 500.00, 14000.00),
        ('2018-10-22', 'East', 'Martha', 'Alexander', 'Cell Phone', 64, 225.00, 14400.00),
        ('2018-11-08', 'East', 'Douglas', 'Karen', 'Cell Phone', 15, 225.00, 3375.00),
        ('2018-11-25', 'Central', 'Hermann', 'Shelli', 'Video Games', 96, 58.50, 5616.00),
        ('2018-12-12', 'Central', 'Douglas', 'John', 'Television', 67, 1198.00, 80266.00),
        ('2018-12-29', 'East', 'Douglas', 'Karen', 'Video Games', 74, 58.50, 4329.00),
        ('2019-01-15', 'Central', 'Timothy', 'David', 'Home Theater', 46, 500.00, 23000.00),
        ('2019-02-01', 'Central', 'Douglas', 'John', 'Home Theater', 87, 500.00, 43500.00),
        ('2019-02-18', 'East', 'Martha', 'Alexander', 'Home Theater', 4, 500.00, 2000.00),
        ('2019-03-07', 'West', 'Timothy', 'Stephen', 'Home Theater', 7, 500.00, 3500.00),
        ('2019-03-24', 'Central', 'Hermann', 'Luis', 'Video Games', 50, 58.50, 2925.00),
        ('2019-04-10', 'Central', 'Martha', 'Steven', 'Television', 66, 1198.00, 79068.00),
        ('2019-04-27', 'East', 'Martha', 'Diana', 'Cell Phone', 96, 225.00, 21600.00),
        ('2019-05-14', 'Central', 'Timothy', 'David', 'Television', 53, 1198.00, 63494.00),
        ('2019-05-31', 'Central', 'Timothy', 'David', 'Home Theater', 80, 500.00, 40000.00),
        ('2019-06-17', 'Central', 'Hermann', 'Shelli', 'Desk', 5, 125.00, 625.00),
        ('2019-07-04', 'East', 'Martha', 'Alexander', 'Video Games', 62, 58.50, 3627.00),
        ('2019-07-21', 'Central', 'Hermann', 'Sigal', 'Video Games', 55, 58.50, 3217.50),
        ('2019-08-07', 'Central', 'Hermann', 'Shelli', 'Video Games', 42, 58.50, 2457.00),
        ('2019-08-24', 'West', 'Timothy', 'Stephen', 'Desk', 3, 125.00, 375.00),
        ('2019-09-10', 'Central', 'Timothy', 'David', 'Television', 7, 1198.00, 8386.00),
        ('2019-09-27', 'West', 'Timothy', 'Stephen', 'Cell Phone', 76, 225.00, 17100.00),
        ('2019-10-14', 'West', 'Douglas', 'Michael', 'Home Theater', 57, 500.00, 28500.00),
        ('2019-10-31', 'Central', 'Martha', 'Steven', 'Television', 14, 1198.00, 16772.00),
        ('2019-11-17', 'Central', 'Hermann', 'Luis', 'Home Theater', 11, 500.00, 5500.00),
        ('2019-12-04', 'Central', 'Hermann', 'Luis', 'Home Theater', 94, 500.00, 47000.00);
        '''
        
        cursor.execute(insert_query)
        print("Table data inserted successfully.")
        db_connection.commit()
        db_connection.close()
    except Exception as e:
        print(e)

def monthwise_sales_graph():
    global monthwise_sales_df
    try:
        myconnection = sqLtor.connect(host='localhost',user='root',password='1234',port='3306',database='IPProjectDB')

        cursor = myconnection.cursor()
        query = '''
        SELECT MONTHNAME(MIN(OrderDate)) AS Month, SUM(Sale_amt) AS TotalSales FROM Sales
        GROUP BY MONTH(OrderDate)
        ORDER BY MONTH(OrderDate);
        '''
        cursor.execute(query)
        result = cursor.fetchall()
        monthwise_sales_df = pd.DataFrame(result, columns=['Month', 'TotalSales'])
        monthwise_sales_df.plot(x='Month' , y='TotalSales')
        pyplot.xticks(rotation = 0)
        pyplot.title('Total Monthwise Sales')
        print(monthwise_sales_df)
        pyplot.show()
        myconnection.close()

    except Exception as e:
        print(e)

def region_sales_graph():
    global region_sales_df
    dbengine1 = create_engine("mysql+pymysql://root:1234@localhost/IPProjectDB")
    connection = dbengine1.connect()
    regions_query = "SELECT DISTINCT Region FROM Sales;"
    regions_df = pd.read_sql(regions_query, connection)
    print("Select a region from the following list:")
    for index, row in regions_df.iterrows():
        print(f"{index + 1}. {row['Region']}")

    region_index = int(input("Enter the number corresponding to the region: ")) - 1
    selected_region = regions_df.loc[region_index, 'Region']

    query = f"""
        SELECT Manager, SUM(Sale_amt) AS SalesRevenue
        FROM Sales
        WHERE Region = '{selected_region}'
        GROUP BY Manager;
    """

    region_sales_df = pd.read_sql_query(query, connection)
    region_sales_df.plot.bar(x='Manager',y='SalesRevenue')
    pyplot.xticks(rotation = 0)
    pyplot.title(f'{selected_region} Region - Sales Revenue by Manager')
    print(region_sales_df)
    pyplot.show()

def sales_person_graph():
    global sales_person_df
    dbengine1 = create_engine("mysql+pymysql://root:1234@localhost/IPProjectDB")
    connection = dbengine1.connect()
    query = f""" select salesman ,sum(sale_amt) AS SalesRevenue from sales GROUP BY salesman; """
    sales_person_df = pd.read_sql_query(query, connection)
    sales_person_df.plot(x="salesman",y="SalesRevenue")
    pyplot.xticks(rotation = 0)
    pyplot.title(" Sales Revenue - SALESMAN")
    print(sales_person_df)
    pyplot.show()
    connection.close()

def insert_query(lst_of_record,table_name = "sales"):
    con = sqLtor.connect(host = 'localhost' ,user = 'root' , passwd = '1234' , database = "IPProjectDB")
    tup_of_records = tuple(lst_of_record)
    mycursor = con.cursor()
    query = f"insert into {table_name} values (%s , %s , %s , %s ,%s , %s , %s ,%s)"
    mycursor.execute(query, tup_of_records)
    print("Data Enter Successfully")
    con.commit()
    con.close()

def delete_query(userdate , unit_enter, item_enter  ,tbname = "sales", ):
    con = sqLtor.connect(host = 'localhost' ,user = 'root' , passwd = '1234' , database = "IPProjectDB")
    mycursor = con.cursor()

    query = f"delete from {tbname} where Orderdate = {userdate} and units = {unit_enter} and item = {item_enter}"
    mycursor.execute(query)
    con.commit()
    con.close()

def LoginId():
    import random
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    login_id = ''
    for i in range(2):
        login_id += random.choice(letters)
    for i in range(2):
        login_id += random.choice(letters)
    for j in range(2):
        numbers = random.randint(0, 10)
        login_id += str(numbers)
    for j in range(2):
        numbers = random.randint(0, 10)
        login_id += str(numbers)
    return login_id


# Function - 2 ==> This Function Prevent Repetition Of User Name
def unique_(matchcase):
    df = pd.read_csv("user.csv", names=["UserName", "LoginId"])
    for row in df.itertuples():
        lst_of_data = list(row)
        user_name = lst_of_data[1]
        if str(user_name).capitalize() == str(matchcase).capitalize():
            return False

def AlphaInUserName(username):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    for letter in letters :
        if letter in username:
            if len(str(username)) >= 4 and len(str(username)) < 12:
                return True