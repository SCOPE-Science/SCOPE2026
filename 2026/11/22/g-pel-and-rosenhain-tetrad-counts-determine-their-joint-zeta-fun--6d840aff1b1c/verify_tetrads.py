#!/usr/bin/env python3
"""Independent exhaustive verification of genus-two Kummer tetrad Frobenius spectra.

Requires Python >=3.9 standard library only; writes a deterministic CSV when given a path.
The two constructions are independent: (i) affine cosets of two-dimensional
subspaces, (ii) direct enumeration of all four-element node sets.
"""
import csv
import itertools
import sys
from collections import Counter, defaultdict

N = 6
FULL = (1 << N) - 1
V = tuple(sorted({min(m, m ^ FULL) for m in range(1 << N) if m.bit_count() % 2 == 0}))
assert len(V) == 16 and V[0] == 0

def add(x, y):
    z = x ^ y
    return min(z, z ^ FULL)

def pairing(x, y):
    return (x & y).bit_count() % 2

def transform(v, perm):
    out = 0
    for i in range(N):
        if (v >> i) & 1:
            out |= 1 << perm[i]
    return min(out, out ^ FULL)

def transform_set(obj, perm):
    return frozenset(transform(x, perm) for x in obj)

def subspace_cosets():
    iso, non = set(), set()
    planes = {frozenset((0, u, v, add(u, v)))
              for u, v in itertools.combinations(V[1:], 2)}
    assert len(planes) == 35
    for plane in planes:
        assert len(plane) == 4
        isotropic = all(pairing(u, v) == 0 for u in plane for v in plane)
        target = iso if isotropic else non
        for x in V:
            target.add(frozenset(add(x, w) for w in plane))
    assert len(iso) == 60 and len(non) == 80 and not iso.intersection(non)
    return iso, non

def direct_quadruples():
    iso, non = set(), set()
    for quad in itertools.combinations(V, 4):
        a, b, c, d = quad
        # A four-point set is an affine plane iff a+b+c+d=0 in V.
        if add(add(a, b), add(c, d)) != 0:
            continue
        assert len({add(a, b), add(a, c), add(a, d)}) == 3
        isotropic = pairing(add(a, b), add(a, c)) == 0
        (iso if isotropic else non).add(frozenset(quad))
    return iso, non

def partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for z in range(minimum, n + 1):
            for rest in partitions(n - z, z):
                yield (z,) + rest

def perm_from_partition(parts):
    p = list(range(N))
    at = 0
    for k in parts:
        for i in range(k):
            p[at + i] = at + ((i + 1) % k)
        at += k
    assert at == N
    return tuple(p)

def permutation_cycle_type(p):
    seen = set()
    lengths = []
    for i in range(N):
        if i in seen:
            continue
        cur = i
        length = 0
        while cur not in seen:
            seen.add(cur)
            length += 1
            cur = p[cur]
        assert cur == i
        lengths.append(length)
    return tuple(sorted(lengths))

def profile(objects, p):
    seen = set()
    lengths = []
    for obj in objects:
        if obj in seen:
            continue
        current = obj
        cycle_length = 0
        while current not in seen:
            seen.add(current)
            cycle_length += 1
            current = transform_set(current, p)
        assert current == obj
        lengths.append(cycle_length)
    assert sum(lengths) == len(objects)
    return tuple(sorted(Counter(lengths).items()))



def trope_cycle_type(perm):
    # The sixteen theta characteristics of a genus-two curve are
    # six singleton Weierstrass classes and ten complementary triples.
    labels = {('odd',i) for i in range(6)}
    for inds in itertools.combinations(range(6),3):
        mask=sum(1<<i for i in inds)
        labels.add(('even',min(mask,mask^FULL)))
    assert len(labels)==16
    def image(t):
        if t[0]=='odd':
            return ('odd',perm[t[1]])
        mask=0
        for i in range(6):
            if t[1]>>i&1:
                mask|=1<<perm[i]
        return ('even',min(mask,mask^FULL))
    seen=set(); length=[]
    for t in labels:
        if t in seen:
            continue
        k=0; u=t
        while u not in seen:
            seen.add(u);k+=1;u=image(u)
        assert u==t
        length.append(k)
    return tuple(sorted(Counter(length).items()))

