"""Exact independent combinatorial count for Frobenius-invariant negative supports.
Uses finite graph restrictions, rather than the intersection-matrix determinant.
Python 3 standard library only.
"""
from itertools import combinations, permutations
from collections import Counter
from math import factorial
V=tuple(range(4))
EDGES=tuple(combinations(V,2))
MATCHINGS=( ((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2)) )

# First 4 indices are strict transforms of the original four lines;
# next 6 are exceptional divisors of pairwise intersection points;
# last 3 are opposite-pair diagonals.

def admissible_supports():
    found=set()
    for g in range(1<<6):
        chosen={EDGES[i] for i in range(6) if g>>i&1}
        deg=[sum(v in e for e in chosen) for v in V]
        permitted=[j for j in range(4) if deg[j]<=1]
        usable=[None]+[k for k,m in enumerate(MATCHINGS)
                       if not any(e in chosen for e in m)]
        for w in range(1<<len(permitted)):
            selected={permitted[i] for i in range(len(permitted)) if w>>i&1}
            if any(deg[u]==1 and deg[v]==1 and u in selected and v in selected
                   for u,v in chosen):
                continue
            base = sum(1<<i for i in selected) + (g<<4)
            for r in usable:
                mask=base if r is None else base|(1<<(10+r))
                assert mask not in found
                found.add(mask)
    return found

def cycle_type(p):
    visited=set();parts=[]
    for i in V:
        if i in visited: continue
        j=i; n=0
        while j not in visited:
            visited.add(j);n+=1;j=p[j]
        parts.append(n)
    return tuple(sorted(parts,reverse=True))

def action(p):
    image=[]
    image += list(p)
    image += [4+EDGES.index(tuple(sorted((p[i],p[j])))) for i,j in EDGES]
    image += [10+MATCHINGS.index(tuple(sorted(tuple(sorted(p[i] for i in e)) for e in m)))
              for m in MATCHINGS]
    assert sorted(image)==list(range(13))
    return image

def transform(mask,a):
    return sum(1<<a[i] for i in range(13) if mask&(1<<i))

supports=admissible_supports()
assert len(supports)==726, len(supports)
expected_polys={
 (1,1,1,1):(1,13,69,186,260,168,29),
 (2,1,1):(1,5,11,16,16,12,5),
 (2,2):(1,5,9,18,16,20,5),
 (3,1):(1,1,0,3,2,0,2),
 (4,):(1,1,1,0,2,2,1)
}
classes={}
for p in permutations(V):
    t=cycle_type(p);a=action(p)
    poly=tuple(sum(1 for mask in supports if mask.bit_count()==k and transform(mask,a)==mask)
               for k in range(7))
    assert poly==expected_polys[t],(t,p,poly)
    if t not in classes: classes[t]=[0,poly]
    assert classes[t][1]==poly
    classes[t][0]+=1
assert {k:v[0] for k,v in classes.items()}=={
    (1,1,1,1):1,(2,1,1):6,(2,2):3,(3,1):8,(4,):6}
# Two independent orbit counts: direct breadth-first and Burnside.
ans=sum(mult*sum(poly) for mult,poly in classes.values())//factorial(4)
assert sum(mult*sum(poly) for mult,poly in classes.values())%factorial(4)==0
seen=set();sizes=Counter()
for root in sorted(supports):
    if root in seen:continue
    block={transform(root,action(p)) for p in permutations(V)}
    assert block <= supports
    seen.update(block);sizes[len(block)]+=1
assert len(seen)==726 and sum(sizes.values())==ans==61
assert sizes=={1:3,3:5,4:6,6:6,12:28,24:13}
for kind in sorted(classes,reverse=True):
    mult,poly=classes[kind]
    print(f'{kind}: class_size={mult}, fixed={sum(poly)}, coefficients={poly}')
print('S4_CHAMBER_ORBITS',ans,'ORBIT_LENGTHS',dict(sorted(sizes.items())))
print('CAYLEY_CHAMBERS_GRAPH_INDEPENDENT_OK')
