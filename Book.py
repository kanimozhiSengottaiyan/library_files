import functions
import random

class books():
    def __init__(self):
        self.flag = 0


    def bookInserting(self):
        Books = functions.getDteails_book()
        self.num_Insert=int(input("Enter the num of times u have to insert the Books : "))
        for i in range(self.num_Insert):
            self.shelfid = input("Enter shelfid :")
            if self.shelfid in Books:
                self.numBooks = int(input("Enter the num of books :"))
                self.count=self.numBooks + len(Books[self.shelfid])
                if self.numBooks <= 10:
                    for i in range(self.numBooks):
                        self.bookid =random.randint(5000,6000)
                        print(self.bookid)
                        self.bookName=input("Enter the Book name :")
                        self.bookPrice=input("Enter the Price :")
                        self.bookAuthor=input("Enter the author name :")
                        Books[self.shelfid][self.bookid] = {'Bookname': self.bookName,'Price': self.bookPrice,'Author' : self.bookAuthor}

                else:
                    print("Shelf has no space")

            else:
                print("This shelfid is missing")
        #print(Books)
        functions.setDetails_book(Books)

    print("-" * 100)


    def find_BookDetails(self):

        Books = functions.getDteails_book()
        self.search=input("Enter the bookid")
        for i in Books:
            if self.search in Books[i].keys():
                print("The book is in the shelf :",i)
                print("Bookname:",Books[i][self.search]['Bookname'])
                print("Author:",Books[i][self.search]['Author'])
                print("Price:",Books[i][self.search]['Price'])
                self.flag+=2
        if self.flag==0:
            print("Book is not available")
        print("-"*100)

    def shelfDisplay(self):
        Books=functions.getDteails_book()
        search1 = input("Enter the shelf id : ")
        if search1 in Books.keys():
            print("The books in the shelf are",Books[search1].keys())
            self.flag=1
        if self.flag==0:
            print("No such shelf")
        print("-"*100)

    def TotalBooks(self):
        self.total = 0
        Books = functions.getDteails_book()
        for key in Books:
          #  print(len(Books[key]))
            #self.total=len(Books[key])
            self.total += len(Books[key].keys())
        print(self.total)
        print("-"*100)




