#def class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#create linked list
ele1 = Node(1)
ele2 = Node(2)
ele3 = Node(3)
ele4 = Node(4)

#connect nodes
ele1.next = ele2
ele2.next = ele3
ele3.next = ele4

print("Before reversing:")

#print linked list
print(ele1.value)
print(ele1.next.value)
print(ele1.next.next.value)
print(ele1.next.next.next.value)

#reverse linked list
prev = None
current = ele1
while current is not None:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

print("After reversing:")

#print reversed linked list
print(prev.value)
print(prev.next.value)
print(prev.next.next.value)
print(prev.next.next.next.value)