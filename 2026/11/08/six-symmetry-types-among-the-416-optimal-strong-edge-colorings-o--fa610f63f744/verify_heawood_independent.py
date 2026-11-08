#!/usr/bin/env python3
"""Independent cyclic-Fano model, exact-cover and permutation checks (stdlib)."""
import itertools
points=tuple(range(7))
# Fano lines as the seven translates of the cyclic difference set {0,1,3}.
lines=[frozenset({i,(i+1)%7,(i+3)%7}) for i in points]
assert len(set(lines))==7 and all(len(x)==3 for x in lines)
# The Heawood graph has separate point and line nodes.
E=[(p,j) for j,line in enumerate(lines) for p in sorted(line)]
assert len(E)==21
edge_id={pair:i for i,pair in enumerate(E)}

def conflict(e,f):
    a,j=E[e]; b,k=E[f]
    return a==b or j==k or a in lines[k] or b in lines[j]

ind3=[frozenset(c) for c in itertools.combinations(range(21),3)
      if all(not conflict(i,j) for i,j in itertools.combinations(c,2))]
assert len(ind3)==84
assert not any(all(not conflict(i,j) for i,j in itertools.combinations(c,2))
               for c in itertools.combinations(range(21),4))
by_edge=[[] for _ in range(21)]
for c in ind3:
    for e in c: by_edge[e].append(c)
assert all(len(s)==12 for s in by_edge)
solutions=set()
def cover(rem,chosen):
    if not rem:
        solutions.add(tuple(sorted(chosen)))
        return
    e=min(rem)
    for c in by_edge[e]:
        if c <= rem: cover(rem-c,chosen+(tuple(sorted(c)),))
cover(frozenset(range(21)),())
assert len(solutions)==416

# An independent construction of all graph automorphisms: try all 7! point
# permutations, retain the 168 preserving the seven Fano lines, then compose
# with the explicit point-line duality p -> line[-p], j -> point[-j].
li={line:j for j,line in enumerate(lines)}
autos=[]
for f in itertools.permutations(points):
    transformed=[frozenset(f[p] for p in line) for line in lines]
    if not all(t in li for t in transformed): continue
    lineperm=[li[t] for t in transformed]
    keep=tuple(edge_id[(f[p],lineperm[j])] for p,j in E)
    dual=tuple(edge_id[((-lineperm[j])%7,(-f[p])%7)] for p,j in E)
    autos.extend((keep,dual))
assert len(set(autos))==336
assert all(all(conflict(e,f)==conflict(a[e],a[f]) for e,f in itertools.combinations(range(21),2)) for a in autos)
seen=set(); sizes=[]
for sol in sorted(solutions):
    if sol in seen: continue
    orbit={tuple(sorted(tuple(sorted(a[e] for e in grp)) for grp in sol)) for a in autos}
    assert orbit<=solutions
    seen.update(orbit)
    sizes.append(len(orbit))
assert sorted(sizes)==[8,16,56,112,112,112] and len(seen)==416
print('independent cyclic-Fano model: edges=21, induced triples=84, induced quadruples=0')
print('seven-color partitions=',len(solutions),'full automorphisms=',len(autos),'orbit sizes=',sorted(sizes))
