# Program to print a rectangular grid
# Author: Jordan Marumure
# Date: 18 March 2025


def main():
    start, rows, cols = get_inputs()
    # We now have guaranteed correct inputs from the get_inputs function
    print_grid(start, rows, cols)
    return

def get_inputs():
    while True:

        while True:
            try:
                start = int(input("Enter the starting number (n):\n"))
                rows = int(input("Enter the number of rows (r):\n"))
                cols = int(input("Enter the number of columns (c):\n"))
                break
            except:
                print("Invalid input. Please enter integers.")

        if rows > 0 and cols >0 and start>0:
            return start, rows, cols
        print("Rows and columns must be positive integers.")

def print_grid(n,r,c):
    for row in range(r):
        for col in range(c):
            if col == c-1:
                print("{:>3}".format(n+col))
                n = n + col + 1
                continue
            print("{:>3}".format(n + col), end=" ")
            ...
if __name__ == "__main__":
    main()