######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################

import sqlite3


class Book():
    def __init__(self, name, writer, time, stock):
        self.status = True
        self.name = name
        self.writer = writer
        self.time = time
        self.stock = stock

    def __str__(self):
        return self.stock


class Library():
    def __init__(self):
        self.connectDatabase()
        self.status = True

    def connectDatabase(self):
        self.network = sqlite3.connect("library.db")
        self.cursor = self.network.cursor()

        command = "CREATE TABlE IF NOT EXISTS books(name TEXT, writer TEXT, time INT, stock INT)"
        self.cursor.execute(command)
        self.network.commit()

    def disconnectDatabase(self):
        self.network.close()

    def add(self, object):
        command = "INSERT INTO books VALUES(?,?,?,?)"
        self.cursor.execute(command, (object.name, object.writer, object.time, object.stock))
        self.network.commit()

    def remove(self, name):
        command2 = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(command2, (name))
        deleteBooks = self.cursor.fetchall()

        if (len(deleteBooks) == 0):
            print("There is no such book.")
        else:
            print("The book was deleted.")

        command3 = "DELETE FROM books WHERE name = ?"
        self.cursor.execute(command3, (name,))
        self.network.commit()

    def seeTimes(self, name):
        command = "SELECT * FROM books WHERE name = ?"
        self.cursor.execute(command, name)
        for data in self.cursor.fetchall():
            bookList = []
            bookList.append(data[0:3])
            print("{} - {}".format(bookList[0][0], bookList[0][2]))

    def totalBooks(self):
        command = "SELECT * FROM books"
        self.cursor.execute(command)
        totalStock = self.cursor.fetchall()

        if (len(totalStock) == 0):
            print("There is no suck book.")
        else:
            totalBookStock = 0
            for i in totalStock:
                totalBookStock += i[3]

            print("Total book {}.".format(totalBookStock))

    def see(self):
        self.cursor.execute("SELECT * FROM books")
        for data in self.cursor.fetchall():
            bookList = []
            bookList.append(data[:2])
            print("{} - {}".format(bookList[0][0], bookList[0][1]))

    def exit(self):
        print("See you later.")
        self.status = False


object = Library()


def run():
    print("""
*--> Welcome to your Library <--*
1- Add book.
2- Remove book.
3- See book entry times.
4- How many books are there?
5- See the list of books.
6- Exit
    """)
    while True:
        entry = input("Enter your selection: ")

        if entry == "6":
            object.exit()
            object.disconnectDatabase()

        elif entry == "1":
            name = input("Enter book's name: ")
            writer = input("Enter book's writer: ")
            time = input("Enter date: ")
            stock = 1
            stock = int(stock)

            book = Book(name, writer, time, stock)
            object.add(book)
            print("It's done.")
            run()

        elif entry == "2":
            object.see()
            name = input("The name of the book you want to delete: ")
            object.remove(name)
            run()

        elif entry == "3":
            object.see()
            name = input("The name of the book you want to search: ")
            object.seeTimes(name)
            run()

        elif entry == "4":
            object.totalBooks()
            run()

        elif entry == "5":
            object.see()
            run()

run()