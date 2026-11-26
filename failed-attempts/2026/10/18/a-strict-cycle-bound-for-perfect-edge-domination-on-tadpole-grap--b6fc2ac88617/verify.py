#!/usr/bin/env python3
"""Exact arithmetic reproduction of the tadpole perfect-edge-domination theorem.

Requires Python 3.9+ standard library only.  No external data are used.
"""
from itertools import product

W, Y, B = 0, 1, 2
STATES = ((W,Y),(Y,W),(Y,Y),(Y,B),(B,Y),(B,B))


def valid(color, neighbors):
    if color == W:
        return all(q == Y for q in neighbors)
    if color == Y:
        return sum(q != W for q in neighbors) == 1
    if color == B:
        return len(neighbors) >= 2 and all(q != W for q in neighbors)
    raise ValueError(color)


def mm(A, B):
    assert len(A[0]) == len(B)
    return [[sum(A[i][j] * B[j][k] for j in range(len(B)))
             for k in range(len(B[0]))] for i in range(len(A))]


def matpow(A, n):
    assert n >= 0
    ans = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
    while n:
        if n & 1:
            ans = mm(ans, A)
        A = mm(A, A)
        n >>= 1
    return ans


def add(A, B):
    return [[a+b for a, b in zip(row, oth)] for row, oth in zip(A, B)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


# State (a,b) -> (b,c) checks the degree-two vertex b.
M = [[int(b == c and valid(b, (a,d)))
      for (c,d) in STATES] for (a,b) in STATES]
assert M == [
    [0,0,1,1,0,0],
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,1,1],
    [0,1,0,0,0,0],
    [0,0,0,0,1,1],
]
assert matpow(M,5) == add(matpow(M,4),matpow(M,2))


def boundary(t):
    """H_t[terminal_pair][start_pair] sums valid colors of the tail.

    start_pair=(v0,v1), terminal_pair=(v_(c-1),v0).
    The vertex v0 has three neighbors (cycle, cycle, first tail).
    Each tail vertex is checked at its true path degree.
    """
    assert t >= 1
    H = [[0]*6 for _ in range(6)]
    for j, (vl,v0) in enumerate(STATES):
        for i, (v0a,v1) in enumerate(STATES):
            if v0 != v0a:
                continue
            for tail in product((W,Y,B), repeat=t):
                if not valid(v0, (vl,v1,tail[0])):
                    continue
                if all(valid(tail[k],
                             (v0 if k == 0 else tail[k-1],) +
                             (() if k == t-1 else (tail[k+1],)))
                       for k in range(t)):
                    H[j][i] += 1
    return H


def path_cycle_count(c,t):
    assert c >= 3 and t >= 1
    return trace(mm(matpow(M,c-1),boundary(t)))


def cycle_count(c):
    assert c >= 3
    return trace(matpow(M,c))


# A second method: exhaustive edge subsets, wholly independent of colors.
def edges(c,t=0):
    E = [(i,(i+1)%c) for i in range(c)]
    if t:
        E.append((0,c))
        E.extend((c+j-1,c+j) for j in range(1,t))
    return E


def ped_bruteforce(c,t=0):
    E = edges(c,t)
    touch = [sum(1 << k for k,(a,b) in enumerate(E)
                 if k != j and (a in (u,v) or b in (u,v)))
             for j,(u,v) in enumerate(E)]
    return sum(all((S & (1 << j)) or (S & touch[j]).bit_count() == 1
                   for j in range(len(E))) for S in range(1 << len(E)))


seed_F = [[3,3,6],[4,5,8],[6,9,12]]
seed_D = [[2,3,4],[2,5,7],[4,6,9]]
assert [[path_cycle_count(c,t) for t in range(1,4)]
        for c in range(3,6)] == seed_F
assert [[cycle_count(c+t)-path_cycle_count(c,t) for t in range(1,4)]
        for c in range(3,6)] == seed_D
assert [cycle_count(n) for n in range(3,9)] == [4,5,6,10,15,21]

# Check the original edge-subset definition, not just the transfer identity.
for c in range(3,11):
    assert cycle_count(c) == ped_bruteforce(c)
    for t in range(1,6):
        assert path_cycle_count(c,t) == ped_bruteforce(c,t)

# Exact recurrence tests away from boundary (the proof supplies infinity).
for c in range(6,13):
    for t in (1,2,3,4,5):
        assert path_cycle_count(c,t) == (path_cycle_count(c-1,t) +
                                         path_cycle_count(c-3,t))
for c in range(3,11):
    for t in range(4,9):
        assert path_cycle_count(c,t) == (path_cycle_count(c,t-1) +
                                         path_cycle_count(c,t-3))
for c in range(3,11):
    for t in range(1,9):
        assert path_cycle_count(c,t) < cycle_count(c+t)

print('VERIFIED: matrix identity, 9 exact seeds, edge-subset replay, recurrences, strict inequalities.')
print('F seeds (rows c=3,4,5; columns t=1,2,3):', seed_F)
print('Deficit seeds (same indexing):', seed_D)
