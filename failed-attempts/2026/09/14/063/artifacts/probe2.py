import sys; sys.path.insert(0,'output/artifacts')
from qscat import *
import sympy as sp
print(lefschetz_decomp(t**3+3*t+3/t+1/t**3))
print(lefschetz_decomp(t+1/t))
print(lefschetz_decomp(t**2+1+1/t**2))
