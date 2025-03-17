import json

# File to save and load the library
data_file = "library.json"

def load_library():
    """Load library data from a file."""
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save library data to a file."""
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    print("Book added successfully!")

def remove_book(library):
    """Remove a book from the library."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_books(library):
    """Search for books by title or author."""
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search term: ").lower()
    
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    
    if results:
        print("Matching Books:")
        for idx, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Display library statistics."""
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books else 0
    print(f"Total books: {total_books}\nPercentage read: {percentage_read:.2f}%")

def main():
    """Main function to run the library manager."""
    library = load_library()
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
