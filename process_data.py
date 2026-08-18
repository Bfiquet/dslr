import csv
import sys
from dataclasses import dataclass, field

@dataclass
class Dataset:
	Houses: list = field(default_factory=lambda: ["Slytherin", "Gryffindor", "Ravenclaw", "Hufflepuff"])
	Slytherin: list = field(default_factory=list)
	Gryffindor: list = field(default_factory=list)
	Ravenclaw: list = field(default_factory=list)
	Hufflepuff: list = field(default_factory=list)
	Students: list = field(default_factory=list)
	subjects: list = field(default_factory=lambda: ["arithmancy", "astronomy", "herbology", "defense", "divination", "studies", "runes", "history", "transfiguration", "potions", "care", "charms", "flying"])

def to_float(value):
	return float(value) if value else None

def process_data(file="datasets/dataset_train.csv"):
	dataset = Dataset()
	with open(file, newline="", encoding="utf-8") as file:
		reader = csv.DictReader(file)
		for row in reader:
			student = {
				# "index": row["Index"],
				"house": row["Hogwarts House"],
				"first_name": row["First Name"],
				"last_name": row["Last Name"],
				"birthday": row["Birthday"],
				"best_hand": row["Best Hand"],
				"arithmancy": to_float(row["Arithmancy"]),
				"astronomy": to_float(row["Astronomy"]),
				"herbology": to_float(row["Herbology"]),
				"defense": to_float(row["Defense Against the Dark Arts"]),
				"divination": to_float(row["Divination"]),
				"studies": to_float(row["Muggle Studies"]),
				"runes": to_float(row["Ancient Runes"]),
				"history" : to_float(row["History of Magic"]),
				"transfiguration": to_float(row["Transfiguration"]),
				"potions": to_float(row["Potions"]),
				"care": to_float(row["Care of Magical Creatures"]),
				"charms": to_float(row["Charms"]),
				"flying": to_float(row["Flying"])
			}
			getattr(dataset, student["house"]).append(student)
			dataset.Students.append(student)
		return dataset

if "logreg_train.py" in sys.argv[0]:
    data = process_data("datasets/dataset_train.csv")
else:
    data = process_data()

if __name__ == "__main__":
	for student in data.Slytherin:
		print(student["first_name"])
	print("--------------------Gryffindor-----------------------")
	for student in data.Gryffindor:
		print(student["first_name"])
	print("--------------------Ravenclaw-----------------------")
	for student in data.Ravenclaw:
		print(student["first_name"])
	print("--------------------Hufflepuff-----------------------")
	for student in data.Hufflepuff:
		print(student["first_name"])