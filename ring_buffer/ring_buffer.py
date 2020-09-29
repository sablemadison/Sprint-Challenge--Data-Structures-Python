class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        elif len(self.storage) == self.capacity:
            self.storage.pop(0)
            self.storage[0] = item
            

    def get(self):
        newList = []
        for element in self.storage:
            if element is None:
                self.storage.remove(element)
            else:
                newList.append(element)
                return newList