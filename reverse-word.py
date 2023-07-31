"""
Problem: Reverse Words in a String

Given an input string s, reverse the order of the words in the string.

A word is defined as a sequence of non-space characters. The input string does not contain leading or trailing spaces,
and the words are separated by a single space.

Write a function called reverse_words that takes a string s as input and returns a new string with the words reversed.
"""

def reverse_words(s: str) -> str:
    l = s.split(" ")
    l.reverse()
    return " ".join(filter(lambda e : len(e) > 0, l))

print(reverse_words("hello world"))  # Output: "world hello"
print(reverse_words("programming is fun"))  # Output: "fun is programming"
print(reverse_words("   hello   world   "))  # Output: "world hello"
