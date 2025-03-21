"""Collatz Conjecture, also known as the 3x + 1 problem, is a mathematical conjecture
    that applies to any positive integer n. The conjecture follows these rules:
    1. If n is even, divide it by 2. That is, n = n / 2.
    2. If n is odd, multiply it by 3 and add 1. That is, n = 3n + 1.
    3. Repeat the process indefinitely.

Author: Jordan Marumure
Date : 18 March 2025
"""

def main():
    number = input("Enter a positive integer:\n")
    try:
        number = int(number)
    except: # Hey,me, fix not to become too broad
        print("Invalid input. Please enter a valid integer.")
        return
    if number > 0:
        compute(number)
        return
    print(f"Please enter a positive integer.")
    return

def compute(n):
    # check for base case
    if n == 1:
        print(n)
        return
    if is_odd(n):
        print(n, end=" ")
        n = 3*n+1
        return compute(n)
    if is_even(n):
        print(n, end=" ")
        n = n//2
        return compute(n)

def is_even(n):
    return n%2 == 0

def is_odd(n):
    return n%2 != 0

if __name__ == "__main__":
    main()