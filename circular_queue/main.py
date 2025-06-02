class CircularQueue:
    def __init__(self, capacity):
        # Initialize queue with fixed capacity
        self.capacity = capacity
        self.queue = [None] * capacity  # Pre-allocate space
        self.front = self.rear = -1     # Start with empty queue

    def is_full(self):
        # Queue is full if next position of rear is front
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        # Queue is empty if front is -1
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("⚠️ Queue is full! Cannot enqueue.")
            return

        if self.is_empty():
            # First element being inserted
            self.front = self.rear = 0
        else:
            # Move rear to next circular position
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item  # Insert the element

    def dequeue(self):
        if self.is_empty():
            print("⚠️ Queue is empty! Cannot dequeue.")
            return None

        data = self.queue[self.front]  # Retrieve front element

        if self.front == self.rear:
            # Only one element was present, reset queue
            self.front = self.rear = -1
        else:
            # Move front to next circular position
            self.front = (self.front + 1) % self.capacity

        return data  # Return dequeued value

    def display(self):
        if self.is_empty():
            print("⚠️ Queue is empty!")
            return

        print("📦 Queue contents:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


# ✅ Example usage
if __name__ == "__main__":
    cq = CircularQueue(5)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)
    cq.display()

    print("🗑️ Dequeued:", cq.dequeue())

    cq.enqueue(60)  # Reuses freed space (circular nature)
    cq.display()