#Leetcode easy - merge two sorted linked lists
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]

#Create a Node class, pass through data and next node
#add function that takes in two node arguments, retruns a node as a return value
class ListNode():
    def __init__(self, data, next_node):
        self.data = data 
        self.next_node = next_node

class Solution():
    def mergeTwoLists(l1, l2):

        if l1 and l2 == None:
            return l1 or l2

        output = None

        while l1 and l2 != None:
            if l1.val <= l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            output = output.next
        
        if l1 is None:
            output.next = l2
        elif l2 is None:
            output.next = l1
        return output.next 

l1 = [1, 2, 4]
l2 = [1, 3, 4]
Solution.mergeTwoLists(l1, l2)

