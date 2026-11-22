"""Exact and supplementary checks for a two-method three-taxon richness comparison.
Run with python3 checker.py; standard library only.
The mathematical proofs of general uniqueness are in RESULT.md, not in this checker.
"""
from fractions import Fraction
from itertools import product
from math import log

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def polynomial_coefficients():
    # Difference sum(y**b)-sum(y**a) for a=(2,3,11), b=(1,6,8)
    p=[0]*12
    for z in (1,6,8):p[z]+=1
    for z in (2,3,11):p[z]-=1
    return p

# -y(y-1)(y^3+y^2-1)(y^6+y^4-1)
y=[0,1]; y_minus_one=[-1,1]; cubic=[-1,0,1,1]; sextic=[-1,0,0,0,1,0,1]
fac=mul(mul(mul(y,y_minus_one),cubic),sextic)
assert [-z for z in fac] == polynomial_coefficients()

# Rational brackets for the two positive roots y6 and y3.
def evalpoly(cs,v):
    out=Fraction(0)
    for coef in reversed(cs):out=out*v+coef
    return out
l3,h3=Fraction(754877,1000000),Fraction(754879,1000000)
l6,h6=Fraction(868836,1000000),Fraction(868838,1000000)
assert evalpoly(cubic,l3)<0<evalpoly(cubic,h3)
assert evalpoly(sextic,l6)<0<evalpoly(sextic,h6)
assert h3<l6
assert mul(cubic, [1])==cubic
assert evalpoly(cubic, Fraction(0))==-1 and evalpoly(cubic,Fraction(1))==1
assert evalpoly(sextic,Fraction(0))==-1 and evalpoly(sextic,Fraction(1))==1

# Exact alternating signs of richness differences at 3 physical effort levels.
# Here y=exp(-V), so decreasing y represents increasing V.
for val, sign in [(Fraction(9,10),1),(Fraction(4,5),-1),(Fraction(1,2),1)]:
    assert sign*evalpoly(polynomial_coefficients(),val)>0

# The two roots are at V = log(rho)/2 and log(rho), rho^3=rho+1.
# The following is only a numerical diagnostic of the exact characterization.
import math
low, high=1.0,2.0
for _ in range(100):
    rho=(low+high)/2
    if rho**3>rho+1:high=rho
    else:low=rho
rho=(low+high)/2
assert abs((rho**3-rho-1))<1e-12
assert abs(-math.log(((l6+h6)/2).numerator/((l6+h6)/2).denominator)-log(rho)/2)<1e-5
assert abs(-math.log(((l3+h3)/2).numerator/((l3+h3)/2).denominator)-log(rho))<1e-5

# Supplementary two-taxon finite testing on a rational y grid.  The proof of
# a continuous one-crossing law is analytical, not based on this enumeration.
checks=0
for a1,a2,b1,b2 in product(range(1,7), repeat=4):
    vals=[]
    for j in range(1,100):
        yy=Fraction(j,100)
        vals.append(yy**b1+yy**b2-yy**a1-yy**a2)
        checks+=1
    signs=[(v>0)-(v<0) for v in vals]
    signs=[s for s in signs if s]
    assert sum(x!=z for x,z in zip(signs,signs[1:]))<=1
    # If one crossing exists, the two endpoint diagnostics must oppose.
    small=(a1+a2)-(b1+b2)
    far=min(a1,a2)-min(b1,b2)
    if sum(x!=z for x,z in zip(signs,signs[1:]))==1:
        assert small*far<0
print('PASS: exact factorization, rational sign certificates, endpoint roots, and',checks,'two-taxon supplementary comparisons')
