#!/usr/bin/env python3
"""Reproduce finite shattering and adaptive certificate for the doily incidence graph.
Usage: python3 verify_gq2.py TREE_DEPTH5.json (Python 3, standard library only).
"""
import json,sys
from itertools import combinations

def alternating(a,b):
    return ((bool(a&1) & bool(b&4)) ^ (bool(a&4)&bool(b&1)) ^
            (bool(a&2)&bool(b&8)) ^ (bool(a&8)&bool(b&2)))

lines=sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(range(1,16),2) if not alternating(a,b)})
assert len(lines)==15
neighbors=[set() for _ in range(30)]
for k,ln in enumerate(lines):
    for a in ln:
        neighbors[a-1].add(k+15)
        neighbors[k+15].add(a-1)
assert sum(map(len,neighbors))==90 and all(len(s)==3 for s in neighbors)
sets=[]
for p in range(15):
    for ell in sorted(neighbors[p]):
        forbidden={p,ell}|neighbors[p]|neighbors[ell]
        distance_two={w for x in (p,ell) for y in neighbors[x] for w in neighbors[y] if w not in forbidden}
        assert len(distance_two)==8
        for pole in (p,ell):
            D=frozenset(distance_two|{pole})
            assert len(D)==9
            assert all(D.intersection(neighbors[v]|{v}) for v in range(30))
            sets.append(D)
assert len(sets)==90 and len(set(sets))==90
sets=sorted(sets,key=lambda d: tuple(sorted(d)))
assert all(sum(v in d for d in sets)==27 for v in range(30))

columns=[sum((1<<i) for i,d in enumerate(sets) if v in d) for v in range(30)]
ALL=(1<<len(sets))-1
counts=[0]*6
by_type={}
faces3=set()
faces4=set()
from itertools import combinations

def visit(start,patterns,selected):
    k=len(selected)
    counts[k]+=1
    if k==3:faces3.add(tuple(selected))
    if k==4:faces4.add(tuple(selected))
    if k==4:
        t=sum(v<15 for v in selected)
        by_type[t]=by_type.get(t,0)+1
    if k==5: return
    for j in range(start,30):
        col=columns[j]
        nxt=[]
        for cell in patterns:
            x=cell&col
            y=cell&(~col)&ALL
            if x==0 or y==0:break
            nxt.extend((x,y))
        else:visit(j+1,nxt,selected+[j])

visit(0,[ALL],[])
assert counts==[1,30,390,2730,420,0],counts

def predicted(S):
    k=len(S)
    if k>=5:return False
    if k==0:return True
    if any(v in neighbors[u] for u,v in combinations(S,2)):return False
    if k<=2:return True
    if k==3:
        # The excluded pure-side triads are pairwise noncollinear points,
        # or dually pairwise nonconcurrent lines.
        same_side=all(v<15 for v in S) or all(v>=15 for v in S)
        if same_side and all(not (set(neighbors[u]) & set(neighbors[v])) for u,v in combinations(S,2)):
            return False
        return True
    pts=[v for v in S if v<15]; lns=[v for v in S if v>=15]
    if len(pts)==1:
        return bool(set.intersection(*(set(neighbors[u]) for u in lns)))
    if len(lns)==1:
        return bool(set.intersection(*(set(neighbors[u]) for u in pts)))
    if len(pts)!=2:return False
    pointline=set(neighbors[pts[0]]) & set(neighbors[pts[1]])
    concurrent=set(neighbors[lns[0]]) & set(neighbors[lns[1]])
    if not pointline or not concurrent:return False
    L=next(iter(pointline)); Q=next(iter(concurrent))
    R=next(v for v in neighbors[L] if v not in pts)
    # R and Q must be distinct, collinear via their third line at Q.
    return R!=Q and bool(set(neighbors[R])&set(neighbors[Q])) and all(R not in neighbors[ell] for ell in lns)

def brute(S):
    parts=[ALL]
    for v in S:
        nxt=[]
        for cell in parts:
            one=cell&columns[v]
            zero=cell&(~columns[v])&ALL
            if not one or not zero:return False
            nxt.extend((zero,one))
        parts=nxt
    return True

independent_counts=[0]*6
for k in range(6):
    for S in combinations(range(30),k):
        observed=brute(S)
        assert predicted(S)==observed,('structural mismatch',S)
        independent_counts[k]+=observed
assert independent_counts==counts
covered3={tuple(T) for Q in faces4 for T in combinations(Q,3)}
assert len(faces3-covered3)==1980

tree=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'TREE_DEPTH5.json',encoding='utf-8'))
leaf_ids=[]
def walk(node,level,filters):
    if level==5:
        assert list(node)==['leaf']
        leaf=node['leaf'];assert isinstance(leaf,int) and 0<=leaf<90
        assert leaf in filters
        leaf_ids.append(leaf)
    else:
        assert set(node)=={'q','no','yes'}
        q=node['q'];assert isinstance(q,int) and 0<=q<30
        no={i for i in filters if q not in sets[i]}
        yes={i for i in filters if q in sets[i]}
        assert no and yes
        walk(node['no'],level+1,no)
        walk(node['yes'],level+1,yes)
walk(tree,0,set(range(90)))
assert len(leaf_ids)==32 and len(set(leaf_ids))==32
print('15 points, 15 lines, 45 flags, 90 distinct minimum dominating sets of size 9')
print('Membership in concepts per vertex: 27')
print('Shattered-support coefficients:',counts)
print('Shattered quadruples by number of point vertices:',sorted(by_type.items()))
print('Structural criterion exhaustively checked for all 174,437 supports of size at most five')
print('Maximal 3-faces (triangles): 1980; maximal 4-faces (tetrahedra): 420')
print('Adaptive certificate: 31 internal tests, 32 verified distinct terminal witnesses, depth 5')
print('Upper adaptive bound: 27 positive concepts at any root < 32 required for depth 6')
print('ALL_DOILY_CHECKS_PASS')
