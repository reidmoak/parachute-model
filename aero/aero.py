#!/usr/bin/env python3

import numpy as np
import sys

sys.path.append("..")

# CONSTANTS @TODO DEFINE THESE
ALPHA_0 = 0
LAMBDA = 0
CD_0 = 0
TAU = 0
MU = 0

def body_to_wind(u):
    # Body-to-wind described by:
    #   1) Rotation about Y Body axis by -alpha
    #   2) Rotation about resulting Z axis by +beta
    #
    # V = magnitude of body-axis velocity vector
    # alpha = angle of attack (wind-axes)
    # beta = bank angle (wind-axes)

    V = np.linalg.norm(u)
    alpha = np.arctan2(u[2], u[0])
    beta = np.arcsin(u[1] / V)

    return [beta, alpha, V]

def compute_CL_alpha(canopy):
    CL_alpha =  (np.pi * canopy.CL_airfoil * canopy.AR
                  / (np.pi * canopy.AR + canopy.CL_airfoil
                  * (1 + TAU)))
    return CL_alpha
     
def compute_CL_lines(canopy, alpha):
    CL_lines = (-1 * canopy.num_lines * canopy.line_d * canopy.R
                * ((np.cos(alpha + MU))**2) * (np.sin(alpha + MU))**2
                / canopy.S)
    return CL_lines

def compute_epsilon(canopy):
    # b = curved/arc span of the canopy
    # R = line length
    return canopy.b / (4 * canopy.R)

def compute_k1(canopy):
    if canopy.AR >= 2.5:
        return 0
    elif canopy.AR > 1:
        return (3.33 - 1.33*canopy.AR)
    else:
        raise Exception("Aspect Ratio cannot be less than 1.")
 
def compute_CL_sys(canopy, alpha, CL_pilot):
    CL_wing = (compute_CL_alpha(canopy) * (alpha - ALPHA_0) 
               * (np.cos(compute_epsilon(canopy)))**2
               + compute_k1(canopy) * (np.sin(alpha - ALPHA_0))**2
               * np.cos(alpha - ALPHA_0))

    CL_lines = compute_CL_lines(canopy, alpha) 

    return (CL_wing + CL_lines + CL_pilot)

def compute_CD_sys(canopy, alpha, CD_pilot):
    CD_wing = (CD_0 + (compute_CL_alpha(canopy)**2 * (alpha - ALPHA_0)**2
                * (1 + LAMBDA) / (np.pi * canopy.AR))
                + compute_k1(canopy) * (np.sin(alpha - ALPHA_0))**3)

    CD_lines = ((canopy.num_lines * canopy.line_d * canopy.R
                * (np.cos(alpha + MU))**3) / canopy.S)

    return (CD_wing + CD_lines + CD_pilot)

