from process_data import data
from math import exp, floor, ceil

def sigmoid(z):
    if z < 0:
        return exp(z) / (1 + exp(z))
    else:
        return 1 / (1 + exp(-z))

def mean_elt(args):
	total = 0
	count = 0
	for value in args.values():
		if isinstance(value, (int, float)):
			total += value
			count += 1
	return total / count if count else 0

def variance(values):
	m = mean(values)
	total = 0
	for value in values:
		total += (value - m) ** 2
	return total / len(values)

def mean(values):
	return sum(values) / len(values)

def get_subject(subject):
	values = []
	for house in data.Houses:
		students = getattr(data, house)
		for student in students:
			value = student[subject]
			if value is not None:
				values.append(value)
	return values

def lowest_variance():
    variances = {}
    for subject in data.subjects:
        values = [
            student[subject]
            for student in data.Students
            if student[subject] is not None
        ]
        variances[subject] = variance(values)
    return sorted(variances.items(), key=lambda x: x[1])[:2]

def percentile(values, p):
    n = len(values)
    if n == 1:
        return values[0]
    pos = (n - 1) * p / 100
    lower = floor(pos)
    upper = ceil(pos)
    if lower == upper:
        return values[lower]
    weight = pos - lower
    return values[lower] * (1 - weight) + values[upper] * weight
