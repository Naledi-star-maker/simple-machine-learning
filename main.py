from sklearn.linear_model import LinearRegression

# Training data
# Hours studied -> Exam score
X = [[1], [2], [3], [4], [5]]
y = [50, 55, 65, 70, 80]

# Create the machine learning model
model = LinearRegression()

# Train the model using our data
model.fit(X, y)

# Ask the model to predict the score for someone
# who studies for 6 hours
prediction = model.predict([[6]])

print("Predicted exam score:", prediction[0])
