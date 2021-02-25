import csv

score = []

level = raw_input("What level rider are you? novice, intermediate, or expert?  ")
if level == "novice":
	score.append(1)
if level == "intermediate":
	score.append(2)
if level == "expert":
	score.append(3)
#print(level)

terrain = raw_input("What type of terrain do you want to ride? freeride, park, piste, powder, race, urban? ")
if terrain == "freeride":
	score.append(.1)
if terrain == "park":
	score.append(.2)
if terrain == "piste":
	score.append(.3)
if terrain == "powder":
	score.append(.4)
if terrain == "race":
	score.append(.5)
if terrain == "urban":
	score.append(.6)
#print(terrain)

boot_size = raw_input("What size boot do you wear? ")
if int(boot_size) < 11.5:
	score.append(.01)
if int(boot_size) >= 11.5:
	score.append(.02)

#print(boot_size)

score_total = (score[0] + score[1] + score[2])
print(score_total)


with open ('board.csv', 'r') as csv_file:
	reader = csv.reader(csv_file)
	if score_total == 1.11:
		for row in reader:
			print(row[1])
	if score_total == 1.12:
		for row in reader:
			print(row[2])
	if score_total == 1.21:
		for row in reader:
			print(row[3])
	if score_total == 1.22:
		for row in reader:
			print(row[4])
	if score_total == 1.31:
		for row in reader:
			print(row[5])
	if score_total == 1.32:
		for row in reader:
			print(row[6])
	if score_total == 1.41:
		for row in reader:
			print(row[7])
	if score_total == 1.42:
		for row in reader:
			print(row[8])
	if score_total == 1.51:
		for row in reader:
			print(row[9])
	if score_total == 1.52:
		for row in reader:
			print(row[10])
	if score_total == 1.61:
		for row in reader:
			print(row[11])
	if score_total == 1.62:
		for row in reader:
			print(row[12])		
###########
	if score_total == 2.11:
		for row in reader:
			print(row[13])
	if score_total == 2.12:
		for row in reader:
			print(row[14])
	if score_total == 2.21:
		for row in reader:
			print(row[15])
	if score_total == 2.22:
		for row in reader:
			print(row[16])
	if score_total == 2.31:
		for row in reader:
			print(row[17])
	if score_total == 2.32:
		for row in reader:
			print(row[18])
	if score_total == 2.41:
		for row in reader:
			print(row[19])
	if score_total == 2.42:
		for row in reader:
			print(row[20])
	if score_total == 2.51:
		for row in reader:
			print(row[21])
	if score_total == 2.52:
		for row in reader:
			print(row[22])
	if score_total == 2.61:
		for row in reader:
			print(row[23])
	if score_total == 2.62:
		for row in reader:
			print(row[24])				
#########
	if score_total == 3.11:
		for row in reader:
			print(row[25])
	if score_total == 3.12:
		for row in reader:
			print(row[26])
	if score_total == 3.21:
		for row in reader:
			print(row[27])
	if score_total == 3.22:
		for row in reader:
			print(row[28])
	if score_total == 3.31:
		for row in reader:
			print(row[29])
	if score_total == 3.32:
		for row in reader:
			print(row[30])
	if score_total == 3.41:
		for row in reader:
			print(row[31])
	if score_total == 3.42:
		for row in reader:
			print(row[32])
	if score_total == 3.51:
		for row in reader:
			print(row[33])
	if score_total == 3.52:
		for row in reader:
			print(row[34])
	if score_total == 3.61:
		for row in reader:
			print(row[35])
	if score_total == 3.62:
		for row in reader:
			print(row[36])


print("If you entered in a boot size of 11.5 or above make sure you look for a wide board. These are often marked by a wide designation or a 'w'.")


adv = raw_input("If you would like to proceed to the advanced questionaire type 'yes'.  ")

if (adv == "yes"):
	flex = raw_input("How much flex do you want in your board? soft, medium, stiff?  ")
	if flex == "soft":
		score.append(.001)
	if flex == "medium":
		score.append(.002)
	if flex == "stiff":
		score.append(.003)

print(score)


