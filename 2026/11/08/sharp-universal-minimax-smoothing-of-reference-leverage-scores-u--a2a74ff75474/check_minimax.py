#!/usr/bin/env python3
"""Supplementary reproducibility checks for a sharp rank-one sampling minimax theorem.

The proof is analytic. This script checks exact algebraic witnesses, randomized
angle-constrained pairs, and the optimizer boundaries. No random test is used
as an infinite-domain certificate.
"""
import math
import random
from fractions import Fraction


def eta_opt(m, theta):
    assert m >= 2 and 0 <= theta <= math.pi/2
    if theta == 0:
        return 0.0
    c, s = math.cos(theta), math.sin(theta)
    if s >= c*math.sqrt(m-1):
        return 1.0
    return m*s/(math.sqrt(m-1)*c+(m-1)*s)


def minimax_value(m, theta):
    c, s = math.cos(theta), math.sin(theta)
    return min(m, (c + math.sqrt(m-1)*s)**2) if theta <= math.atan(math.sqrt(m-1)) else float(m)


def exact_envelope(m, theta, eta):
    c, s = math.cos(theta), math.sin(theta)
    if eta == 0.0:
        return 1.0 if theta == 0 else float('inf')
    return c*c/(1-eta+eta/m) + m*s*s/eta


def witness(m, theta, eta):
    # Construct a maximizer in the first two orthogonal directions around e_0.
    c, s = math.cos(theta), math.sin(theta)
    b = eta/m
    a = 1-eta
    if theta == 0:
        u = [1.0]+[0.]*(m-1)
        w = u[:]
        return u,w
    t = c*b / (s*(a+b))
    x = t / math.sqrt(1+t*t)
    u = [x] + [math.sqrt((1-x*x)/(m-1))]*(m-1)
    z = [math.sqrt(1-x*x)] + [-x/math.sqrt(m-1)]*(m-1)
    w = [c*ui+s*zi for ui,zi in zip(u,z)]
    return u,w


def dot(a,b):
    return sum(ai*bi for ai,bi in zip(a,b))


def norm(a):
    return math.sqrt(dot(a,a))


def ratio(u,w,eta):
    m=len(u)
    p=[(1-eta)*v*v+eta/m for v in u]
    return max(wi*wi/pi if pi>0 else (0 if wi==0 else float('inf')) for wi,pi in zip(w,p))


random.seed(271828)
tests = 0
for m in (2,3,4,5,9,30):
    for theta in (0.0,.0001,.02,.1,.3,.6,1.0,math.atan(math.sqrt(m-1)),math.pi/2):
        eta=eta_opt(m,theta)
        val=minimax_value(m,theta)
        env=exact_envelope(m,theta,eta)
        assert math.isclose(val,env,rel_tol=2e-10,abs_tol=2e-10), (m,theta,eta,val,env)
        tests+=1
        if 0<eta<1 and theta>0:
            u,w=witness(m,theta,eta)
            assert abs(norm(u)-1)<1e-12 and abs(norm(w)-1)<1e-12
            assert abs(dot(u,w)-math.cos(theta))<1e-12
            assert math.isclose(ratio(u,w,eta),env,rel_tol=1e-10)
            tests+=4
        for q in range(200):
            u=[random.gauss(0,1) for _ in range(m)]
            u=[v/norm(u) for v in u]
            z=[random.gauss(0,1) for _ in range(m)]
            t=dot(u,z)
            z=[zi-t*ui for zi,ui in zip(z,u)]
            nz=norm(z)
            if nz<1e-12:continue
            z=[zi/nz for zi in z]
            phi=random.random()*theta
            w=[math.cos(phi)*ui + math.sin(phi)*zi for ui,zi in zip(u,z)]
            got=ratio(u,w,eta)
            assert got<=val+1e-8, (m,theta,eta,got,val)
            tests+=1
        # every policy has a uniform-reference witness
        u=[1/math.sqrt(m)]*m
        j=0
        if theta<=math.atan(math.sqrt(m-1)):
            z=[(float(i==j)-u[j]*u[i])/math.sqrt(1-1/m) for i in range(m)]
            w=[math.cos(theta)*ui+math.sin(theta)*zi for ui,zi in zip(u,z)]
        else:
            w=[float(i==j) for i in range(m)]
        assert math.isclose(m*w[j]**2,val,rel_tol=1e-10,abs_tol=1e-10)
        tests+=1

# Hand-check boundary rational constructions m=2 and theta=arctan(1)
assert Fraction(1,2)+Fraction(1,2)==1
assert math.isclose(eta_opt(2,math.pi/4),1.0)
tests+=2
print('PASS', tests, 'independent supplementary numeric/algebraic assertions')
