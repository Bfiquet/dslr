import json
from process_data import data
from utils import sigmoid, mean, variance

def get_stats():
    stats = {}
    for subject in data.subjects:
        values = [
            student[subject]
            for student in data.Students
            if student[subject] is not None
        ]
        avg = mean(values)
        std = variance(values) ** 0.5
        stats[subject] = (avg, std)
    return stats

def create_data(house, stats):
    X = []
    y = []
    for student in data.Students:
        row = []
        skip = False
        for subject in data.subjects:
            value = student[subject]
            if value is None:
                skip = True
                break
            mean, std = stats[subject]
            if std == 0:
                value = 0
            else:
                value = (value - mean) / std
            row.append(value)
        if skip:
            continue
        X.append(row)
        if student["house"] == house:
            y.append(1)
        else:
            y.append(0)
    return X, y

def get_weights():
    weights = {}
    stats = get_stats()
    for house in data.Houses:
        X, y = create_data(house, stats)
        theta = [0.0] * (len(data.subjects) + 1)
        theta = gradient_descent(X, y, theta)
        print("Fin maison :", house)
        weights[house] = theta
    with open("weights.json", "w", encoding="utf-8") as file:
        json.dump(weights, file, indent=4, ensure_ascii=False)

def gradient_descent(X, y, theta):
    learning_rate = 0.001
    m = len(X)
    for iteration in range(10000):
        if iteration % 1000 == 0:
            print("iteration :", iteration)
        gradients = [0.0] * len(theta)
        for i in range(m):
            prediction = sigmoid(
                theta[0] + sum(
                    X[i][j] * theta[j + 1]
                    for j in range(len(X[i]))
                )
            )
            error = prediction - y[i]
            gradients[0] += error
            for j in range(len(X[i])):
                gradients[j + 1] += error * X[i][j]
        for j in range(len(theta)):
            theta[j] -= learning_rate * gradients[j] / m
    return theta

if __name__ == "__main__":
    get_weights()