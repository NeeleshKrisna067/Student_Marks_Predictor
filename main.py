import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import joblib

# Load data - corrected filename to student_data.csv
data = pd.read_csv("student_data.csv")

print("Data Preview:")
print(data.head())
print("\nData Stats:")
print(data.describe())

# Prepare features and target
X = data[['study_hours', 'sleep_hours', 'attendance']]
y = data['marks']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.pkl")
print("Model saved to model.pkl")

# Prediction test
prediction = model.predict([[5, 7, 80]])
print("\nPredicted Marks for [5, 7, 80]:", prediction[0])

# Evaluate model
y_pred = model.predict(X_test)
error = mean_absolute_error(y_test, y_pred)
print("\nMean Absolute Error:", error)

# Visualization
plt.scatter(data['study_hours'], data['marks'])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()