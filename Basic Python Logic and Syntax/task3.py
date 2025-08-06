def factorial(n):
    """
    Calculates factorial using recursion.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Note:
        - Simple and elegant.
        - Not memory-efficient for large n (due to stack depth).
    """
    if n==(0):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(1))  # Test the function with n=1
print(factorial(2))  # Test the function with n=2
print(factorial(5))  # Test the function with n=5



# memory efficient

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using an iterative approach.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: Factorial of n.
    """

    result = 1
    for i in range(2, n+1):
        result *= i
    return result # returning the result so the function is more flexible.

print(factorial(1))  # Test the function with n=1
print(factorial(2))  # Test the function with n=2
print(factorial(5))  # Test the function with n=5
