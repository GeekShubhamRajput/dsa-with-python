## DLL: Partition List ( ** Interview Question)

# Write a method called partition_list(self, x) that rearranges the nodes in a 
# doubly linked list so that all nodes with a value less than a given number x 
# come before all nodes with a value greater than or equal to x.
# You must maintain the original relative order of the nodes in each of the two partitions.
# The partitioning must be performed in-place. You cannot create
# new nodes (other than dummy nodes).
# Both .next and .prev pointers must be updated correctly.
# If the list is empty, nothing should happen.

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

  def print_list(self):
    output = []
    current_node = self.head
    while current_node is not None:
      output.append(str(current_node.value))
      current_node = current_node.next
    print(" <-> ".join(output))
    
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = new_node
      new_node.prev = temp
    self.length += 1
    return True

  def make_empty(self):
    self.head = None
    self.tail = None
    self.length = 0

  def partition_list(self, x):
    if self.head is None:
      return

    less_head = less_tail = None
    greater_head = greater_tail = None

    current = self.head

    while current is not None:
      next_node = current.next

      current.next = None
      current.prev = None

      if current.value < x:
        if less_head is None:
          less_head = less_tail = current
        else:
          less_tail.next = current
          current.prev = less_tail
          less_tail = current
      else:
        if greater_head is None:
          greater_head = greater_tail = current
        else:
          greater_tail.next = current
          current.prev = greater_tail
          greater_tail = current

      current = next_node

    if less_tail is not None:
      less_tail.next = greater_head

    if greater_head is not None:
      greater_head.prev = less_tail

    self.head = less_head if less_head is not None else greater_head
    self.tail = greater_tail if greater_tail is not None else less_tail

print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList(3)
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.print_list()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.print_list()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList(6)
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.print_list()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList(1)
dll4.make_empty()
print("BEFORE: ", end="")
dll4.print_list()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.print_list()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList(1)
print("BEFORE: ", end="")
dll5.print_list()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.print_list()
