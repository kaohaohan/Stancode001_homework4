"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
Users put in a random number, and the program will identify whether it is odd or even.
If the number is odd then multiple 3 and add 1,
the program will identify the number again until the number becomes 1.
If the number is even then will be divided by 2, the program will identify the number again until number becomes 1.
    """
    n = int(input('Enter a number: '))
    hailstone(n)


def hailstone(n):
    steps = 0
    while n != 1:
        old_n = n
        steps += 1
        if n % 2 == 1:
            n = 3*n + 1
            print(str(old_n) + ' is odd, so I make 3n+1:' + str(n))
        else:
            n = n/2
            print(str(old_n) + ' is even, so I take half:' + str(n))
    print('It took ' + str(steps) + ' to reach 1.')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
