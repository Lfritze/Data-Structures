"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('doubly_linked_list.py')

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if not self.storage.head:
            return
        return self.storage.remove_from_head()

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if not self.storage:
#             return #return none - 
#             # else return
#         return self.storage.pop()

# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?

#     def __len__(self):
#         pass

#     def push(self, value):
#         pass

#     def pop(self):
#         pass
