#!/usr/bin/env python3
"""Exact finite checks of a two-tail-lag unitary correlation theorem.
Uses Python 3 standard library; finite checks supplement the written proof.
"""
from fractions import Fraction as F
from itertools import product


def polynomial_defect(a,b,c,d):
    """Quartic identity with nonnegative real amplitudes a,b,c,d."""
    p0,p1,p2,p3=a*a,b*b,c*c,d*d
    A,B=p0+p3,p1+p2
    s=A+B
    q=(a*c+b*d)**2+p0*p3
    squares=(a*b-c*d)**2+(p0-p3)**2/F(4)+F(3,16)*(A-B)**2
    return s*(7*A+3*B)/16-q-squares


def walsh(N):
    assert N>=4
    W=[[F(0) for _ in range(N)] for _ in range(N)]
    for j,(a,b) in enumerate(((1,1),(1,-1),(-1,1),(-1,-1))):
        for i,x in zip((0,1,N-2,N-1),(1,a,b,a*b)):
            W[i][j]=F(x,2)
    for j in range(4,N):
        W[j-2][j]=F(1)
    return W


def dot(u,v):
    return sum((a*b for a,b in zip(u,v)),F(0))


def energy(W,k):
    N=len(W)
    total=F(0)
    for j in range(N):
        gamma=sum((W[i][j]*W[i+k][j] for i in range(N-k)),F(0))
        total+=gamma*gamma
    return total


def main():
    # Degree in each variable is at most four: exact vanishing on five
    # nodes per variable proves the polynomial identity, not merely a sample.
    for aa,bb,cc,dd in product(range(5),repeat=4):
        assert polynomial_defect(F(aa),F(bb),F(cc),F(dd))==0
    checks=5**4
    for N in range(4,25):
        W=walsh(N)
        for j in range(N):
            for k in range(N):
                assert dot((W[i][j] for i in range(N)),
                           (W[i][k] for i in range(N)))==int(j==k)
                checks+=1
        assert energy(W,N-2)==1
        assert energy(W,N-1)==F(1,4)
        assert energy(W,N-2)+energy(W,N-1)==F(5,4)
        assert F(5,N)<=F(5,4)
        checks+=4
    print('PASS: exact quartic polynomial identity and Walsh unitarity/energies')
    print('Checks:',checks)


if __name__=='__main__':
    main()
