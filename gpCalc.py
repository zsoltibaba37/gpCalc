#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Peto"
__license__ = "MIT"
__copyright__ = "Copyright 2026"
__version__ = "0.1"
__status__ = "Stable"

from sys import argv, exit
from termcolor import cprint
import datetime

d = datetime.datetime.now()
example = 145.99

def linea():
    print("----------------------------------------")

def usage():
    print(f"{argv[0]} {__version__}")
    print(f"{__copyright__} {__author__}\n")
    print("Usage:")
    print(f"$> python {argv[0]} {example}\n")

if len(argv) < 2:
    usage()
    print(f"Need Frequency !!! \n")
    exit(1)

try:
    x = float(argv[1])
    if x <= 0:
        raise ValueError
except ValueError:
    usage()
    print("Use float number !")
    print("The number is zero or smaller then zero\n")
    exit()



f = float(argv[1]) * 1e6    # Frequency
c = 299_792_458             # Speed of light ~
vf = 0.96                   # Velocity factor

##################################################################
########## Calculations ##########
'''
Vertical Monopole Radiating Element (λ*0.25)*vf
Radials                             (λ*0.28)*vf
'''
l = c / f
v = l * 0.25 * vf * 1e3
r = l * 0.28 * vf * 1e3
linea()
print("    - Ground Plane Antenna Design -")
linea()
print(f" The frequency is  : ", end='')
cprint(f"{argv[1]} MHz", "yellow")
linea()
print(f" Vertical element  : ", end='')
cprint(f"{v:.2f} mm", "green")
print(f" Radials           : ", end='')
cprint(f"{r:.2f} mm", "yellow")
print(" Radials angle     : 45°")
linea()
print("        ", end='')
cprint(d.strftime("%c"), "green")
linea()
########## END ##########
