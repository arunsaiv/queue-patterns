import heapq

class PriorityQueue:
    def __init__(self):
        # Initialize an empty list to store elements
        self.queue = []

    def enqueue(self, priority, item):
        """
        Insert an element with a given priority.
        Lower priority number means higher priority (min-heap).
        """
        heapq.heappush(self.queue, (priority, item))
        print(f"✅ Enqueued: {item} with priority {priority}")

    def dequeue(self):
        """
        Remove and return the item with the highest priority (lowest number).
        """
        if self.is_empty():
            print("⚠️ Queue is empty! Cannot dequeue.")
            return None

        priority, item = heapq.heappop(self.queue)
        print(f"🗑️ Dequeued: {item} (priority {priority})")
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        """
        Show the priority queue content in sorted priority order.
        """
        if self.is_empty():
            print("⚠️ Queue is empty!")
            return

        print("📦 Queue contents (priority: item):")
        for priority, item in sorted(self.queue):
            print(f"{priority}: {item}")


# ✅ Example usage
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.enqueue(3, "Low Priority Task")
    pq.enqueue(1, "High Priority Task")
    pq.enqueue(2, "Medium Priority Task")

    pq.display()

    pq.dequeue()
    pq.display()