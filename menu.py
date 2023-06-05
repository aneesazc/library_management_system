from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
today = datetime.now()

import database

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


#importing the functions from other files
from bookSearch import SearchRecord
from bookCheckout import CheckOut, Reserve
from bookReturn import Return
from BookSelect import recc


def Lib():
    SearchRecord(SEARCH, tree)

def check():
    CheckOut(bookid,memid,today)

def res():
    Reserve(bookid2,memid2,today)

def ret():
    Return(bookid3)

def popular():
    recc()

    
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
btn_search = Button(LeftViewForm, activebackground="#5F5F9E", text="Search", bg="#0052cc", fg="#ffffff", command=Lib)
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

#setting width of the columns
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

button1 = Button(frame1, activebackground="#5F5F9E", text="Checkout", bg="#0052cc", fg="#ffffff", command = check)
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

button2 = Button(frame2, activebackground="#5F5F9E", text="Reserve",bg="#0052cc", fg="#ffffff", command = res)
button2.pack(side=TOP, padx=10, pady=10, fill=X)


#setting the return part
frame3 = LabelFrame(LeftViewForm, text="Returning Books", padx=40,pady=40)
frame3.pack(padx=5, pady=5)

label6 = Label(frame3, text = "Book ID")
label6.pack(side=TOP, anchor=W)
bookid3 = Entry(frame3)
bookid3.pack(side=TOP, padx=10, fill=X)

button3 = Button(frame3, activebackground="#5F5F9E", text="Return", bg="#0052cc", fg="#ffffff", command = ret)
button3.pack(side=TOP, padx=10, pady=10, fill=X)


#setting the recommendation part
frame = LabelFrame(text="Reccomendation", padx=20,pady=20)
frame.pack(padx=100, pady=100)

label7 = Label(frame, text = "Budget of the Library: 500 pounds")
label7.pack(side=TOP, anchor=W)
button4 = Button(frame, font= ('Helvetica 10 bold'), activebackground="green", text="Popular Genres" , command = popular, 
padx=10, pady=10, width=20, height=1, bg="#0052cc", fg="#ffffff")
button4.pack()


#running the mainloop
if __name__=='__main__':
    mainloop()