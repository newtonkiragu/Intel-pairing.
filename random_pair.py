#!/usr/bin/env python

# Module that randomizes items in a list.
from random import shuffle

# Opens a text file with names of x students
with open('x.txt') as x_names:
  names = x_names.readlines()

# Strips the line breaks
x_list = [name.strip() for name in names]
# print(name_list)

# Opens a text file with name of k students
with open('k.txt') as k_names:
  names = k_names.readlines()

k_list = [name.strip() for name in names]


# Randomizes the name list
shuffle(x_list)
shuffle(k_list)

# Transforms the two list into a list with tuples with pairs
pair_list = list(zip(x_list, k_list))
# print(pair_list)

# Creates and writes the name of pairs
with open("random_pair.txt", "w") as output_file:
  # Iterates through the list and then extracts the names from the tuples. Puts the pair in new lines.
  output_file.write('\n'.join('{}, {}'.format(x[0], x[1]) for x in pair_list))

# print(output_file)

"""
For prep i have estimated that i need 6 randomized pairings before group projects.

So roughly 8 including the first week of prep.

For core i estimate 20 pairings. 4 for the Js, 8 python, 8 django.
This is minus the group project for the python module and capstone for the django module.
"""