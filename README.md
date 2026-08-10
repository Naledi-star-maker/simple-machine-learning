# Simple Machine Learning Example

## Introduction

This project demonstrates a very simple example of machine learning using Python and the scikit-learn library.

The program uses **linear regression** to predict an exam score based on the number of hours a student studies.

The purpose of this project is to demonstrate the basic process of machine learning in a simple way.

## How it works

The program is given some training data:

| Hours studied | Exam score |
| ------------: | ---------: |
|             1 |         50 |
|             2 |         55 |
|             3 |         65 |
|             4 |         70 |
|             5 |         80 |

The number of hours studied is the input, also called a **feature**.

The exam score is the value that the model is trying to predict, also called the **target**.

The program uses `LinearRegression` from scikit-learn:

```python
model = LinearRegression()
```

A linear regression model tries to find a straight-line relationship between the input and the target.

The model is trained using:

```python
model.fit(X, y)
```

This is where the model learns from the examples provided in the training data.

After training, the program asks the model to predict the exam score for someone who studied for 6 hours:

```python
prediction = model.predict([[6]])
```

The model uses the relationship it learned from the training examples to make its prediction.

## Why this is machine learning

This is an example of **supervised machine learning** because the model is given examples where both the input and the correct result are known.

The process is:

1. Provide training data.
2. Create a machine learning model.
3. Train the model.
4. Give the model new data.
5. Make a prediction.

The model is learning a relationship from examples instead of us manually programming a rule for the answer.

## Requirements

You need:

* Python 3
* pip
* scikit-learn

## Installation

Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project folder:

```bash
cd simple-machine-learning
```

Install the required Python package:

```bash
pip install -r requirements.txt
```

## Running the program

Run:

```bash
python main.py
```

The program will output a predicted exam score for a student who studied for 6 hours.

The exact prediction is approximately 84.

## Limitations

This is only a demonstration of machine learning. The dataset is extremely small and real exam results depend on many other factors.

The model should therefore not be used to make real decisions about students.

The purpose of this project is to demonstrate the basic machine-learning process of training a model and using it to make a prediction.
