'''This is program to create a class book with instance object bookid, title and price. Initialise
    them via __init__() method. Also define method to show book variable '''

#class created
class book:
    def __init__(self, bookid=None, title=None, price=None):
        self.bookid=bookid
        self.title=title
        self.price=price
        

    def setdetails(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
        return bookid, title, price

    def getdetails(self):
        book.setdetails(self,self.bookid,self.title,self.price)
        print("Book id : ",self.bookid)
        print("Book title : ",self.title)
        print("Book price : ",self.price)

my_book = book(123, "The Great Gatsby", 9.99)
my_book.getdetails()