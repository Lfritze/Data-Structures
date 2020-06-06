class Node():

  def __init__(self, value):
    self.value = value
    self.next = None

class SingleLinkedList:

  def __init__(self):
    self.head = None
  
  def display_list(self):
    if self.head is None:
      print("List is empty")
      return
    else:
      print("List is :  ")
      current_node = self.head
      while current_node is not None:
        print(current_node.value, " ", end='')
        current_node = current_node.next
      print()
  
  def count_nodes(self):
    current_node = self.head
    noders = 0
    while current_node is not None:
      noders += 1
      current_node = current_node.next
    print("Number of nodes in the list = " ,noders)

  def search(self, x):
    position = 1
    current_node = self.head
    while current_node is not None:
      if current_node.value == x:
        print(x," is at position ", position)
        return True
      position+=1
      current_node = current_node.next
    else:
      print(x," not found in list")
      return False

  def insert_in_beginning(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      return

    p = self.head
    while p.next is not None:
      p = p.next
    p.next = new_node

  def create_list(self):
    number = int(input("Enter number of nodes : "))
    if number == 0:
      return
    for i in range(number):
      value = int(input("Enter the element to be inserted : "))
      self.insert_at_end(value)

  def insert_after(self, data, x):
    p = self.head
    while p is not None:
      if p.value == x:
        break 
      p = p.next

    if p is None:
      print(x, "Not present in the list")
    else:
      new_node = Node(data)
      new_node.next = p.next
      p.next = new_node

  def insert_before(self, data, x):
    # If list is empty
    if self.head is None:
      print("List is empty")
      return

    # x is in the first node, new node is to be inserted before first node
    if x == self.head.value:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
      return

    # Find reference to predecessor of node containing x
    p = self.head
    while p.next is not None:
      if p.next.value == x:
        break
      p = p.next

    if p.next is None:
      print(x, " not present in the list")
    else:
      new_node = Node(data)
      new_node.next = p.next
      p.next = new_node

  def insert_at_position(self, value, k):
    pass

  def delete_node(self, x):
    pass

  def delete_first_node(self):
    pass

def delete_last_node(self):
    pass

def reverse_list(self):
    pass

def bubble_sort_exdata(self):
    pass

def bubble_sort_exlinks(self):
    pass

def has_cycle(self):
  pass

def find_cycle(self):
  pass

def remove_cycle(self):
  pass

def insert_cycle(self, x):
  pass

def merge2(self, list2):
  pass

def _merge2(self, p1, p2):
  pass

def merge_sort(self):
  pass

def merge_sort_rec(self, listStart):
  pass

def _divide_list(self, p):
  pass

list = SingleLinkedList()

list.create_list()

while True:
  print("1. Display List")
  print("2. Count the number of nodes")
  print("3. Search for an element")
  print("4. Insert in empty list at beginning")
  print("5. Insert node at the end of list")
  print("6. Insert node after a specified node")
  print("7. Insert node before a specified node")
  print("8. Insert a node at a given position")
  print("9. Delete First node")
  print("10. Delete last node")
  print("11. Delete any node")
  print("12. Reverse the list")
  print("13. Bubble sort by exchanging data")
  print("14. Bubble sort by exchanging links (next)")
  print("15. MergeSort")
  print("16. Insert Cycle")
  print("17. Detect Cycle")
  print("18. Remove Cycle")
  print("19. Quit")

  option = int(input("Enter your choice: " ))

  if option ==1:
    list.display_list()
  elif option ==2:
    list.count_nodes()
  elif option ==3:
    value = int(input("Enter the element to be searched : "))
    list.search(value)
  elif option ==4:
    value = int(input("Enter the element to be inserted : "))
    list.insert_in_beginning(value)
  elif option ==5:
    value = int(input("Enter the element to be inserted : "))
    list.insert_at_end(value)
  elif option ==6:
    value = int(input("Enter the element to be inserted : "))
    x = int(input("Enter the element after which to insert : "))
    list.insert_after(value,x)
  elif option ==7:
    value = int(input("Enter the element to be inserted : "))
    x = int(input("Enter the element before which to insert : "))
  elif option ==8:
    value = int(input("Enter the element to be inserted : "))
    k = int(input("Enter the position at which to insert : "))
    list.insert_at_position(value,k)
  elif option ==9:
    list.delete_first_node()
  # elif option ==10:
  #   list.delete_last_node
  # elif option ==11:
  #   value = int(input("Enter the element to be deleted : "))
  #   list.delete_node(value)
  # elif option ==12:
  #   list.reverse_list()
  # elif option ==13:
  #   list.bubble_sort_exdata()
  # elif option ==14:
  #   list.bubble_sort_exlinks()
  # elif option ==15:
  #   list.merge_sort()
  # elif option ==16:
  #   value = int(input("Enter the element at which the cycle has to be inserted : "))
  #   list.insert_cycle(value)
  # elif option ==17:
  #   if list.has_cycle():
  #     print("List has a cycle")
  #   else:
  #     print("List does not have a cycle")
  # elif option ==18:
  #   list.remove_cycle()
  elif option ==19:
    break
  else:
    print("Wrong option")

    