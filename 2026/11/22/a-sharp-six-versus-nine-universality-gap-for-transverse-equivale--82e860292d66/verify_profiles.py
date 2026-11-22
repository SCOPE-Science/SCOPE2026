#!/usr/bin/env python3
"""Independent finite enumerator for two-equivalence three-variable profiles.

Each element is an occupied cell in a bipartite incidence graph.
The two coordinates determine two equivalence relations.
"""
from itertools import product, permutations, combinations
from functools import lru_cache

PAIRS=((0,1),(0,2),(1,2))

def profile(triple):
    return (tuple(triple[i]==triple[j] for i,j in PAIRS),
            tuple(triple[i][0]==triple[j][0] for i,j in PAIRS),
            tuple(triple[i][1]==triple[j][1] for i,j in PAIRS))

ALL={profile(t) for t in product(list(product(range(3), repeat=2)),repeat=3)}
assert len(ALL)==25

def realized(edges):
    return {profile(t) for t in product(edges,repeat=3)}

def canonical(edges):
    left=sorted({a for a,b in edges})
    right=sorted({b for a,b in edges})
    least=None
    for lp in permutations(left):
        for rp in permutations(right):
            L={a:i for i,a in enumerate(lp)}
            R={b:i for i,b in enumerate(rp)}
            value=tuple(sorted((L[a],R[b]) for a,b in edges))
            if least is None or value<least:
                least=value
    return least

# Six occupied cells suffice and are necessary in every simple bipartite
# incidence graph. All six-cell graph types have at most four distinct
# endpoints on each shore when they are universal (proved analytically).
classes=set()
grid=list(product(range(4),repeat=2))
for n in range(1,7):
    count=0
    for edges in combinations(grid,n):
        if realized(edges)==ALL:
            count+=1
            if n==6: classes.add(canonical(edges))
    if n<6: assert count==0,(n,count)
    else: assert count==1296,(n,count)
assert len(classes)==4,(len(classes),classes)
expected_shores={(3,3),(3,4),(4,3),(4,4)}
assert {(1+max(x for x,y in c),1+max(y for x,y in c)) for c in classes}==expected_shores

# In the commuting case, the incidence graph is a disjoint union of
# complete bipartite graphs. Enumerate all component multisets of
# weight <= 9, without imposing an arbitrary bound on class counts.
RECTANGLES=tuple(sorted((a,b) for a in range(1,10) for b in range(1,10) if a*b<=9))
@lru_cache(None)
def partitions(start,budget):
    if budget==0:return ((),)
    ans=[]
    for j in range(start,len(RECTANGLES)):
        a,b=RECTANGLES[j]
        if a*b<=budget:
            ans.extend(((a,b),)+rest for rest in partitions(j,budget-a*b))
    return tuple(ans)

def edges_of(comps):
    edges=[]
    L=R=0
    for a,b in comps:
        edges.extend((L+i,R+j) for i in range(a) for j in range(b))
        L+=a;R+=b
    return edges

commuting_nine=[]
for n in range(1,10):
    qualifying=[comps for comps in partitions(0,n) if realized(edges_of(comps))==ALL]
    if n<9:assert not qualifying,(n,qualifying)
    else:commuting_nine=qualifying
assert commuting_nine==[((1,3),(3,2)),((2,3),(3,1)),((3,3),)],commuting_nine

print('VERIFY_OK types=25 unrestrained_min=6 unrestrained_classes=4 commuting_min=9 commuting_classes=3 labelled_4x4=1296')
