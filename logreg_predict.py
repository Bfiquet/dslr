import csv
from process_data import data
from utils import sigmoid
from logreg_train import get_stats
import json

def predict(student):
    probabilities = {}
    stats = get_stats()
    with open(f"weights.json", "r", encoding="utf-8") as file:
        weights = json.load(file)
    for house in data.Houses:
        theta = weights[house]
        z = theta[0]
        for j, subject in enumerate(data.subjects):
            value = student[subject]
            if value is None:
                return None
            mean, std = stats[subject]
            value = (value - mean) / std
            z += theta[j + 1] * value
        probabilities[house] = sigmoid(z)
    return max(probabilities, key=probabilities.get)

def predict_house():
    predicted_house = []
    for index, student in enumerate(data.Students):
        house = predict(student)
        if house is not None:
            predicted_house.append((index, house))
    with open("houses.csv", "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["Index", "Hogwarts House"])
        for index, house in predicted_house:
            spamwriter.writerow([index, house])


def accuracy():
    correct = 0
    total = 0
    for student in data.Students:
        if student["house"] is None:
            continue
        predicted = predict(student)
        if predicted is None:
            continue
        total += 1
        if predicted == student["house"]:
            correct += 1
    print("Correct :", correct)
    print("Total   :", total)
    print("Accuracy:", correct / total)

predict_house()
accuracy()