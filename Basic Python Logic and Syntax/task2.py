def is_palindrome(s):
    s=s.lower()     # convert string to lower case for comparison
    if s == s[::-1]:     # check if string is equal to its reverse
        print("Palindrome")
    else:
        print("Not a palindrome")

is_palindrome("Radar")
is_palindrome("solomon")