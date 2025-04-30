from enum import Enum
from datetime import datetime, timedelta

class BookFormat(Enum):
    HARDCOVER="HARDCOVER"
    PAPERBACK="PAPERBACK"
    EBOOK="EBOOK"
    AUDIOBOOK="AUDIOBOOK"


class BookStatus(Enum):
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    CHECKED_OUT="CHECKED_OUT"
    LOST = "LOST"






