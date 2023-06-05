from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
today = datetime.now()

import database

import sqlite3

def Return(bookid3):
    '''Function for returning books.
       Takes Book ID.
    '''
    
    # conn = database.connection()
    # c = database.connection()
    conn = sqlite3.connect('Library6.db')

    c = conn.cursor()
    new_bookid = bookid3.get()
    today_str3 = today.strftime("%d-%m-%Y")
    if new_bookid.isdigit():
        c.execute('SELECT * FROM books')
        a = c.fetchall()
        if a[int(new_bookid)-1][7] == "Checked Out":
            c.execute('UPDATE loan_books SET Return_Date=? WHERE Book_ID=? AND Return_Date IS NULL',(today_str3,new_bookid))
            conn.commit()
            b = int(new_bookid)
            c.execute('UPDATE books SET Availability = "Yes" WHERE ID=?',(b,))
            conn.commit()
            messagebox.showinfo("Done", "The book has been returned")
        elif a[int(new_bookid)-1][7] == "Reserved":
            print("error")
            messagebox.showerror("Error", "The Book that is reeserved cannot be returned")
        else:
            messagebox.showerror("Error", "The Book that is available cannot be returned")
    else:
        messagebox.showerror("Error", "Invalid Book ID")

