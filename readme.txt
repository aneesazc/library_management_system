Library Management System Project

For executing the project main.py is used which contains all the functions and code in the same file.

menu.py imports all the data and functions from different files but unfortunately does not run in the virtual environment. 
Only main.py runs in the virtual environment.



NOTE: run main.py for executing the program instead of menu.py



We start by creating a database.py file which is used to create a database. 

The book_info.txt file is imported and a table named books is created. 
We alter the table later and add a column to show the availability of the books.

The loan_reservation_history.txt is imported and a table named loan_books is created. 

bookSearch.py is then created to make functions for searching books from the database. 
Treeview is used show all the books with its details like ID, Genre, Author, Purchase Date, 
Price, Availability after entering the book title in the search box.


bookCheckout.py is created to check out available books. Two functions are used checkout() and reserve().

checkout() takes Book ID and Member ID
from the user, checks if it's valid, checks if the books are available and lets us check out a book. 
If the book is already checked out it shows a messagebox to reserve a book.

reserve() takes Book ID and Member ID from the user, checks if it's valid, checks if the book is checked out and lets us reserve a book. 
If the book is already reserved or available it shows a messagebox with the appropriate message.


bookReturn.py is created to return a checked out book. 
It contains the function Return() which takes the Book ID from the user checks if the book has been checked out, 
if it has been checked out then return date is updated in the database and the book is returned.


bookSelect.py is created to recommend book genres. 
It counts and displays the genres of the book that has been checked out and reserved the most. 
We plot the 'No. of books' and 'Genre' into a bar graph which lets the librarian know which popular genre to order based on the library budget.


test cases:

For searching: 
Book = "d"

shows all the book title copies and other book details that have a d in them

Book = "dune"

shows all the book title copies and other book details with that book title


For checking out:
Book ID = 1
Member = 234
 
Error message showing invalid Member ID

Book ID = 1
Member = 23##

Error message showing invalid Member ID

Book ID = 1
Member = 2333

message that says that the book has been checked out

Book ID = 5(previously reserved)

an error message pops up that says that that a book that is reserved

If the same Book ID is entered the message shows the book has already been checked out and to reserve a book


For reserving:
Book ID = 1
Member = 234
 
Error message showing invalid Member ID

Book ID = 1
Member = 23##

Error message showing invalid Member ID

Book ID = 1
Member = 2399

message shows that the book has been successfully reserved

If the same Book ID is entered the message prompts us to try a different book ID

If a book ID that is already reserved or available is entered the message prompts us to try a different book ID


For returning:
Book ID = ##

error message that shows that an invalid Book ID had been used

Book ID = 5(previously reserved)

an error message pops up that says that that a book that is reserved cannot be returned

Book ID = 2(an ID that is available i.e neither checked out nor reserved)

an error message pops up that says that that a book that is available cannot be returned

Book ID = 1(checked out book)

a message that shows that the book has been returned



menu.py is the main file which imports and calls all the other data, functions and which is used by 
the librarian for the management of the books(since this does not work in virtual environment main.py is used instead)