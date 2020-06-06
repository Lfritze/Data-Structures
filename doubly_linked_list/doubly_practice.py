class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insertEnd(self, new_node):
    pass




node_one = Node('Joe')
node_two = Node('Mary')
node_three = Node('Grace')
linked_list = LinkedList()
linked_list.insertEnd(node_one)
