<div align="center">

```
╔══════════════════════════════════════════════════╗
║                                                  ║
║   ←  LINKED LIST REVERSAL                        ║
║      in Python                                   ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)
![DSA](https://img.shields.io/badge/Topic-Linked%20Lists-f59e0b?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-22c55e?style=flat-square)

*A clean, from-scratch implementation of singly linked list reversal — one of the most iconic problems in computer science.*

</div>

---

## 🔗 What is this?

This project implements a **singly linked list** and demonstrates its **in-place reversal** using a classic three-pointer technique — all in pure Python, no libraries, no magic.

If you've ever prepared for a coding interview or explored data structures from the ground up, you've met this problem. This repo makes it crystal clear.

---

## 🧠 How it Works

### The Data Structure

Each node holds a value and a pointer to the next node:

```
[ 1 ] → [ 2 ] → [ 3 ] → [ 4 ] → None
```

### The Reversal

Using three pointers — `prev`, `current`, and `next_node` — we rewire each link one step at a time:

```
Step 1:   None ← [ 1 ]   [ 2 ] → [ 3 ] → [ 4 ]
Step 2:   None ← [ 1 ] ← [ 2 ]   [ 3 ] → [ 4 ]
Step 3:   None ← [ 1 ] ← [ 2 ] ← [ 3 ]   [ 4 ]
Step 4:   None ← [ 1 ] ← [ 2 ] ← [ 3 ] ← [ 4 ]
```

Result:
```
[ 4 ] → [ 3 ] → [ 2 ] → [ 1 ] → None
```

---

## 📁 File Structure

```
📦 linked-list-reversal/
 ┗ 📄 reverse_linked_list.py   ← The full implementation
```

---

## 🚀 Getting Started

No dependencies. Just Python.

```bash
# Clone the repo
git clone https://github.com/your-username/linked-list-reversal.git

# Navigate into it
cd linked-list-reversal

# Run it
python reverse_linked_list.py
```

### Output

```
Before reversing:
1
2
3
4

After reversing:
4
3
2
1
```

---

## 🔍 Code Walkthrough

```python
# 1. Define the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None       # Points to next node (or None if tail)

# 2. Build the linked list: 1 → 2 → 3 → 4
ele1 = Node(1)
ele2 = Node(2)
ele3 = Node(3)
ele4 = Node(4)

ele1.next = ele2
ele2.next = ele3
ele3.next = ele4

# 3. Reverse it in-place using three pointers
prev = None
current = ele1

while current is not None:
    next_node = current.next   # Save next
    current.next = prev        # Flip the pointer
    prev = current             # Advance prev
    current = next_node        # Advance current

# prev now points to the new head: 4 → 3 → 2 → 1
```

---

## ⏱ Complexity

| | Complexity |
|---|---|
| **Time** | `O(n)` — single pass through the list |
| **Space** | `O(1)` — only 3 pointers used, in-place |

---

## 💡 Key Concepts

- **Singly Linked List** — each node stores data and a reference to the next node
- **In-place reversal** — no extra list or array is created
- **Three-pointer technique** — `prev`, `current`, `next_node` work in tandem to reverse links
- **Iterative approach** — straightforward and memory-efficient

---

## 🎯 Why This Problem Matters

Linked list reversal is a **fundamental DSA problem** that tests your understanding of:

- Pointer manipulation
- Iterative thinking
- Edge case awareness (empty list, single node)

It appears frequently in interviews at companies like **Google**, **Meta**, **Amazon**, and more.

---

## 🌱 Possible Extensions

- [ ] Wrap the logic into a `LinkedList` class with a `.reverse()` method
- [ ] Add a recursive reversal implementation
- [ ] Handle edge cases: empty list, single node
- [ ] Reverse only a sub-section of the list (LeetCode #92)
- [ ] Detect cycles before reversing

---

## 📜 License

MIT — free to use, learn from, and build upon.

---

<div align="center">

*Made with curiosity and a love for fundamentals.*

</div>
