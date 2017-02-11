from sys import stdin

def main():
	lines = stdin.read().splitlines() #Use ctrl+d to finish read process
	for curr_Line in lines:
		print(curr_Line)
		
	return 

main()
