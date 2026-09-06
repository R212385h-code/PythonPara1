class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book1 = Book("Python Programming", "Ngoni", 15)
book2 = Book("Computer Science", "Tacu", 20)

book1.display()
book2.display()