# Your First NumPy Array
# You're now going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of numpy, a powerful package to do data science.

# A list baseball has already been defined in the Python script, representing the height of some baseball players in centimeters. Can you add some code to create a numpy array from it?

# Instructions
# 100 XP
# Import the numpy package as np, so that you can refer to numpy with np.
# Use np.array() to create a numpy array from baseball. Name this array np_baseball.
# Print out the type of np_baseball to check that you got it right.

# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# output:

# <class 'numpy.ndarray'>


# -----------------------------------------------------------------------------


# Baseball players' height
# You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for some more statistics on the height of the main players. They pass along data on more than a thousand players, which is stored as a regular Python list: height_in. The height is expressed in inches. Can you make a numpy array out of it and convert the units to meters?

# height_in is already available and the numpy package is loaded, so you can start straight away (Source: stat.ucla.edu).

# Instructions
# 100 XP
# Create a numpy array from height_in. Name this new array np_height_in.
# Print np_height_in.
# Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
# Print out np_height_m and check if the output makes sense.


# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)


# output :

# [74 74 72 72 73 69 69 71 76 71 73 73 74 74 69 70 73 75 78 79]
# [1.8796 1.8796 1.8288 1.8288 1.8542 1.7526 1.7526 1.8034 1.9304 1.8034
#  1.8542 1.8542 1.8796 1.8796 1.7526 1.778  1.8542 1.905  1.9812 2.0066]


# --------------------------------------------------------------------------------------------------------


# Subsetting NumPy Arrays
# Subsetting (using the square bracket notation on lists or arrays) works exactly the same with both lists and arrays.

# This exercise already has two lists, height_in and weight_lb, loaded in the background for you. These contain the height and weight of the MLB players as regular lists. It also has two numpy array lists, np_weight_lb and np_height_in prepared for you.

# Instructions
# 100 XP
# Subset np_weight_lb by printing out the element at index 50.
# Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.


import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])


# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


# output : 

# <script.py> output:
#     200
#     [73 74 72 73 69 72 73 75 75 73 72]


# --------------------------------------------------------------------------------------------------------


# Your First 2D NumPy Array
# Before working on the actual MLB data, let's try to create a 2D numpy array from a small list of lists.

# In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. baseball is already coded for you in the script.

# Instructions
# 100 XP
# Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.

# Print out the type of np_baseball.
# Print out the shape attribute of np_baseball. Use np_baseball.shape.


import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# output : 
# <class 'numpy.ndarray'>
# (4, 2)

# --------------------------------------------------------------------------------------------------------

# Baseball data in 2D form
# You realize that it makes more sense to restructure all this information in a 2D numpy array.

# You have a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this list is baseball and it has been loaded for you already (although you can't see it).

# Store the data as a 2D array to unlock numpy's extra functionality.

# Instructions
# 100 XP
# Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
# Print out the shape attribute of np_baseball


import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball

print(np_baseball.shape)

# output:  (1015, 2)



# ----------------------------------------------------------------------------------------------------------------------

# Subsetting 2D NumPy Arrays
# If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

# # numpy
# import numpy as np
# np_x = np.array(x)
# np_x[:, 0]
# The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

# Instructions
# 100 XP
# Print out the 50th row of np_baseball.
# Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
# Select the height (first column) of the 124th baseball player in np_baseball and print it out.

import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]


# Print out height of 124th player
print(np_baseball[123, 0])


#output: 

# [ 70 195]
# 75


# --------------------------------------------------------------------------------------------------------------------


# 2D Arithmetic
# 2D numpy arrays can perform calculations element by element, like numpy arrays.

# np_baseball is coded for you; it's again a 2D numpy array with 3 columns representing height (in inches), weight (in pounds) and age (in years). baseball is available as a regular list of lists and updated is available as 2D numpy array.

# Instructions
# 100 XP
# You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
# You want to convert the units of height and weight to metric (meters and kilograms, respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
# Multiply np_baseball with conversion and print out the result.

import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)


# output :

# [[ 75.2303559  168.83775102  23.99      ]
#  [ 75.02614252 231.09732309  35.69      ]
#  [ 73.1544228  215.08167641  31.78      ]
#  ...
#  [ 76.09349925 209.23890778  26.19      ]
#  [ 75.82285669 172.21799965  32.01      ]
#  [ 73.99484223 203.14402711  28.92      ]]
# [[ 1.8796  81.64656 22.99   ]
#  [ 1.8796  97.52228 34.69   ]
#  [ 1.8288  95.25432 30.78   ]
#  ...
#  [ 1.905   92.98636 25.19   ]
#  [ 1.905   86.18248 31.01   ]
#  [ 1.8542  88.45044 27.92   ]]


# --------------------------------------------------------------------------------------------------------------------


# Basic Statistic

# Average versus median
# You now know how to use numpy functions to get a better feeling for your data.

# The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers. np_baseball is available.

# Instructions
# 100 XP
# Create numpy array np_height_in that is equal to first column of np_baseball.
# Print out the mean of np_height_in.
# Print out the median of np_height_in.

import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# **Output:**
# ```
# 1586.46
# 74.0


# --------------------------------------------------------------------------------------------------------------------


# Explore the baseball data
# Because the mean and median are so far apart, you decide to complain to the MLB. They find the error and send the corrected data over to you. It's again available as a 2D NumPy array np_baseball, with three columns.

# The Python script in the editor already includes code to print out informative messages with the different summary statistics and numpy is already loaded as np. Can you finish the job? np_baseball is available.

# Instructions
# 100 XP
# The code to print out the mean height is already included. Complete the code for the median height.
# Use np.std() on the first column of np_baseball to calculate stddev.
# Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr


avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

# output :

# Average: 73.6896551724138
# Median: 74.0
# Standard Deviation: 2.312791881046546
# Correlation: [[1.         0.53153932]
#  [0.53153932 1.        ]]





