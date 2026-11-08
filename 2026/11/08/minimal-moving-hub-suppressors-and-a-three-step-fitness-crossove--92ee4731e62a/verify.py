#!/usr/bin/env python3
"""Exact rational-and-polynomial verification of the moving-hub P3 theorem.

Standard-library only. In addition to direct chain solving, a proved degree bound
makes the complete finite interpolation test an infinite polynomial identity proof.
"""
from fractions import Fraction as F
from math import comb

CERT = {1: {'A': [57, 100, 74, 16], 'B': [16, 58, 99, 58, 16], 'S': [-25, -50, -25]}, 2: {'A': [3720, 33454, 109187, 167472, 144766, 69876, 17600, 1792], 'B': [1792, 15808, 57788, 120432, 156227, 120432, 57788, 15808, 1792], 'S': [-136, -3902, -18879, -30340, -18879, -3902, -136]}, 3: {'A': [269088, 3785968, 23028676, 78687618, 166237563, 228306192, 211408302, 132678516, 55479000, 14763360, 2259712, 151552], 'B': [151552, 2108160, 12924288, 46340680, 109366512, 180729408, 213814347, 180729408, 109366512, 46340680, 12924288, 2108160, 151552], 'S': [34016, 346832, 1219836, 1323222, -1556931, -3962976, -1556931, 1323222, 1219836, 346832, 34016]}, 4: {'A': [18927744, 364559296, 3171001248, 16450923320, 56647510380, 136569244450, 237662529635, 304372892016, 290324831326, 206776451988, 109238709944, 42099963088, 11480909376, 2097078656, 230108160, 11468800], 'B': [11468800, 218639360, 1897367040, 9948101632, 35322862704, 90366770560, 173057191808, 253836883968, 288198537683, 253836883968, 173057191808, 90366770560, 35322862704, 9948101632, 1897367040, 218639360, 11468800], 'S': [4009856, 69270336, 528155488, 2335241928, 6659634020, 13048359694, 18650229405, 20776523048, 18650229405, 13048359694, 6659634020, 2335241928, 528155488, 69270336, 4009856]}}


def poly_eval(c, r):
    v = 0
    for x in reversed(c):
        v = v*r + x
    return v


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c


def scaled(a,c):
    return [c*x for x in a]


def matrix_mul(A,B):
    n=len(A)
    R=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]: continue
            for j in range(n):
                if B[k][j]: R[i][j] += A[i][k]*B[k][j]
    return R


def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def power(A,t):
    R=identity(len(A))
    for _ in range(t): R=matrix_mul(R,A)
    return R


def transition(edges,r):
    # A state is a three-bit mask; one parent is chosen proportional to fitness,
    # and one of that parent's neighbors is replaced uniformly.
    adj=[[] for _ in range(3)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    P=[[F(0) for _ in range(8)] for _ in range(8)]
    for mask in range(8):
        m=mask.bit_count()
        d=r*m+3-m
        for u in range(3):
            w=r if mask>>u&1 else 1
            for v in adj[u]:
                nxt=mask|(1<<v) if mask>>u&1 else mask & ~(1<<v)
                P[mask][nxt]+=F(w,d*len(adj[u]))
    return P


def solve(M,b):
    # Gauss-Jordan in exact rationals, with row pivoting.
    n=len(b)
    E=[list(M[i])+[b[i]] for i in range(n)]
    for i in range(n):
        pivot=next(k for k in range(i,n) if E[k][i])
        E[i],E[pivot]=E[pivot],E[i]
        z=E[i][i]
        for j in range(i,n+1): E[i][j]/=z
        for k in range(n):
            if k==i: continue
            z=E[k][i]
            if not z: continue
            for j in range(i,n+1): E[k][j]-=z*E[i][j]
    return [E[i][n] for i in range(n)]


def fixation(r,t):
    P=transition([(0,1),(0,2)],r)
    Q=transition([(0,1),(1,2)],r)
    W=matrix_mul(power(P,t),power(Q,t))
    states=range(1,7)
    M=[[F(i==j)-W[i+1][j+1] for j in range(6)] for i in range(6)]
    b=[W[i+1][7] for i in range(6)]
    x=solve(M,b)
    return (x[0]+x[1]+x[3])/3


def static_fixation(r):
    P=transition([(0,1),(0,2)],r)
    M=[[F(i==j)-P[i+1][j+1] for j in range(6)] for i in range(6)]
    x=solve(M,[P[i+1][7] for i in range(6)])
    return (x[0]+x[1]+x[3])/3


def verify():
    # Polynomial exactness of the difference certificates:
    # (r^2+r+1)*A - (r+2)*B = (r-1)*S.
    for t in range(1,5):
        A,B,S=(CERT[t][k] for k in ('A','B','S'))
        assert len(A)==4*t and len(B)==4*t+1
        lhs=add(mul([1,1,1],A),scaled(mul([2,1],B),-1))
        rhs=mul([-1,1],S)
        assert lhs[:len(rhs)]==rhs and all(v==0 for v in lhs[len(rhs):]), ('difference polynomial',t)
        if t in (1,2): assert all(v<0 for v in S)
        if t==4: assert all(v>0 for v in S)

    # The tau=3 palindromic sign polynomial is r^5*H(r+1/r-2).
    # H has a negative constant, strictly positive other coefficients.
    h=[-1229026,21114193,17279678,5185052,686992,34016]
    reconstruction=[0]*11
    for k,c in enumerate(h):
        for j in range(2*k+1):
            reconstruction[5-k+j]+=c*comb(2*k,j)*(-1)**(2*k-j)
    assert reconstruction==CERT[3]['S']
    assert h[0]<0 and all(v>0 for v in h[1:])

    # Degree certificate: each transient matrix entry after 2*t steps has a
    # common denominator ((r+2)*(2*r+1))^(2*t) and numerator degree <= 4*t.
    # A six-by-six Cramer determinant has degree <= 24*t. Both candidate
    # numerator and denominator have degree <= 4*t+1. Thus the cross-
    # multiplied difference has degree <= 28*t+1, and equality at 28*t+2
    # distinct positive points proves the rational-function identity for ALL
    # positive real r, not merely those sampled.
    counts={}
    for t in range(1,5):
        A,B=CERT[t]['A'],CERT[t]['B']
        samples=28*t+2
        for r in range(1,samples+1):
            actual=fixation(r,t)
            candidate=F(r*r*poly_eval(A,r),(r+2)*poly_eval(B,r))
            assert actual==candidate, ('interpolation',t,r,actual,candidate)
        counts[t]=samples

    # Static P3 is a strict amplifier; the separate derivation uses a
    # Cramer degree bound <= 12 for actual numerator/denominator and degree
    # <= 5 for the candidate, hence 18 points suffice.
    for r in range(1,19):
        assert static_fixation(r)==F(r*r*(2*r+3),(r+2)*(2*r*r+r+2))
    print('PASS: difference polynomials, tau=3 unique crossover, and')
    print('      exact interpolation certificate for each tau:',counts)
    print('PASS: static P3 formula (18-point degree certificate)')
    print('PASS: all sign factors apply for EVERY real fitness r>0.')

if __name__=='__main__':
    verify()
