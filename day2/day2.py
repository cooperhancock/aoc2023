# input puzzle input as list
lines = []
with open('day2.txt', 'r') as f:
    lines = f.readlines()

# remove endlines, split at space
lines = [l[:-1].split(' ')[2:] for l in lines]

# PART 1

sum=0
for i, line in enumerate(lines):
	possible = True
	for j in range(0, len(line), 2):
		color = line[j+1][0]
		num = int(line[j])
		if (color == 'r' and num > 12) or (color == 'b' and num > 14) or (color == 'g' and num > 13):
			possible = False
			break
	sum += i+1 if possible else 0	
	
print(sum)

# PART 2

sum=0
for line in lines:
	red=0
	green=0
	blue=0
	for j in range(0, len(line), 2):
		color = line[j+1][0]
		num = int(line[j])
		if color == 'r':
			red = max(red, num)
		elif color == 'g':
			green = max(green, num)
		elif color == 'b':
			blue = max(blue, num)
	sum += red * green * blue

print(sum)
