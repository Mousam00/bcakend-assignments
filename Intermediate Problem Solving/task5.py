# =========================================
# 1. Simple Sorted Comparison Approach
# =========================================

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

print("Sorted Comparison Approach:")
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False


# =========================================
# 2. Counting Characters with Dictionary
# =========================================

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    counter = {}

    for char in str1:
        counter[char] = counter.get(char, 0) + 1

    for char in str2:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1
    
    return True

print("\nCounting Characters Approach:")
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
