import json
from process_data import data
from utils import sigmoid

def create_data(house):
    X = []
    y = []
    for student in data.Students:
        row =[]
        skip = False
        for subject in data.subjects:
            value = student[subject]
            if value is None:
                skip = True
                break
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
    for house in data.Houses:
        X, y = create_data(house)
        tab = [0.0] * (len(data.subjects) + 1)
        thetas = gradient_descent(X, y, tab)
        print("Fin maison :", house)
        with open(f"{house}.json", "w", encoding="utf-8") as file:
            json.dump(thetas, file, indent=4, ensure_ascii=False)

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

get_weights()