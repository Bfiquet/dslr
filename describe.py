from process_data import data
from utils import *
from math import sqrt
		
def describe():
	results = {}
	for subject in data.subjects:
		values = [student[subject] for student in data.Students
				  if student[subject] is not None]
		values.sort()
		n = len(values)
		results[subject] = {
			"Count": n,
			"Missing": len(data.Students) - n,
			"Mean": mean(values),
			"Std": sqrt(variance(values)),
			"Min": values[0],
			"25%": percentile(values, 25),
			"50%": percentile(values, 50),
			"75%": percentile(values, 75),
			"Variance": variance(values),
			"Range": values[-1] - values[0],
			"Max": values[-1]
		}
	subjects_per_line = 7
	
	for start in range(0, len(data.subjects), subjects_per_line):
		subjects = data.subjects[start:start + subjects_per_line]
		print(f"{'':<12}", end="")
		for subject in subjects:
			print(f"{subject:<17}", end="")
		print()
		for stat in ["Count", "Missing", "Mean", "Std", "Min",
					 "25%", "50%", "75%", "Variance", "Range", "Max"]:
			print(f"{stat:<12}", end="")
			for subject in subjects:
				value = results[subject][stat]
				if stat in ["Count", "Missing"]:
					formatted = f"{value:.0f}"
				elif stat == "Variance":
					formatted = f"{value:.2e}"
				else:
					formatted = f"{value:.2f}"
				print(f"{formatted:<17}", end="")
			print()
		print()
		
describe()
