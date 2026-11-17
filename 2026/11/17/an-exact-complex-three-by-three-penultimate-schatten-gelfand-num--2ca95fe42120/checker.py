"""Finite diagnostics for an equilateral complex Schatten matrix pencil.

The analytic proof is given separately; this script checks representative
parameter grids and the sharp singular rank-two witness.
"""
import cmath
import math

zeta = cmath.exp(2j*math.pi/3)
assert abs(zeta**3 - 1) < 1e-12

def val(s, e):
    if math.isinf(e):
        return max(s)
    return sum(t**e for t in s)**(1/e)

checks=0
for p in (0.2,0.5,0.75,1.0):
    for q in (2.0,4.0,float('inf')):
        sharp=2**((0 if math.isinf(q) else 1/q)-1/p)
        for t in (0.0,0.1,0.5,1.0,1.2,2.0,4.0):
            for k in range(96):
                a=1.0
                b=t*cmath.exp(2j*math.pi*k/96)
                s=[abs(a+b*zeta**j) for j in range(3)]
                assert val(s,q)/val(s,p) <= sharp+2e-9
                checks+=1
        s=[0.0,abs(1-zeta),abs(1-zeta**2)]
        assert abs(val(s,q)/val(s,p)-sharp)<1e-10
        checks+=1
print('COMPLEX_SCHATTEN_PENCIL_DIAGNOSTICS_OK', checks)
