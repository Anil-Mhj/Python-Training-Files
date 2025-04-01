class Library:
    def __init__(self):
        """Initialize the library with an empty book list."""
        self.books = []  # List to store books as dictionaries

    def display_books(self):
        """Displays all available books in the library."""
        if not self.books:
            print("\nNo books available in the library.")
        else:
            print("\nAvailable Books:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book['name']} by {book['author']}")

    def add_book(self):
        """Adds a new book to the library."""
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")
        self.books.append({"name": book_name, "author": author_name})
        print(f"Book '{book_name}' by {author_name} added successfully!")

    def remove_book(self):
        """Removes a book from the library."""
        self.display_books()
        try:
            book_index = int(input("Enter book number to remove: ")) - 1
            if 0 <= book_index < len(self.books):
                removed_book = self.books.pop(book_index)
                print(
                    f"Book '{removed_book['name']}' by {removed_book['author']} removed successfully!"
                )
            else:
                print("Invalid book number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the library management system."""
    library = Library()
    while True:
        print("\nLibrary Management System:")
        print("1) Display Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            library.add_book()
        elif choice == "3":
            library.remove_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
