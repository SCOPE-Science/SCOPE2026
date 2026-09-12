import numpy as np
from fractions import Fraction
# Exact rational certificate of frame FAILURE.
# Strategy: find rational point (y0,th0) where det M(y0,th0) = 0 exactly (or lambda_min = 0 with explicit kernel vector),
# then extend by continuity to a positive-measure neighborhood where lambda_min < A for any A>0? No: single zero only kills lower bound if zero persists on positive measure OR we build Weyl sequence.
# Actually for Gabor frames with nice windows, S has purely continuous (fiber) spectrum: if fiber M(y0,th0) is singular at ONE point, then A must be 0. Proof: fiber eigenvalues are continuous in (y,th); if lambda_min(y0,th0)=0 then essinf=0. A single-point zero suffices! (No need for positive-measure kernel field.)
# So it suffices to exhibit ONE (y0,th0) with det M = 0 exactly + continuity argument.
# Search: from numerics, near-zero at y~delta/2? Let's do exact rational arithmetic at candidate lattice points.
def B3(x):
    ax=abs(x)
    if ax<1: return (Fraction(4)-6*x*x+3*ax**3)/6
    elif ax<=2: return (Fraction(2)-ax)**3/6
    else: return Fraction(0)
a=Fraction(1,2); beta=Fraction(6,11); delta=Fraction(1,22); binv=Fraction(6,11)
def Gk(k,x):
    tot=Fraction(0)
    for n in range(-10,11):
        tot+=B3(x-n*a)*B3(x-n*a-k*beta)
    return tot
# try y0 = delta/2 = 1/44? and theta values 0, 1/2, and scan theta = t/24
y0=Fraction(1,44)
# Build M(y0,theta) as matrix over Q(zeta) with zeta = e^{2pi i theta}; for theta with small denominator entries are in cyclotomic field; det is algebraic number.
# Instead compute exact rational Gk values at the 11 nodes:
nodes=[y0+s*delta for s in range(11)]
for s in range(11):
    print("node",s,float(nodes[s]),"G0=",float(Gk(0,nodes[s])),"G1=",float(Gk(1,nodes[s])),"G-1=",float(Gk(-1,nodes[s])))
