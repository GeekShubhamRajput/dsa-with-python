## BinarySearchTree : Contains

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return True
    
    temp = self.root
    while (True):
      if new_node.value == temp:
        return False
      elif new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        temp = temp.left 
      else:
        if temp.right is None:
          temp.right = new_node
          return True
        temp = temp.right

  def contains(self, value):
    temp = self.root
    while temp is not None:
      if value < temp.value:
        if temp.value == value:
          return True
        temp = temp.left
      elif value > temp.value:
        if temp.value == value:
          return True
        temp = temp.right
      else:
        return True
    return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(10))
print(my_tree.contains(47))
print(my_tree.contains(82))
print(my_tree.contains(17))
