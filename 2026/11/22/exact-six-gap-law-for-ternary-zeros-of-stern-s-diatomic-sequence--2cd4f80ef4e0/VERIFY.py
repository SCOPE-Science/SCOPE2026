#!/usr/bin/env python3
"""Exact finite-state certificate for gaps between multiples of three in Stern's sequence.
No third-party packages are needed. Run: python VERIFY.py
"""
from collections import defaultdict, deque
from fractions import Fraction as F


def left(u):
    a, b = u
    return (a, (a+b) % 3)


def right(u):
    a, b = u
    return ((a+b) % 3, b)


def children(pair):
    a, b = pair
    return (left(a), right(a)), (right(a), left(b))


def exact_solve(matrix, rhs):
    n = len(rhs)
    a = [[F(matrix[i][j]) for j in range(n)] + [F(rhs[i])]
         for i in range(n)]
    for j in range(n):
        k = next(i for i in range(j, n) if a[i][j])
        a[j], a[k] = a[k], a[j]
        d = a[j][j]
        a[j] = [v/d for v in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                d = a[i][j]
                a[i] = [a[i][h] - d*a[j][h] for h in range(n+1)]
    return [a[i][n] for i in range(n)]


root = ((0, 1), (1, 1))
pairs = [root]
index = {root: 0}
for w in pairs:
    for nxt in children(w):
        if nxt not in index:
            index[nxt] = len(pairs)
            pairs.append(nxt)
assert len(pairs) == 20
assert all(u != (0,0) and v != (0,0) for u,v in pairs)
M = [[0] * 20 for _ in range(20)]
for j, w in enumerate(pairs):
    for nxt in children(w):
        M[index[nxt]][j] += 1
assert all(sum(M[i][j] for i in range(20)) == 2 for j in range(20))
# Verify strong connectivity and aperiodicity by a fixed-point loop.
rev = [[] for _ in range(20)]
for j in range(20):
    for nxt in children(pairs[j]):
        rev[index[nxt]].append(j)
seen = {0}
queue = [0]
for a in queue:
    for b in rev[a]:
        if b not in seen:
            seen.add(b)
            queue.append(b)
assert len(seen) == 20 and 0 in [index[v] for v in children(root)]
Q = [[2 * int(i == j) - M[i][j] for j in range(20)] for i in range(20)]
Q[-1] = [1] * 20
rhs = [0] * 19 + [1]
pi = exact_solve(Q, rhs)
assert sum(pi) == 1 and all(v > 0 for v in pi)
assert all(sum(F(M[i][j]) * pi[j] for j in range(20)) == 2*pi[i]
           for i in range(20))
expected_weights = [F(x) for x in ('1/14','1/28','1/14','1/56','1/8',
 '1/28','1/8','1/14','1/14','1/56','1/14','1/28','1/28','1/14',
 '1/28','1/56','1/56','1/28','1/56','1/56')]
assert pi == expected_weights

# Stern values at the block endpoints; these are *integers*, not just residues.
s = [0, 1]
for j in range(2, 9):
    s.append(s[j//2] if not j % 2 else s[j//2]+s[j//2+1])
assert s == [0,1,1,2,1,3,2,3,1]
Z = {}
for a,b in {x for p in pairs for x in p}:
    Z[(a,b)] = tuple(j for j in range(8)
        if (s[8-j] * a + s[j] * b) % 3 == 0)
expected_sets = {
    (0,1):(0,5,7), (0,2):(0,5,7),
    (1,0):(1,3), (2,0):(1,3),
    (1,1):(2,6), (2,2):(2,6),
    (1,2):(4,), (2,1):(4,),
}
assert Z == expected_sets
weights = defaultdict(F)
for i, (a,b) in enumerate(pairs):
    z = Z[a]
    for h,t in zip(z,z[1:]):
        weights[t-h] += pi[i]
    weights[8+Z[b][0]-z[-1]] += pi[i]
assert dict(weights) == {
    2:F(4,7), 3:F(2,7), 4:F(2,7),
    5:F(4,7), 6:F(1,7), 8:F(1,7)
}
assert sum(weights.values()) == 2
assert sum(d*v for d,v in weights.items()) == 8
assert max(weights) == 8

# Independent direct enumeration on a sizeable initial segment.
N = 1 << 16
smod = [0] * (N + 1)
smod[1] = 1
for n in range(2, N+1):
    smod[n] = (smod[n//2] if n % 2 == 0 else
               smod[n//2]+smod[n//2+1]) % 3
zeros = [n for n in range(N+1) if smod[n] == 0]
assert all(zeros[i+1]-zeros[i] in weights for i in range(len(zeros)-1))
assert set(zeros[i+1]-zeros[i] for i in range(len(zeros)-1)) == set(weights)
print('CHECK_OK 20-state exact stationary law; six sharp gap values; 65537 indices')
print('gap probabilities:', ', '.join(f'{d}:{weights[d]/2}' for d in sorted(weights)))
