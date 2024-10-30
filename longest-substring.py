"""
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Write a function called length_of_longest_substring that takes a string s as input and returns an integer representing the
length of the longest substring without repeating characters
"""
def length_of_longest_substring(s: str) -> int:
    longest = 0
    current = ""

    while len(s) > 0:
        current = f"{current}{s[0]}" if current.find(s[0]) == -1 else s[0]
        
        if len(current) > longest:
            longest = len(current)
        
        s = str(s[1:])

    return longest


print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc" or "bca" or "cab")
print(length_of_longest_substring("bbbbb"))  # Output: 1 ("b")
print(length_of_longest_substring("pwwkew"))  # Output: 3 ("wke" or "kew")
