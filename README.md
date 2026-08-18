# DSLR — Data Science × Logistic Regression

DSLR is a **Data Science and Machine Learning project written in Python**.
The goal is to explore a dataset, understand and visualize its characteristics, clean and prepare the data, and finally build a **logistic regression model from scratch** to solve a classification problem.

This project is part of a Machine Learning learning path and focuses on understanding what happens **before, during, and after** training a classification model.

> The objective is to understand and implement the mathematical concepts behind the algorithm.

---

## 📌 Project Overview

Machine Learning is not only about training a model.

Before giving data to an algorithm, it is essential to understand:

* What the dataset contains
* Which features are relevant
* How the data is distributed
* Whether there are missing or invalid values
* How different variables are correlated
* How the data should be normalized or transformed
* Which features can be used to train the model

In DSLR, we explore these different steps before implementing a **logistic regression classifier**.

The project is divided into two main parts:

1. **Data Science** — exploration, visualization, cleaning and preprocessing
2. **Machine Learning** — implementation and training of a logistic regression model

---

## 🎯 Objectives

The main objectives of this project are to:

* Learn how to read and manipulate a dataset
* Explore data using statistical methods
* Visualize relationships between variables
* Identify relevant features
* Detect and handle unnecessary or problematic data
* Understand data preprocessing
* Implement logistic regression
* Train a classification model
* Evaluate the model's performance
* Understand the mathematics behind logistic regression

---

## 🧠 Logistic Regression

The model estimates the probability that an observation belongs to a particular class.

For a binary classification problem, the logistic function, also called the **sigmoid function**, is used:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

where:

$$
z = \theta_0 + \theta_1x_1 + \theta_2x_2 + \dots + \theta_nx_n
$$

The output of the sigmoid function is a value between **0 and 1**, which can be interpreted as a probability.

A threshold can then be used to determine the predicted class:

```text
P(class = 1) >= 0.5  →  class 1
P(class = 1) <  0.5  →  class 0
```

The model parameters are optimized using **gradient descent** in order to minimize the cost function.

---

## 🔬 Data Science

The first part of the project focuses on understanding the dataset before training the model.

### Dataset exploration

The dataset is loaded and analyzed manually to understand:

* Number of observations
* Number of features
* Data types
* Value ranges
* Missing values
* Distribution of features
* Relationships between variables

### Data visualization

Different types of visualizations can be used to better understand the dataset:

* Histograms
* Scatter plots
* Pair plots

Visualization is particularly useful for identifying patterns and determining whether some features could help distinguish between classes.

### Data preprocessing

Before training the model, the data needs to be prepared.

This may include:

* Removing unnecessary information
* Handling missing values
* Selecting relevant features
* Normalizing or standardizing numerical values
* Separating features from target labels

---

## 📊 Model Training

Once the data has been prepared, the logistic regression model is trained.

The training process consists of:

1. Initializing the model parameters
2. Computing predictions using the sigmoid function
3. Calculating the cost
4. Computing gradients
5. Updating the parameters
6. Repeating the process until convergence

Conceptually:

```text
Dataset
   │
   ▼
Data exploration
   │
   ▼
Data cleaning
   │
   ▼
Feature selection
   │
   ▼
Normalization
   │
   ▼
Train / Test split
   │
   ▼
Logistic Regression
   │
   ▼
Predictions
   │
   ▼
Model evaluation
```

---

## 📈 Evaluation

The model is evaluated using data that was not used during training.

The main objective is not simply to obtain a high score, but to understand **why the model makes its predictions** and how the different features influence the result.

---

## 🛠️ Technologies

The project is implemented in **Python**.

Main tools used include:

* **Python 3**
**csv** — reading and creating CSV files 
**json** — reading and creating JSON files
* **Matplotlib** — data visualization

The core logistic regression algorithm is implemented manually rather than relying on a ready-made machine learning implementation.

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
cd DSLR
```
Install the dependencies:

```bash
pip install -r requirements.txt
```
---

## ▶️ Usage

The project provides several scripts for data analysis, visualization, and logistic regression.

### 📊 Data Visualization

#### Pair Plot

Visualize the relationships between all features of the dataset:

```bash
python3 src/pair_plot.py
```

#### Scatter Plot

Visualize the relationship between two selected features:

```bash
python3 src/scatter_plot.py
```

#### Histogram

Visualize the distribution of the dataset's features:

```bash
python3 src/histogram.py
```

### 🔎 Data Analysis

Analyze and explore the dataset:

```bash
python3 src/data_analysis.py
```

### 🤖 Logistic Regression

Train the logistic regression model:

```bash
python3 src/logreg_train.py
```

> **Note:** Make sure the dataset is located in the expected directory before running the scripts.

## 📚 What I Learned

This project provides an introduction to several important concepts in Data Science and Machine Learning:

* Dataset exploration
* Data visualization
* Feature selection
* Data preprocessing
* Normalization
* Logistic regression
* Sigmoid functions
* Gradient descent
* Model evaluation
* Machine Learning fundamentals

Understanding the dataset before training the model is just as important as the algorithm itself.

---

## 🔭 Future Improvements

Possible improvements include:

* Add more fields to the describe
* Implement optimization algorithms

---

## 👤 Author

**<Bfiquet>**

Project developed as part of a Machine Learning / Data Science curriculum.

---