def fixed_via_directions(perm):
    # A fixed affine plane must have a fixed direction H; a coset x+H
    # is fixed exactly when (A-I)x belongs to H.
    directions = {frozenset((0, u, v, add(u, v)))
                  for u, v in itertools.combinations(V[1:], 2)}
    counts = [0,0]
    for H in directions:
        if transform_set(H,perm) != H:
            continue
        fixed_representatives = sum(1 for x in V if add(transform(x,perm),x) in H)
        assert fixed_representatives % 4 == 0
        category = 0 if all(pairing(u,v)==0 for u in H for v in H) else 1
        counts[category] += fixed_representatives//4
    return tuple(counts)

def fixed(profile_data, power):
    return sum(d * n for d, n in profile_data if power % d == 0)

def monomial(prof):
    return " ".join(f"{d}^{count}" for d, count in prof)

def main(outpath=None):
    iso1, non1 = subspace_cosets()
    iso2, non2 = direct_quadruples()
    assert iso1 == iso2 and non1 == non2
    universe = iso1 | non1
    assert len(universe) == 140
    # Check equivariance and stability of both geometric families under all S6.
    perm_profiles = defaultdict(set)
    for p in itertools.permutations(range(N)):
        assert {transform(x, p) for x in V} == set(V)
        assert {transform_set(t, p) for t in iso1} == iso1
        assert {transform_set(t, p) for t in non1} == non1
        key = permutation_cycle_type(p)
        perm_profiles[key].add((profile(iso1, p), profile(non1, p)))
    assert len(perm_profiles) == 11
    assert all(len(s) == 1 for s in perm_profiles.values())
    # A full node/trope pair loses two branch distinctions; the tetrad
    # counts resolve precisely one of those two ambiguous pairs.
    a,b=perm_from_partition((1,1,2,2)),perm_from_partition((2,2,2))
    assert profile({frozenset((x,)) for x in V},a)==profile({frozenset((x,)) for x in V},b)
    assert trope_cycle_type(a)==trope_cycle_type(b)
    assert fixed_via_directions(a)==(8,8)
    assert fixed_via_directions(b)==(16,0)
    data=[]
    for part in partitions(N):
        G, R = next(iter(perm_profiles[part]))
        p=perm_from_partition(part)
        assert profile(iso2,p)==G and profile(non2,p)==R
        assert fixed_via_directions(p)==(fixed(G,1),fixed(R,1))
        data.append(dict(partition=" ".join(map(str,part)),
                         gopel_cycles=monomial(G),rosenhain_cycles=monomial(R),
                         gopel_F1=fixed(G,1),rosenhain_F1=fixed(R,1),
                         gopel_F2=fixed(G,2),rosenhain_F2=fixed(R,2),
                         gopel_F3=fixed(G,3),rosenhain_F3=fixed(R,3)))
    by_profile=defaultdict(list)
    by_base=defaultdict(list)
    for row in data:
        by_profile[row['gopel_cycles'],row['rosenhain_cycles']].append(row['partition'])
        by_base[row['gopel_F1'],row['rosenhain_F1']].append(row['partition'])
    assert len(by_profile)==10 and len(by_base)==10
    expected=[['1 1 4','2 4']]
    assert [sorted(x) for x in by_profile.values() if len(x)>1]==expected
    assert [sorted(x) for x in by_base.values() if len(x)>1]==expected
    assert next(r for r in data if r['partition']=='1 1 2 2')['gopel_F1']==8
    assert next(r for r in data if r['partition']=='2 2 2')['gopel_F1']==16
    assert next(r for r in data if r['partition']=='3 3')['rosenhain_F1']==2
    assert next(r for r in data if r['partition']=='6')['gopel_F1']==1
    if outpath:
        with open(outpath,'w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    print('VERIFIED: 16 nodes, 35 planes, 60 Goepel and 80 Rosenhain tetrads; 720 S6 permutations; 11 cycle types; 10 joint spectra; unique collision 1 1 4 vs 2 4; base-field pair is complete for joint zeta functions')
if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else None)
