from repository import Repository
from book import Book
class BookService:
    
    def add_book(self, booksList):
        print("\n----> \tAgregando libro...")
        lastKey = -1
        for key in Repository.booksList:
            lastKey = key
        lastKey = lastKey + 1
        Repositorio.[lastKey] = booksList.__dict__
        print("\n----> \tAgregado.")

    def update_book(self, key, book):
        Repositorio.booksList[key]['_name'] = booksList.name
        Repositorio.booksList[key]['_authorName'] = booksList.authorName
        Repositorio.booksList[key]['_memberLegajo']= booksList.memberLegajo