##DYNAMIC ARRAY
class DynamicArray:
    """
    Simulates a dynamic array (like Python list) with manual resizing.
    Internal storage uses a plain Python list, but resizing and shifting
    logic is implemented from scratch.
    """

    def __init__(self, initial_capacity=2):
        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * self._capacity

    def _resize(self, new_capacity):
        """Copy elements to a new array of doubled capacity."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
        print(f"  [RESIZE] Capacity doubled → new capacity = {self._capacity}")

    def append(self, x):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = x
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty array")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val

    def __str__(self):
        elements = [str(self._data[i]) for i in range(self._size)]
        return f"[{', '.join(elements)}]  (size={self._size}, capacity={self._capacity})"




class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = SLLNode(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = SLLNode(x)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, x):
        if self.head is None:
            print(f"  [DELETE] List is empty. Cannot delete {x}.")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.data == x:
                curr.next = curr.next.next
                return
            curr = curr.next
        print(f"  [DELETE] Value {x} not found in list.")

    def traverse(self):
        if self.head is None:
            print("  (empty list)")
            return
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("  SLL: " + " → ".join(elements) + " → None")



class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, x):
        new_node = DLLNode(x)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_after_node(self, target, x):
        """Insert x after the first occurrence of target value."""
        curr = self.head
        while curr:
            if curr.data == target:
                new_node = DLLNode(x)
                new_node.next = curr.next
                new_node.prev = curr
                if curr.next:
                    curr.next.prev = new_node
                else:
                    self.tail = new_node
                curr.next = new_node
                return
            curr = curr.next
        print(f"  [INSERT] Target value {target} not found.")

    def delete_at_position(self, pos):
        """Delete node at given 0-based position."""
        if self.head is None:
            print("  [DELETE] List is empty.")
            return
        curr = self.head
        index = 0
        while curr:
            if index == pos:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next   
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev   
                return
            curr = curr.next
            index += 1
        print(f"  [DELETE] Position {pos} out of range.")

    def traverse(self):
        if self.head is None:
            print("  (empty list)")
            return
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print("  DLL: None ↔ " + " ↔ ".join(elements) + " ↔ None")




class Stack:
    """
    Stack (LIFO) built on top of SinglyLinkedList.
    Push/pop at head → O(1).
    """

    def __init__(self):
        self._list = SinglyLinkedList()
        self._size = 0

    def push(self, x):
        self._list.insert_at_beginning(x)
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Stack underflow: pop from empty stack")
        val = self._list.head.data
        self._list.head = self._list.head.next
        self._size -= 1
        return val

    def peek(self):
        if self._size == 0:
            raise IndexError("Stack underflow: peek on empty stack")
        return self._list.head.data

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        if self._size == 0:
            return "Stack: (empty)"
        curr = self._list.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return "Stack (top→bottom): " + " → ".join(elements)





class Queue:
    """
    Queue (FIFO) built on top of SinglyLinkedList.
    Enqueue at tail, dequeue at head → both O(1).
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, x):
        new_node = SLLNode(x)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError("Queue underflow: dequeue from empty queue")
        val = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return val

    def front(self):
        if self._size == 0:
            raise IndexError("Queue underflow: front on empty queue")
        return self._head.data

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        if self._size == 0:
            return "Queue: (empty)"
        curr = self._head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return "Queue (front→rear): " + " → ".join(elements)




def is_balanced(expr):
    """
    Returns True if the expression has balanced brackets.
    Uses our custom Stack implementation (not Python list).
    Supports: (), {}, []
    """
    stack = Stack()
    matching = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in '({[':
            stack.push(ch)
        elif ch in ')}]':
            if stack.is_empty():
                return False
            if stack.pop() != matching[ch]:
                return False

    return stack.is_empty()





