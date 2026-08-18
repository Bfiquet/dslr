import csv
from process_data import data
from pathlib import Path
from utils import sigmoid
import json

def predict(student):
    probabilities = {}
    for house in data.Houses:
        with open(f"{house}.json", "r", encoding="utf-8") as file:
            theta = json.load(file)
        z = theta[0]
        for j, subject in enumerate(data.subjects):
            if student[subject] is None:
                return None
            z += theta[j + 1] * student[subject]
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

predict_house()