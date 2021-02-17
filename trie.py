class trieNode:
    """ defines a trieNode class """

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

class Trie(object):
    """ initializes an empty trieNode """

    def __init__(self):
        self.root = trieNode("")

    def insert(self, word):
        """checks if char in list of children. If not, we make a new trieNode and 
        adds it to the list of children """

        node = self.root

        for char in word:
            # is the character in the list?
            if char in node.children:
                node = node.children[char]
            else:
                # else, make a new TrieNode for the char
                newNode = trieNode(char)
                #this adds new node to list of children
                node.children[char] = newNode
                node = newNode
        node.is_end = True 

    def dfs(self, node, pre):
        """performs the dfs search. If word is_end is true, we append the word to output list"""

        if node.is_end:
            self.output.append((pre + node.char))
        
        for child in node.children.values():
            self.dfs(child, pre + node.char)
    
    def search(self, x):
        """ search function """

        node = self.root
        """ traverses search query and moves it down the trie """

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                """if query doesn't match the nodes in trie"""
                return []
        
        self.output = []
        self.dfs(node, x[:-1])

        return self.output 


tr = Trie()
tr.insert("here")
tr.insert("hear")
tr.insert("he")
tr.insert("hello")
tr.insert("how ")
tr.insert("her")
