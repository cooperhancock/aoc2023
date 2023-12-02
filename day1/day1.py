# input puzzle input as list
lines = []
with open('day1.txt', 'r') as f:
    lines = f.readlines()

# remove endlines
lines = [l[:-1] for l in lines]

def parse1(line):
	firstval = -1
	lastval = -1
	for char in line:
		if not char.isalpha():
			# set firstval only once
			firstval = int(char) if firstval<0 else firstval
			# update lastval each time
			lastval = int(char)
	return firstval, lastval

def match(strings):
	match_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for n, s in enumerate(strings):
		if s in match_list:
			return match_list.index(s) + 1, n
	return -1, n

def parse2(line):
	match_strings = []
	firstval = -1
	lastval = -1
	for char in line:
		# add new match string
		match_strings.append("")
		if char.isalpha():
			# append char to match strings for analysis
			match_strings = list(map(lambda s: s + char, match_strings))
		else:
			# set firstval only once
			firstval = int(char) if firstval<0 else firstval
			# update lastval each time
			lastval = int(char)
			# reset match_string
			match_strings = []
			continue
		# analyze match string
		num, index = match(match_strings)
		if num != -1:
			# set firstval only once
			firstval = int(num) if firstval<0 else firstval
			# update lastval each time
			lastval = int(num)
			# reset match_string
			match_strings = match_strings[index+1:]
	return firstval, lastval	

# PART 1

sum = 0
for line in lines:
	firstval, lastval = parse1(line)
	sum = sum + (10*firstval + lastval)
print(sum)

# PART 2

sum = 0
for line in lines:
	firstval, lastval = parse2(line)
	sum = sum + (10*firstval + lastval)
print(sum)

