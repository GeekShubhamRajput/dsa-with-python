# LL: Find Kth Node From End

# Implement the find_kth_from_end function, which takes the LinkedList (ll) 
# and an integer k as input, and returns the k-th node from the end of the 
# linked list WITHOUT USING LENGTH.

# NOTE: This is a SEPARATE FUNCTION that is NOT a method within the LinkedList class.  
# This means you need to indent the function all the way to the LEFT. 

# Given this LinkedList: 1 -> 2 -> 3 -> 4 -> 5
# If k=1 then return the first node from the end (the last node) which contains the value of 5.
# If k=2 then return the second node from the end which contains the value of 4, etc.
# If the index is out of bounds, the program should return None.

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
      
  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    return True

def find_kth_from_end(ll, k):
  slow = ll.head
  fast = ll.head

  for _ in range(k):
    if fast is None:
      return None
    fast = fast.next

  while fast is not None:
    slow = slow.next
    fast = fast.next
  return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
result = find_kth_from_end(my_linked_list, 2)

print(result.value)
"""
EXPECTED OUTPUT:
----------------
4
"""
