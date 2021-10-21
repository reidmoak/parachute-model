#!/usr/bin/env python3

import numpy as np

class Canopy:

    def __init__(self, name, size):
        self.name = str(name)
        self.S = int(size)
        
        self.model = {
            'sabre2'       : 'SA2',
            'sabre3'       : 'SA3',
            'katana'       : 'KA',
            'velocity'     : 'VE',
            'comp velocity': 'VC',
            'valkyrie'     : 'VK'
        }.get(self.name.lower(), 'UNK')

        self.AR = {
            'SA2'          : 2.58,
            'SA3'          : 2.59,
            'KA'           : 2.74,
            'VE'           : 2.68,
            'VC'           : 2.68,
            'VK'           : 2.84
        }.get(self.model, 'UNK')

        if self.model == 'SA2':
            self.c = {
                97         : 5.85,
                107        : 6.15,
                120        : 6.51
            }.get(self.S, 0)
        else:
            self.c = 0

        self.R = 110.85 / 12 # feet - Sabre2 120, averaged across A lines

    def print_fields(self):
        print("name: " + self.name)
        print("model: " + self.model)
        print("size: " + str(self.S) + " sq ft")
        print("Aspect Ratio: " + str(self.AR))
        print("Chord Length: " + str(self.c) + " ft")
        print("Line Length: " + str(self.R) + " ft")
