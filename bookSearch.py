from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
today = datetime.now()

# import sqlite3

# conn = sqlite3.connect('Library6.db')

#creating window
# window = Tk()

# window.title("LMS")
# global tree
# global SEARCH
# SEARCH = StringVar()

from tkinter import messagebox
import database

import sqlite3

def SearchRecord(SEARCH, tree):
    '''Function to search the database
       for books
    '''
    # conn = database.connection()
    # c = database.connection()
    conn = sqlite3.connect('Library6.db')

    c = conn.cursor()
    
    if SEARCH.get() != "":
        
        tree.delete(*tree.get_children())


        c=conn.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + str(SEARCH.get()) + '%',))

        fetch = c.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        c.close()
        conn.close()
