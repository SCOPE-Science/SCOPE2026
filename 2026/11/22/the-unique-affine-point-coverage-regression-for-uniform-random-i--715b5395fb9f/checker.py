#!/usr/bin/env python3
"""Exact finite checks for edge/point-coverage regression in uniform interval graphs."""
from fractions import Fraction as Q
from itertools import product
from math import comb


def poly_multiply(p, q):
    out = {}
    for (a, b), x in p.items():
        for (c, d), y in q.items():
            out[a+c, b+d] = out.get((a+c, b+d), Q(0)) + x*y
    return out


def random_interval_moment(poly):
    # Density two on 0 < left=a < right=b < 1.
    return sum((x*Q(2, (a+1)*(a+b+2)) for (a, b), x in poly.items()), Q(0))


# If a random interval is [a,b], the chance to meet an independent interval is
# 1-a*a-(1-b)*(1-b) = 2*b-a*a-b*b.
contact = {(0, 1): Q(2), (2, 0): Q(-1), (0, 2): Q(-1)}
assert random_interval_moment(contact) == Q(2,3)
assert random_interval_moment(poly_multiply(contact,contact)) == Q(22,45)
assert random_interval_moment(poly_multiply(contact,contact)) - Q(2,3)**2 == Q(2,45)
checks = 3


def regression(n, k, t):
    c = 2*t*(1-t)
    s = 1-c
    q_nn = Q(2,3)*(t**4+(1-t)**4)/s**2
    return Q(comb(k,2)) + Q(2,3)*k*(n-k)+q_nn*comb(n-k,2)


def state_pair_prob(u,v):
    if u == 'C' and v == 'C':
        return Q(1)
    if (u == 'L' and v == 'R') or (u == 'R' and v == 'L'):
        return Q(0)
    return Q(2,3)


def enumeration(n,t):
    prob={'L':t*t,'C':2*t*(1-t),'R':(1-t)**2}
    mass=[Q(0)]*(n+1)
    edge=[Q(0)]*(n+1)
    EK=EE=EKE=Q(0)
    for states in product('LCR',repeat=n):
        w=Q(1)
        for u in states: w*=prob[u]
        k=states.count('C')
        e=sum((state_pair_prob(states[i],states[j]) for i in range(n) for j in range(i+1,n)), Q(0))
        mass[k]+=w
        edge[k]+=w*e
        EK+=w*k
        EE+=w*e
        EKE+=w*k*e
    return mass,edge,EK,EE,EKE

for t in [Q(1,5),Q(1,4),Q(2,5),Q(1,2),Q(3,4)]:
    c=2*t*(1-t)
    s=1-c
    assert Q(2,3)*(t**4+(1-t)**4)/s**2 == Q(2,3)-c*c/(3*s*s)
    checks += 1
    for n in range(2,7):
        mass, edge, EK, EE, EKE = enumeration(n,t)
        assert sum(mass)==1
        assert EK==n*c
        assert EE==Q(n*(n-1),3)
        assert EKE-EK*EE == Q(n*(n-1),3)*c*c
        checks += 4
        for k in range(n+1):
            assert mass[k] == comb(n,k)*c**k*s**(n-k)
            assert edge[k] == mass[k]*regression(n,k,t)
            checks += 2
        for k in range(n-1):
            dd=regression(n,k+2,t)-2*regression(n,k+1,t)+regression(n,k,t)
            assert dd== (2*t-1)**2/(3*s*s)
            checks += 1
        if t == Q(1,2):
            for k in range(n+1):
                assert regression(n,k,t) == Q(n*(n-1),6)+Q((n-1)*k,3)
                checks += 1
        expected_var_E = Q(n*(n-1)*(2*n+1),45)
        expected_var_K = n*c*s
        expected_cov = Q(n*(n-1),3)*c*c
        rho_sq=expected_cov**2/(expected_var_E*expected_var_K)
        assert rho_sq==Q(5*(n-1),2*n+1)*c**3/s
        checks +=1

for n in range(2,41):
    rsq=Q(5*(n-1),4*(2*n+1))
    assert Q(0)<rsq<Q(5,8)
    checks += 1
print('PASS', checks, 'independent exact-rational assertions')
