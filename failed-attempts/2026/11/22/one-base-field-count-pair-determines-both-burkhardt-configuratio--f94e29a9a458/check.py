#!/usr/bin/env python3
"""Finite symplectic-geometry certificate for Burkhardt node/plane Frobenius spectra.

Requires Python >= 3.9, standard library only. Reconstructs all 25920 elements
of PSp(4,3), all twenty conjugacy classes, and 40/45-point orbit spectra.
"""
from itertools import product, combinations
from collections import Counter, defaultdict
from math import lcm
import csv
from pathlib import Path

V = list(product(range(3), repeat=4))
def omega(a,b):
    return (a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2]) % 3

def norm(v):
    k = next(i for i,x in enumerate(v) if x != 0)
    f = 1 if v[k] == 1 else 2
    return tuple(f*x % 3 for x in v)

pts = sorted({norm(v) for v in V if any(v)})
assert len(pts) == 40
planes = {}
for a,b in combinations(pts,2):
    U = tuple(sorted({norm(tuple((u*a[j]+v*b[j])%3 for j in range(4)))
                      for u in range(3) for v in range(3) if u or v}))
    assert len(U) == 4
    planes[U] = omega(a,b) != 0
assert len(planes) == 130 and sum(planes.values()) == 90
nd = sorted(U for U, nondeg in planes.items() if nondeg)
nd_set = set(nd)
node_set = set()
for U in nd:
    perp = tuple(sorted(v for v in pts if all(omega(v,w)==0 for w in U)))
    assert len(perp) == 4 and perp in nd_set and U != perp
    node_set.add(tuple(sorted((U,perp))))
nodes = sorted(node_set)
assert len(nodes) == 45
assert sum(any(v in U for U in node) for v in pts for node in nodes) == 360
assert all(sum(any(v in U for U in node) for node in nodes) == 9 for v in pts)
assert all(sum(any(v in U for U in node) for v in pts) == 8 for node in nodes)

obj = pts + nodes
lookup = {x:i for i,x in enumerate(obj)}

def trans(v,x):
    c = omega(x,v)
    return tuple((x[i]+c*v[i])%3 for i in range(4))

gen_vectors = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
               (1,0,1,0),(1,0,0,1)]
gens = []
for v in gen_vectors:
    def image_plane(U):
        return tuple(sorted(norm(trans(v,x)) for x in U))
    s = bytes([lookup[norm(trans(v,x))] for x in pts] +
              [lookup[tuple(sorted((image_plane(U),image_plane(W))))]
               for U,W in nodes])
    assert sorted(s) == list(range(85))
    for i,pt in enumerate(pts):
        for j,node in enumerate(nodes):
            assert any(pt in U for U in node) == any(pts[s[i]] in U for U in nodes[s[40+j]-40])
    gens.append(s)

def mult(a,b):
    return bytes(a[b[i]] for i in range(85))

def inverse(a):
    res = [0]*85
    for i,v in enumerate(a):res[v] = i
    return bytes(res)

identity = bytes(range(85))
all_group = {identity}
queue = [identity]
for g in queue:
    for s in gens:
        h = mult(g,s)
        if h not in all_group:
            all_group.add(h)
            queue.append(h)
assert len(all_group) == 25920  # equals the exact order of PSp(4,3)

def cycles(g,lo,hi):
    used = set()
    counts = Counter()
    for i in range(lo,hi):
        if i in used: continue
        k = i; d = 0
        while k not in used:
            used.add(k); d += 1; k = g[k]
        assert k == i
        counts[d] += 1
    return tuple(sorted(counts.items()))

def fixed(c):
    return sum(n for d,n in c if d == 1)

remaining = set(all_group)
inv_gens = [inverse(g) for g in gens]
classes = []
while remaining:
    rep = min(remaining)
    orbit = {rep}
    queue = [rep]
    for h in queue:
        for g,gi in zip(gens,inv_gens):
            x = mult(mult(g,h),gi)
            if x not in orbit:
                orbit.add(x);queue.append(x)
    assert orbit <= remaining
    remaining -= orbit
    cp = cycles(rep,0,40)
    cn = cycles(rep,40,85)
    classes.append((lcm(*(d for d,n in cycles(rep,0,85))),len(orbit),cp,cn))
classes.sort(key=lambda c:(c[0],c[1],c[2],c[3]))
assert len(classes)==20 and sum(c[1] for c in classes)==25920

def zeta_signature(spec):return ';'.join(f'{d}:{n}' for d,n in spec)

full={(cp,cn) for _,_,cp,cn in classes}
first={(fixed(cp),fixed(cn)) for _,_,cp,cn in classes}
assert len(full)==15 and len(first)==15
lookup_full=defaultdict(set)
for _,_,cp,cn in classes:
    lookup_full[(fixed(cp),fixed(cn))].add((cp,cn))
assert all(len(v)==1 for v in lookup_full.values())
assert sum(len([c for c in classes if (c[2],c[3])==spec])==2 for spec in full)==5
out = Path(__file__).with_name('spectra.csv')
with out.open(encoding='utf-8',newline='') as f:
    actual = list(csv.DictReader(f))
expected=[]
for i,(order,class_size,cp,cn) in enumerate(classes,1):
    expected.append({'class_index':str(i),'order':str(order),'class_size':str(class_size),
                     'plane_cycles':zeta_signature(cp),'node_cycles':zeta_signature(cn),
                     'rational_planes':str(fixed(cp)),'rational_nodes':str(fixed(cn))})
assert actual==expected, 'The supplied spectra.csv does not agree with exhaustive construction'
print('BURKHARDT_40_PLANES_45_NODES_25920_GROUP_20_CLASSES_15_JOINT_SPECTRA_VERIFIED')
