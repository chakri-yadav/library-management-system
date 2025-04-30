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

