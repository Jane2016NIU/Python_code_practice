class MinStack:

    def __init__(self):
      self.list = []
      self.minimum = []

    def push(self, val: int) -> None:

      if len(self.list) == 0:
        self.minimum.append(val)

      elif val < self.minimum[len(self.minimum)-1]:
        self.minimum.append(val)
        
      self.list.append(val)
      print('List: ' + str(self.list)[1:-1], 'Min list: ' + str(self.minimum)[1:-1])

    def pop(self) -> None:
      if len(self.list) == 0:
        print('Stack is empty.')
      else:
        if self.list[len(self.list)-1] == self.minimum[len(self.minimum)-1]:
          self.list.pop()
          self.minimum.pop()

        else:
          self.list.pop()
      print('List: ' + str(self.list)[1:-1])
      
      print(self.minimum)

    def top(self) -> int:
      if len(self.list) == 0:
        print("empty list!")
      else:
        return self.list[len(self.list)-1]
        
    def getMin(self) -> int:
      if len(self.list) == 0:
        print("Empty list!")
        return None
      else:
        return self.minimum[len(self.minimum)-1]
      
      
        



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.push(5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print("param_3 = ", param_3)
print("param_4 = ", param_4)

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# push(val) pushes the element val onto the stack.
# pop() removes the element on the top of the stack.
# top() gets the top element of the stack.
# getMin() retrieves the minimum element in the stack.
