#!/usr/bin/env python3
"""Exact-rational verification of two-patch synchronous-disaster occupancy identities.
Uses only Python's standard library. The proof of continuum-wide monotonicity
is analytical; the finite checks are independent diagnostics.
"""
from fractions import Fraction as F
from itertools import product


def solve_linear(A,b):
    n=len(b)
    aug=[[F(z) for z in A[i]]+[F(b[i])] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if aug[j][k])
        aug[k],aug[j]=aug[j],aug[k]
        v=aug[k][k]
        aug[k]=[x/v for x in aug[k]]
        for i in range(n):
            if i!=k:
                t=aug[i][k]
                if t:aug[i]=[x-t*y for x,y in zip(aug[i],aug[k])]
    return [a[-1] for a in aug]


def generator(lam, mu, c, kap, theta):
    # States 00, 10, 01, 11. Rates are per transition.
    Q=[[F(0) for _ in range(4)] for _ in range(4)]
    edges=[(0,1,lam),(0,2,lam),
           (1,0,mu+kap),(2,0,mu+kap),
           (1,3,lam+c),(2,3,lam+c),
           (3,1,mu+kap*(1-theta)),(3,2,mu+kap*(1-theta)),
           (3,0,kap*theta)]
    for i,j,v in edges:
        Q[i][j]+=v
    for i in range(4):Q[i][i]=-sum(Q[i])
    return Q


def stationary(Q):
    n=len(Q)
    A=[[Q[j][i] for j in range(n)] for i in range(n)]
    A[-1]=[F(1)]*n
    b=[F(0)]*(n-1)+[F(1)]
    return solve_linear(A,b)


def explicit(lam,mu,c,kap,theta):
    h=mu+kap
    den=2*((h+lam)**2+lam*c)+kap*theta*(c-h-lam)
    p0=(2*h**2+kap*theta*(c-h+lam))/den
    p1=2*lam*(2*h-kap*theta)/den
    p2=2*lam*(c+lam)/den
    return (p0,p1,p2,den)


def main():
    tests=0
    rates=[F(1,4),F(1,2),F(1),F(2),F(5)]
    thetas=[F(0),F(1,5),F(1,2),F(4,5),F(1)]
    for lam,mu,c,kap in product(rates,repeat=4):
        for theta in thetas:
            pi=stationary(generator(lam,mu,c,kap,theta))
            p0,p1,p2,D=explicit(lam,mu,c,kap,theta)
            assert D>0
            assert pi[0]==p0 and pi[1]+pi[2]==p1 and pi[3]==p2
            assert sum(pi)==1 and all(0<x<1 for x in pi)
            tests+=1
        # Cross-check analytical differences using exact rational arithmetic.
        r0=explicit(lam,mu,c,kap,F(0))
        r1=explicit(lam,mu,c,kap,F(1))
        assert (r1[0]-r0[0]>0)
        assert (r1[1]+2*r1[2]-r0[1]-2*r0[2]<0)
        delta=c-mu-kap-lam
        assert (r1[2]-r0[2]>0)==(delta<0) if delta else r1[2]==r0[2]
        tests+=3
    print('PASS',tests,'exact rational assertions; 4-state independent generator.')

if __name__=='__main__':main()
