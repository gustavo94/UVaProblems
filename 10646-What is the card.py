from sys import stdin
# exapmle input:
# ex_in = "2\nAC  KC  QC  JC  TC  9C  8C  7C  6C  5C  4C  3C  2C  AD  KD  QD  JD  TD  9D  8D  7D  6D  5D  4D  3D  2D  AH  KH QH  JH  TH  9H  8H  7H  6H  5H  4H  3H  2H  AS  KS  QS  JS  TS  9S  8S  7S  6S  5S  4S  3S  2S\nAC  KC  QC  JC  TC  9C  8C  7C  6C  5C  4C  3C  2C  AD  KD  QD  JD  TD  9D  8D  7D  6D  5D  4D  3D  2D  AH  KH QH  JH  TH  9H  8H  7H  6H  5H  4H  3H  2H  AS  KS  QS  JS  TS  9S  8S  7S  6S  5S  4S  3S  2S"

def card_value(card):
	if card[0] in ['A','K','Q','J','T']:
		return 10
	return int(card[0])

def main():
	lines = stdin.read().splitlines() #Use ctrl+d to finish read process
	# lines = ex_in.splitlines() # Testing
	cases_quantity = int(lines[0])
	# print(cases_quantity)
	for case_number in range(1,cases_quantity+1):
		cards = lines[case_number].split()
		cards_in_hand = cards[27:52]
		pile = cards[0:27]
		Y=0 # Same Y of the problem description
		for i in range(1,4):
			pile_size = len(pile)
			X = card_value(pile[pile_size-1]) # Same X of the problem description
			droped_cards = (10 - X) +1 # (10 - X) is from the problem description and the +1 is the top card used for get X value
			pile = pile[0:pile_size - droped_cards]
			Y+= X
		cards = pile + cards_in_hand
		print("Case %s: %s"%(case_number,cards[Y-1])) # -1 because the list start in the position cero ...
	return

main()
