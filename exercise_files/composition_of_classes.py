class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self. author = author
        self.chapters = []

    def addChapter(self, chapter):
        self.chapters.append(chapter)

    def getPageCount(self):
        pagesCount = 0
        for chapter in self.chapters:
            pagesCount += chapter.pages
        return pagesCount

class Author:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"{self.fname} {self.lname}"
    
class Chapter:
    def __init__(self, name, pages) -> None:
        self.name = name
        self.pages = pages

author = Author("Leo", "Tolstoy")
book = Book("War and peace", 39.0, author)

book.addChapter(Chapter("Chapter 1", 125))
book.addChapter(Chapter("Chapter 2", 97))
book.addChapter(Chapter("Chapter 3", 143))

print(book.title)
print(book.author)
print(book.getPageCount())