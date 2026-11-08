#!/usr/bin/env python3
"""Independent exact rational checks for the star coalescence transform.

Uses finite-state Markov first-step linear algebra, not the product recursion's
state elimination. The continuous-time limit proof is analytical.
"""
from fractions import Fraction as Q


def solve(A, v):
    n = len(v)
    M = [[Q(x) for x in row] + [Q(v[i])] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col]), None)
        assert pivot is not None
        M[col], M[pivot] = M[pivot], M[col]
        z = M[col][col]
        M[col] = [t/z for t in M[col]]
        for r in range(n):
            if r != col:
                z = M[r][col]
                if z:
                    M[r] = [a-z*b for a, b in zip(M[r], M[col])]
    return [M[i][-1] for i in range(n)]


def generator(b):
    states = [(h,k) for h in (0,1) for k in range(b+1) if h+k >= 2]
    d = {s:i for i,s in enumerate(states)}
    G = [[Q(0) for _ in states] for _ in states]
    exit_rates = [Q(0) for _ in states]
    for i,(h,k) in enumerate(states):
        moves = []
        if h:
            if k:
                moves.append(((0,k),Q(k,b)))
            if k<b:
                moves.append(((0,k+1),Q(b-k,b)))
        if k:
            moves.append(((1,k-1),Q(k)))
        for tgt,r in moves:
            if tgt in d:
                G[i][d[tgt]] += r
            else:
                exit_rates[i] += r
        G[i][i] -= h+k
    return states,d,G,exit_rates


def product(b,s):
    f=Q((b+1))*Q(s+2)/(b*(s+2)**2-2*(b-1))
    for j in range(2,b+1):
        f *= Q(j*(j+1+s)*((b+1)*j+b*s), (j+s)*(b*(j+1+s)**2-(b-j)*(j+1)))
    return f


def test():
    count = 0
    for b in range(1,9):
        states,d,G,r=generator(b)
        for s in [Q(0),Q(1,3),Q(1,2),Q(1),Q(2)]:
            A=[[Q(s)*(i==j)-G[i][j] for j in range(len(states))]
               for i in range(len(states))]
            F=solve(A,r)
            assert F[d[(1,b)]]==product(b,s), (b,s,F[d[(1,b)]],product(b,s))
            count += 1
        A=[[-G[i][j] for j in range(len(states))] for i in range(len(states))]
        E=solve(A,[Q(1)]*len(states))
        harmonic=sum((Q(1,j) for j in range(1,b+1)),Q(0))
        assert E[d[(1,b)]] == Q(b,b+1)*harmonic+Q(b-1,b+1)
        count += 1
    print('VERIFY_OK',count,'exact generator/product/mean assertions')

if __name__=='__main__':
    test()
