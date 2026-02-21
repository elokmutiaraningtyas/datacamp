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



