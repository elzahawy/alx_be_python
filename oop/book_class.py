class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor that initializes the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation (for users)."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (for developers)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
