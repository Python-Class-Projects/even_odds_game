'''
The program will ask the user for a list of integers. Then it will calculate the numbers retrieved and print the sum of the evens, 
sum of the odds, the total sum, and which side -end or odd- won. This process will repeat if the user indicates to want to. 
A function must be use called "is_even" to determine if a number is even. 
'''

def is_even(integer):
	int_evens = 0 #Initialization of variables to store even/odds.
	int_odds = 0

	if integer % 2 == 0: #Condition that determines if even.
		int_evens += integer

	elif integer % 2 > 0: #Conditions that determines if odd.
		int_odds += integer

	return int_evens, int_odds #Returns the values of evens and odds.

#Determines who wins: evens or ods. Will then print a line of code to state who won.
def who_wins(even, odd): 
	if even > odd:
		print("The evens win.")
	elif even < odd:
		print("The odds win.")
	else:
		print("It is a tie! No one wins.")

#Loop in which the user will play the game inside. 
play_again = "y"
while play_again == "y":

	int_values = input("Enter a list of integers seperated by spaces: ")
	values_array = int_values.split(" ")

	#Initialization of variables to track the values for each iteration.
	int_total_tracker = 0
	int_even_tracker = 0
	int_odd_tracker = 0
	for i in values_array:
		i = int(i) #Converting the string into an integer.
		int_total_tracker += i #keeps track of integers to keep total value.
		int_evens, int_odds = is_even(i) #Used to obtain the values after determining if even or odd.
		int_even_tracker += int_evens #Tracks the evens total.
		int_odd_tracker += int_odds #Tracks the odd total.

	#Printing the values and sum. Asking the user to play again.
	print(f"Sum of Evens = {int_even_tracker}")
	print(f"Sum of odds = {int_odd_tracker}")
	print(f"Total Sum = {int_total_tracker}")
	who_wins(int_even_tracker, int_odd_tracker)
	play_again = input("Again? ")
	play_again = play_again.lower()

print("\nEND OF PROGRAM\n")