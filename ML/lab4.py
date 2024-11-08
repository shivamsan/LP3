import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return (x + 3) ** 2


def derivative(x):
    return 2 * (x + 3)


learning_rate = 0.1  
n_iterations = 50    
x_start = 2          


x_values = [x_start]
y_values = [function(x_start)]


x = x_start
for i in range(n_iterations):
    gradient = derivative(x)           
    x = x - learning_rate * gradient    
    y = function(x)                     

    x_values.append(x)
    y_values.append(y)


x_range = np.linspace(-10, 4, 100)
y_range = function(x_range)


plt.figure(figsize=(10, 6))
plt.plot(x_range, y_range, label="y = (x + 3)^2", color="blue")
plt.scatter(x_values, y_values, color="red", label="Gradient Descent Path")
plt.plot(x_values, y_values, color="red", linestyle="--")
plt.title("Gradient Descent to Find Local Minima of y = (x + 3)^2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
# Show the plot
plt.show()