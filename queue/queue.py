class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size = self.size + 1
  
  def dequeue(self):
    if len(self.storage) is not 0:

      deleted = self.storage[0] 
      self.storage.pop(0)
      self.size = self.size -1
      return deleted
    else:
      return None

  def len(self):
    return self.size
