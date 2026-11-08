#!/usr/bin/env python3
"""Exact state-space checks for K-Fibonacci companion permutations modulo powers of two."""
from collections import Counter
from math import gcd


def expected(r):
    if r == 1:
        return {1: 2, 2: 1}
    out = {1: 2, 2: 1, 4: 3 if r == 2 else 7}
    for j in range(3, r):
        out[2**j] = 3*2**(j-1)
    if r >= 3:
        out[2**r] = 2**(r-1)
    return out


def count_cycles(k, r):
    n = 1 << r
    marked = bytearray(n*n)
    counts = Counter()
    for x in range(n):
        for y in range(n):
            u = x*n+y
            if marked[u]:
                continue
            a, b = x, y
            length = 0
            while not marked[a*n+b]:
                marked[a*n+b] = 1
                length += 1
                a, b = (k*a+b) % n, a
            assert (a,b)==(x,y), (k,r,x,y,a,b)
            counts[length] += 1
    assert sum(L*C for L,C in counts.items()) == n*n
    return dict(sorted(counts.items()))


def matmul(X,Y):
    return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
            [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]


def vp(n):
    if n==0:
        return 1000
    n=abs(n)
    return (n & -n).bit_length()-1


def valuations(A):
    entries = [z for row in A for z in row]
    a = min(vp(z) for z in entries)
    d = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d != 0
    return a, vp(d)-a


def smith_checks(k,max_j):
    A = [[k,1],[1,0]]
    P = [[1,0],[0,1]]
    for j in range(max_j+1):
        if j==0: P=A
        else: P=matmul(P,P)
        E=[[P[a][b] - int(a==b) for b in range(2)] for a in range(2)]
        observed=valuations(E)
        anticipated = (0,1) if j==0 else ((1,1) if j==1 else (j,j+1))
        assert observed==anticipated,(k,j,observed,anticipated)


def main():
    for k in (2,6,10,14,18,22):
        smith_checks(k,8)
        for r in range(1,8):
            actual = count_cycles(k,r)
            assert actual == expected(r), (k,r,actual,expected(r))
        print(f'K={k}: SNF valuations j=0..8 and exhaustive state-space census r=1..7 PASS')
    print('Total: 54 symbolic-integer matrix exponent tests; 42 complete modular state-space checks; all PASS.')
    for r in range(1,8):
        print('r=%d: %s, total_cycles=%d' % (r, expected(r), sum(expected(r).values())))

if __name__ == '__main__':
    main()
