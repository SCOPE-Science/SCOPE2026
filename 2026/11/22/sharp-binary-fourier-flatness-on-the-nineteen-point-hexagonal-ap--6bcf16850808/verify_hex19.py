#!/usr/bin/env python3
"""Direct-correlation exhaustive verifier (requires NumPy)."""
from collections import Counter
import numpy as np

S = [(x, y) for x in range(-2, 3) for y in range(-2, 3)
     if max(abs(x), abs(y), abs(x + y)) <= 2]
assert len(S) == 19
idx = {p: i for i, p in enumerate(S)}
anchor = idx[(0, 0)]
free = [j for j in range(19) if j != anchor]
rows = np.arange(1 << len(free), dtype=np.uint32)
signs = np.ones((len(rows), 19), dtype=np.int8)
for b, j in enumerate(free):
    signs[:, j] = 1 - 2 * ((rows >> b) & 1).astype(np.int8)
positive = sorted({d if d[0] > 0 or (d[0] == 0 and d[1] > 0)
                   else (-d[0], -d[1])
                   for p in S for q in S if p != q
                   for d in [(p[0]-q[0], p[1]-q[1])]})
assert len(positive) == 30
energy = np.full(len(rows), 19**2, dtype=np.int32)
for d in positive:
    pairs = [(i, j) for i, p in enumerate(S) for j, q in enumerate(S)
             if q[0] - p[0] == d[0] and q[1] - p[1] == d[1]]
    autocorr = np.zeros(len(rows), dtype=np.int16)
    for i, j in pairs:
        autocorr += signs[:, i] * signs[:, j]
    energy += 2 * autocorr.astype(np.int32) ** 2
values, counts = np.unique(energy, return_counts=True)
minima = set(int(x) for x in rows[energy == values[0]])
assert (int(values[0]), len(minima), int(values[1]), int(values[-1])) == (467, 72, 475, 3259)
assert sum(int(y) for y in counts) == 262144

def vec(mask):
    a = [1]*19
    for b, i in enumerate(free):
        a[i] = -1 if (mask >> b) & 1 else 1
    return a

def mask(a):
    return sum((1 << b) for b, i in enumerate(free) if a[i] == -1)

def rot(p):
    x, y = p
    return -y, x+y

def reflect(p):
    return p[1], p[0]

def transform(a, nrot, ref, u, v):
    out = [0]*19
    for i, p in enumerate(S):
        q = p
        for _ in range(nrot):
            q = rot(q)
        if ref:
            q = reflect(q)
        out[idx[q]] = a[i] * (-1 if (u*q[0] + v*q[1]) % 2 else 1)
    return out

orbits = []
remaining = set(minima)
while remaining:
    seed = min(remaining)
    orbit = {mask(transform(vec(seed), nrot, ref, u, v))
             for nrot in range(6) for ref in range(2)
             for u in range(2) for v in range(2)}
    assert orbit <= minima
    orbits.append((seed, orbit))
    remaining -= orbit
assert sorted((seed,len(orbit)) for seed,orbit in orbits) == [(3441,24),(8151,24),(10446,24)]
assert sum(len(orbit) for _,orbit in orbits) == 72
print('DIRECT_EXHAUSTIVE_PASS')
print('sites=19 nonzero_shift_pairs=30 assignments=262144')
print(f'min={values[0]} minimizers_center_plus={len(minima)} next={values[1]} max={values[-1]}')
print('first_12_histogram=', list(zip(values[:12].tolist(), counts[:12].tolist())))
print('orbit_representative_and_size=', [(seed,len(orbit)) for seed,orbit in orbits])
for seed,_ in orbits:
    print('representative', seed,'negative_sites',[S[i] for i,t in enumerate(vec(seed)) if t<0])
