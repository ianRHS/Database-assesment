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
    'A: 1080p monitors with 120hz or higher\n'
    'B: 1440p monitors with 144hz or higher\n'
    'C: highest resolution monitor\n'
    'D: Lowest response time monitor\n'
    'E: most expensive monitor\n'
    'F: cheapest monitor\n'
    'G: biggest screen size monitor\n'
    'H: highest refresh rate monitor\n'
    'I: ACER manufactured monitors\n
    'J: ASUS manufactured monitors\n
    'K: Smallest screen size monitor\n
    'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('1080p monitors with 120hz or higher')
    elif menu_choice == 'B': 
        print_query('1440p monitors with 144hz or higher')
    elif menu_choice == 'C':
        print_query('highest resolution monitor')
    elif menu_choice == 'D':  
        print_query('Lowest response time monitor')
    elif menu_choice == 'E':
        print_query('most expensive monitor')
    elif menu_choice == 'F':
        print_query('cheapest monitor')
    elif menu_choice == 'G':
        print_query('biggest screen size monitor')
    elif menu_choice == 'H':
        print_query('highest refresh rate monitor')
    elif menu_choice == 'I':
        print_query('ACER manufactured monitors')
    elif menu_choice == 'J':
        print_query('ASUS manufactured monitors')
    elif menu_choice == 'K':
        print_query('Smallest screen size monitor')






