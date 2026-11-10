## Queue Using Stacks: Dequeue ( ** Interview Question)

# You have been tasked with implementing a queue data structure using two stacks 
# in Python, and you need to write the dequeue method.

class MyQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, value):
    while len(self.stack1) > 0:
      self.stack2.append(self.stack1.pop())
    
    self.stack1.append(value)
    
    while len(self.stack2) > 0:
      self.stack1.append(self.stack2.pop())

  def dequeue(self):
    if self.stack1:
      return self.stack1.pop()

  def peek(self):
    return self.stack1[-1]

  def is_empty(self):
    return len(self.stack1) == 0

q = MyQueue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Front of the queue:", q.peek())

print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

q.enqueue(4)

print("Front of the queue:", q.peek())

print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

print("Is the queue empty?", q.is_empty())
print("Dequeued value from empty queue:", q.dequeue())
"""
EXPECTED OUTPUT:
----------------
Front of the queue: 1
Dequeued value: 1
Dequeued value: 2
Front of the queue: 3
Dequeued value: 3
Dequeued value: 4
Is the queue empty? True
Dequeued value from empty queue: None
"""
