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
import sys

class ListNode(object):
    def __init__(self, data, next_node):
        self.data = data 
        self.next_node = next_node

def convertPythonListToLinkedList(pylist):
    result = None
    prev = None

    for item in pylist:
        node = ListNode(item, None)
        if prev is not None:
            prev.next_node = node
        prev = node
        if result is None:
            result = node
    
    return result

def convertLinkedListToPythonList(l):
    pylist = []
    while l is not None:
        pylist.append(l.data)
        l = l.next_node
    return pylist

class Solution():
    def mergeTwoLists(self, l1, l2):
        result = None
        prev = None

        while l1 is not None or l2 is not None:
            #while l1 or l2 have values in their list

            value1 = sys.maxsize if l1 is None else l1.data
            value2 = sys.maxsize if l2 is None else l2.data
            # create variables to assign to each node on each linked list
            #max size = maximum number python supports
            if value1 < value2:
                if prev is not None:
                    #if we are not at the start of the list
                    prev.next_node = l1
                    #move to the next node on the list
                prev = l1
                #
                l1 = l1.next_node
            else:
                if prev is not None:
                    prev.next_node = l2
                prev = l2
                l2 = l2.next_node

            if result is None:
                result = prev
        return result

if __name__ == '__main__':
  l1 = convertPythonListToLinkedList([1, 2, 3])
  l2 = convertPythonListToLinkedList([2, 3, 4])
  s = Solution()
  merged = s.mergeTwoLists(l1, l2)
  print(convertLinkedListToPythonList(merged))
