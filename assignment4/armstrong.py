# Program for determining whether a number is armstrong or not
# Author: Jordan Marumure
# Date: 18 March 2025

def main():
    string_input = input("Enter a number:\n") # read number as a string
    try:
        number_list = [int(i) for i in string_input] # create a list of integers from the string input
    except:
        print(f"Invalid input. Please enter a valid integer.")
        return

    if is_armstrong(int(string_input), number_list):
        print(f"{string_input} is an Armstrong number.")
        return
    print(f"{string_input} is not an Armstrong number.")

def is_armstrong(n, number_list):
    d = len(number_list)
    total = 0
    for i in number_list:
        total += i**d
    return total == n

if __name__ == "__main__":
    main()