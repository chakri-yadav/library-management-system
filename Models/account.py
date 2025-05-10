from abc import ABC
from datetime import datetime, timedelta
from Models.bookLending import BookLending,Fine
from utils.constants import BookStatus


class Account(ABC):
    def __init__(self,id,password,person,status="Active"):
        self.__id=id
        self.__password=password
        self.__status=status
        self.__person=person
    def get_id(self):
        return self.__id

    def reset_password(self,new_password):
        self.__password=new_password
        print(f"Password reset for account {self.__id}")

class Librarian(Account):
    def __init__(self,id,password,person,status="Active"):
        super().__init__(id,password,status,person)

    def add_book(self,book):
        print(f"book '{book}' has been added to the catalog")
    def remove_book(self,book):
        print(f"book '{book}' has been removed from the catalog")
    def block_member(self,member):
        print(f"Member '{member} has been blocked")
    def un_block_member(self,member):
        print(f"Member '{member} has been unblocked")


class Member(Account):
    def __init__(self,id,password,person,status="Active"):
        super().__init__(id,password,person,status)
        self.__date_of_membership=datetime.today().date()
        self.__total_books_checked_out=0
    def get_total_books_checked_out(self):
        return self.__total_books_checked_out
    def reserve_book(self):
        pass
    def checkout_book_item(self, book_item):
        if self.__total_books_checked_out>=5:
            print("Cannot check out")
            return False
        if book_item.get_status()!=BookStatus.AVAILABLE:
            print("Book not available")
            return False
        print(f"Book '{book_item} has been checkout")
        self.__total_books_checked_out+=1
        return True

    def return_book_item(self,book_item):
        print(f"Book {book_item} has been returned")
        self.__total_books_checked_out-=1
        return True
    def check_for_fine(self, book_item):
        lending = BookLending.lending_records.get(book_item.get_barcode())
        if not lending:
            print("No Lending record found")
            return
        due_date = lending.due_date
        today = datetime.today()
        if today.date() > due_date:
            delay = (today.date() - due_date).days
            Fine.collect_fine(self.get_id(), delay)




