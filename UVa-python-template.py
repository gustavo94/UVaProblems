from sys import stdin
# exapmle input:
ex_in = "6 3 1 10\n10 2 1 50\n50 5 3 14\n50 6 4 1\n50 6 3 1\n1 1 1 1\n0 0 0 0\n"

def main():
	lines = stdin.read().splitlines() #Use ctrl+d to finish read process
	#lines = ex_in.splitlines() # Testing
	for curr_Line in lines:
		print(curr_Line)

	return

main()
