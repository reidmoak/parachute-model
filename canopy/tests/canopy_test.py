#!/usr/bin/env python3

import numpy as np
import sys

sys.path.insert(1, '/home/reidm/Python_Projects/parachute-model/')

from canopy import Canopy

c = Canopy('Sabre2', 120)

c.print_fields()
