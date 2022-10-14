"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
Users put 3 numbers(a, b, and c)
and these three numbers will be brought into the equation (b ** 2-4*a*c)
If discriminant greater than 0, the console are going to print two real roots.
if discriminant equals 0, the console are going to print one root.
If discriminant less than 0, the console are going to tell users "No real roots".

	"""
	get_root()


def get_root():
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = b ** 2-4*a*c
	# print(discriminant)
	if discriminant > 0:
		x1 = (-b+math.sqrt(discriminant))/2*a
		x2 = (-b-math.sqrt(discriminant))/2*a
		print('Two roots: ' + str(x1)+' ,' + str(x2))
	elif discriminant == 0:
		x1 = -b/2*a
		print('One root: ' + str(x1))
	else:
		print('No real roots')



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