def separator(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def run_task1():
    separator("TASK 1: Dynamic Array Simulation")

    da = DynamicArray(initial_capacity=2)
    print(f"\nInitial state: {da}")
    print("\nAppending 10 elements (initial capacity = 2):")

    for i in range(1, 11):
        print(f"  append({i})", end="")
        da.append(i)
        print(f"  → {da}")

    print("\nPopping 3 elements:")
    for _ in range(3):
        val = da.pop()
        print(f"  pop() returned {val}  → {da}")


def run_task2():
    separator("TASK 2A: Singly Linked List")

    sll = SinglyLinkedList()
    print("\nInserting 3 elements at beginning: 10, 20, 30")
    for val in [10, 20, 30]:
        sll.insert_at_beginning(val)
        sll.traverse()

    print("\nInserting 3 elements at end: 40, 50, 60")
    for val in [40, 50, 60]:
        sll.insert_at_end(val)
        sll.traverse()

    print("\nDelete by value: 20")
    sll.delete_by_value(20)
    sll.traverse()

    print("\nDelete by value: 60 (tail)")
    sll.delete_by_value(60)
    sll.traverse()

    print("\nDelete by value: 99 (not found)")
    sll.delete_by_value(99)

    separator("TASK 2B: Doubly Linked List")

    dll = DoublyLinkedList()
    print("\nBuilding list: 10 → 20 → 30 → 40 → 50")
    for val in [10, 20, 30, 40, 50]:
        dll.insert_at_end(val)
    dll.traverse()

    print("\nInsert 25 after node with value 20:")
    dll.insert_after_node(20, 25)
    dll.traverse()

    print("\nInsert 99 after node with value 50 (tail):")
    dll.insert_after_node(50, 99)
    dll.traverse()

    print("\nDelete at position 1 (0-based → removes 20):")
    dll.delete_at_position(1)
    dll.traverse()

    print("\nDelete at position 0 (head):")
    dll.delete_at_position(0)
    dll.traverse()

    print("\nDelete at last position (current size - 1 = 4):")
    dll.delete_at_position(4)
    dll.traverse()


def run_task3():
    separator("TASK 3A: Stack ADT (LIFO) using Singly Linked List")

    stack = Stack()
    print("\nPushing: 10, 20, 30, 40")
    for val in [10, 20, 30, 40]:
        stack.push(val)
        print(f"  push({val}) → {stack}")

    print(f"\n  peek() = {stack.peek()}")

    print("\nPopping 2 elements:")
    for _ in range(2):
        val = stack.pop()
        print(f"  pop() returned {val}  → {stack}")

    print(f"\n  peek() = {stack.peek()}")

    print("\nPopping remaining:")
    while not stack.is_empty():
        print(f"  pop() returned {stack.pop()}")

    print("\nTrying to pop from empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"  Exception caught → {e}")

    separator("TASK 3B: Queue ADT (FIFO) using Singly Linked List")

    queue = Queue()
    print("\nEnqueueing: A, B, C, D")
    for val in ['A', 'B', 'C', 'D']:
        queue.enqueue(val)
        print(f"  enqueue({val}) → {queue}")

    print(f"\n  front() = {queue.front()}")

    print("\nDequeueing 2 elements:")
    for _ in range(2):
        val = queue.dequeue()
        print(f"  dequeue() returned {val}  → {queue}")

    print(f"\n  front() = {queue.front()}")

    print("\nDequeueing remaining:")
    while not queue.is_empty():
        print(f"  dequeue() returned {queue.dequeue()}")

    print("\nTrying to dequeue from empty queue:")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"  Exception caught → {e}")


def run_task4():
    separator("TASK 4: Balanced Parentheses Checker")

    test_cases = [
        ("([])",   True),
        ("([)]",   False),
        ("(((", False),
        ("",     True),
        ("{[()]}",True),
        ("((()))",True),
        ("{[(])}",False),
        (")",      False),
    ]

    print(f"\n{'Expression':<20} {'Expected':<12} {'Got':<12} {'Pass?'}")
    print("-" * 55)
    for expr, expected in test_cases:
        result = is_balanced(expr)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        display = f'"{expr}"' if expr else '""  (empty)'
        print(f"  {display:<18} {'Balanced' if expected else 'Not Balanced':<12} {'Balanced' if result else 'Not Balanced':<12} {status}")


if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   Linear Data Structures Toolkit (LDST)                 ║")
    print("║   ETCCDS202 | Unit 2 Assignment                         ║")
    print("║   Roll No: 2501730189                                    ║")
    print("╚══════════════════════════════════════════════════════════╝")

    run_task1()
    run_task2()
    run_task3()
    run_task4()

    print("\n" + "=" * 60)
    print("  All tasks completed successfully.")
    print("=" * 60)
