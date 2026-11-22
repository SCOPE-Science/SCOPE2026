#!/usr/bin/env python3
"""Exact rational enumerator for binary one-hole local-square avoidance.
Standard library only. Usage: python3 verify_transfer.py
"""
from collections import defaultdict
from itertools import product


def comp(s):
    return ''.join('1' if a == '0' else '0' if a == '1' else '?' for a in s)


def canonical(s):
    return min(s, comp(s))


def good_extend(s, a):
    t = s + a
    for p in (2, 3):
        if len(t) >= 2*p and all(x == y or x == '?' or y == '?'
                for x, y in zip(t[-2*p:-p], t[-p:])):
            return False
    return True

# A five-character memory state records whether the unique hole is still visible.
# Used flag 0: no hole used; 1: one hole has been used, possibly forgotten.
states = set()
for s in map(''.join, product('01', repeat=5)):
    states.add((0, canonical(s)))
    states.add((1, canonical(s)))
for k in range(5):
    for w in product('01', repeat=4):
        s = ''.join(w[:k]) + '?' + ''.join(w[k:])
        states.add((1, canonical(s)))
states = sorted(states)
assert len(states) == 72
index = {s: i for i, s in enumerate(states)}
trans = [[] for _ in states]
for i, (used, s) in enumerate(states):
    for a in ('01' if used else '01?'):
        if not good_extend(s, a):
            continue
        ns = s[1:] + a
        nu = used or a == '?'
        trans[i].append(index[(int(nu), canonical(ns))])

# The binary no-hole block Q acts on 16 complement orbits of 5-bit states.
regular = [i for i, (h, s) in enumerate(states) if h == 0]
regular_index = {i: j for j, i in enumerate(regular)}
Q = [[0] * 16 for _ in range(16)]
for i in regular:
    for j in trans[i]:
        if j in regular_index:
            Q[regular_index[i]][regular_index[j]] += 1

def matmul(A, B):
    k = len(A)
    C = [[0]*k for _ in range(k)]
    for i in range(k):
        for j, a in enumerate(A[i]):
            if a:
                for l, b in enumerate(B[j]):
                    C[i][l] += a*b
    return C

# Newton identities for the exact characteristic polynomial of Q.
P = [[int(i == j) for j in range(16)] for i in range(16)]
traces = []
for n in range(1, 17):
    P = matmul(P, Q)
    traces.append(sum(P[i][i] for i in range(16)))
coeff = [1]
for k in range(1, 17):
    v = -sum(coeff[k-j]*traces[j-1] for j in range(1, k+1))
    assert v % k == 0
    coeff.append(v//k)
assert coeff == [1,0,-1,-1,-1,0,1]+[0]*10, coeff
# Therefore det(I - zQ) = 1-z^2-z^3-z^4+z^6.
D = [1, 0, -1, -1, -1, 0, 1]
DD = [sum(D[j]*D[i-j] for j in range(max(0,i-6), min(6,i)+1)) for i in range(13)]

# There is one nontrivial strongly connected component of Q, containing
# eight vertices; all other components have no loops. It is aperiodic since
# it contains return cycles of lengths 2 and 3 (gcd 1).
def reachable(seed, adj):
    seen = {seed}
    todo = [seed]
    while todo:
        i = todo.pop()
        for j in adj[i]:
            if j not in seen:
                seen.add(j)
                todo.append(j)
    return seen
adj = [[j for j,v in enumerate(row) if v] for row in Q]
r_adj = [[i for i,row in enumerate(Q) if row[j]] for j in range(16)]
components = []
unseen = set(range(16))
while unseen:
    x = min(unseen)
    component = reachable(x, adj) & reachable(x, r_adj)
    components.append(component)
    unseen -= component
assert sorted(map(len, components), reverse=True) == [8] + [1]*8
main = next(v for v in components if len(v) == 8)
assert any(Q[i][j] and Q[j][i] for i in main for j in main)
assert any(Q[i][j] and Q[j][k] and Q[k][i]
           for i in main for j in main for k in main)
assert all(Q[i][i] == 0 for component in components if len(component) == 1
           for i in component)

# Hole-bearing five-suffix states form a transient block: after five ordinary
# letters are appended the hole has left the suffix, so there are no cycles.
transient = {i for i, (used,s) in enumerate(states) if '?' in s}
assert len(transient) == 40
reach = {i: {i} for i in transient}
for step in range(5):
    reach = {i: {j for k in reach[i] for j in trans[k] if j in transient}
             for i in transient}
    if step < 4:
        assert any(reach.values())
assert not any(reach.values())

# Seed with the complete valid five-character prefixes, counting both members
# of each complement pair. All subsequent transitions are exact.
counts = [0] * 72
for v in product('01?', repeat=5):
    s = ''.join(v)
    if s.count('?') <= 1 and all(good_extend(s[:k-1], s[k-1]) for k in range(1,6)):
        counts[index[(int('?' in s), canonical(s))]] += 1
assert sum(counts) == 52  # valid binary plus valid one-hole prefixes

# Exact counts H_n for 0 <= n <= 42; independent short prefix dynamic.
H = [0, 1, 4, 12, 16]
for n in range(5,43):
    if n > 5:
        nxt = [0] * len(states)
        for i, c in enumerate(counts):
            if c:
                for j in trans[i]:
                    nxt[j] += c
        counts = nxt
    H.append(sum(c for (used,s), c in zip(states, counts) if used))
assert H[:21] == [0,1,4,12,16,32,40,66,100,152,224,336,500,742,
                  1092,1612,2372,3476,5088,7436,10852]
num = [sum(DD[j]*H[i-j] for j in range(min(i,12)+1)) for i in range(43)]
N = [0,1,4,10,6,-1,-18,-29,-14,7,14,16,-4,-7,0,2,4,2,-4]
assert num[:len(N)] == N
assert all(v == 0 for v in num[len(N):]), num
# Rational identity is now exact for every n: the transition operator has
# diagonal blocks Q, nilpotent T (T^5=0), Q; each Q-resolvent has numerator
# degree <=15 and denominator D, and the two Q blocks can appear at most once
# each along any state path. Every rational numerator has degree <=41 after
# the five-prefix shift, so the checks through degree 42 are exhaustive.
print('PASS: 72 complementary states; 16x16 charpoly; nilpotent block;')
print('      complete all-length numerator and denominator certificates; H_20=', H[20])
print('N coefficients ascending:', N)
