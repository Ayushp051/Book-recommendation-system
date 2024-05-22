#trie data strucutre
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
print("welcome ti book recoomendation system")
choice = 0
while choice != 6:
    print("Options:")
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
    elif choice == '2':
        continue
    elif choice == '3':
            username = input("Enter your username: ")
            continue
    elif choice == '4':
            username = input("Enter your username: ")
            continue
    elif choice == '5':
        prefix = input("Enter book title prefix: ")
        continue
    else:
            break
