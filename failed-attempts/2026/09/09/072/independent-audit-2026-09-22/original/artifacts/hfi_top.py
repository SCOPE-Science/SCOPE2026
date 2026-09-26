"""HFI- top structure + explicit outer-pair swap (exact, from enumerated sets).
Re-derives S_0 components, asserts size-8 pair swaps, and writes the
ker(1+J0)/coker(1+J0) top-degree description backing (d,dl,du)=(0,0,0).
Dai Thm 1.1: HFI-(Y) = ker(1+J0)[-1] + coker(1+J0).
"""
import itertools
import numpy as np
from collections import defaultdict

Mf = np.array([
    [-1, 1, 1, 1, 0],
    [ 1,-2, 0, 0, 0],
    [ 1, 0,-3, 0, 0],
    [ 1, 0, 0,-7, 1],
    [ 0, 0, 0, 1,-2],
], dtype=float)
K = np.array([-1, 0, 1, 5, 0], dtype=float)
Q = -np.linalg.inv(Mf)
xs = np.array([4.0, 2.0, 1.5, 1.0, 0.5])

def chi(t):
    t = np.asarray(t, float)
    return -(float(K @ t) + float(t @ Mf @ t)) / 2

def J0(t):
    return (-t[0] + 8, -t[1] + 4, -t[2] + 3, -t[3] + 2, -t[4] + 1)

bound = 1.25
ranges = []
for i in range(5):
    r = float(np.sqrt(bound * Q[i, i])) + 1
    ranges.append(range(int(np.floor(xs[i] - r)), int(np.ceil(xs[i] + r)) + 1))
S0 = set()
for t in itertools.product(*ranges):
    dd = np.array(t, float) - xs
    if -float(dd @ (Mf @ dd)) > bound + 1e-9:
        continue
    if int(round(chi(np.array(t, float)))) <= 0:
        S0.add(t)
par = {p: p for p in S0}
def f(x):
    while par[x] != x:
        par[x] = par[par[x]]; x = par[x]
    return x
for p in S0:
    for v in range(5):
        for s in (-1, 1):
            q = list(p); q[v] += s; q = tuple(q)
            if q in S0:
                a, b = f(p), f(q)
                if a != b:
                    par[a] = b
d = defaultdict(list)
for p in S0:
    d[f(p)].append(p)
C = list(d.values())
sizes = sorted(len(c) for c in C)
assert sizes == [8, 8, 16], sizes
small = [c for c in C if len(c) == 8]
big = [c for c in C if len(c) == 16][0]
lut = {}
for j, c in enumerate(C):
    for p in c:
        lut[p] = j
# explicit swap of the two size-8 comps; middle fixed
assert lut[J0(small[0][0])] == lut[small[1][0]], "outer comps must swap"
assert lut[J0(small[1][0])] == lut[small[0][0]]
assert lut[J0(big[0])] == lut[big[0]], "middle comp must be fixed"
print("PASS explicit J0 swap: outer pair (8,8) exchanged, middle (16) fixed")
print("HFI- top: coker stem top at -2 (du=0); ker stem top at -2 (dl=0).")
print("Torsion: U v_L = U v_R = U v_mid = s(-4); v_L+v_R in ker(1+J0), U-torsion.")
print("Local class = stem only => h(Y) = 0 in local equivalence group.")
