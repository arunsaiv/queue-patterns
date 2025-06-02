import threading
import time
import queue

# Create a thread-safe queue
q = queue.Queue()

# Producer function
def producer():
    for i in range(5):
        print(f"👨‍🏭 Producer: producing item {i}")
        q.put(i)
        time.sleep(1)
    print("✅ Producer done producing")

# Consumer function
def consumer():
    while True:
        item = q.get()
        print(f"🧑‍🔧 Consumer: consuming item {item}")
        time.sleep(2)
        q.task_done()

# Start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer, daemon=True)

producer_thread.start()
consumer_thread.start()

# Wait for producer to finish
producer_thread.join()

# Wait until all items are processed
q.join()
print("🎉 All tasks completed.")