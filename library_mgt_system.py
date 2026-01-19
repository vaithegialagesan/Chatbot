books = {}     
users = {}     
book_id_counter = 1
user_id_counter = 1
FINE_PER_DAY = 5  

def add_book():
    global book_id_counter
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    books[book_id_counter] = {
        "title": title,
        "author": author,
        "available": True,
        "issued_to": None,
        "days_issued": 0
    }
    print(f"Book added successfully! Book ID: {book_id_counter}")
    book_id_counter += 1


def list_books():
    if not books:
        print("No books in the library.")
        return
    print("\nBooks in Library:")
    for bid, info in books.items():
        status = "Available" if info["available"] else f"Issued to User {info['issued_to']}"
        print(f"ID: {bid}, Title: {info['title']}, Author: {info['author']}, Status: {status}")
    print()

def add_user():
    global user_id_counter
    name = input("Enter user name: ")
    users[user_id_counter] = {"name": name, "borrowed_books": []}
    print(f"User added successfully! User ID: {user_id_counter}")
    user_id_counter += 1


def list_users():
    if not users:
        print("No users in the system.")
        return
    print("\nUsers:")
    for uid, info in users.items():
        print(f"ID: {uid}, Name: {info['name']}, Borrowed Books: {info['borrowed_books']}")
    print()


def issue_book():
    user_id = int(input("Enter user ID: "))
    if user_id not in users:
        print("User not found!")
        return
    book_id = int(input("Enter book ID: "))
    if book_id not in books:
        print("Book not found!")
        return
    if not books[book_id]["available"]:
        print("Book is already issued.")
        return

    books[book_id]["available"] = False
    books[book_id]["issued_to"] = user_id
    books[book_id]["days_issued"] = int(input("Enter number of days for which the book is issued: "))
    users[user_id]["borrowed_books"].append(book_id)
    print(f"Book ID {book_id} issued to User ID {user_id} for {books[book_id]['days_issued']} days.")


def return_book():
    user_id = int(input("Enter user ID: "))
    if user_id not in users:
        print("User not found!")
        return
    book_id = int(input("Enter book ID: "))
    if book_id not in books:
        print("Book not found!")
        return
    if book_id not in users[user_id]["borrowed_books"]:
        print("This book was not borrowed by this user.")
        return

    
    actual_days = int(input("Enter number of days the book was borrowed: "))
    issued_days = books[book_id]["days_issued"]
    fine = 0
    if actual_days > issued_days:
        fine = (actual_days - issued_days) * FINE_PER_DAY

    books[book_id]["available"] = True
    books[book_id]["issued_to"] = None
    books[book_id]["days_issued"] = 0
    users[user_id]["borrowed_books"].remove(book_id)
    
    print(f"Book ID {book_id} returned by User ID {user_id}.")
    if fine > 0:
        print(f"Late return! Fine to pay: {fine} units.")
    else:
        print("Returned on time. No fine!")

def search_books():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for bid, info in books.items():
        if keyword in info["title"].lower() or keyword in info["author"].lower():
            status = "Available" if info["available"] else f"Issued to User {info['issued_to']}"
            print(f"ID: {bid}, Title: {info['title']}, Author: {info['author']}, Status: {status}")
            found = True
    if not found:
        print("No matching books found.")


def main():
    while True:
        print("\n==== Library Management System ====")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. List Users")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Search Books")
        print("8. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            add_user()
        elif choice == "4":
            list_users()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            search_books()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
