import unittest
from datetime import datetime, timedelta
from Models.account import Member
from Models.book import BookItem
from Models.bookLending import BookLending, Fine
from utils.constants import BookStatus

class TestLibrarySystems(unittest.TestCase):

    def test_return_book(self):
        def setUp(self):
            self.member=Member(id="123",password="password",person="John_yadav")
            self.book_item=BookItem.create_sample_book(barcode="XYZ123")
    def test_checkout_book_item(self):
        result=self.member.checkout_book_item(self.book_item)
        self.assertTrue(result)
        self.assertEqual(self.member.get_total_books_checkedout(),1)

    def test_fine_collection(self):
        Fine.collect_fine("123",extra_days=5)
        self.assertEqual(Fine.fine_records["123"],5)

    def test_check_for_fine_method(self):
        member_id = self.member._Account__id
        lending=BookLending(self.book_item.barcode,member_id)
        lending.due_date=datetime.now().date() - timedelta(days=3)
        self.member.check_for_fine(self.book_item)
        self.assertEqual(Fine.fine_records[member_id],3)

    if __name__=='__main__':
        unittest.main()




