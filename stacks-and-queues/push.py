class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, value):
    new_node = Node(value)
    self.top = new_node
    self.height = 1

  def print_list(self):
    temp = self.top
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def push(self, value):
    new_node = Node(value)
    if self.height == 0:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node
    self.height += 1

my_stack = Stack(10)
my_stack.print_list()
my_stack.push(11)
my_stack.push(12)
my_stack.push(13)
my_stack.push(14)
print("----After adding nodes-----")
my_stack.print_list()
