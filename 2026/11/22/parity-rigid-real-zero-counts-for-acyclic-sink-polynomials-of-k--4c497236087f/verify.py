#!/usr/bin/env python3
"""Exact finite tests for acyclic-sink polynomials of complete bipartite graphs."""
from collections import Counter
from math import comb

def predicted(n):
    # Coefficients of 2(z+2)^n-(z+1)^n with corrections at degrees 0,1,2.
    a = [2 * comb(n, j) * (2 ** (n-j)) - comb(n, j) for j in range(n + 1)]
    a[0] -= 2**(n+1) - 1
    a[1] += 2**(n+1) - 2
    a[2] += 1
    return a

def brute(n):
    # Each of n vertices in the larger shore has 2 incoming/outgoing bits.
    # Kahn source deletion detects a directed cycle independently of type classification.
    counts = Counter()
    total = n + 2
    for encoding in range(4**n):
        adjacency = [[] for _ in range(total)]
        indegree = [0]*total
        code = encoding
        for j in range(n):
            mask = code % 4
            code //= 4
            for a in (0, 1):
                u, v = (a, j+2) if (mask >> a) & 1 else (j+2, a)
                adjacency[u].append(v)
                indegree[v] += 1
        sinks = sum(len(row) == 0 for row in adjacency)
        work = [i for i, d in enumerate(indegree) if d == 0]
        visited = 0
        while work:
            u = work.pop()
            visited += 1
            for v in adjacency[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    work.append(v)
        if visited == total:
            counts[sinks] += 1
    return [counts[j] for j in range(n+1)]

def Qcoeffs(n):
    # S_n(-x-2), coefficient order ascending, from the symbolic formula.
    const = [0]*(n+1)
    for j in range(n+1):
        const[j] = ((-1)**n) * ((2 if j==n else 0) - comb(n,j))
    const[0] += 9-3*2**(n+1)
    const[1] += 6-2**(n+1)
    const[2] += 1
    return const

def verify():
    for n in range(2,9):
        p, b = predicted(n), brute(n)
        assert p == b, (n,p,b)
        assert sum(p) == 2*(3**n) - 2**n
        assert p[0] == 0 and all(v > 0 for v in p[1:])
    print('INDEPENDENT_FULL_ORIENTATION_CENSUS_PASS n=2..8')
    for n in range(2,201):
        q=Qcoeffs(n)
        if n%2==0 and n>=4:
            assert q[-1]>0 and all(v<0 for v in q[:-1]),(n,q)
        if n%2==1 and n>=5:
            assert q[-1]<0 and all(v>0 for v in q[2:-1]),(n,q)
            assert q[1]<0 and q[0]<0
            value = sum(q[j]*3**j for j in range(n+1))
            assert value == 4**n-2*3**n-6*2**(n+1)+36 > 0
    assert predicted(2)==[0,12,2]
    assert predicted(3)==[0,35,10,1]
    print('EXACT_SIGN_PATTERN_AND_WITNESS_CHECK_PASS n=2..200')
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
