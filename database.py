import sqlite3
import numpy as np
import pandas as pd

def connection():
    '''Function for creating, connecting the database and cursor'''

    conn = sqlite3.connect('Library6.db')

    c = conn.cursor()
    return conn, c
    
def tab1():
    '''Creates table books.
       Imports data from book_info.txt
    '''
    conn = connection()
    c = connection()
    table1 = """CREATE TABLE books(ID INTEGER PRIMARY KEY, Genre VARCHAR, Title VARCHAR, Author VARCHAR, Purchase_Price INTEGER, Purchase_Date VARCHAR)"""
    c.execute(table1)


    df = pd.read_table("book_info.txt")
    print(df)

    df.to_sql(name="books", con=conn, if_exists='replace')
    conn.commit()
    

def tab2():
    '''Creates table loan_books.
       Imports data from loan_reservation_history.txt
    '''
    conn = connection()
    c = connection()
    table2 = """CREATE TABLE loan_books(Book_ID INTEGER, Reservation_Date VARCHAR, Checkout_Date VARCHAR, Return_Date VARCHAR, Member_ID INTEGER)"""
    c.execute(table2)
    print(table2)
    df2 = pd.read_table("loan_reservation_history.txt")
    print(df2)

    df2.to_sql(name="loan_books", con=conn, if_exists='replace')
    conn.commit()

def alt():
    '''Alters the table initially by adding default value to show book availability'''
    conn = connection()
    c = connection()
    c.execute("""ALTER TABLE books ADD COLUMN Availability TEXT DEFAULT 'Yes'""")

# tab1()
# tab2()

# alt()

# conn.close()
