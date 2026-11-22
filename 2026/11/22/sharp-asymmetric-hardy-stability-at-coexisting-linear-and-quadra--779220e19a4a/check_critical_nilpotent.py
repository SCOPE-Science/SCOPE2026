"""Standalone reproducibility checks for a two-well spectral-set stability law.
No finite computation is used as proof of a universal statement.
"""
import math
import numpy as np
import sympy as sp

x = sp.symbols('x', real=True)
trace = 4*x + 3*(1-x)**2
determinant = 3*x*x
assert sp.simplify(9-3*trace+determinant-6*x*(1-x)) == 0
# At the critical weights, a normalized nilpotent shift has square
# singular-value trace 4*x+3*y*y and determinant 3*x*x.
checks = 1
for i in range(1, 100):
    xx = i / 100
    for j in range(1, 21):
        yy = (1-xx)*j/20
        B = np.array([[math.sqrt(3*xx),math.sqrt(3)*yy],[0.,math.sqrt(xx)]])
        top = np.linalg.norm(B,2)**2
        assert top <= 3.000000001
        assert 3-top >= 2*xx*(1-xx)-1e-10
        checks += 2
for t in [0.5,0.2,0.1,0.05,0.02,0.01,0.005,0.001]:
    # f_t(z)=z(z-t)/(1-tz) is inner, with coefficients -t, 1-t^2
    B = np.array([[-math.sqrt(3)*t, math.sqrt(3)*(1-t*t)], [0., -t]])
    deficit = 3 - np.linalg.norm(B,2)**2
    d2_square = 2*t*t
    assert abs(d2_square/deficit - 1) < 5*t*t+1e-6
    checks += 1
for h in [0.3,0.1,0.03,0.01,0.003,0.001]:
    t = 1-h
    B = np.array([[-math.sqrt(3)*t, math.sqrt(3)*(1-t*t)], [0., -t]])
    deficit = 3-np.linalg.norm(B,2)**2
    d1_square=2*(1-t)
    assert abs(d1_square/deficit-1/3) < 10*h+1e-6
    checks+=1
print(f'CRITICAL_NILPOTENT_TWO_WELL_CHECK_OK {checks}')
