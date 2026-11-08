#!/usr/bin/env python3
"""Independent finite exact checks of parking-polytope vertex covariance formulas.

Run: python3 check_parking_covariance.py
No external packages required. The finite tests are not proofs of the limit.
"""
from fractions import Fraction as F
from math import factorial, e
from itertools import permutations


def weights(n, a):
    js = range(0 if a > 1 else 1, n + 1)
    raw = {j: F(1, factorial(j)) for j in js}
    z = sum(raw.values())
    return {j: v / z for j, v in raw.items()}


def layer(n, a, b, j):
    return [F(1)] * j + [a + i * b for i in range(j, n)]


def covariance_formula(n, a, b):
    p = weights(n, a)
    d = {j: j * (a-1) + b * j * (j-1)/2 for j in p}
    full = n*a + b*n*(n-1)/2
    mean_d = sum(w*d[j] for j,w in p.items())
    mean_d2 = sum(w*d[j]*d[j] for j,w in p.items())
    parallel = (mean_d2-mean_d*mean_d)/n
    s2_full = n*a*a + a*b*n*(n-1) + b*b*n*(n-1)*(2*n-1)/6
    perpsum = F(0)
    for j,w in p.items():
        s = full-d[j]
        q = sum(z*z for z in layer(n,a,b,j))
        perpsum += w * (q-s*s/n)
    perp = perpsum/(n-1)
    return parallel, perp


def covariance_bruteforce(n,a,b):
    vs = set()
    for j in weights(n,a):
        vs.update(permutations(layer(n,a,b,j)))
    count=F(len(vs))
    mu = [sum(v[i] for v in vs)/count for i in range(n)]
    c = [[sum((v[i]-mu[i])*(v[k]-mu[k]) for v in vs)/count
          for k in range(n)] for i in range(n)]
    u=[F(1)]*n
    pvec=[F(1),F(-1)]+[F(0)]*(n-2)
    lampar=sum(c[0])/1  # C1 has constant coordinates
    lamperp=sum(c[0][k]*pvec[k] for k in range(n))
    for i in range(n):
        assert sum(c[i])==lampar
        assert sum(c[i][k]*pvec[k] for k in range(n)) == lamperp*pvec[i]
    return lampar,lamperp,len(vs)

for n in range(2,7):
    for aa,bb in [(F(1),F(1)),(F(2),F(1)),(F(3),F(2))]:
        expected=covariance_formula(n,aa,bb)
        actual = covariance_bruteforce(n,aa,bb)
        assert tuple(expected)==tuple(actual[:2]),(n,aa,bb,expected,actual)
        assert expected[0]>0 and expected[1]>0
        print('exact',n,int(aa),int(bb),'vertices',actual[2],'eigenvalues',*[str(x) for x in expected])

from math import exp
V_boundary=e*(6*e-7)/(4*(e-1)**2)
for aa,bb,lim in [(1,1,V_boundary),(2,1,4.5),(3,2,4+8+6)]:
    # c^2+2bc+(3/2)b^2; for a=3,b=2 =>4+8+6=18.
    for n in (100,500,2000):
        par,perp=covariance_formula(n,F(aa),F(bb))
        obs1=n*float(par)
        obs2=float(perp)/(n*n)
        obs3=(float(perp)/float(par))/(n**3)
        target=(bb*bb)/(12*lim)
        if n == 2000:
            assert abs(obs1-lim)<1e-6,(aa,bb,obs1,lim)
            assert abs(obs2-bb*bb/12)<0.0002
            assert abs(obs3-target)<0.0002
        print('asymptotic',aa,bb,n,'n_parallel',obs1,'perp/n2',obs2,'condition/n3',obs3)
print('PARKING_VERTEX_SPECTRUM_CHECKS_PASSED')
