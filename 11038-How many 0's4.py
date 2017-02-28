from sys import stdin

def zeros_until(number):
	power_of_ten = 10
	# power_n = 1
	zeros = 1 #count from 0
	while power_of_ten <= number:
		if power_of_ten == 10:
			zeros += number // power_of_ten
		else:
			previous_power_of_ten = power_of_ten // 10
			zeros += ((number // power_of_ten) - 1) * previous_power_of_ten
			mod = number % power_of_ten
			if mod < previous_power_of_ten:
				zeros += mod + 1
			else:
				zeros += previous_power_of_ten
		power_of_ten = power_of_ten * 10
	return zeros
def main():
	lines = stdin.read().splitlines() #Use ctrl+d to finish read process
	for curr_Line in lines:
		number1,number2 = curr_Line.split()
		number1_zeros = number1.count('0')
		number1 = int(number1)
		if number1 < 0:
			return
		number2 = int(number2)
		zeros_until_number1 = zeros_until(number1)
		zeros_until_number2 = zeros_until(number2)
		#print('until number 2: '+str(zeros_until_number2)+' until number 1: '+str(zeros_until_number1)+' zeros from number1: '+str(number1_zeros))
		print(zeros_until_number2 - zeros_until_number1 + number1_zeros)
	return

main()
