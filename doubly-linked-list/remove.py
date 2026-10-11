class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      self.length += 1
      return True
  
  def pop(self):
    if self.length == 0:
      return None
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      self.length -= 1
    return temp

  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return True

  def pop_first(self):
    if self.length == 0:
      return None
    
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      temp.next = None
    self.length -= 1
    return temp

  def get(self, index):
    if index < 0 or index > self.length:
      return None
    if index < (self.length/2):
      temp = self.head
      for _ in range(index):
        temp = temp.next
    else:
      temp = self.tail
      for _ in range(self.length - 1, index, -1):
        temp = temp.prev
    return temp

  def set_value(self, index, value):
    temp = self.get(index)
    if temp is not None:
      temp.value = value
      return True
    return False

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return None
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    prev_node = self.get(index - 1)
    after_node = prev_node.next

    new_node.prev = prev_node
    new_node.next = after_node
    prev_node.next = new_node
    after_node.prev = new_node
    self.length += 1
    return True

  def remove(self, index):
    if index < 0 or index > self.length:
      return None
    if index == 1:
      return self.pop_first()
    if index == self.length:
      return self.pop()
    temp = self.get(index - 1)
    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    self.length -= 1  
    return temp

my_doubly_linked_list = DoublyLinkedList(10)
my_doubly_linked_list.append(100)
my_doubly_linked_list.append(200)
my_doubly_linked_list.append(300)
my_doubly_linked_list.append(400)
my_doubly_linked_list.print_list()
print("-----Remove 1st ------")
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()
print("-----Remove 4th ------")
my_doubly_linked_list.remove(4)
my_doubly_linked_list.print_list()
print("-----Remove 2nd ------")
my_doubly_linked_list.remove(2)
my_doubly_linked_list.print_list()
