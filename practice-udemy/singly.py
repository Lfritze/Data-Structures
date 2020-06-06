# How to make a Singly Linked List

#create Nodes
# Create linked list
# add nodes to linked list
#Print linked list

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, newNode):
    # head=> John=>None
    if self.head is None:
      self.head = newNode
    else:
      #head=>John=>Ben=>None
      lastNode = self.head
      while True:
        if lastNode.next is None:
          break
        lastNode = lastNode.next
      lastNode.next = newNode

  def printList(self):
    # head=>John->Ben->Matthew->None
    if self.head is None:
      print("The list is empty")
      return
    currentNode = self.head
    while True:
      if currentNode is None:
        break
      print(currentNode.data)
      currentNode = currentNode.next



#Node => data, next
# firstNode.data => John, firstNode.next => None
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
# linkedList.insert(thirdNode)
fourthNode = Node("Jeff")
# linkedList.insert(fourthNode)

linkedList.printList()

# COMMENT BACK IN the INSERTS to see a non-empty list