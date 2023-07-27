"""
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
For example, "radar" and "A man, a plan, a canal, Panama!" are palindromes.

Write a function called is_palindrome that takes a string as input and returns True if the string is a palindrome, and False otherwise.
The function should be case-insensitive and should ignore spaces and non-alphanumeric characters.

Constraints:

The input string will contain only printable ASCII characters.
The maximum length of the input string will not exceed 10^4.
During the interview, I would ask you the following questions:
"""

import re

def is_palindrome(s: str) -> bool:
    clean_s = re.sub(r"[!@#$%^?/,()!&*]", "", s.lower().replace(" ", ""))
    stringList = list(clean_s)
    
    return ''.join(stringList[::-1]) == clean_s
    
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("race a car"))  # Output: False
