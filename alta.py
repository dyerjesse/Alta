import csv

score = []

sport = raw_input("Are you looking for skis or snowboards? ski, board  ")

level = raw_input("What level rider are you? novice, intermediate, advanced, expert?  ")
if level == "novice":
	score.append(1)
if level == "intermediate":
	score.append(2)
if level == "advanced":
	score.append(3)
if level == "expert":
	score.append(4)
#print(level)

terrain = raw_input("What type of terrain do you want to ride? freeride, park, piste, powder, race, urban, touring?  ")
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
if terrain == "touring":
	score.append(.7)
#print(terrain)

if sport == ("board"):
	boot_size = raw_input("What size boot do you wear? ")
	if int(boot_size) < 11.5:
		score.append(.01)
	if int(boot_size) >= 11.5:
		score.append(.02)
#print(boot_size)

if sport == ("board"):
	score_total = (score[0] + score[1] + score[2])
else :
	score_total = (score[0] + score[2])
print(score_total)
print(score)


if sport == ("board") :
	with open ('board.csv', 'r') as board_db:
		reader = csv.reader(board_db)
		#Novice start
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
		#Intermediate Start 
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
		#Advanced Start
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
		if score_total == 3.71:
			for row in reader:
				print(row[37])
		if score_total == 3.72:
			for row in reader:
				print(row[38])
		#Expert Start 
		if score_total == 4.11:
			for row in reader:
				print(row[39])
		if score_total == 4.12:
			for row in reader:
				print(row[40])
		if score_total == 4.21:
			for row in reader:
				print(row[41])
		if score_total == 4.22:
			for row in reader:
				print(row[42])
		if score_total == 4.31:
			for row in reader:
				print(row[43])
		if score_total == 4.32:
			for row in reader:
				print(row[44])
		if score_total == 4.41:
			for row in reader:
				print(row[44])
		if score_total == 4.42:
			for row in reader:
				print(row[45])
		if score_total == 4.51:
			for row in reader:
				print(row[46])
		if score_total == 4.52:
			for row in reader:
				print(row[47])
		if score_total == 4.61:
			for row in reader:
				print(row[48])
		if score_total == 4.62:
			for row in reader:
				print(row[49])
		if score_total == 4.71:
			for row in reader:
				print(row[50])
		if score_total == 4.72:
			for row in reader:
				print(row[51])

"""
if sport == ("ski"):
	with open('ski.csv', 'r') as ski_db:
		ski_reader = csv.reader(ski_db)
		if score_total == 1.1:
			for row in ski_reader:
			print(row[1])
		if score_total == 1.2:
			for row in ski_reader::
			print(row[2])
		if score_total == 1.3:
			for row in ski_reader::
			print(row[3])
		if score_total == 1.4:
			for row in ski_reader::
			print(row[4])
		if score_total == 1.5:
			for row in ski_reader::
			print(row[5])
		if score_total == 1.6:
			for row in ski_reader::
			print(row[6])
"""

#print("If you entered in a boot size of 11.5 or above make sure you look for a wide board. These are often marked by a wide designation or a 'w'.")


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


