#!/usr/bin/env python3
"""Independent finite verification of icosahedral erasure-safe identifying codes.
Only Python standard library is required. Scientific graph data are generated here.
"""
from itertools import combinations
from collections import Counter

V = tuple(range(12))
E = set()
def edge(a,b): E.add(tuple(sorted((a,b))))
for i in range(5):
    a, an = 1+i, 1+(i+1)%5
    b, bn, bp = 6+i, 6+(i+1)%5, 6+(i-1)%5
    for u,v in ((0,a),(11,b),(a,an),(b,bn),(a,b),(a,bp)):
        edge(u,v)
assert len(E)==30
N = {v:{v}|{b if a==v else a for a,b in E if v in (a,b)} for v in V}
assert all(len(N[v])==6 for v in V)

# Independent set-based definition: each remaining detector must dominate
# and distinguish vertices even after arbitrary erasures of up to t-1 detectors.
optima={}
for t in range(1,5):
    solutions=[]
    for k in range(13):
        candidates=[]
        for combo in combinations(V,k):
            S=set(combo)
            if (all(len(S & N[v])>=t for v in V) and
                all(len(S & (N[u]^N[v]))>=t for u,v in combinations(V,2))):
                candidates.append(frozenset(S))
        if candidates:
            solutions=candidates
            break
    optima[t]=solutions
    print(f'threshold {t}: minimum size={k}, number={len(solutions)}')
assert [(len(optima[t][0]),len(optima[t])) for t in range(1,5)] == [
    (5,120),(6,20),(11,12),(12,1)]
assert not any(all(len(set(combo)&N[v])>=5 for v in V) and
    all(len(set(combo)&(N[u]^N[v]))>=5 for u,v in combinations(V,2))
    for k in range(13) for combo in combinations(V,k))

# Every optimal single-erasure code is a triangle with one private external leaf
# at each triangle vertex, and every triangle yields one such code.
faces=[frozenset(t) for t in combinations(V,3) if all(tuple(sorted(e)) in E for e in combinations(t,2))]
assert len(faces)==20
suns=[]
for T in faces:
    leaves=[v for v in V if v not in T and len((N[v]-{v})&T)==1]
    assert len(leaves)==3
    assert {next(iter((N[v]-{v})&T)) for v in leaves}==T
    assert all(tuple(sorted((a,b))) not in E for a,b in combinations(leaves,2))
    suns.append(T|frozenset(leaves))
assert len(set(suns))==20 and set(suns)==set(optima[2])

# Every smallest ordinary code extends uniquely to a smallest one-erasure code.
for S in optima[1]:
    extensions=[T for T in optima[2] if S<T]
    assert len(extensions)==1
assert len({S for T in optima[2] for S in map(frozenset,combinations(T,5))})==120

# Antipodal pairs, distinguishing-block multiplicities and sharp all-vertex bound.
def dist(s):
    d={s:0};todo=[s]
    for u in todo:
        for v in N[u]-{u}:
            if v not in d: d[v]=d[u]+1;todo.append(v)
    return d
D={v:dist(v) for v in V}
P=sorted({tuple(sorted((v,next(w for w in V if D[v][w]==3)))) for v in V})
assert len(P)==6
assert all(sum(int(a in N[v])+int(b in N[v]) for a,b in P)==6 for v in V)
blocks=Counter(frozenset(N[a]^N[b]) for a,b in E)
assert len(blocks)==15 and set(blocks.values())=={2}
assert set(blocks)=={frozenset(p+q) for p,q in combinations(P,2)}
print('faces=20, one-erasure optima=20 three-suns; ordinary optima=120 uniquely extendible')
print('six antipodal pairs, 15 pair-union separators (each twice): PASS')
print('all checks PASS')
