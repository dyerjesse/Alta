import csv

def intial(switch) :
	switch = "one"
	switcher = {
		1: "one",
		2: "two",
		3: "three"
	}
	print switcher.get(switch, "invalid number")

