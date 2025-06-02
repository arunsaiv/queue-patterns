# 🧱 Queue Patterns in Python

This project explores different types of **queues**, their **real-world use cases**, advantages, and Python implementations. Each pattern is explained with code, comments, and where it’s practically used in modern software systems.

---

## 🚀 What’s Inside

- Simple Queue
- Circular Queue
- Priority Queue
- Double-Ended Queue (Deque)
- Concurrent Queue
- Message Queue

---

## 📚 Queue Types

### 1. 🎯 Simple Queue

A First-In-First-Out (FIFO) structure where the first item added is the first one removed.

**Use Cases:**
- Print queues
- Task scheduling
- Customer support systems

---

### 2. 🔁 Circular Queue

A queue where the last position is connected back to the first to form a circle.

**Use Cases:**
- Memory buffers
- Round-robin scheduling
- Streaming data pipelines

---

### 3. ⏫ Priority Queue

Elements are processed based on their priority instead of arrival time.

**Use Cases:**
- Task scheduling (OS-level)
- Network routers (QoS)
- Emergency services management systems

---

### 4. 🔄 Double-Ended Queue (Deque)

Elements can be added or removed from both the front and the back.

**Use Cases:**
- Undo/Redo systems
- Sliding window algorithms
- Palindrome checking
- Caching systems (e.g. LRU Cache)

---

### 5. 🤝 Concurrent Queue

Supports safe, multi-threaded access to the queue.

**Use Cases:**
- Web server request handling
- Job processing systems
- Real-time analytics pipelines

---

### 6. 📩 Message Queue (Job Queue)

Decouples producers and consumers for asynchronous, distributed task handling.

**Popular Tools:**
- RabbitMQ, Kafka, Redis Streams, Amazon SQS, Celery

**Use Cases:**
- Background tasks (emails, reports)
- Microservices communication
- Event-driven architectures
- Load leveling for APIs

---

## 🛠 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

If using threads/multiprocessing, no external packages are required.

## 📌 License

MIT - feel free to use, contribute, and share!

## 💬 Contributions

If you’d like to contribute another queue pattern or improve current ones, PRs are welcome!