#!/usr/bin/env python3

import sys
sys.path.insert(1, '/home/reidm/Python_Projects/parachute-model/')

import numpy as np
import aero
import canopy.canopy as canopy

# @TODO: Create functions with multiple unit test cases for each function...
# Use actual test features in Python

c = canopy.Canopy('Sabre2', 120)
alpha = 0.175

def body_to_wind_test():
    print("Test: body_to_wind")
    assert aero.body_to_wind([1, 0, 0]) == [0.0, 0.0, 1.0], "[1, 0, 0] failed"
# WRONG    assert aero.body_to_wind(0) == None, "Invalid input."
    print("")

body_to_wind_test()

print("Test: compute_CL_alpha")
print(aero.compute_CL_alpha(c))
print("")

#print("Test: compute_CL_lines")
#print(aero.compute_CL_lines(c, alpha))

print("Test: compute_epsilon")
print(aero.compute_epsilon(c))
print("")

