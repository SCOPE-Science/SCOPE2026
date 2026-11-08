#!/usr/bin/env python3
"""Exact standalone checks for the group-coupon Hessian spectrum.
Requires only Python's standard library; calculations are finite and do not
substitute for the all-parameter sign proof.
"""
from itertools import combinations
from fractions import Fraction
from math import comb

checks = 0

def insist(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def eig(n, s, j):
    m = c(n, s)
    return 2 * sum(((-1)**(n-b+1)) * c(b-j, s-j) * c(n-s-j, b-s)
                    / (1-Fraction(c(b, s), m))**3
                    for b in range(s, n))


def difference_eig(n, s, j):
    m = c(n, s)
    N = n-s-j
    def g(k):
        return Fraction(c(s+k-j, s-j), 1) / (1-Fraction(c(s+k, s),m))**3
    return 2 * (-1)**(j+1) * sum((-1)**(N-k) * c(N,k) * g(k)
                                    for k in range(N+1))


def direct_hv(n, s, v, subs):
    m=c(n,s)
    vv=[Fraction(0) for _ in subs]
    ix={S:i for i,S in enumerate(subs)}
    for b in range(s,n):
        coeff=2* (-1)**(n-b+1) / (1-Fraction(c(b,s),m))**3
        for B in combinations(range(n),b):
            B=set(B)
            isub=[ix[S] for S in subs if set(S)<=B]
            val=sum((v[i] for i in isub), Fraction(0))
            if val:
                for i in isub:
                    vv[i]+=coeff*val
    return vv


def eq(n,s,j,subs):
    return [Fraction(__import__('math').prod((int(2*r in S)-int(2*r+1 in S)
                 for r in range(j))),1) for S in subs]

for n in range(3,9):
    for s in range(1,n):
        subs=list(combinations(range(n),s))
        d=min(s,n-s)
        m=c(n,s)
        for j in range(1,d+1):
            lam=eig(n,s,j)
            insist(lam==difference_eig(n,s,j),f'finite-difference identity {(n,s,j)}')
            insist(lam!=0 and ((lam>0)==(j%2==1)),f'alternating sign {(n,s,j)}')
            v=eq(n,s,j,subs)
            insist(sum(v)==0 and any(v),f'nonzero tangent vector {(n,s,j)}')
            hv=direct_hv(n,s,v,subs)
            for i in range(len(v)):
                insist(hv[i]==lam*v[i],f'incidence eigenrelation {(n,s,j,i)}')
        insist(sum(c(n,j)-c(n,j-1) for j in range(d+1))==m,
               f'Johnson multiplicity partition {(n,s)}')

# Test sign of actual finite nonuniform expected waiting time on two independent
# harmonic slice directions (the two curvatures are opposite).
def expectation(n,s,probs,subs):
    val=Fraction(0)
    for b in range(n):
        for B in combinations(range(n),b):
            B=set(B)
            r=sum((probs[i] for i,S in enumerate(subs) if set(S)<=B),Fraction(0))
            val+= (-1)**(n-b+1) / (1-r)
    return val

for n,s in [(4,2),(5,2),(6,3),(7,4)]:
    subs=list(combinations(range(n),s)); m=c(n,s)
    unif=[Fraction(1,m)]*m
    base=expectation(n,s,unif,subs)
    for j in (1,2):
        v=eq(n,s,j,subs)
        eps=Fraction(1,100*m)
        plus=[p+eps*w for p,w in zip(unif,v)]
        minus=[p-eps*w for p,w in zip(unif,v)]
        insist(min(plus)>0 and min(minus)>0, f'interior p {(n,s,j)}')
        q=expectation(n,s,plus,subs)+expectation(n,s,minus,subs)-2*base
        insist((q>0)==(j==1),f'actual finite diff sign {(n,s,j)}')

print('PASS:',checks,'independent exact-rational checks')
