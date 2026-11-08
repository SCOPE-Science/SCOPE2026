#!/usr/bin/env python3
"""Exact coefficient check for centroidal radial moments of a uniform triangle.
Uses only Python standard library; no floating-point arguments of correctness.
"""
from fractions import Fraction as Q
from math import factorial
from collections import defaultdict

def plus(*polys):
    z=defaultdict(Q)
    for p in polys:
        for k,c in p.items(): z[k]+=c
    return {k:v for k,v in z.items() if v}

def scale(p,c):
    return {k:v*c for k,v in p.items() if v*c}

def times(p,q):
    z=defaultdict(Q)
    for a,c in p.items():
        for b,d in q.items(): z[tuple(i+j for i,j in zip(a,b))]+=c*d
    return {k:v for k,v in z.items() if v}

# Monomials ordered as squared side lengths A,B,C, barycentric variables u,v.
one={(0,0,0,0,0):Q(1)}
A={(1,0,0,0,0):Q(1)}
B={(0,1,0,0,0):Q(1)}
C={(0,0,1,0,0):Q(1)}
u={(0,0,0,1,0):Q(1)}
v={(0,0,0,0,1):Q(1)}
l1=u; l2=v; l3=plus(one,scale(u,-1),scale(v,-1))
d1=plus(l1,scale(one,-Q(1,3)))
d2=plus(l2,scale(one,-Q(1,3)))
d3=plus(l3,scale(one,-Q(1,3)))
# Squared distance from centroid: Z=-A*d2*d3-B*d3*d1-C*d1*d2.
z=scale(plus(times(A,times(d2,d3)),times(B,times(d3,d1)),times(C,times(d1,d2))),-1)

def exact_integral(p):
    out=defaultdict(Q)
    for (a,b,c,i,j),v in p.items():
        out[a,b,c]+=v*Q(2*factorial(i)*factorial(j),factorial(i+j+2))
    return {k:v for k,v in out.items() if v}

def exp_poly(p,n):
    out=one
    for _ in range(n):out=times(out,p)
    return out

def subtract(a,b):return plus(a,scale(b,-1))

p1=plus(A,B,C)
p2=plus(times(A,B),times(A,C),times(B,C))
p3=times(A,times(B,C))
formulas=[
    scale(p1,Q(1,36)),
    scale(subtract(times(p1,p1),scale(p2,2)),Q(1,270)),
    plus(scale(exp_poly(p1,3),Q(163,408240)),scale(times(p1,p2),-Q(19,22680)),scale(p3,-Q(1,756)))
]
for n in (1,2,3):
    computed=exact_integral(exp_poly(z,n))
    expected={k[:3]:v for k,v in formulas[n-1].items() if k[3:]==(0,0)}
    assert computed==expected,(n,computed,expected)

# Two triangles: squared sides (1,2,3) and (3/2,(9 +/- sqrt(13))/4).
# The latter has sum 6, sum of squared entries 14, and product 51/8.
def moment_vals(e1,e2,e3):
    return (e1/Q(36), (e1*e1-2*e2)/Q(270),
        Q(163,408240)*e1**3-Q(19,22680)*e1*e2-e3/Q(756))
m=moment_vals(Q(6),Q(11),Q(6))
n=moment_vals(Q(6),Q(11),Q(51,8))
assert m[:2]==n[:2]==(Q(1,6),Q(7,135))
assert m[2]-n[2]==Q(1,2016)
assert m[2]==Q(29,1260) and n[2]==Q(227,10080)

# Exact reconstruction via all permutations, including equilateral/isoceles.
from itertools import product
tested=0
for aa,bb,cc in product(range(1,7), repeat=3):
    aa,bb,cc=Q(aa),Q(bb),Q(cc)
    if 4*(aa*bb+aa*cc+bb*cc)<=(aa+bb+cc)**2:continue
    tested+=1
    e1=aa+bb+cc; e2=aa*bb+aa*cc+bb*cc; e3=aa*bb*cc
    m1,m2,m3=moment_vals(e1,e2,e3)
    v1=36*m1
    v2=(v1*v1-270*m2)/2
    v3=756*(Q(163,408240)*v1**3-Q(19,22680)*v1*v2-m3)
    assert (v1,v2,v3)==(e1,e2,e3)
    assert 81*m1*m1-Q(135,4)*m2==Q(4*e2-e1*e1,16)
assert tested==201
print(f'VERIFY_OK universal_polynomial_identities=3 exact_triangle_cases={tested} sharp_two_moment_pair=1 exact_area_formula=checked')
