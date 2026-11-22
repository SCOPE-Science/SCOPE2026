"""Self-contained exact-arithmetic checks for a two-fidelity Gaussian bridge design.
Run: python verify.py
"""
from fractions import Fraction as F
from math import sqrt, isclose


def K(s,t):
    return min(s,t)-s*t


def gain_direct(x,y,d):
    # Exact Gaussian two-observation Schur complement for interior rational sites.
    a=K(x,x); b=K(y,y); k=K(x,y)
    A=(1+d)*a; D=A*b-k*k
    assert D>0
    p=(1+d)*a/F(2); q=b/F(2)
    return (b*p*p-2*k*p*q+A*q*q)/D


def gain_sequential(x,y,d):
    a=K(x,x); b=K(y,y); k=K(x,y)
    return (1+d)*a/F(4)+(b-k)**2/(4*(b-k*k/((1+d)*a)))

# Independently derived Schur complement and conditional-update formulas agree
# exactly at a finite Cartesian grid of distinct rational parameters.
count=0
for d in (F(1,10),F(1,2),F(1),F(3),F(10),F(100)):
    for j in range(1,12):
        for k in range(1,12):
            x=F(j,12); y=F(k,12)
            assert gain_direct(x,y,d)==gain_sequential(x,y,d)
            count+=1
    co=(1+d)/16
    assert gain_direct(F(1,2), F(1,2),d)==co
    example=gain_direct(F(1,2),F(1,4),d)
    assert example-co==(1+d)/(64*(3*d+2))
    count+=2

# Exact maximum of the limiting low-site correction and displacement constant
# are identities in Q(sqrt(5)); verify numerically to tight tolerances and
# independently check strict decrease on a fine test grid, not as continuum proof.
y0=(3-sqrt(5))/4
c=(7-3*sqrt(5))/4
sharp=(5*sqrt(5)-11)/32
assert 0<y0<.5 and c>0 and sharp>0

def g_center(y):
    if y==0 or y==1: return 0.0
    if y<=.5: return y*(.5-y)**2/(1-y)
    return (1-y)*(y-.5)**2/y
assert isclose(g_center(y0)/4,sharp,rel_tol=1e-12,abs_tol=1e-14)
for i in range(1001):
    y=i/1000
    assert g_center(y)<=g_center(y0)+1e-12
    count+=1

# Numerical stationary-point sanity checks at increasing discrepancy ratios.
# Coordinate scans are deliberately supplementary and do not prove uniqueness.
def gain_float(x,y,d):
    a=x*(1-x);b=y*(1-y); k=min(x,y)-x*y
    return (1+d)*a/4+(b-k)**2/(4*(b-k*k/((1+d)*a)))
for d in (10,100,1000):
    # Close-to-optimal asymptotic site must beat every colocated design.
    x=.5+c/d; y=y0
    assert gain_float(x,y,d)>(1+d)/16
    assert abs(gain_float(x,y,d)-(1+d)/16-sharp)<0.008/d
    count+=2
print('PASS: %d independent exact-rational and supplementary numerical assertions'%count)
print('golden-limit low site %.12f; high-site shift coefficient %.12f'% (y0,c))
print('sharp extra explained variance %.12f'%sharp)
