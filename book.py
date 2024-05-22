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
