# DSA — Reverse a Linked List

A Python implementation of one of the most fundamental and frequently tested linked list problems in DSA — **reversing a singly linked list** using the classic **three-pointer iterative algorithm**. This is the first Python program in this series, and it demonstrates the core building blocks of linked list construction, pointer manipulation, and in-place reversal — all without any standard library dependencies.

---

## Problem Statement

Given a singly linked list, reverse the direction of all `next` pointers so that the last node becomes the head and the first node becomes the tail.

**Before Reversing:**
```
1 → 2 → 3 → 4 → None
```

**After Reversing:**
```
4 → 3 → 2 → 1 → None
```

**Output:**
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

## The Code

```python
# def class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# create linked list
ele1 = Node(1)
ele2 = Node(2)
ele3 = Node(3)
ele4 = Node(4)

# connect nodes
ele1.next = ele2
ele2.next = ele3
ele3.next = ele4

print("Before reversing:")
# print linked list
print(ele1.value)
print(ele1.next.value)
print(ele1.next.next.value)
print(ele1.next.next.next.value)

# reverse linked list
prev = None
current = ele1
while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

print("After reversing:")
# print reversed linked list
print(prev.value)
print(prev.next.value)
print(prev.next.next.value)
print(prev.next.next.next.value)
```

---

## First Python Program in This Series

Every previous program in this series was written in C++. This is the first Python implementation — and with it come some structural differences worth noting upfront:

| Aspect | C++ (previous programs) | Python (this program) |
|--------|------------------------|-----------------------|
| Class definition | `struct` or `class` with explicit types | `class` with `__init__` |
| Null pointer | `nullptr` | `None` |
| Memory management | Manual / stack-allocated | Garbage collected automatically |
| Pointer syntax | `node->next` | `node.next` |
| No `return 0` needed | Implicit in C++11+ | Not applicable |
| Type declarations | `int`, `bool`, `string` | Dynamic — no type annotations needed |

The algorithm itself — `prev`, `current`, `next_node` — is identical in both languages. Only the syntax changes.

---

## The `Node` Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

Each node holds two fields:
- **`value`** — the data stored at this node
- **`next`** — a reference to the next node in the list; `None` by default (equivalent to `nullptr` in C++)

The comment `# def class` above the class definition is a shorthand notation — an informal label marking where the class definition begins. It is not Python syntax.

---

## How the List is Built — Manual Node Construction

The list is constructed in two explicit stages:

**Stage 1 — Create nodes:**
```python
ele1 = Node(1)   # Node holding value 1, next = None
ele2 = Node(2)   # Node holding value 2, next = None
ele3 = Node(3)   # Node holding value 3, next = None
ele4 = Node(4)   # Node holding value 4, next = None
```

**Stage 2 — Connect nodes:**
```python
ele1.next = ele2
ele2.next = ele3
ele3.next = ele4
# ele4.next remains None — marks the end of the list
```

After these six lines, the linked list in memory looks like:

```
ele1       ele2       ele3       ele4
[1 | ●]──→[2 | ●]──→[3 | ●]──→[4 |None]
```

---

## The Pre-Reversal Print — Chained `.next` Access

```python
print(ele1.value)                    # 1
print(ele1.next.value)               # 2
print(ele1.next.next.value)          # 3
print(ele1.next.next.next.value)     # 4
```

This approach traverses the list by chaining `.next` calls — each one following one pointer further into the list. It is **explicit, readable for small lists, and completely non-scalable** — adding a fifth node would require manually adding a fifth print line.

A general traversal loop would handle any list size:

```python
current = ele1
while current is not None:
    print(current.value)
    current = current.next
```

The hardcoded chaining approach is intentional here — it makes the pointer structure visible and concrete for learning purposes.

---

## The Three-Pointer Reversal Algorithm

The reversal loop is the most important part of this program:

```python
prev = None
current = ele1

while current is not None:
    next_node = current.next    # 1. save the next node before overwriting
    current.next = prev         # 2. reverse the pointer
    prev = current              # 3. advance prev
    current = next_node         # 4. advance current
```

Three pointers work together:

| Pointer | Role |
|---------|------|
| `prev` | The node that `current` should now point back to |
| `current` | The node currently being processed |
| `next_node` | Temporary save of `current.next` before it is overwritten |

**Why `next_node` is essential:** `current.next = prev` overwrites the forward link. Without saving `current.next` first, the rest of the list would be lost — unreachable and effectively deleted. `next_node` is the safety net that preserves the forward chain before the pointer is reversed.

---

## Step-by-Step Trace

**Initial state:**
```
prev = None
current = ele1 [1→2→3→4→None]
```

**Iteration 1 — Processing node `1`:**
```
next_node = ele2           (save: 2→3→4→None)
ele1.next = None           (reverse: 1→None)
prev = ele1                (prev now at 1)
current = ele2             (advance to 2)
```
```
[1 |None]   [2→3→4→None]
  ↑ prev      ↑ current
```

**Iteration 2 — Processing node `2`:**
```
next_node = ele3           (save: 3→4→None)
ele2.next = ele1           (reverse: 2→1→None)
prev = ele2                (prev now at 2)
current = ele3             (advance to 3)
```
```
[1 |None]←[2 | ●]   [3→4→None]
              ↑ prev    ↑ current
```

