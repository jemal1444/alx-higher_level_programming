#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the alphabet in lowercase, not followed by a new line."""
"""You can only use one print function with string format"""
"""You can only use one loop in your code"""
"""You are not allowed to store characters in a variable"""
"""You are not allowed to import any module"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
