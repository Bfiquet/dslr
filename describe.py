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
    print(f"{'':<10}", end="")
    for subject in data.subjects:
        print(f"{subject:<15}", end="")
    print()
    for stat in ["Count", "Missing", "Mean", "Std", "Min", "25%", "50%", "75%", "Variance", "Range", "Max"]:
        print(f"{stat:<10}", end="")
        for subject in data.subjects:
            value = results[subject][stat]
            print(f"{value:<15.6f}", end="")
        print()
        
describe()
