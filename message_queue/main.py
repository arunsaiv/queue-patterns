import queue
import threading
import time

# This is just for an example of a how message queue work but in realtime 
# we use multiple tools like Kafka, RabbitMQ, Amazon SQS etc.

# Create a job queue
job_queue = queue.Queue()

# Worker function
def worker():
    while True:
        job = job_queue.get()
        if job is None:
            break
        print(f"Processing job: {job}")
        time.sleep(1)
        job_queue.task_done()

# Add jobs
for i in range(5):
    job_queue.put(f"Job-{i+1}")

# Start worker thread
thread = threading.Thread(target=worker)
thread.start()

# Wait for queue to be empty
job_queue.join()
job_queue.put(None)  # Signal to stop the thread
thread.join()