**Iteration 3 — Processing node `3`:**
```
next_node = ele4           (save: 4→None)
ele3.next = ele2           (reverse: 3→2→1→None)
prev = ele3                (prev now at 3)
current = ele4             (advance to 4)
```

**Iteration 4 — Processing node `4`:**
```
next_node = None           (save: None — end of original list)
ele4.next = ele3           (reverse: 4→3→2→1→None)
prev = ele4                (prev now at 4)
current = None             (advance to None — loop exits)
```

**Final state:**
```
[1 |None]←[2 | ●]←[3 | ●]←[4 | ●]
                              ↑ prev (new head)
```

---

## Why `prev` is the New Head After the Loop

When the loop exits (`current is None`), `prev` holds the **last node that was processed** — which is the original last node (`ele4`, value `4`). Since every pointer has been reversed, `ele4` now points back through the entire chain to `ele1`.

```
prev → 4 → 3 → 2 → 1 → None
```

`prev` is therefore the **new head** of the reversed list — and the post-reversal print uses it directly:

```python
print(prev.value)                    # 4
print(prev.next.value)               # 3
print(prev.next.next.value)          # 2
print(prev.next.next.next.value)     # 1
```

If `current` were used instead, it would be `None` — dereferencing it would raise `AttributeError`.

---

## Algorithm (Pseudocode)

```
prev    ← None
current ← head

while current is not None:
    next_node    ← current.next   # save forward link
    current.next ← prev           # reverse pointer
    prev         ← current        # advance prev
    current      ← next_node      # advance current

new_head ← prev
```

---

## Complexity Analysis

| Metric | Complexity |
|--------|------------|
| Time   | **O(n)** — each node visited exactly once |
| Space  | **O(1)** — only three pointer variables (`prev`, `current`, `next_node`); no auxiliary list |

---

## Hardcoded List — Scope Note

The list is fixed at exactly 4 nodes with values `1, 2, 3, 4`. There is no user input. This is a deliberate scope choice — the program focuses entirely on demonstrating the reversal algorithm without input-handling overhead.

A general implementation accepting any list would wrap construction in a class with append, traverse, and reverse methods:

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" → ")
            current = current.next
        print("None")
```

The reversal logic inside `reverse()` is byte-for-byte identical to the current implementation.

---

## Edge Cases

| Scenario | Behavior in general implementation |
|----------|-----------------------------------|
| Empty list (`head = None`) | `prev = None`, loop skipped — `prev` remains `None`. New head is `None` ✅ |
| Single node | One iteration: `next_node = None`, `node.next = None`, `prev = node`. Correctly returns single node ✅ |
| Two nodes `[1→2]` | After reversal: `[2→1→None]` ✅ |
| Already reversed | Reversal produces original order — correct ✅ |

*(The current hardcoded implementation does not handle these — they apply to the general version)*

---

## Repository Structure

```
DSA-Reverse-Linked-List/
│
├── reverse_linked_list.py     # Main Python implementation
└── README.md                  # Project documentation
```

---

## How to Run

**Prerequisites:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/rishita-ops/DSA-Reverse-Linked-List.git
cd DSA-Reverse-Linked-List

# Run
python reverse_linked_list.py
```

**On Windows:**
```bash
python reverse_linked_list.py
```

**Expected Output:**
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

## Key Concepts Covered

- **Singly linked list construction** — creating `Node` objects and manually wiring `next` references
- **`None` as the null terminator** — Python's equivalent of `nullptr`; marks the end of the list
- **Three-pointer reversal** — `prev`, `current`, `next_node` working in coordinated steps
- **`next_node` as a safety save** — why the forward link must be preserved before overwriting
- **`prev` as the new head** — understanding why `prev`, not `current`, holds the result after the loop
- **Chained `.next` access** — explicit traversal for fixed-size lists; contrast with loop traversal
- **O(1) space reversal** — in-place pointer manipulation with no auxiliary data structure
- **Python `__init__`** — the constructor method for class initialization

---

## Why This Problem Matters in DSA

Reversing a linked list is one of the most-asked problems in technical interviews and the foundation for a wide family of linked list manipulations:

| Problem / Concept | Connection |
|-------------------|------------|
| **LeetCode #206** (Reverse Linked List) | This exact problem — the canonical reference |
| **LeetCode #92** (Reverse Linked List II) | Reverse only a sublist `[left, right]` — uses this as a subroutine |
| **LeetCode #25** (Reverse Nodes in k-Group) | Reverses every k nodes — calls this reversal repeatedly |
| **LeetCode #234** (Palindrome Linked List) | Reverse the second half, compare with first — uses this directly |
| **LeetCode #143** (Reorder List) | Split, reverse second half, merge — reverse is one of three steps |
| **Two-pointer technique** | `prev` and `current` moving together is the same pattern as two-pointer array problems |
| **Stack-based reversal** | Pushing all values onto a stack and popping achieves the same result in O(n) space — understanding why O(1) is better starts here |

The three-pointer pattern — save, reverse, advance, advance — is the mental model. Once internalized here, every list-reversal variant in interviews becomes a controlled variation of these four lines.

---

## Contributing

Contributions are welcome. Consider adding:
- A **general `LinkedList` class** with `append`, `reverse`, and `display` methods
- A **recursive reversal** implementation for comparison
- A **traversal loop** version of the pre/post print instead of hardcoded chaining
- Implementations in C++, Java, or JavaScript

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
# Then open a Pull Request
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

*Part of a structured DSA practice series — fundamentals, done right.*
