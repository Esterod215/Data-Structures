class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)


  def contains(self, target):
    if self.value == target:
      return True
   
    elif target < self.value:
      if not self.left:
        return False
      
      else:
        return self.left.contains(target)
    
    elif target > self.value:
      if not self.right:
        return False
     
      else:
        return self.right.contains(target)


  def get_max(self):
    current_max = self.value
    
    if self.right is not None:
      return self.right.get_max()

    return current_max




  def for_each(self, cb):
    cb(self.value)
    if self.left is None and self.right is None:
      return
    
    else:
      if self.left is not None:
        self.left.for_each(cb)
      elif self.right is not None:
        self.right.for_each(cb)
      

    return


# test for contains function
BST = BinarySearchTree(7)
BST.insert(8)
if BST.contains(8):
  print("its there")
else:
  print("we got ", BST.contains(8))

#test for get_max()
print('expected 8 got: ',BST.get_max())