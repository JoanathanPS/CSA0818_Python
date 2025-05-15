class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []
        self.borrowed = {}

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def borrow_book(self, title, user):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                self.borrowed[title] = user
                return f"{user} borrowed {title}"
        return "Book not available"

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                user = self.borrowed.pop(title, None)
                return f"{user} returned {title}"
        return "Book not borrowed"

lib = Library()
lib.add_book("1984", "Orwell")
lib.add_book("Python Basics", "Someone")

print(lib.borrow_book("1984", "Alice"))
print(lib.return_book("1984"))