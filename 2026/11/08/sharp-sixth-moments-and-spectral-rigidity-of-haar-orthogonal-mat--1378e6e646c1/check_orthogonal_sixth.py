#!/usr/bin/env python3
"""Exact rational verification of sixth moments for real Haar-orthogonal matrix coefficients.
Run: python check_orthogonal_sixth.py
Third-party dependencies: sympy only.
"""
from itertools import combinations
from math import comb, factorial
import random
import sympy as sp


def pairings(indices):
    if not indices:
        yield ()
    else:
        a = indices[0]
        for b in indices[1:]:
            for tail in pairings(tuple(x for x in indices[1:] if x != b)):
                yield ((a, b),) + tail


def components(p, q, m=6):
    parent = list(range(m))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in p + q:
        parent[root(a)] = root(b)
    return len(set(root(i) for i in range(m)))

P = list(pairings(tuple(range(6))))
n = sp.symbols('n', integer=True, positive=True)
G = sp.Matrix(15, 15, lambda i, j: n**components(P[i], P[j]))
# Orthogonal invariance gives exactly three pairing-double-coset classes.
a = (n**2 + 3*n - 2)/(n*(n-2)*(n-1)*(n+2)*(n+4))
b = -1/(n*(n-2)*(n-1)*(n+4))
c = 2/(n*(n-2)*(n-1)*(n+2)*(n+4))
W = sp.Matrix(15,15, lambda i,j: {3:a, 2:b, 1:c}[components(P[i],P[j])])
assert all(sp.cancel(v)==int(i==j) for i in range(15) for j,v in enumerate((G*W).row(i)))
print('ORTHOGONAL_SIXTH_WEINGARTEN_15_BY_15_INVERSE_EXACT_OK')

S,T,U=sp.symbols('S T U')
E6=15*((n**2+3*n-2)*S**3-6*(n+2)*S*T+16*U)/(n*(n-2)*(n-1)*(n+2)*(n+4))
assert sp.factor(E6 - (15*a*S**3+90*b*S*T+120*c*U))==0
print('ORTHOGONAL_MATRIX_COEFFICIENT_SIXTH_MOMENT_POLYNOMIAL_EXACT_OK')


def odd_double_factorial(j):
    if j<1: return 1
    out=1
    for k in range(j,0,-2):out*=k
    return out

def sphere_mixed_moment(dim,s,l):
    den=1
    for j in range(s+l):den*=dim+2*j
    return sp.Rational(odd_double_factorial(2*s-1)*odd_double_factorial(2*l-1),den)

def frame_pair_sixth(dim, aa, bb):
    total=sp.Rational(0)
    for r in range(4):
        # first column uniform on S^(n-1), second uniform on S^(n-2) perpendicular
        s=3-r
        fact=sp.Rational(odd_double_factorial(2*r-1),sp.prod(dim-1+2*j for j in range(r)))
        e= sum((-1)**ell*comb(r,ell)*sphere_mixed_moment(dim,s,ell) for ell in range(r+1))
        total+=comb(6,2*r)*aa**(2*s)*bb**(2*r)*fact*e
    return sp.factor(total)

for d in range(3,11):
    for x,y in [(1,0),(0,2),(1,1),(1,-2),(2,3)]:
        power2=sp.Rational(x*x+y*y)
        exact=E6.subs({n:d,S:power2,T:x**4+y**4,U:x**6+y**6})
        assert sp.simplify(frame_pair_sixth(d,x,y)-exact)==0,(d,x,y)
print('INDEPENDENT_SEQUENTIAL_STIEFEL_SPHERE_INTEGRATION_EXACT_OK 40_CASES')

# Two mathematically independent evaluations of the sixth-moment endpoints.
Kfac=15*n**2/((n-2)*(n-1)*(n+2)*(n+4))
for d in range(3,81):
    for k in range(1,d+1):
        x=[sp.Rational(1,k)]*k
        e=[sp.Integer(1)]+[sp.Integer(0)]*(k-1)
        def F(p):return d*d+3*d-2-6*(d+2)*sum(t**2 for t in p)+16*sum(t**3 for t in p)
        lower=d*d-3*d+2
        upper=d*d+3*d-2-sp.Rational(6*(d+2),k)+sp.Rational(16,k*k)
        assert F(e)==lower and F(x)==upper
        assert upper>=lower
        if k==d: assert sp.factor((Kfac*upper).subs(n,d)) == 15
print('SHARP_RANK_ONE_AND_EQUAL_SINGULAR_ENDPOINTS_EXACT_OK n=3..80')

rnd=random.Random(1138)
for d in range(3,18):
    for k in range(2,d+1):
        for t in range(8):
            xx=[sp.Rational(rnd.randrange(0,12),1) for _ in range(k)]
            if not any(xx):xx[0]=sp.Integer(1)
            z=sum(xx); xx=[a/z for a in xx]
            p2=sum(y*y for y in xx);p3=sum(y*y*y for y in xx)
            base=d*d+3*d-2 -6*(d+2)*p2+16*p3
            low=d*d-3*d+2
            high=d*d+3*d-2-sp.Rational(6*(d+2),k)+sp.Rational(16,k*k)
            deficit_min=sum(xx[i]*xx[j]*(12*d-8-16*(xx[i]+xx[j])) for i,j in combinations(range(k),2))
            deficit_max=sum((xx[i]-xx[j])**2*(6*(d+2)-sp.Rational(16,k)-16*(xx[i]+xx[j])) for i,j in combinations(range(k),2))/k
            assert sp.simplify(base-low-deficit_min)==0
            assert sp.simplify(high-base-deficit_max)==0
            assert deficit_min>=0 and deficit_max>=0
print('BOTH_EXACT_NONNEGATIVE_SPECTRAL_DEFICITS_OK 1080_CASES')
print('ALL_ORTHOGONAL_SIXTH_MOMENT_CERTIFICATES_PASSED')
