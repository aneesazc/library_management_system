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


def recc():
    '''Function for recommending books.
       Displays a bar graph.
    '''
    
    # conn = database.connection()
    # c = database.connection()
    conn = sqlite3.connect('Library6.db')

    c = conn.cursor()
    c.execute("""SELECT books.Genre, COUNT(Checkout_Date) 
    FROM loan_books 
    INNER JOIN books ON books.ID = loan_books.Book_ID GROUP BY Genre""")
    a = c.fetchall()
    # print(a)
    df1 = pd.DataFrame(a, columns=['Genre','No. of Books'])
    # print(df1)

    root = Tk()
    root.title("Recommendation")
    figure1 = plt.Figure(figsize=(13, 10), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack()
    df1 = df1[['Genre', 'No. of Books']].groupby('Genre').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Most Popular books Genre-wise')

    root.mainloop()
