from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
today = datetime.now()

import sqlite3

conn = sqlite3.connect('Library6.db')

#creating window
window = Tk()
window.title("LMS")
width= window.winfo_screenwidth()
height= window.winfo_screenheight()

#setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.iconbitmap("images/img6.ico")
global tree
global SEARCH
SEARCH = StringVar()



def SearchRecord():
    '''Function to search the database
        for books
    '''
    
    if SEARCH.get() != "":
        
        tree.delete(*tree.get_children())

        conn = sqlite3.connect('Library6.db')

        cursor=conn.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + str(SEARCH.get()) + '%',))

        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def DisplayData():
    '''Function the access dsiplay the book details
       from the database
    '''

    tree.delete(*tree.get_children())

    conn = sqlite3.connect('Library6.db')

    cursor=conn.execute("SELECT * FROM books")

    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def CheckOut():
    '''Function for checking out books.
       Takes Book ID and Member ID.
    '''

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

def Reserve():
    '''Function for resreving books.
       Takes Book ID and Member ID.    
    '''

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

def Return():
    '''Function for returning books.
       Takes Book ID.
    '''
    
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

def recc():
    '''Function for recommending books.
       Displays a bar graph.
    '''
    
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


#creating frame
TopViewForm = Frame(window, width=500, bd=1, relief=SOLID)
TopViewForm.pack(side=TOP, fill=X)
LeftViewForm = Frame(window, width=500)
LeftViewForm.pack(side=LEFT, fill=Y)
MidViewForm = Frame(window)
MidViewForm.pack(side=TOP)
mylabel = Label(TopViewForm, text="Library Management System", font=('verdana', 18), width=600,bg="#5F5F9E",fg="white")
mylabel.pack(fill=X)
label_txt = Label(LeftViewForm, text="Book", font=('verdana', 15))
label_txt.pack(side=TOP, anchor=W)

#setting the search box for book search
search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
search.pack(side=TOP, padx=10, fill=X)
btn_search = Button(LeftViewForm, activebackground="#5F5F9E", text="Search", bg="#0052cc", fg="#ffffff", command=SearchRecord)
btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

#setting scrollbar
scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
tree = ttk.Treeview(MidViewForm, columns=("", "ID", "Genre", "Title","Author","Purchase Price", "Purchase Date", "Availability"),)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

#setting headings for the columns
tree.heading('', text="")
tree.heading('ID', text="ID")
tree.heading('Genre', text="Genre")
tree.heading('Title', text="Title")
tree.heading('Author', text="Author")
tree.heading('Purchase Price', text="Purchase Price")
tree.heading('Purchase Date', text="Purchase Date")
tree.heading('Availability', text="Avaibility")

# setting width of the columns
tree.column('#0', width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=50)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=150)
tree.column('#5', stretch=NO, minwidth=0, width=150)
tree.column('#6', stretch=NO, minwidth=0, width=100)
tree.column('#7', stretch=NO, minwidth=0, width=100)
tree.pack()



#setting the checkout
frame1 = LabelFrame(LeftViewForm, text="Checking Out Books", padx=40,pady=40)
frame1.pack(padx=10, pady=10)

label1 = Label(frame1, text = "Book ID")
label1.pack(side=TOP, anchor=W)
bookid = Entry(frame1)
bookid.pack(side=TOP, padx=10, fill=X)

label3 = Label(frame1,text = "Member ID")
label3.pack(side=TOP, anchor=W)
memid = Entry(frame1)
memid.pack(side=TOP, padx=10, fill=X)

button1 = Button(frame1, activebackground="#5F5F9E", text="Checkout", bg="#0052cc", fg="#ffffff", command = CheckOut)
button1.pack(side=TOP, padx=10, pady=10, fill=X)


#setting the reservation part
frame2 = LabelFrame(LeftViewForm, text="Reserving Books", padx=40,pady=40)
frame2.pack(padx=10, pady=10)

label4 = Label(frame2, text = "Book ID")
label4.pack(side=TOP, anchor=W)
bookid2 = Entry(frame2)
bookid2.pack(side=TOP, padx=10, fill=X)

label5 = Label(frame2,text = "Member ID")
label5.pack(side=TOP, anchor=W)
memid2 = Entry(frame2)
memid2.pack(side=TOP, padx=10, fill=X)

button2 = Button(frame2, activebackground="#5F5F9E", text="Reserve",bg="#0052cc", fg="#ffffff", command = Reserve)
button2.pack(side=TOP, padx=10, pady=10, fill=X)


#setting the return part
frame3 = LabelFrame(LeftViewForm, text="Returning Books", padx=40,pady=40)
frame3.pack(padx=5, pady=5)

label6 = Label(frame3, text = "Book ID")
label6.pack(side=TOP, anchor=W)
bookid3 = Entry(frame3)
bookid3.pack(side=TOP, padx=10, fill=X)

button3 = Button(frame3, activebackground="#5F5F9E", text="Return", bg="#0052cc", fg="#ffffff", command = Return)
button3.pack(side=TOP, padx=10, pady=10, fill=X)


#setting the recommendation part
frame = LabelFrame(text="Recommendation", padx=20,pady=20)
frame.pack(padx=100, pady=100)

button4 = Button(frame, font= ('Helvetica 10 bold'), activebackground="green", text="Popular Genres" , command = recc, 
padx=10, pady=10, width=20, height=1, bg="#0052cc", fg="#ffffff")
button4.pack()


#calling function
DisplayData()

#running the mainloop
if __name__=='__main__':
    mainloop()