class SimpleQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
if __name__ == "__main__":
    q = SimpleQueue()
    q.enqueue("apple")
    q.enqueue("banana")
    print("Dequeued:", q.dequeue())
    print("Queue size:", q.size())    