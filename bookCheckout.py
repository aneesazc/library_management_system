from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
today = datetime.now()

import sqlite3

from tkinter import messagebox
import database

def CheckOut(bookid,memid,today):
    '''Function for checking out books.
       Takes Book ID and Member ID.
    '''

    # conn = database.connection()
    # c = database.connection()
    conn = sqlite3.connect('Library6.db')

    c = conn.cursor()

    new_bookid = bookid.get()
    new_memid = memid.get()
    today_str = today.strftime("%d-%m-%Y")
    if len(new_memid) == 4 and new_memid.isdigit():
        c.execute('SELECT * FROM books')
        a = c.fetchall()
        # print(a)
        if a[int(new_bookid)-1][7] == "Yes":
            c.execute("INSERT INTO loan_books(Book_ID,Checkout_Date,Member_ID) VALUES(?,?,?)",(new_bookid,today_str,new_memid))
            conn.commit()
            b = int(new_bookid)
            c.execute('UPDATE books SET Availability = "Checked Out" WHERE ID=?',(b,))
            conn.commit()
            messagebox.showinfo("Succesful", "The Book has been checked out")
        elif a[int(new_bookid)-1][7] == "Reserved":
            messagebox.showerror("Error", "The book is reserved")
        else:
            # print("error")
            messagebox.showerror("Error", "Already Checked out. Reserve a book instead")
        
    else:
        messagebox.showerror("Error", "Invalid Member ID")


def Reserve(bookid2,memid2,today):
    '''Function for resreving books.
       Takes Book ID and Member ID.    
    '''

    # conn = database.connection()
    # c = database.connection()
    conn = sqlite3.connect('Library6.db')

    c = conn.cursor()
    new_bookid = bookid2.get()
    new_memid = memid2.get()
    today_str2 = today.strftime("%d-%m-%Y")
    if len(new_memid) == 4 and new_memid.isdigit():
        c.execute('SELECT * FROM books')
        a = c.fetchall()
        if a[int(new_bookid)-1][7] == "Checked Out":
            c.execute("INSERT INTO loan_books(Book_ID,Reservation_Date,Member_ID) VALUES(?,?,?)",(new_bookid,today_str2,new_memid))
            conn.commit()
            b = int(new_bookid)
            c.execute('UPDATE books SET Availability = "Reserved" WHERE ID=?',(b,))
            conn.commit()
            messagebox.showinfo("Succesful", "The Book has been reserved succesfully")
        else:
            messagebox.showinfo("Error", "Try a different Book ID")
    else:
        messagebox.showerror("Error", "Invalid Member ID")
