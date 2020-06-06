"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

# Arrays allow you to index and append.
# Linked Lists are sequences using nodes to connect each value
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('./doubly_linked_list')

# linked list implementation as the underlying storage structure

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if not self.storage.head:
            return
        return self.storage.remove_from_tail()

# Array as underlying storage structure
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#        if len(self.storage) !=0:
#            return self.storage.pop(0)

# q = Queue()
# print(q.__len__())
# q.enqueue('Bear')
# q.enqueue('Tiger')
# q.enqueue('Gorilla')
# print(q.__len__())
# print(q.storage)
# q.dequeue()
# print(q.storage)



