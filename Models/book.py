from abc import ABC
from utils.constants import BookStatus, BookFormat


class Book(ABC):
    def __init__(self, ISBN, title, subject, publisher,Number_Of_pages,languages):
        self.__ISBN=ISBN
        self.__title=title
        self.__subject=subject
        self.__publisher=publisher
        self.__Number_Of_Pages=Number_Of_pages
        self.__languages=languages
        self.__authors=[]
    def add_author(self,author):
        self.__authors.append(author)


class BookItem(Book):
    def __init__(self, barcode, is_reference_only, price, due_date, book_format: BookFormat, borrowed, status:BookStatus, date_of_purchase, placed_at, publication_date,
                 ISBN,title, subject,languages=None):
        super().__init__(ISBN, title, subject,languages)
        self.__barcode=barcode
        self.__is_reference_only=is_reference_only
        self.__price=price
        self.__due_date=due_date
        self.__book_format=book_format
        self.__borrowed=borrowed
        self.__status=BookStatus.AVAILABLE
        self.__date_of_purchase=date_of_purchase
        self.__placed_at=placed_at
        self.__publication_date=publication_date
    def checkout(self,member_id):
        if self.__is_reference_only:
            print("The book is only for reference purpose and can't be checked out")
            return False
        self.__status="LOANED"
        return True
    def get_barcode(self):
        return self.__barcode

    @staticmethod
    def create_sample_book(barcode="ABC123",status=BookStatus.AVAILABLE):
        from datetime import datetime, timedelta
        return BookItem(
            barcode=barcode,
            status=status,
            is_reference_only=False,
            price=10.0,
            due_date=datetime.now() + timedelta(days=14),
            book_format=BookFormat.HARDCOVER,
            borrowed=False,
            date_of_purchase=datetime.now().date(),
            placed_at="A3_shelf",
            publication_date=datetime.now().date(),
            title="Sample Book",
            author="John_yadav",
            subject="programming",
            ISBN="123-4567890123"
        )



