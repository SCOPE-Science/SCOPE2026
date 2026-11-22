"""Exact and independent geometric checks for five-cube two-level section volumes.

Usage: python3 verify.py
Requires Python 3 with sympy, numpy, scipy.
"""
from itertools import product
from math import comb, sqrt
import numpy as np
import sympy as sp
from scipy.linalg import null_space
from scipy.spatial import ConvexHull

z = sp.symbols('z', positive=True)
intervals = {
    (2, 3): (sp.S(0), sp.Rational(2, 3), sp.S(1)),
    (3, 2): (sp.S(0), sp.Rational(1, 2), sp.S(1)),
    (1, 4): (sp.S(0), sp.Rational(1, 4), sp.Rational(1, 2), sp.S(1)),
    (4, 1): (sp.S(0), sp.S(1)),
}
expected = {
    (2, 3): [1 - 13*z/32,
             (3*z**4-24*z**3+216*z**2-96*z+16)/(192*z**3)],
    (3, 2): [(9-2*z**2)/12,
             (16*z**4-96*z**3+216*z**2-24*z+3)/(192*z**2)],
    (1, 4): [sp.S(1),
             -(64*z**4-256*z**3+96*z**2-16*z+1)/(192*z**4),
             (128*z**3-16*z+3)/(192*z**4)],
    (4, 1): [(3*z**3-16*z**2+128)/192]
}
expected_derivatives = {
    (2, 3): [-(39*z*z-48*z+13)/16,
             (z-1)*(3*z**5-9*z**4-8*z**3+40*z**2-48*z+16)/(32*z**4)],
    (3, 2): [-z*(2*z*z-1)/2,
             (z-1)*(16*z**5-48*z**4+40*z**3-8*z**2-9*z+3)/(32*z**3)],
    (1, 4): [4*z,
             -(64*z**6-96*z**4+96*z**3-51*z**2+12*z-1)/(48*z**5),
             -(z-1)*(3*z-1)/(16*z**5)],
    (4, 1): [z**2*(z-3)*(z-1)/16]
}

def truncated_convolution_density(p, q, mid):
    """Inclusion-exclusion density of p unit and q z-weighted uniforms."""
    numerator = sp.S(0)
    for j in range(p+1):
        for k in range(q+1):
            knot = sp.Rational(p,2)-j+(sp.Rational(q,2)-k)*z
            if knot.subs(z,mid)>0:
                numerator += (-1)**(j+k)*comb(p,j)*comb(q,k)*knot**4
    return sp.cancel(numerator/(24*z**q))

checks = 0
for (p,q), breaks in intervals.items():
    for i,(lo,hi) in enumerate(zip(breaks,breaks[1:])):
        mid = (lo+hi)/2
        f=truncated_convolution_density(p,q,mid)
        assert sp.simplify(f-expected[(p,q)][i])==0
        checks+=1
        D=sp.factor((p+q*z*z)*sp.diff(f,z)+q*z*f)
        assert sp.simplify(D-expected_derivatives[(p,q)][i])==0
        checks+=1
        # Validate symbolic formula at three rational interior positions.
        for r in (sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)):
            t=lo+(hi-lo)*r
            assert sp.simplify(f.subs(z,t)-expected[(p,q)][i].subs(z,t))==0
            checks+=1

# All branches join continuously and with continuous first derivatives.
for pq, breaks in intervals.items():
    for i,knot in enumerate(breaks[1:-1]):
        f1=expected[pq][i];f2=expected[pq][i+1]
        assert sp.simplify((f1-f2).subs(z,knot))==0
        assert sp.simplify((sp.diff(f1,z)-sp.diff(f2,z)).subs(z,knot))==0
        checks+=2

# Exact sign certificates for the two nontrivial polynomial factors.
p23 = 3*z**5-9*z**4-8*z**3+40*z**2-48*z+16
p32 = 16*z**5-48*z**4+40*z**3-8*z**2-9*z+3
p14 = 64*z**6-96*z**4+96*z**3-51*z**2+12*z-1
u=sp.symbols('u')
assert sp.simplify(p32.subs(z,(1+u)/2)-(u**5-u**4-4*u**3-6*u-2)/2)==0
checks+=1

def bernstein_coefficients(pol,degree):
    pp=sp.Poly(sp.expand(pol),u)
    a=[pp.nth(k) for k in range(degree+1)]
    return [sp.factor(sum(a[k]*sp.Rational(comb(j,k),comb(degree,k)) for k in range(j+1))) for j in range(degree+1)]

b23=bernstein_coefficients(-p23.subs(z,(2+u)/3),5)
b14=bernstein_coefficients(-p14.subs(z,(1+u)/4),6)
assert b23==[sp.Rational(160,81),sp.Rational(128,45),sp.Rational(488,135),sp.Rational(196,45),sp.Rational(77,15),sp.S(6)]
assert b14==[sp.Rational(3,64),sp.Rational(3,32),sp.Rational(3,16),sp.Rational(5,16),sp.Rational(37,80),sp.Rational(5,8),sp.Rational(3,4)]
assert all(v>0 for v in b23+b14)
checks+=3

alpha=(24-sp.sqrt(69))/39
assert sp.simplify((39*z**2-48*z+13).subs(z,alpha))==0
assert sp.Rational(2,5)<alpha<sp.Rational(1,2)
assert (24+sp.sqrt(69))/39>sp.Rational(2,3)
checks+=3

# Independent Euclidean 4-volume via clipping all 80 cube edges.
vertices=np.array(list(product((-0.5,0.5),repeat=5)),float)
for p,q,tvals in [(2,3,[.18,.37,.41,.58,.73,.9]),
                  (3,2,[.2,.44,.57,.72,.88]),
                  (1,4,[.12,.3,.46,.65,.86]),
                  (4,1,[.13,.35,.62,.85])]:
    for t in tvals:
        normal=np.array([1.0]*p+[t]*q)
        dots=vertices @ normal
        intersections=[]
        for i,v in enumerate(vertices):
            for axis in range(5):
                if v[axis]>0: continue
                j=i^(1<<(4-axis))
                a=dots[i];b=dots[j]
                if a*b<0:
                    intersections.append(v+(a/(a-b))*(vertices[j]-v))
        assert len(intersections)>=5
        basis=null_space(normal[None,:])
        coords=np.array(intersections)@basis
        hull=ConvexHull(coords)
        fcase=next(expected[(p,q)][j] for j,(left,right) in enumerate(zip(intervals[(p,q)],intervals[(p,q)][1:])) if float(left)<t<float(right))
        closed=float(sp.sqrt(p+q*sp.Rational(str(t))**2)*fcase.subs(z,sp.Rational(str(t))))
        assert abs(hull.volume-closed)<3e-10,(p,q,t,hull.volume,closed)
        checks+=1

print('PASS',checks,'exact symbolic identities/positivity conditions and independent geometric volume comparisons')
print('critical small/large ratio:', sp.N(alpha,18))
print('critical normalized large coordinate:', sp.N((2+3*alpha**2)**(-sp.Rational(1,2)),18))
print('critical section volume:', sp.N(sp.sqrt(2+3*alpha**2)*(1-13*alpha/32),18))
