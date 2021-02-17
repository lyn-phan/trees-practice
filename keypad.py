# key letter = A, S  OR x
# minimum = 5, max = 7

def numKeypadSolutions(wordlist, keypads):
    
    success_count = []

    for char in wordlist:
        if char in keypads:
            success_count[char] = success_count
            success_count[char] += 1
    return success_count
    
# class trieNode:
#     def __init__(self, char):
#         self.char = char
#         self.is_end = False
#         self.children = {}

# class Trie(object):
#     def __init__(self):
#         self.root = trieNode("")
    
#     def insert(self, wordlist):

#         node = self.root

#         for char in wordlist:
#             if char in node.children:
#                 node = node.children[char]
#             else:
#                 newNode = trieNode(char)
#                 node.children[char] = newNode
#                 node = newNode
#         node.is_end = True
    
#     def dfs(self, node, pre):

#         if node.is_end:
#             self.output.append((pre + node.char))
        
#         for child in node.children.values():
#             self.dfs(child, pre + node.char)

#     def search(self, keypads):
#         node = self.root

#         for char in keypads:
#             if char in node.children:
#                 node = node.children[char]
#             else:
#                 return []
        
#         self.output = []
#         self.dfs(node, keypads[:-1])

#         return self.output


# tr = Trie()
# tr.insert("PLEASE")
# tr.insert("APPLE")

# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# #     wordlist_count = int(input().strip())

# #     wordlist = []

# #     for _ in range(wordlist_count):
# #         wordlist_item = input()
# #         wordlist.append(wordlist_item)

# #     keypads_count = int(input().strip())

# #     keypads = []

# #     for _ in range(keypads_count):
# #         keypads_item = input()
# #         keypads.append(keypads_item)

# #     result = numKeypadSolutions(wordlist, keypads)

# #     fptr.write('\n'.join(map(str, result)))
# #     fptr.write('\n')

# #     fptr.close()
