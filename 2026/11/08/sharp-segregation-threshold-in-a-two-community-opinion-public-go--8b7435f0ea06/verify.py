#!/usr/bin/env python3
"""Exact-rational exhaustive tests of a two-community public-goods equilibrium law.

Only Python standard library modules are needed.
"""
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache

def inverse(A):
    n = len(A)
    B = [[Q(v) for v in A[i]] + [Q(i == j) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if B[i][k] != 0)
        B[k], B[p] = B[p], B[k]
        scale = B[k][k]
        B[k] = [v / scale for v in B[k]]
        for i in range(n):
            if i != k:
                z = B[i][k]
                if z:
                    B[i] = [B[i][j] - z * B[k][j] for j in range(2*n)]
    return [line[n:] for line in B]

def influence(m, a):
    n = 2*m
    return [[(a / (m-1) if i//m == j//m else (1-a) / m)
             if i != j else Q(0) for j in range(n)] for i in range(n)]

@lru_cache(maxsize=None)
def solve_data(m, a, c):
    n = 2*m
    W = influence(m, a)
    B = inverse([[Q(i == j)-c*W[i][j] for j in range(n)]
                 for i in range(n)])
    return W, B

def enumerated_fixed_points(m, a, alpha, beta, lam, multiplier):
    n = 2*m
    c = beta / (beta+lam)
    d = lam / (beta+lam)
    K = beta*lam/(beta+lam)
    W, B = solve_data(m, a, c)
    stationary = set()
    for x in product((0, 1), repeat=n):
        y = [d*sum(B[i][j]*x[j] for j in range(n)) for i in range(n)]
        z = [sum(W[i][j]*y[j] for j in range(n)) for i in range(n)]
        benefit = [alpha*(multiplier / n-1)+K*(z[i]-Q(1,2))
                   for i in range(n)]
        if all((x[i] == 1) == (benefit[i] > 0) for i in range(n)):
            stationary.add(x)
    return stationary

def formula(m, a, alpha, beta, lam, multiplier):
    n=2*m
    c=beta/(beta+lam)
    d=1-c
    K=beta*lam/(beta+lam)
    delta=alpha*(1-multiplier/n)/K
    states={tuple([0]*n)}
    if delta < Q(1,2):
        states.add(tuple([1]*n))
    h=2*a-1
    if h*d>2*delta*(1-c*h):
        states.add(tuple([1]*m+[0]*m))
        states.add(tuple([0]*m+[1]*m))
    return states

def main():
    tests=0
    profiles=0
    for m in (2,3,4):
        n=2*m
        for a in (Q(0),Q(1,4),Q(1,2),Q(3,4),
                  Q(4,5),Q(5,6),Q(9,10),Q(1)):
            for alpha in (Q(1,20),Q(1,9),Q(1,10),Q(1,5)):
                for split in (Q(1,3),Q(1,2),Q(2,3)):
                    beta=(1-alpha)*split
                    lam=(1-alpha)*(1-split)
                    for r in (Q(2),Q(n,2),Q(n-1)):
                        if r<=1 or r>=n:
                            continue
                        expected=formula(m,a,alpha,beta,lam,r)
                        actual=enumerated_fixed_points(
                            m,a,alpha,beta,lam,r)
                        assert actual == expected, (
                            m,a,alpha,beta,lam,r,actual,expected)
                        tests += 1
                        profiles += 2**n
    # Equality at the homophily threshold: tie resolves to defection.
    assert len(enumerated_fixed_points(
        2,Q(5,6),Q(1,9),Q(4,9),Q(4,9),Q(2)))==2
    assert len(enumerated_fixed_points(
        2,Q(9,10),Q(1,9),Q(4,9),Q(4,9),Q(2)))==4
    # Equality at the cooperation threshold excludes cooperation.
    assert len(enumerated_fixed_points(
        2,Q(1),Q(1,5),Q(2,5),Q(2,5),Q(2)))==1
    print(f"PASS: {tests} exact parameter/network cases, "
          f"{profiles} exhaustive binary-action profiles; "
          "three sharp-boundary cases.")

if __name__ == "__main__":
    main()
