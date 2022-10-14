"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
Users are able to input random numbers which represent temperature.
The program can identify maximum temperature, lowest temperature, average temperature,
and how many low temperature alarm days.
	"""
	print("standCode \"Weather Master 4.0\"!")
	n = int(input('Next Temperature: (or -100 to quit)? '))
	if n == -100:
		print("No temperatures were entered.")

	else:
		highest_temp = n
		lowest_temp = n
		sum_temp = n
		count = 1
		cold_days = 0
		if n < 16:
			cold_days += 1
		while True:
			n = int(input('Next Temperature: (or -100 to quit)? '))
			if n == -100:
				print("No temperatures were entered.")
				break
			sum_temp += n
			count += 1
			if highest_temp < n:
				print(highest_temp)
				highest_temp = n
			if lowest_temp > n:
				lowest_temp = n
			if n < 16:
				cold_days +=1

		average = sum_temp /count


		print("Highest temperature = " + str(highest_temp))
		print("Lowest temperature = " + str(lowest_temp))
		print("Average= "+ str(average))
		print(str(cold_days)+" cold day(s)")










			# highest_temp = n
			# count += 1
		# elif lowest_temp > n:
		# 	lowest_temp = n
		# 	# count += 1
		# print("lowest_temp = "+ str(n))









# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
