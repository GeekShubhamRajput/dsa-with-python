## DLL: Reverse Between ( ** Interview Question)

# Write a method reverse_between that reverses a portion of a doubly linked list in place.
# You are given a start index and an end index (inclusive range). 
# Reverse only the nodes between those indices.
# Indexing is zero-based.
# The list is made of nodes with both next and prev pointers.
# Make sure the list remains fully connected after the reversal in both directions.
# If the list has fewer than two nodes or the start and end indices are the same, 
# leave the list unchanged.

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList:
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
      new_node.prev = current
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
    if self.length <= 1 or start_index == end_index:
      return

    dummy = Node(0)
    dummy.next = self.head
    self.head.prev = dummy

    prev = dummy
    for _ in range(start_index):
      prev = prev.next

    current = prev.next

    for _ in range(end_index - start_index):
      node_to_move = current.next

      current.next = node_to_move.next
      if node_to_move.next:
        node_to_move.next.prev = current

      node_to_move.next = prev.next
      prev.next.prev = node_to_move
      prev.next = node_to_move
      node_to_move.prev = prev

    self.head = dummy.next
    self.head.prev = None

print("\nTest 1: Middle segment reversal")
dll1 = DoublyLinkedList(3)
for v in [8, 5, 10, 2, 1]:
  dll1.append(v)
print("BEFORE: ", end="")
dll1.print_list()
dll1.reverse_between(1, 4)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest 2: Full list reversal")
dll2 = DoublyLinkedList(1)
for v in [2, 3, 4, 5]:
  dll2.append(v)
print("BEFORE: ", end="")
dll2.print_list()
dll2.reverse_between(0, 4)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest 3: No-op on single node")
dll3 = DoublyLinkedList(9)
print("BEFORE: ", end="")
dll3.print_list()
dll3.reverse_between(0, 0)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest 4: Reversal with head involved")
dll4 = DoublyLinkedList(7)
for v in [8, 9]:
  dll4.append(v)
print("BEFORE: ", end="")
dll4.print_list()
dll4.reverse_between(0, 2)
print("AFTER:  ", end="")
dll4.print_list()
