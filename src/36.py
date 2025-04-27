import numpy as np
from sklearn.ensemble import RandomForestRegressor

data = [
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50],
    [50, 60]
]

features = data[0][:]
labels = data[1:]

model = RandomForestRegressor(n_estimators=10)
model.fit(features, labels)

predicted_values = model.predict([data[2:]])
print("Predicted values:", predicted_values)
