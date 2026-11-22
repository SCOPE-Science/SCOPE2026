#!/usr/bin/env python3
"""Independent orbit-and-set verifier for H(3,3) minimum power-domination geometry."""
from itertools import combinations,permutations,product
from collections import deque,Counter

vertices=tuple(product((0,1,2),repeat=3))
neighbor={x:{y for y in vertices if sum(a!=b for a,b in zip(x,y))==1} for x in vertices}

def process(selected):
    seen=set(selected)
    for q in selected: seen.update(neighbor[q])
    while True:
        found={next(iter(pending)) for p in seen if len(pending:=neighbor[p]-seen)==1}
        if not found: return len(seen),len(seen)==len(vertices)
        seen.update(found)

symmetries=[]
for coordinate_permutation in permutations((0,1,2)):
    for perm0,perm1,perm2 in product(permutations((0,1,2)),repeat=3):
        relabel=(perm0,perm1,perm2)
        symmetries.append({v:tuple(relabel[d][v[coordinate_permutation[d]]] for d in range(3)) for v in vertices})
assert len(symmetries)==1296

triples={frozenset(c) for c in combinations(vertices,3)}
classes=[]
while triples:
    sample=min(triples,key=lambda z:tuple(sorted(z)))
    orbit={frozenset(mapping[x] for x in sample) for mapping in symmetries}
    assert orbit<=triples
    triples.difference_update(orbit)
    good=process(sample)[1]
    for member in orbit:
        assert process(member)[1]==good
    ds=tuple(sorted(sum(a!=b for a,b in zip(x,y)) for x,y in combinations(sorted(sample),2)))
    classes.append((sample,len(orbit),ds,good,orbit))
assert len(classes)==10
assert Counter((ds,size,ok) for _,size,ds,ok,_ in classes)==Counter({
    ((1,1,1),27,False):1,((1,1,2),324,False):1,((1,2,2),324,False):1,
    ((1,2,3),648,False):1,((1,3,3),324,True):1,((2,2,2),54,False):1,
    ((2,2,2),216,False):1,((2,2,3),648,True):1,((2,3,3),324,True):1,
    ((3,3,3),36,False):1})

for a in vertices:
    assert not process({a})[1]
for a,b in combinations(vertices,2):
    assert not process({a,b})[1]

valid=set().union(*(orbit for _,_,_,yes,orbit in classes if yes))
assert len(valid)==1296
adj_jump={s:set() for s in valid};adj_slide={s:set() for s in valid}
for s in valid:
    for old in s:
        for new in vertices:
            if new in s:continue
            s2=frozenset((s-{old})|{new})
            if s2 in valid:
                adj_jump[s].add(s2)
                if new in neighbor[old]:adj_slide[s].add(s2)
assert sum(map(len,adj_jump.values()))//2==24300
assert sum(map(len,adj_slide.values()))//2==7290

def distances(source,graph):
    dist={source:0};queue=deque([source])
    while queue:
        s=queue.popleft()
        for t in graph[s]:
            if t not in dist:
                dist[t]=dist[s]+1
                queue.append(t)
    assert len(dist)==len(valid)
    return dist

# Orbit representatives suffice, since all transformations are preserved by the symmetries.
jump_pairs=Counter();slide_pairs=Counter();detours=Counter()
per_orbit={}
for representative,weight,signature,ok,orb in classes:
    if not ok:continue
    d1=distances(representative,adj_jump)
    d2=distances(representative,adj_slide)
    c1=Counter(d1.values());c2=Counter(d2.values())
    per_orbit[signature]=(weight,c1,c2)
    for dest in valid:
        if dest!=representative:
            jump_pairs[d1[dest]]+=weight
            slide_pairs[d2[dest]]+=weight
            detours[d2[dest]-d1[dest]]+=weight
    print('TYPE',signature,'SIZE',weight,'JUMP_SPHERES',dict(sorted(c1.items())),'SLIDE_SPHERES',dict(sorted(c2.items())))
# Directed distinct endpoints were counted; every unordered pair occurs twice.
assert all(value%2==0 for h in (jump_pairs,slide_pairs,detours) for value in h.values())
jump_pairs=Counter({k:v//2 for k,v in jump_pairs.items()})
slide_pairs=Counter({k:v//2 for k,v in slide_pairs.items()})
detours=Counter({k:v//2 for k,v in detours.items()})
assert jump_pairs=={1:24300,2:224208,3:590328,4:324}
assert slide_pairs=={1:7290,2:45360,3:170262,4:336960,5:244620,6:34668}
assert detours=={0:103356,1:370008,2:324648,3:41148}
assert per_orbit[(2,2,3)][1][4]==1
assert all(per_orbit[ds][1][4]==0 for ds in [(1,3,3),(2,3,3)])
print('SYMMETRY_OK 10 orbits 3 successful types 1296 optima; jump and slide connected; diameters 4,6; unique jump-antipodes for type 223; detours 0..3')
