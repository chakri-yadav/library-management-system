# 📚 Library Management System (LLD Implementation in Python)

This project is a comprehensive **Low-Level Design (LLD)** implementation of a Library Management System, built using **Python 3** and solid **Object-Oriented Programming (OOP)** principles. It is structured to reflect real-world systems, focusing on clean architecture, modular design, code readability, and maintainability.

The project serves as a **reference-grade LLD model for entry-level software engineering roles**, and simulates the actual business logic followed in library domains such as book checkout, fine calculation, and user role handling (Members vs Librarians).

---

## 🧠 Objectives

- Demonstrate practical understanding of **LLD patterns** and class design
- Implement **core system functionality** through real-world abstractions
- Apply **OOP principles** in a scalable, testable architecture
- Simulate production-like logic suitable for mid-level and entry-level SDE interviews

---

## 🧱 Features Overview

| Feature | Description |
|--------|-------------|
| 👤 Member System | Members can check out and return books, with a borrow limit |
| 👮 Librarian System | Librarians can add/remove books, block/unblock members |
| 📚 Book Handling | Books are represented as `BookItem` objects with metadata and status |
| 📆 Lending Tracker | Tracks due dates, lending status, and member-lending relationships |
| 💰 Fine Management | Calculates and stores fines based on overdue duration |
| 📦 Enum Safety | Uses Python `Enum` for book status and format to prevent invalid data |
| ✅ Unit Testing | Full test suite written using Python `unittest` to verify behavior |

---

## 🧩 System Architecture

### Object-Oriented Components

- **Account (Abstract)**  
  Base class for both `Member` and `Librarian`, encapsulating shared properties like ID, password, and reset logic.

- **Member**  
  Inherits from `Account`, with methods for checkout, return, and fine checking.

- **Librarian**  
  Inherits from `Account`, responsible for administrative operations like adding or removing books.

- **BookItem**  
  Represents physical book instances with properties like barcode, status, format, and due date.

- **BookLending**  
  Maintains lending records, due dates, and links between members and borrowed books.

- **Fine**  
  Static class that tracks fines on a per-member basis.

- **Enums**  
  Strongly-typed status and format indicators using Python `Enum`.

---

## 🗂️ Folder Structure
LibraryManagementSystem/ ├── Models/ │ ├── account.py # Base Account class, and Member & Librarian roles │ ├── book.py # BookItem model with status, format, and factory method │ ├── bookLending.py # BookLending and Fine management with static records │ └── testing/ │ ├── init.py │ └── test_library.py # Unit tests for checkout, fine collection, and more │ ├── utils/ │ ├── init.py │ └── constants.py # Enum definitions for BookStatus and BookFormat │ ├── .gitignore # Ignores .venv/, pycache/, and system files ├── README.md # Project documentation and overview └── main.py # (Optional) Entry point for CLI or UI extensions
---

## 🚀 How to Run Tests

1. Clone the repository:

```bash
git clone https://github.com/chakri-yadav/library-management-system.git
cd library-management-system

---

## 📝 Acknowledgments

This project was independently developed by **Chakravarthi Nukala** as part of his Low-Level Design (LLD) and software engineering interview preparation journey.

Special thanks to:

- The open-source Python community for best practices in OOP and testing
- Python’s built-in `unittest` module for simplifying functional verification
- GitHub and PyCharm for making modern software development efficient
- Everyone contributing to LLD and system design knowledge online

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to:
- ✅ Use this project for personal or commercial purposes
- ✅ Modify and adapt it to your needs
- ✅ Distribute it as long as the license and attribution remain intact

> For full legal terms, visit: [MIT License](https://choosealicense.com/licenses/mit)

Please respect third-party library licenses if you expand the project.

---

## ℹ️ About

This project is maintained by **Chakravarthi Nukala**.  
It was created to strengthen understanding of object-oriented design and demonstrate SDE readiness.

📧 Email: [chakravarthinukala@gmail.com](mailto:chakravarthinukala@gmail.com)  
🔗 GitHub: [@chakri-yadav](https://github.com/chakri-yadav)

Feel free to contribute, ask questions, or collaborate.

---



