from datetime import datetime, timedelta

class BookLending:
    lending_records = {}

    def __init__(self, book_item_barcode, member_id):
        self.book_item_barcode = book_item_barcode
        self.member_id = member_id
        self.lending_date=datetime.now()
        self.due_date=self.lending_date+timedelta(days=10)

        BookLending.lending_records[book_item_barcode]=self

    @staticmethod
    def lend_book(barcode,member_id):
        lending=BookLending(barcode,member_id)
        print(f"lending book with {barcode} to member {member_id}")
        return True
    @staticmethod
    def fetch_lending_details(self,barcode):
        return BookLending.lending_records.get(barcode)

class Fine:
    fine_records={}
    @staticmethod
    def collect_fine(member_id,extra_days):
        fine_amount=extra_days*1
        if member_id in Fine.fine_records:
            Fine.fine_records[member_id]+=fine_amount
        else:
            Fine.fine_records[member_id]=fine_amount
        print(f"Collected amount {fine_amount} from member {member_id}")
        return fine_amount
    def get_fine(self,member_id):
        return Fine.fine_records.get(member_id)