# Digital Library (Python Project)

This is a small digital library program I made for my flipped course project.  
I kept everything in one Python file to keep it simple and easy to read.  
The program lets you add books, manage users, search books, borrow/return them, and also delete a book if it's not issued.

## Features
- Add books with ID, title, and author
- Add users
- View all books
- Search books by title
- Borrow and return books
- Delete a book (only if not issued)
- Saves data automatically using JSON files

## How It Works
When the script runs, it loads existing data from two files:
- `books.json`
- `users.json`

If these files don’t exist, they get created when you add something for the first time.Although
some sample books are already available in the booklist section which are available once the program runs.

## How to Run
1. Install Python (any version above 3.7 should work)
2. Put the `digital_library.py` file in a folder
3. Open terminal/cmd inside that folder
4. Run:

## Instructions for Testing

To verify the system is working correctly, follow this test flow:

1.  **Start the App:** Run the script. You will see the "Digital Library" menu.
2.  **Add a User:** Select option **2** and create a user (e.g., ID: `U01`, Name: `Alice`).
3.  **View Books:** Select option **3** to see the default list of books. Note that they are all "Free".
4.  **Borrow a Book:**
    * Select option **5**.
    * Enter a Book ID (e.g., `B001`).
    * Enter the User ID you created (`U01`).
    * The system should say "Issued."
5.  **Verify Status:** Select option **3** again. `B001` should now say "Taken".
6.  **Return the Book:**
    * Select option **6**.
    * Enter the Book ID (`B001`).
    * The system should say "Returned."
7.  **Exit and Restart:** Select option **8** to exit. Run the script again. Check option **3** to ensure your data persisted.
