#imports
import mysql.connector
import pandas as pd

#create a connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789",
  database="mydatabase")

#assigning cursor
mycursor = mydb.cursor()

#create table
mycursor.execute("CREATE TABLE IF NOT EXISTS stock ( \
    Company_Name VARCHAR(50), \
    Date DATE, \
    Time TIME, \
    Open Float, \
    Close Float, \
    High Float, \
    Low Float)")

#checking last updated row
mycursor.execute("SELECT COUNT(*) FROM stock")  
skip_rows = list(mycursor)[0][0]

#reading csv
data = pd.read_csv('C:/Users/VK/Desktop/1 Project/stock.csv', 
                  skiprows=[i for i in range (1, skip_rows + 1)])
data_stock = data[['Company_Name', 'Date', 'Time', 'Open', 'Close', 'High', 'Low']]

#new data insertion
insert = "INSERT INTO stock (Company_Name, Date, Time, Open, Close, High, Low) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)"
for i, row in data_stock.iterrows():
    mycursor.execute(insert, list(row))

#final commit    
mydb.commit()
