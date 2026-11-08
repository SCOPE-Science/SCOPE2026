"""Exact, standard-library checks for leaf imbalance in root-doubling trees.

Usage: python verify.py
The proof of the infinite-time identities is analytical; finite generator
checks and Taylor coefficients are supplementary reproducibility tests.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial


def transitions(state):
    s, e, d = state
    assert s >= 3 and (s + e) % 2 == 0
    leaves = (s + e) // 2
    assert 0 <= leaves <= s - 1
    nonleaf = s - 1 - leaves
    return [((2*s+1, 2*e-1, d+1), 1),
            ((s+1, e-1, d), leaves),
            ((s+1, e+1, d), nonleaf)]


def generator(f, state):
    s = state[0]
    return sum(rate*(f(nxt)-f(state)) for nxt, rate in transitions(state))

checks = 0
for s in range(3, 20):
    for leaves in range(1, s):
        e = 2*leaves-s
        for d in range(4):
            st = (s,e,d)
            assert generator(lambda x:x[0],st) == 2*s
            assert generator(lambda x:x[1],st) == -2
            assert generator(lambda x:x[1]**2,st) == e**2-6*e+s
            assert generator(lambda x:x[2],st) == 1
            assert generator(lambda x:x[1]*x[2],st) == -2*d+2*e-1
            checks += 5
            for z in (Q(0),Q(1,2),Q(2,3),Q(1),Q(4,3)):
                assert generator(lambda x:z**x[2],st) == (z-1)*z**d
                assert generator(lambda x:x[1]*z**x[2],st) == (2*(z-1)*e-(1+z))*z**d
                checks+=2

# The k-fold transpose generator gives the exact kth derivative at t=0,
# with no sample paths or floating point approximation.
weights = {(3,1,0):1}
zs = [Q(0), Q(1,2), Q(2,3), Q(1), Q(4,3)]
H = {}
for z in zs: H[z] = [Q(1)]
g=[Q(1)]
for k in range(9):
    for z in zs:
        obs = sum(Q(w)*e*z**d for (s,e,d),w in weights.items())
        assert obs == H[z][k] * factorial(k), ("mixed",k,z,obs,H[z][k]*factorial(k))
        checks += 1
    sq = sum(Q(w)*e*e for (s,e,d),w in weights.items())
    assert sq == g[k]*factorial(k), ("square",k,sq,g[k]*factorial(k))
    checks+=1
    ed = sum(Q(w)*e*d for (s,e,d),w in weights.items())
    assert ed == (1 if k==1 else -6 if k==2 else 0)
    checks+=1
    if k == 8: break
    for z in zs:
        a=z-1
        Fk=a**k/Q(factorial(k))
        H[z].append((2*a*H[z][k]-(1+z)*Fk)/Q(k+1))
    e_coeff = Q(1) if k==0 else Q(-2) if k==1 else Q(0)
    g.append((g[k] + 3*Q(2**k,factorial(k)) - 6*e_coeff)/Q(k+1))
    new=defaultdict(int)
    for st,w in weights.items():
        s=st[0]
        new[st]-=w*s
        for dest,rate in transitions(st):
            if rate:new[dest]+=w*rate
    weights={st:w for st,w in new.items() if w}
print('PASS:',checks,'exact integer/rational generator and Taylor checks')
