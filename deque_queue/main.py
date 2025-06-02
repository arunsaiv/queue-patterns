from collections import deque

class DequeQueue:
    def __init__(self):
        # Initialize a double-ended queue
        self.queue = deque()

    def enqueue_front(self, item):
        """
        Add an item to the front of the deque.
        """
        self.queue.appendleft(item)
        print(f"🔼 Enqueued at front: {item}")

    def enqueue_rear(self, item):
        """
        Add an item to the rear (end) of the deque.
        """
        self.queue.append(item)
        print(f"🔽 Enqueued at rear: {item}")

    def dequeue_front(self):
        """
        Remove and return an item from the front of the deque.
        """
        if self.is_empty():
            print("⚠️ Queue is empty! Cannot dequeue from front.")
            return None

        item = self.queue.popleft()
        print(f"🗑️ Dequeued from front: {item}")
        return item

    def dequeue_rear(self):
        """
        Remove and return an item from the rear (end) of the deque.
        """
        if self.is_empty():
            print("⚠️ Queue is empty! Cannot dequeue from rear.")
            return None

        item = self.queue.pop()
        print(f"🗑️ Dequeued from rear: {item}")
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        """
        Display the current contents of the deque.
        """
        if self.is_empty():
            print("⚠️ Queue is empty!")
            return

        print("📦 Deque contents:")
        print(list(self.queue))


# ✅ Example usage
if __name__ == "__main__":
    dq = DequeQueue()

    dq.enqueue_rear("Task A")
    dq.enqueue_front("Task B")
    dq.enqueue_rear("Task C")

    dq.display()

    dq.dequeue_front()
    dq.display()

    dq.dequeue_rear()
    dq.display()    