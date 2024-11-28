# SQL to CSV Exporter

This Python script retrieves data from a SQL Server database and exports it to a CSV file. It demonstrates two approaches for exporting the data: using the `csv` module and the `pandas` library.

## Features
- Connects to a SQL Server database using `pyodbc`.
- Executes an SQL query to retrieve data from a specified table.
- Exports the data to a CSV file with UTF-8 encoding.
- Provides two methods for exporting:
  - Using Python's built-in `csv` module.
  - Using the `pandas` library for efficient data handling.

## Prerequisites
To run this script, you need:
- Python 3.x installed on your system.
- Required Python libraries:
  - `pyodbc`
  - `pandas`
  - `csv` (built-in).
- Access to a SQL Server database and credentials for connection.

## How to Use
1. Update the SQL Server connection details:
   ```python
   conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=your_server;'
                         'Database=your_database;'
                         'Trusted_Connection=yes;')
