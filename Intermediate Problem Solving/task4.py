# =========================================
# 1. Recursive Fibonacci (Naive)
# =========================================

# Very slow for n > 30 due to repeated calculations.
def fib_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fib_fibonacci(n - 1) + fib_fibonacci(n - 2)

def fibonacci(n):
    return [fib_fibonacci(i) for i in range(n)]

print("Naive Recursive Fibonacci:")
print(fibonacci(15))  # Test the function with n=15


# =========================================
# 2. Recursive Fibonacci with Memoization
# =========================================

def memo_fibonacci(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = memo_fibonacci(n - 1) + memo_fibonacci(n - 2)
    return memo[n]  # Returning the result so the function is more flexible.

def fibonacci(n):
    return [memo_fibonacci(i) for i in range(n)]

print("\nMemoized Recursive Fibonacci:")
print(fibonacci(15))  # Test the function with n=15


# =========================================
# 3. Iterative Fibonacci (Memory Efficient)
# =========================================

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print("\nIterative Fibonacci:")
print(fibonacci(15))  # Test the function with n=15
