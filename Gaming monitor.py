# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'gaming_monitors.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()


menu_choice =''
while menu_choice != 'z':
    menu_choice = input('Welcome to the gaming monitors Database!\n\n'
    'type the letter for the information you want:\n'
    'A: monitor names and manufacturer\n'
    'B: monitor names and price\n'
    'C:monitor names of top 10 highest refresh rate sorted by refresh rate\n'
    'D:monitor name of 144hz monitors\n'
    'Z: EXIT\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        





