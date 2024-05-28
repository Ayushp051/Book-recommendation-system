#trie data strucutre
import json

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.books = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, title, book_info):
        node = self.root
        for char in title:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.books.append(book_info)
    
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_books_from_node(node)
    
    def _get_books_from_node(self, node):
        result = []
        if node.is_end_of_word:
            result.extend(node.books)
        for child in node.children.values():
            result.extend(self._get_books_from_node(child))
        return result
    

class BookSystem:
    def __init__(self):
        self.books = []
        self.ratings = {}
        self.trie = Trie()
        self.load_data()
    
    def load_data(self):
        try:
            with open('books.json', 'r') as file:
                data = json.load(file)
                self.books = data['books']
                self.ratings = data['ratings']
                for book in self.books:
                    self.trie.insert(book['title'], book)
        except FileNotFoundError:
            self.books = []
            self.ratings = {}

    def save_data(self):
        data = {
            'books': self.books,
            'ratings': self.ratings
        }
        with open('books.json', 'w') as file:
            json.dump(data, file)
    
    def add_book(self, title, author, genre):
        book = {'title': title, 'author': author, 'genre': genre}
        self.books.append(book)
        self.trie.insert(title, book)
        self.save_data()

    def view_books(self):
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
    
    def rate_book(self, username, title, rating):
        if username not in self.ratings:
            self.ratings[username] = {}
        self.ratings[username][title] = rating
        self.save_data()
    
    def search_books(self, prefix):
        results = self.trie.search(prefix)
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
    
    def get_recommendations(self, username):
        if username not in self.ratings:
            print("No ratings found for user.")                                                             
            return
        
        user_ratings = self.ratings[username]
        if not user_ratings:
            print("No ratings found for user.")
            return
        
        max_rated_book = max(user_ratings, key=user_ratings.get)
        genre = next(book['genre'] for book in self.books if book['title'] == max_rated_book)

        recommendations = [book for book in self.books if book['genre'] == genre and book['title'] != max_rated_book]
        for book in recommendations:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")


book_system = BookSystem()
choice = 0
while choice!= 6:
    print("\nOptions:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Rate Book")
    print("4. Get Recommendations")
    print("5. Search Books")
    print("6. Exit")
    choice = input("Choose an option: ")
        
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        book_system.add_book(title, author, genre)
    elif choice == '2':
        book_system.view_books()
    elif choice == '3':
        username = input("Enter your username: ")
        book_system.view_books()
        book_index = int(input("Enter the number of the book you want to rate: ")) - 1
        rating = int(input(f"Enter your rating for {book_system.books[book_index]['title']} (1-5): "))
        book_system.rate_book(username, book_system.books[book_index]['title'], rating)
    elif choice == '4':
        username = input("Enter your username: ")
        book_system.get_recommendations(username)
    elif choice == '5':
        prefix = input("Enter book title prefix: ")
        book_system.search_books(prefix)
    else:
        break
