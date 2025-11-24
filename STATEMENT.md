# Project Statement: Digital Library Management System

## Problem Statement
Managing a library inventory using physical ledgers or unorganized spreadsheets is inefficient, prone to human error, and time-consuming. Librarians often struggle to quickly locate books, track their current status (whether they are on the shelf or borrowed), and identify who currently holds a specific item. Without a centralized digital system, the risk of losing books increases, and the checkout process remains slow and cumbersome.

## Scope of the Project
This project aims to develop a lightweight, console-based application to automate the core administrative tasks of a library. The scope includes:
* **Inventory Control:** Creating a digital database of books and users.
* **Transaction Handling:** Automating the logic for borrowing and returning books to ensure real-time availability tracking.
* **Data Persistence:** Implementing a file-based storage system (JSON) so that records remain intact between sessions.
* **Search Capability:** Providing a quick lookup mechanism for library resources.

The system is designed as a standalone local application, focusing on essential functionality for small to medium-sized collections without the need for complex server infrastructure.

## Target Users
* **Small Library Administrators:** Librarians in schools, community centers, or small offices.
* **Personal Collectors:** Individuals with extensive personal book collections who wish to track items lent to friends.
* **Educational Institutions:** Teachers or department heads managing classroom resources.
* **Book Clubs:** Organizers needing to track shared reading materials among members.

## High-Level Features
* **Book & User Management:** Simple interface to add new books to the catalog and register new users.
* **Real-Time Availability Check:** Instantly view whether a book is "Free" or "Taken" before attempting to issue it.
* **Circulation System:**
    * **Issue Book:** Links a specific book ID to a user ID and updates status.
    * **Return Book:** Unlinks the user and marks the book as available again.
* **Search Functionality:** Allows administrators to find books using keyword matching on titles.
* **Safety Mechanisms:** Prevents deleting books that are currently issued out to users.
* **Auto-Save:** Automatically persists data to local files (`books.json` and `users.json`) to prevent data loss.
