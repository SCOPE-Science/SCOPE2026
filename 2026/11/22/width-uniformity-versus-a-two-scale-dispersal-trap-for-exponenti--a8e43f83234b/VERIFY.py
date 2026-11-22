"""Independent arithmetic checks for a two-band exponential dispersal theorem.

The analytic proof establishes all-real-parameter assertions; these checks are
supplementary, not a finite substitute for its universal quantifiers.
Run: python3 VERIFY.py
Requirements: Python 3, mpmath, sympy.
"""
from fractions import Fraction as Q
import mpmath as mp
import sympy as sy

mp.mp.dps = 65
z = sy.symbols('z')
assert Q(1)-Q(2,9)-Q(27,32) == -Q(19,288)
assert Q(129,1100)-Q(11,100) > 0
assert mp.e > mp.mpf(27)/10 and mp.e < mp.mpf(11)/4
assert 9*mp.exp(-mp.mpf(9)/2) < mp.mpf(11)/100
assert (mp.e-2)/(mp.e**2) > mp.mpf(3)/32
checks=5

def g(x):
    return mp.exp(-x)-mp.exp(-2*x)
def gp(x):
    return 2*mp.exp(-2*x)-mp.exp(-x)
def fp(t,L):
    return gp(t)+L*gp(L*t)
def F(t,L):
    return g(t)+g(L*t)

# Sturm root certificate for the dimensionless L=9 instance.
# Under z=exp(-t), the derivative is z*(-1+2*z-9*z**8+18*z**17).
P = -1+2*z-9*z**8+18*z**17
assert sy.count_roots(P, 0, 1) == 3
checks += 1

for L in [9, 10, 11, 20, 100]:
    L=mp.mpf(L)
    bounds=[mp.mpf('0'),1/L,mp.mpf('0.5'),mp.log(2)]
    signs=[fp(t,L) for t in bounds]
    assert signs[0]>0 and signs[1]<0 and signs[2]>0 and signs[3]<0
    roots=[mp.findroot(lambda v:fp(v,L),(bounds[i],bounds[i+1]),solver='anderson')
           for i in range(3)]
    assert all(bounds[i]<roots[i]<bounds[i+1] for i in range(3))
    assert max(abs(fp(t,L)) for t in roots)<mp.mpf('1e-30')
    assert F(roots[0],L)>F(roots[2],L)
    assert F(roots[2]/L,L)>F(roots[2],L)
    checks += 6
    if L==9:
        printed=[float(v) for v in roots]
        values=[float(F(t,L)) for t in roots]
        assert abs(printed[0]-0.1021949953)<2e-9
        assert abs(printed[1]-0.4050914132)<2e-9
        assert abs(printed[2]-0.6418028141)<2e-9
        assert abs(values[0]-0.3274304997)<2e-9
        assert abs(values[2]-0.2523968476)<2e-9

# Equal-width log curvature, exact formula checked at diverse parameters.
for a,w,b in [(1,1,2),(1,1,100),(mp.mpf('0.2'),3,mp.mpf('9.2'))]:
    alpha=mp.mpf(a)/w
    delta=(mp.mpf(b)-a)/w
    for t in [mp.mpf('0.1'),1,5]:
        x=t/2
        curvature= -1/(4*mp.sinh(x)**2)+delta**2/(4*mp.cosh(delta*x)**2)
        assert curvature<0
        checks+=1

print('PASS:',checks,'supplementary tests; L=9 critical rates and values:',printed,values)
