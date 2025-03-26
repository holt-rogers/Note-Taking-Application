from math import *
import math

# settings
using_degrees  = False

# constants
g = 9.8067
G = 6.6743 * 10**-11

# math functions built in

# delete these and reimplement to follow using_degrees
del globals()["sin"]
del globals()["cos"]
del globals()["tan"]

del globals()["asin"]
del globals()["acos"]
del globals()["atan"]

def sin(x):
    if using_degrees:
        x = radians(x)
    return math.sin(x)

def cos(x):
    if using_degrees:
        x = radians(x)
    return math.cos(x)

def tan(x):
    if using_degrees:
        x = radians(x)
    return math.tan(x)

def asin(x):
    theta = math.asin(x)
    if using_degrees:
        theta = degrees(theta)
    return theta
    
def acos(x):
    theta = math.acos(x)
    if using_degrees:
        theta = degrees(theta)
    return theta

def atan(x):
    theta = math.atan(x)
    if using_degrees:
        theta = degrees(theta)
    return theta
