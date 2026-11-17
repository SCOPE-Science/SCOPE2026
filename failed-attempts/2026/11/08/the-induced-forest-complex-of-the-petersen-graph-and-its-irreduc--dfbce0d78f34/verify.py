#!/usr/bin/env python3
"""Exact finite checks for the induced-forest complex of KG(5,2)."""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque
from fractions import Fraction

V=list(combinations(range(5),2))
E=[(i,j) for i in range(10) for j in range(i+1,10) if set(V[i]).isdisjoint(V[j])]
assert len(E)==15

def forest_dsu(mask):
    parent=list(range(10))
    def root(u):
        while parent[u]!=u:
            u=parent[u]
        return u
    for u,v in E:
        if mask>>u&1 and mask>>v&1:
            a,b=root(u),root(v)
            if a==b:return False
            parent[a]=b
    return True

def forest_dfs(mask):
    nbr=[[] for _ in range(10)]
    for u,v in E:
        if mask>>u&1 and mask>>v&1:
            nbr[u].append(v);nbr[v].append(u)
    seen=set()
    def walk(u,parent):
        seen.add(u)
        for w in nbr[u]:
            if w==parent:continue
            if w in seen or not walk(w,u):return False
        return True
    for u in range(10):
        if mask>>u&1 and u not in seen and not walk(u,-1):return False
    return True

all_faces={m for m in range(1<<10) if forest_dsu(m)}
assert all(forest_dsu(m)==forest_dfs(m) for m in range(1<<10))
assert len(all_faces)==786
assert [sum(m.bit_count()==k for m in all_faces) for k in range(1,11)]==[10,45,120,210,240,140,20,0,0,0]

remaining=all_faces-{0}
matching=[]
for v in range(10):
    pairs=[(m,m|(1<<v)) for m in sorted(remaining) if not m>>v&1 and m|(1<<v) in remaining]
    for a,b in pairs:
        assert a in remaining and b in remaining and b.bit_count()==a.bit_count()+1
        remaining.remove(a);remaining.remove(b)
    matching.extend(pairs)
critical=sorted(remaining)
assert len(matching)==389 and critical==[1,946,948,952,978,980,984]
matchset=set(matching)
nonzero=all_faces-{0}
adj={m:[] for m in nonzero};indeg={m:0 for m in nonzero};covers=0
for high in nonzero:
    for v in range(10):
        if high>>v&1:
            low=high^(1<<v)
            if not low:continue
            assert low in nonzero
            covers+=1
            source,target=(low,high) if (low,high) in matchset else (high,low)
            adj[source].append(target);indeg[target]+=1
assert covers==3470
front=deque(m for m in indeg if not indeg[m]);sorted_count=0
while front:
    m=front.popleft();sorted_count+=1
    for dest in adj[m]:
        indeg[dest]-=1
        if indeg[dest]==0:front.append(dest)
assert sorted_count==len(nonzero)==785
assert Counter(m.bit_count()-1 for m in critical)=={0:1,5:6}

# Independent mod-two reduced boundary calculation: exact bitset Gaussian elimination.
faces_by_size={k:sorted(m for m in nonzero if m.bit_count()==k) for k in range(1,8)}
ranks={}
for k in range(2,8):
    previous={m:j for j,m in enumerate(faces_by_size[k-1])}
    piv={}
    for m in faces_by_size[k]:
        c=0
        for v in range(10):
            if m>>v&1:c^=1<<previous[m^(1<<v)]
        while c:
            p=c.bit_length()-1
            if p in piv:c^=piv[p]
            else:piv[p]=c;break
    ranks[k]=len(piv)
betti={k-1:len(faces_by_size[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(1,8)}
betti[0]-=1
assert betti=={0:0,1:0,2:0,3:0,4:0,5:6,6:0}

# All 120 automorphisms: trace on oriented faces, corrected for augmentation.
classes=defaultdict(set)
def class_type(p):
    seen=set();out=[]
    for i in range(5):
        if i in seen:continue
        j=i;k=0
        while j not in seen:
            seen.add(j);k+=1;j=p[j]
        out.append(k)
    return tuple(sorted(out,reverse=True))
def face_action(p):
    mapping=[V.index(tuple(sorted((p[a],p[b])))) for a,b in V]
    lefs=0
    for m in nonzero:
        inds=[i for i in range(10) if m>>i&1]
        ims=[mapping[i] for i in inds]
        if sum(1<<j for j in ims)!=m:continue
        inversions=sum(ims[a]>ims[b] for a in range(len(ims)) for b in range(a+1,len(ims)))
        lefs+=(-1)**(len(inds)-1+inversions)
    return -(lefs-1)  # degree 5: L_reduced = -trace H5
for p in permutations(range(5)):
    typ=class_type(p)
    val=face_action(p)
    fixed=sum(p[i]==i for i in range(5))
    pp=tuple(p[p[i]] for i in range(5))
    fixedsq=sum(pp[i]==i for i in range(5))
    exterior=((fixed-1)**2-(fixedsq-1))//2
    assert val==exterior,(typ,val,exterior)
    classes[typ].add(val)
assert len(classes)==7 and all(len(v)==1 for v in classes.values())
expected={(1,1,1,1,1):6,(2,1,1,1):0,(2,2,1):-2,(3,1,1):0,(3,2):0,(4,1):0,(5,):1}
assert {k:next(iter(v)) for k,v in classes.items()}==expected
# Character inner product over S5 is one; hence irreducible.
from math import factorial
inner=Fraction(0,1)
for typ,x in expected.items():
    z=1
    for cyc,multiplicity in Counter(typ).items():z*=cyc**multiplicity*factorial(multiplicity)
    inner+=Fraction(x*x,z)
assert inner==1
print('GRAPH_VERTICES=10 GRAPH_EDGES=15')
print('FACE_VECTOR=(10,45,120,210,240,140,20) TOTAL_NONEMPTY=785')
print('MORSE_PAIRS=389 CRITICAL_0=1 CRITICAL_5=6 COVERING_RELATIONS=3470 DAG_VERTICES=785')
print('INDEPENDENT_MOD2_BETTI_5=6 ALL_OTHER_REDUCED_BETTI=0')
print('S5_CLASS_ORDER=identity,2,2+2,3,3+2,4,5')
print('S5_CHARACTER='+str([expected[t] for t in [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]]))
print('S5_CHARACTER_NORM=1, EXTERIOR_SQUARE_STANDARD_MATCH=120/120')
print('INDUCED_FOREST_CERTIFICATE_PASS')
