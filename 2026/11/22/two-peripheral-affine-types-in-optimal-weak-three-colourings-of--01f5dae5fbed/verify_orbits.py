#!/usr/bin/env python3
"""Exhaustive, independent affine-plane weak-colouring verifier (Python stdlib)."""
from collections import Counter, deque
from itertools import combinations, permutations, product
from math import comb

P = tuple(product(range(3), repeat=2))
# In F_3, the third point on the affine line through p and q is -p-q.
L = set()
for a, b in combinations(range(9), 2):
    middle = tuple((-P[a][i]-P[b][i]) % 3 for i in range(2))
    L.add(tuple(sorted((a, b, P.index(middle)))))
L = tuple(sorted(L))
assert len(L) == 12 and all(len(l) == 3 for l in L)
valid = {v for v in product(range(3), repeat=9)
         if all(not (v[a] == v[b] == v[c]) for a, b, c in L)}
assert len(valid) == 3762

# The full GL(2,3) semidirect translations group times the colour-name group.
transforms = []
for a, b, c, d in product(range(3), repeat=4):
    if (a*d-b*c) % 3 == 0:
        continue
    for dx, dy in P:
        t = tuple(P.index(((a*x+b*y+dx) % 3, (c*x+d*y+dy) % 3))
                  for x, y in P)
        transforms.append(t)
assert len(transforms) == 432
assert all(tuple(sorted(t[i] for i in l)) in L for t in transforms for l in L)

def orbit(state):
    ans = set()
    for t in transforms:
        z = [0]*9
        for i, j in enumerate(t):
            z[j] = state[i]
        for s in permutations(range(3)):
            ans.add(tuple(s[c] for c in z))
    return ans

def adjacent(v):
    for i in range(9):
        for c in range(3):
            if c != v[i]:
                w = v[:i] + (c,) + v[i+1:]
                if w in valid:
                    yield w

def distances(src):
    d = {src:0}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in adjacent(u):
            if v not in d:
                d[v] = d[u]+1
                q.append(v)
    assert len(d) == len(valid), 'disconnected state graph'
    return d

seen = set()
rows = []
for v in sorted(valid):
    if v in seen:
        continue
    O = orbit(v)
    assert O <= valid and not (O & seen)
    seen |= O
    d = distances(v)
    shape = tuple(sorted(Counter(v).values()))
    counts = []
    for aa,bb in ((1,0),(0,1),(1,1),(1,2)):
        rainbow = 0
        for cc in range(3):
            line = tuple(i for i,(x,y) in enumerate(P)
                         if (aa*x+bb*y)%3 == cc)
            rainbow += (len({v[i] for i in line}) == 3)
        counts.append(rainbow)
    spread = tuple(sorted(counts))
    degree = len(tuple(adjacent(v)))
    ecc = max(d.values())
    rows.append((len(O), shape, spread, degree, ecc, Counter(d.values())))
assert seen == valid
signature = Counter((s, shape, rainbow, degree, ecc) for s,shape,rainbow,degree,ecc,_ in rows)
assert signature == Counter({
    (144,(3,3,3),(0,0,0,3),9,10):1,
    (162,(1,4,4),(0,0,0,0),8,10):1,
    (864,(3,3,3),(0,1,1,1),9,9):1,
    (1296,(2,3,4),(0,0,0,2),9,9):1,
    (1296,(2,3,4),(0,0,1,1),9,9):1})
assert sum(s for s,*_ in rows)==3762
assert sum(s*degree for s,_,_,degree,_,_ in rows)//2 == 16848
assert sum(s*d[10] for s,_,_,_,_,d in rows)//2 == 306
assert sum(s*d.get(10, 0) for s,_,_,_,_,d in rows) == 612
assert min(ecc for s,_,_,_,ecc,_ in rows) == 9
assert max(ecc for s,_,_,_,ecc,_ in rows) == 10

# Inclusion-exclusion across all twelve line-monochromaticity constraints.
coeff = Counter()
for mask in range(1 << len(L)):
    uf = list(range(9))
    def root(x):
        while x != uf[x]:
            x = uf[x]
        return x
    for j, line in enumerate(L):
        if (mask >> j) & 1:
            r = root(line[0])
            for x in line[1:]:
                uf[root(x)] = r
    coeff[len({root(i) for i in range(9)})] += (-1)**mask.bit_count()
assert dict(coeff) == {9:1, 7:-12, 5:66, 4:-72, 3:-4, 2:27, 1:-6}
assert sum(c*3**k for k,c in coeff.items()) == 3762
assert sum(c*2**k for k,c in coeff.items()) == 0
print('PASS: lines=12, proper named 3-colourings=3762, components=1')
print('PASS: affine-and-colour-name orbits:', sorted(signature.elements()))
print('PASS: edges=16848, radius=9, diameter=10, diametral pairs=306')
print('PASS: full chromatic polynomial coefficients', sorted(coeff.items()))
