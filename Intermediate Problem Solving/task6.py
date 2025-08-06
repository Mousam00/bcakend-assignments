def missingNum(arr):
    n = len(arr) + 1  # Since one number is missing, total numbers are length+1
    expected = n * (n + 1) // 2  # Sum of first n natural numbers
    actual = sum(arr)  # Sum of elements present in array
    return expected - actual  # Missing number is the difference

# Test case
print(missingNum([1, 2, 3, 5]))  # Output should be 4
