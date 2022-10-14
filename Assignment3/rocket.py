"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    Users are able to input the random number to build up the rocket.
    The rocket will base on the numbers to turn out different size.
    """
    size = int(input('SIZE: '))
    head(size)
    belt(size)
    upper(size)
    lower(size)
    head(size)

def head(n):
    """
      The rocket head. This function comes up the rocket head and bottom
    """
    for i in range(n):
        print(" ", end='')
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range( i + 1):
            print('/', end='')
        for f in range( i + 1):
            print('\\', end='')
        print('\n', end='')


def belt(n):
    """
      The belt connects the head with the upper body,
      and the lower body with the bottom
     """

    print("+", end='')
    for i in range (0 , 2*n , 1):
        print("=", end="")
    print("+")

def upper(n):
    """
      The rocket upper body
     """

    for i in range(n):
        print('|', end='')
        for j in range(n - i - 1):
            print('.', end='')
        for k in range(i+1 ):
            print('/', end='')
            print('\\', end='')
        for a in range(n - i - 1):
            print('.', end='')
        print("|")
        print('', end='')

def lower(n):
    """
      The rocket lower body
     """

    for i in range(n):
        print('|', end='')
        for a in range(i):
            print('.', end='')
        for j in range(n-i):
            print('\\', end='')
            print('/', end='')
        for k in range(i):
            print('.', end='')
        print("|")
        print('', end='')







if __name__ == "__main__":
    main()
