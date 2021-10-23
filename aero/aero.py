import numpy as np
from canopy import Canopy

ALPHA_0 = 0
LAMBDA = 0

def body_to_wind(u):
    # Body-to-wind described by:
    #   1) Rotation about Y Body axis by -alpha
    #   2) Rotation about resulting Z axis by +beta
    #
    # V = magnitude of body-axis velocity vector
    # alpha = angle of attack (wind-axes)
    # beta = bank angle (wind-axes)

    V = np.linalg.norm(u)
    alpha = np.arctan2(u[3], u[1])
    beta = np.arcsin(u[2] / V)

    return [beta, alpha, V]

def compute_CL(canopy, alpha, CL_pilot):

    return CL

def compute_CD(canopy, alpha, CD_pilot):
    return CD

def compute_epsilon(canopy):
    return epsilon

def compute_k1(canopy):
    if canopy.AR >= 2.5:
        return 0
    elif canopy.AR > 1:
        return (3.33 - 1.33*canopy.AR)
    else:
        raise Exception("Aspect Ratio cannot be less than 1.")
 
