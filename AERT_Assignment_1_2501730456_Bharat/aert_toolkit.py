# Stack ADT Implementation

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Factorial (Recursive)

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci (Naive Recursion)

naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


# Fibonacci (Memoized)

memo_calls = 0

def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# Tower of Hanoi

moves_stack = StackADT()

def hanoi(n, source, auxiliary, destination):

    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        moves_stack.push(move)
        return

    hanoi(n - 1, source, destination, auxiliary)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    moves_stack.push(move)

    hanoi(n - 1, auxiliary, source, destination)


# Recursive Binary Search

def binary_search(arr, key, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)

    else:
        return binary_search(arr, key, mid + 1, high)


# Main Function (Test Cases)

def main():

    print(" Factorial Tests ")
    for n in [0, 1, 5, 10]:
        print(f"{n}! =", factorial(n))


    print(" Fibonacci Tests ")

    for n in [5, 10, 20, 30]:

        global naive_calls
        global memo_calls

        naive_calls = 0
        memo_calls = 0

        naive_result = fib_naive(n)
        memo_result = fib_memo(n)

        print(f"\nFor n = {n}")
        print("Naive Fibonacci:", naive_result)
        print("Naive Calls:", naive_calls)

        print("Memoized Fibonacci:", memo_result)
        print("Memoized Calls:", memo_calls)


    print(" Tower of Hanoi (N = 3) ")

    hanoi(3, 'A', 'B', 'C')


    print(" Binary Search Tests ")

    arr = [1, 3, 5, 7, 9, 11, 13]

    test_keys = [7, 1, 13, 2]

    for key in test_keys:
        result = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Search {key} -> Index:", result)


    print("\nEmpty Array Test:")
    print(binary_search([], 5, 0, -1))


# Run Program

if __name__ == "__main__":
    main()
