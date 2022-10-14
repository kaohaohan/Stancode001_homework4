"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
The program allows the user to input a random number and determine
whether the number is a prime number or not.
	"""
	print("Ｗelcome to the prime checker!")
	n = int(input('n: '))
	while n != -100:
		for i in range(2, n):
			if n % i == 0:
				print(str(n) + ' is a not a prime number')
				break
			elif i == n-1:
				print(str(n) + ' is a prime number')
		n = int(input('n: '))
		if n == -100:
			print('Have a good one!')






# 	if n % c == 0:
# 		print (str(n)+' is a not a prime number')
# 		break


# while c < n:
	# 	if n % c == 0:
	# 		print (str(n)+' is a not a prime number')
	# 		break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
