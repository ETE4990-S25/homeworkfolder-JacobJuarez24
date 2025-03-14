## Part 1

# Inports here
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create histogram
data = np.random.randn(1000) 
"""Create random data."""

plt.figure(figsize=(8,6))
plt.hist(data, bins=30, color='blue', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Line Plot
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # Sine wave
"""Define the amount of points used, and define the sine wave."""

plt.figure(figsize=(10,6))
plt.plot(x, y, label="sin(x)", color='blue')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
"""Create random data."""

plt.figure(figsize=(10,6))
plt.scatter(x, y, color='green')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Pie Plot
sizes = [15, 30, 45, 10]  # Representing percentages
labels = ['A', 'B', 'C', 'D']

plt.figure(figsize=(10,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()

# Area Plot
x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.figure(figsize=(10,6))
plt.fill_between(x, y, color='pink', alpha=0.3)
plt.plot(x, y, color='red', label='cos(x)')
plt.title("Area Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# 3-D Plot - Bar Plot
x = np.arange(5)                    # X positions of bars
y = np.random.rand(5)               # Y positions of bars
z = np.zeros(5)                     # Z positions (ground level)
dx = np.ones(5)                     # Width of each bar
dy = np.ones(5)                     # Depth of each bar
dz = np.random.randint(1, 10, 5)    # Heights of bars

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(x, y, z, dx, dy, dz, color='purple')

plt.title("3D Bar Plot")
plt.show()

## Part 2

# Define the dtype for the structured array
dtype = [
    ('Name', 'U100'),   # Name as a string of up to 100 characters
    ('Year', 'i4'),     # Year as an integer
    ('NA_Sales', 'f4'), # North America sales as a float
]

# Load data from the CSV file
game_sales_data = np.genfromtxt(
    'video_game_sales.csv', 
    delimiter=',',  # Change this delimiter if the file uses something else
    skip_header=1,  # Skip the header row
    dtype=dtype,    # Use the defined dtype to parse the columns
    usecols=(1, 2, 9)  # Columns 1, 2, and 59 are Name, Year, and NA_Sales
)

# Display the first few rows to verify
print("First 5 rows of original data:")
print(data[:5])

# Sort the data by Name, Year, and NA_Sales
sorted_game_sales_data = np.sort(game_sales_data, order=['Name', 'Year', 'NA_Sales'])

# Display the sorted data
print("First 10 rows of sorted data:")
print(sorted_game_sales_data[:10])