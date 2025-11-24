import json
import os

data_books = "books.json"
data_users = "users.json"

booklist = {
    "B001": {"id": "B001", "ttl": "To Kill a Mockingbird", "auth": "Harper Lee", "free": True, "who": None},
    "B002": {"id": "B002", "ttl": "1984", "auth": "George Orwell", "free": True, "who": None},
    "B003": {"id": "B003", "ttl": "Pride and Prejudice", "auth": "Jane Austen", "free": True, "who": None},
    "B004": {"id": "B004", "ttl": "The Great Gatsby", "auth": "F. Scott Fitzgerald", "free": True, "who": None},
    "B005": {"id": "B005", "ttl": "Harry Potter and the Sorcerer's Stone", "auth": "J.K. Rowling", "free": True, "who": None},
    "B006": {"id": "B006", "ttl": "The Catcher in the Rye", "auth": "J.D. Salinger", "free": True, "who": None},
    "B007": {"id": "B007", "ttl": "The Hobbit", "auth": "J.R.R. Tolkien", "free": True, "who": None},
    "B008": {"id": "B008", "ttl": "Fahrenheit 451", "auth": "Ray Bradbury", "free": True, "who": None}
}
userlist = {}


def loadall():
    if os.path.exists(data_books):
        with open(data_books, "r") as f:
            for b in json.load(f):
                booklist[b["id"]] = b

    if os.path.exists(data_users):
        with open(data_users, "r") as f:
            for u in json.load(f):
                userlist[u["id"]] = u


def saveall():
    with open(data_books, "w") as f:
        json.dump(list(booklist.values()), f, indent=4)

    with open(data_users, "w") as f:
        json.dump(list(userlist.values()), f, indent=4)


def addbook():
    bid = input("Book ID: ").strip()
    ttl = input("Title: ").strip()
    auth = input("Author: ").strip()

    booklist[bid] = {
        "id": bid,
        "ttl": ttl,
        "auth": auth,
        "free": True,
        "who": None
    }

    saveall()
    print("Book added.\n")


def adduser():
    uid = input("User ID: ").strip()
    nm = input("Name: ").strip()

    userlist[uid] = {
        "id": uid,
        "nm": nm
    }

    saveall()
    print("User added.\n")


def showbooks():
    print("\n--- Books ---")
    for b in booklist.values():
        st = "Free" if b["free"] else "Taken"
        print(f"{b['id']} | {b['ttl']} | {b['auth']} | {st}")
    print("-------------\n")


def searchbook():
    key = input("Search title: ").lower()
    ok = False

    for b in booklist.values():
        if key in b["ttl"].lower():
            ok = True
            print(f"{b['id']} | {b['ttl']} | {b['auth']}")

    if not ok:
        print("No match.\n")


def borrowbook():
    bid = input("Book ID: ").strip()
    uid = input("User ID: ").strip()

    if bid not in booklist:
        print("No such book.\n")
        return
    if uid not in userlist:
        print("No such user.\n")
        return
    if not booklist[bid]["free"]:
        print("Already taken.\n")
        return

    booklist[bid]["free"] = False
    booklist[bid]["who"] = uid
    saveall()

    print("Issued.\n")


def returnbook():
    bid = input("Book ID: ").strip()

    if bid not in booklist:
        print("No such book.\n")
        return

    booklist[bid]["free"] = True
    booklist[bid]["who"] = None
    saveall()

    print("Returned.\n")


def deletebook():
    bid = input("Book ID to delete: ").strip()

    if bid not in booklist:
        print("No such book.\n")
        return
    if not booklist[bid]["free"]:
        print("Cannot delete. Book is issued.\n")
        return

    del booklist[bid]
    saveall()

    print("Book removed.\n")


def menu():
    loadall()

    while True:
        print("\n=== Digital Library ===")
        print("1. Add Book")
        print("2. Add User")
        print("3. View Books")
        print("4. Search Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Delete Book")
        print("8. Exit")

        ch = input("Choose: ").strip()

        if ch == "1":
            addbook()
        elif ch == "2":
            adduser()
        elif ch == "3":
            showbooks()
        elif ch == "4":
            searchbook()
        elif ch == "5":
            borrowbook()
        elif ch == "6":
            returnbook()
        elif ch == "7":
            deletebook()
        elif ch == "8":
            print("Bye.")
            break
        else:
            print("Invalid.\n")


menu()
