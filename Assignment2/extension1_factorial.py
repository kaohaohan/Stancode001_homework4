"""
File: extension1_factioral.py
Name: 
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
Users can input a positive integer and get factorial of the number.
	"""
	print("Ｗelcome to standCode factorial master!")
	n = int(input('Give me a number, and I will list the answer of factorial: '))
	k = 1
	while True:
		if n == -100:
			print("- - - - - - See ya! - - - - - - ")
			return
		if n < 0:
			k = 1
			n = int(input('Give me a number, and I will list the answer o2factorial: '))
		else:
			for i in range(1, n+1):
				k = k * i
			print("Answer: " + str(k))
			k = 1
			n = int(input('Give me a number, and I will list the answer of factorial: '))




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()