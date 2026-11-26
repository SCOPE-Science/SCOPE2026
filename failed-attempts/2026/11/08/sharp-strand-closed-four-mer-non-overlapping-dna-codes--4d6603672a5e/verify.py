#!/usr/bin/env python3
"""Independent recursive weighted-clique census for strand-symmetric length-four non-overlapping DNA codes."""
from itertools import product, permutations
from collections import Counter
import json
from pathlib import Path
A4=range(4)
bar=(1,0,3,2)
def rho(w): return tuple(bar[x] for x in reversed(w))
def no_overlap(u,v):
    return all(u[:k] != v[-k:] and v[:k] != u[-k:] for k in (1,2,3))
def make_case(starts):
    A=set(starts)
    B={bar[x] for x in A}
    words=[w for w in product(A4,repeat=4) if w[0] in A and w[-1] in B]
    assert all(rho(w) in words for w in words)
    orbits=sorted({frozenset((w,rho(w))) for w in words},key=lambda X:tuple(sorted(X)))
    orbits=[O for O in orbits if all(no_overlap(x,y) for x in O for y in O)]
    n=len(orbits)
    edges=[0]*n
    for i in range(n):
        for j in range(i):
            if any(not no_overlap(x,y) for x in orbits[i] for y in orbits[j]):
                edges[i] |= 1<<j
                edges[j] |= 1<<i
    best=0
    maximizers=[]
    def search(available,chosen,weight):
        nonlocal best,maximizers
        if weight + sum(len(orbits[i]) for i in range(n) if available>>i&1) < best:
            return
        if available==0:
            if weight>best: best,maximizers=weight,[chosen]
            elif weight==best: maximizers.append(chosen)
            return
        pivot=max((i for i in range(n) if available>>i&1),key=lambda j:(edges[j]&available).bit_count())
        search(available & ~((1<<pivot)|edges[pivot]), chosen|(1<<pivot), weight+len(orbits[pivot]))
        search(available & ~(1<<pivot),chosen,weight)
    search((1<<n)-1,0,0)
    codes=[frozenset().union(*(O for i,O in enumerate(orbits) if mask>>i&1)) for mask in maximizers]
    assert len(codes)==len(set(codes))
    assert all(all(no_overlap(x,y) for x in C for y in C) and {rho(x) for x in C}==set(C) for C in codes)
    return orbits, edges, best, codes, maximizers
small=make_case((0,))
large=make_case((0,2))
assert (len(small[0]),small[2],len(small[3])) == (6,7,2)
assert (len(large[0]),large[2],len(large[3])) == (20,17,8)
# all complementary-pair preserving relabelings form order-8 group
perms=[p for p in permutations(A4) if all(p[bar[i]]==bar[p[i]] for i in A4)]
assert len(perms)==8
all_codes={frozenset(tuple(p[i] for i in w) for w in C) for p in perms for C in large[3]}
assert len(all_codes)==32
remaining=set(all_codes);symmetry_classes=[]
while remaining:
    rep=min(remaining,key=lambda C:tuple(sorted(C)))
    orb={frozenset(tuple(p[i] for i in w) for w in rep) for p in perms}
    assert orb <= remaining
    symmetry_classes.append((len(orb),rep))
    remaining-=orb
assert Counter(x for x,_ in symmetry_classes)=={8:4}
# Optional embedded certificate check.
cert_path=Path(__file__).resolve().parent/'certificate.json'
if cert_path.exists():
    cert=json.loads(cert_path.read_text('utf-8'))
    def fmt(C): return sorted(''.join(map(str,w)) for w in C)
    assert cert['small']['n_orbits']==len(small[0])
    assert cert['small']['optimum']==small[2]
    assert cert['small']['num_maximizers']==len(small[3])
    assert cert['large']['n_orbits']==len(large[0])
    assert cert['large']['optimum']==large[2]
    assert cert['large']['num_maximizers']==len(large[3])
    assert cert['large']['orbits']==[sorted(fmt(O)) for O in large[0]]
    assert cert['large']['adjacency']==large[1]
    assert cert['large']['representative_maximizers']==sorted([fmt(C) for C in large[3]])
    assert cert['symmetry_class_representatives']==sorted([fmt(C) for _,C in symmetry_classes])
print('VERIFY_OK small=7/2 large=17/8 global=32 classes=4x8')
