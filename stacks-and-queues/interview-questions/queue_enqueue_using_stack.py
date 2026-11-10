## Queue Using Stacks: Enqueue ( ** Interview Question)

# You are given a class MyQueue that implements a queue using two stacks.

class MyQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, value):
    while self.stack1:
      self.stack2.append(self.stack1.pop())

    self.stack1.append(value)

    while self.stack2:
      self.stack1.append(self.stack2.pop())

  def peek(self):
    return self.stack1[-1]

  def is_empty(self):
    return len(self.stack1) == 0

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Front of the queue:", q.peek())
print("Is the queue empty?", q.is_empty())
"""
EXPECTED OUTPUT:
----------------
Front of the queue: 1
Is the queue empty? False
"""
