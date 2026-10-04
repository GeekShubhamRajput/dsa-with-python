# LL: Reverse Between ( ** Interview Question)

# You are given a singly linked list and two integers start_index and end_index.
# Your task is to write a method reverse_between within the LinkedList class that reverses 
# the nodes of the linked list from start_index to  end_index (inclusive using 0-based indexing)
# in one pass and in-place.
# Note: the Linked List does not have a tail which will make the implementation easier.
# Assumption: You can assume that start_index and end_index are not out of bounds.

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
        
class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
    else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    self.length += 1
    return True
    
  def print_list(self):
    values = []
    temp = self.head
    while temp is not None:
      values.append(str(temp.value))
      temp = temp.next
    result = " -> ".join(values) if values else "Empty"
    print(result + " -> None")
    return result    
            
  def make_empty(self):
    self.head = None
    self.length = 0

  def reverse_between(self, start_index, end_index):
    if start_index == end_index:
      return

    dummy = Node(0)
    dummy.next = self.head

    previous = dummy

    for _ in range(start_index):
      previous = previous.next

    current = previous.next

    for _ in range(end_index - start_index):
      node_to_move = current.next

      current.next = node_to_move.next
      node_to_move.next = previous.next
      previous.next = node_to_move

    self.head = dummy.next

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
EXPECTED OUTPUT:
----------------
  Original linked list: 
  1 -> 2 -> 3 -> 4 -> 5 -> None
  Reversed sublist (2, 4): 
  1 -> 2 -> 5 -> 4 -> 3 -> None
  Reversed entire linked list: 
  3 -> 4 -> 5 -> 2 -> 1 -> None
  Reversed sublist of length 1 (3, 3): 
  3 -> 4 -> 5 -> 2 -> 1 -> None
  Reversed empty linked list: 
  Empty -> None   
"""
