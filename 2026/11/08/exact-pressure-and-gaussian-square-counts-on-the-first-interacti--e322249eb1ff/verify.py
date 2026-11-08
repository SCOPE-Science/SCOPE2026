#!/usr/bin/env python3
"""Exact transfer-matrix verification for mixed domino/3-square 4-row strips.

Requires Python 3.9+ and SymPy (tested using locally installed SymPy).
No external data files, remote network operations, or random sampling.
"""
from collections import defaultdict, deque
from functools import lru_cache
import math
import sympy as sp

H = 4
FULL = (1 << H) - 1

@lru_cache(None)
def transitions(state):
    a, b, c = state
    out = defaultdict(int)
    def fill(x, y, z, k):
        if x == FULL:
            out[((y, z, 0), k)] += 1
            return
        row = next(r for r in range(H) if not (x >> r) & 1)
        bit = 1 << row
        if not y & bit:
            fill(x | bit, y | bit, z, k)
        if row + 1 < H and not (x & (bit << 1)):
            fill(x | bit | (bit << 1), y, z, k)
        if row + 2 < H:
            bits = 7 << row
            if not ((x | y | z) & bits):
                fill(x | bits, y | bits, z | bits, k + 1)
    fill(a, b, c, 0)
    return dict(out)

states = [(0, 0, 0)]
index = {states[0]: 0}
edges = []
for state in states:
    adj = {}
    for (target, count_squares), multiplicity in transitions(state).items():
        if target not in index:
            index[target] = len(states)
            states.append(target)
        adj[index[target], count_squares] = multiplicity
    edges.append(adj)
assert len(states) == len(edges) == 18

# Check strong connectivity by direct graph reachability from every state.
def reaches(start):
    seen = {start}
    frontier = [start]
    for node in frontier:
        for target, _ in edges[node]:
            if target not in seen:
                seen.add(target)
                frontier.append(target)
    return seen
assert all(len(reaches(i)) == 18 for i in range(18))
assert edges[0].get((0, 0), 0) >= 1  # Aperiodicity by a unit-length loop.

z, u = sp.symbols('z u')
M = sp.eye(18)
for i, adjacency in enumerate(edges):
    for (j, k), weight in adjacency.items():
        M[i,j] -= z * weight * u ** k
P = (1-z**2)*(z**4+z**3-3*z**2-z+1)
Q = 1-2*z-7*z**2+8*z**3+17*z**4-4*z**5-9*z**6+z**8-2*u**2*z**6*(1-z**2)**2
exact_entry = sp.cancel(M.inv(method='DM')[0,0])
assert sp.cancel(exact_entry - P/Q) == 0

# Independently compute each exact 4 x N square-count histogram using
# cell-level placements, not the column-state transfer matrix.
def direct_histogram(n):
    full = (1 << (4*n))-1
    @lru_cache(None)
    def count(occupied):
        if occupied == full:
            return {0:1}
        first = next(k for k in range(4*n) if not (occupied >> k)&1)
        row, col = divmod(first,n)
        res = defaultdict(int)
        for height, width in ((1,2),(2,1),(3,3)):
            if row+height>4 or col+width>n:
                continue
            bits=0
            for rr in range(row,row+height):
                for cc in range(col,col+width):
                    bits |= 1 << (rr*n+cc)
            if occupied & bits:
                continue
            for k, v in count(occupied | bits).items():
                res[k + (height == 3)] += v
        return dict(res)
    return count(0)

vec = {(0, 0):1} # (state-index, count-square) -> multiplicity
record = []
for n in range(10):
    trans_hist = {k:v for (i,k),v in vec.items() if i == 0 and v}
    direct = direct_histogram(n) if n else {0:1}
    assert trans_hist == direct, (n, trans_hist, direct)
    assert all(k % 2 == 0 for k in trans_hist)
    record.append((n, sum(trans_hist.values()),trans_hist))
    nxt=defaultdict(int)
    for (i,k),count in vec.items():
        for (j,kk),weight in edges[i].items():
            nxt[j,k+kk]+=count*weight
    vec=dict(nxt)
assert record[6][2] == {0:281,2:2}
assert record[9][2] == {0:6336,2:108}

# Positive/zero square closed walks with distinct square density establish
# asymptotic variance > 0 by the finite-state Markov additive criterion.
# The positive cycle is witnessed by two aligned 3x3 tiles in a 4x6 rectangle.
assert direct_histogram(6)[2] == 2

Q1 = sp.Poly(Q.subs(u,1), z)
root = next(float(sp.re(root)) for root in sp.nroots(Q1, maxsteps=400)
            if abs(float(sp.im(root))) < 1e-10 and 0.35 < float(sp.re(root)) < 0.36)
Qr, Qu = sp.diff(Q,z), sp.diff(Q,u)
rs = -u*Qu/Qr
rss=-(sp.diff(Q,z,2)*rs**2+2*u*sp.diff(Q,z,u)*rs+u*Qu+u**2*sp.diff(Q,u,2))/Qr
at={z:root,u:1}
mu = float((-rs/z).subs(at))
variance = float((rs**2/z**2 - rss/z).subs(at))
assert 0.009767 < mu < 0.009769
assert 0.01819 < variance < 0.01820
assert 2.8549 < 1/root < 2.8550

print('VERIFY_OK states=18 strong_connected=True exact_rational_identity=True '
      'independent_board_counts=4x0..9 even_square_parity=True '
      'mean=%.12f variance=%.12f lambda=%.12f' % (mu,variance,1/root))
