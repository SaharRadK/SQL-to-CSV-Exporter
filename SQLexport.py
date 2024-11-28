# Import the required libraries
import pyodbc
import csv
import pandas as pd

# Connect to the SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=your_server_name;'
                      'Database=your_DB_name;'
                      'Trusted_Connection=yes;')

# SQL query to select data from the table
sql_query = "SELECT * FROM apnuser_for140301"

# Using the csv module
with open('apnuser_140301.csv', 'w', newline='', encoding='UTF-8-sig') as file:
    writer = csv.writer(file)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    # Write the header
    writer.writerow([x[0] for x in cursor.description])
    
    # Write the data
    for row in cursor:
        writer.writerow(row)

# Using the pandas package
df = pd.read_sql_query(sql_query, conn)
df.to_csv('apnuser_140301.csv', index=False, encoding='UTF-8-sig')