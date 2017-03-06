from sys import stdin
from math import floor

# exapmle input:
ex_in = "6 3 1 10\n10 2 1 50\n50 5 3 14\n50 6 4 1\n50 6 3 1\n1 1 1 1\n97 56 3 10\n56 3 1 5\n0 0 0 0"

def cal_limit_day(U,D,fatigue):
	limit_day = floor((U-D)/fatigue)
	if limit_day <= 0:
		limit_day = 1
	return limit_day

def total_down_by_fatigue(day, fatigue):
	fatigue_application_times = ((day-1)*day)/2
	return fatigue_application_times * fatigue

def climbed_distance(day,U,fatigue):
	last_day_of_climbing = floor(U/fatigue)
	if day > last_day_of_climbing:
		return (last_day_of_climbing * U) - (total_down_by_fatigue(last_day_of_climbing,fatigue))
	return (U*day) - (total_down_by_fatigue(day,fatigue))

def total_climbed_before_night_at(day,U,fatigue,D): #total climbed at the end of the day
	night_sliding = D*(day-1)
	return climbed_distance(day,U,fatigue) - night_sliding

def total_climbed_after_night_at(day,U,fatigue,D): #total climbed at the end of the night
	night_sliding = D*(day)
	return climbed_distance(day,U,fatigue) - night_sliding

def can_the_snail_climb_the_well_at(day,U,fatigue,D,H):
	total_climbed_at_day = total_climbed_before_night_at(day,U,fatigue,D)
	answer = False
	if (total_climbed_at_day > H):
		answer = True
	return answer


def day_for_succes(limit_day,U,fatigue,D,H):
	day = limit_day
	for day in range(limit_day,0,-1):
		if not(can_the_snail_climb_the_well_at(day-1,U,fatigue,D,H)):
			break
	return day

def day_for_fail(day,U,fatigue,D):
	min_limit = 1
	total_climbed = total_climbed_after_night_at(day,U,fatigue,D)
	while True: #binary search
		if total_climbed >= 0:
			min_limit = day
			day = day *2
			total_climbed = total_climbed_after_night_at(day,U,fatigue,D)
		else:
			if total_climbed_after_night_at((day-1),U,fatigue,D) >= 0 : #if the previos day the total climbed is positive then day is the day of failure
				break
			middle_day = floor((day+min_limit)/2)
			if total_climbed_after_night_at(middle_day,U,fatigue,D) >= 0:
				min_limit = middle_day
			else:
				day = middle_day
	return day

# def brute_force(H,U,D,fatigue):
# 	day = 1
# 	height = 0
# 	while True:
# 		height += U
# 		U -= fatigue
# 		if U < 0:
# 			U = 0
# 		if height > H:
# 			print("success on day " + str(day))
# 			break
# 		height -= D
# 		if height < 0:
# 			print("failure on day "+ str(day))
# 			break
# 		day += 1


def main():
	lines = stdin.read().splitlines() #Use ctrl+d to finish read process
	# lines = ex_in.splitlines() # Testing
	for curr_Line in lines:
		H,U,D,F = [int(param) for param in curr_Line.split()] #the semantic of H,U,D and F is on the problem description
		if H <= 0:
			return
		fatigue  = U * (F/100)
		limit_day = cal_limit_day(U,D,fatigue) #This day the snail cannot climb more because de fatigue
		answer = can_the_snail_climb_the_well_at(limit_day,U,fatigue,D,H)
		if answer:
			day = day_for_succes(limit_day,U,fatigue,D,H)
			print("success on day " + str(day))
		else:
			day = day_for_fail(limit_day,U,fatigue,D)
			# print(total_climbed_before_night_at(31,U,fatigue,D))
			print("failure on day "+ str(day))
		# brute_force(H,U,D,fatigue)
	return

main()
