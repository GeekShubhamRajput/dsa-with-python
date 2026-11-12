## BinarySearchTree : 

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

my_binary_search_tree = BinarySearchTree()

print(my_binary_search_tree.root)
