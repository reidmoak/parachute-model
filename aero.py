import numpy as nu

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



