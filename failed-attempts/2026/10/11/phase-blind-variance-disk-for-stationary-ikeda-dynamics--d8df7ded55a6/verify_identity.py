#!/usr/bin/env python3
import sympy as sp

a, R, x, y = sp.symbols("a R x y", real=True)
s = 1 - R**2
q = (2*a*x - a**2) / s
variance_from_balance = q - x**2 - y**2
variance_disk = a**2*R**2/s**2 - ((x-a/s)**2 + y**2)
assert sp.simplify(variance_from_balance - variance_disk) == 0
print("IDENTITY_OK")
