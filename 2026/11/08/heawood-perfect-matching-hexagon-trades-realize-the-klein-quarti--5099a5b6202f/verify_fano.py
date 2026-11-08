#!/usr/bin/env python3
"""Independent permutation/Fano-plane verification of Heawood hexagon trades.
No imported graph routines; incidence comes from arithmetic in GF(8).
"""
from itertools import permutations, combinations
from collections import Counter

# The primitive root of X^3+X+1 realizes the Fano cyclic model.
a=1;powers=[]
for i in range(7):
    powers.append(a)
    a <<= 1
    if a&8:a^=0b1011
assert powers==[1,2,4,3,6,7,5] and a==1

# Lines are the distinct 3-element sets closed under binary vector addition.
triples=set()
for x,y in combinations(powers,2):
    triples.add(frozenset((x,y,x^y)))
assert len(triples)==7
line_sets=[frozenset((powers[j],powers[(j+1)%7],powers[(j+3)%7])) for j in range(7)]
assert set(line_sets)==triples
incident=[[powers[p] in line_sets[j] for j in range(7)] for p in range(7)]
assert all(sum(row)==3 for row in incident)

# An entirely different enumeration: test all 7! bijections, not all 3^7 choices.
S=[pi for pi in permutations(range(7)) if all(incident[p][pi[p]] for p in range(7))]
assert len(S)==24
V={s:i for i,s in enumerate(S)}

def dist(a,b): return sum(x!=y for x,y in zip(a,b))
# Girth six rules out four-cycle symmetric differences. So exactly 3
# displaced points is equivalent to one alternating six-cycle flip.
adj=[set() for _ in S]
for i,j in combinations(range(24),2):
    if dist(S[i],S[j])==3:
        adj[i].add(j);adj[j].add(i)
assert all(len(n)==7 for n in adj)
assert sum(map(len,adj))//2==84

# The Cayley-type complete metric is computed without a graph library.
def bfs(i, graph):
    layer={i:0};q=[i]
    for v in q:
        for w in graph[v]:
            if w not in layer:
                layer[w]=layer[v]+1;q.append(w)
    return layer
for i in range(24):
    dd=bfs(i,adj)
    assert Counter(dd.values())==Counter({0:1,1:7,2:14,3:2})
    for j in range(24):
        if dd[j]==0:continue
        k=dd[j]
        vals=Counter(dd[w]-k for w in adj[j])
        assert vals.get(-1,0)=={1:1,2:2,3:7}[k]
        assert vals.get(0,0)=={1:2,2:4,3:0}[k]
        assert vals.get(1,0)=={1:4,2:1,3:0}[k]

# Build 28 six-cycles directly as 28 noncollinear Fano point triples.
side={}
for p,q in combinations(range(7),2):
    line=[j for j in range(7) if incident[p][j] and incident[q][j]]
    assert len(line)==1
    side[p,q]=side[q,p]=line[0]
hexagons=[]
for p,q,r in combinations(range(7),3):
    if side[p,q]==side[q,r]:continue
    c=frozenset(((p,side[p,q]),(q,side[p,q]),
                 (q,side[q,r]),(r,side[q,r]),
                 (r,side[r,p]),(p,side[r,p])))
    hexagons.append(c)
assert len(hexagons)==28 and len(set(hexagons))==28
# Map matchings to Coxeter heptagons and check all 24 are different.
cx=[set() for _ in hexagons]
for i,j in combinations(range(28),2):
    points_i={p for p,l in hexagons[i]}; points_j={p for p,l in hexagons[j]}
    lines_i={l for p,l in hexagons[i]};lines_j={l for p,l in hexagons[j]}
    if not points_i&points_j and not lines_i&lines_j:
        cx[i].add(j);cx[j].add(i)
assert all(len(n)==3 for n in cx)
hepts=[]
for pi in S:
    m=frozenset(enumerate(pi))
    h=frozenset(k for k,c in enumerate(hexagons) if len(m&c)==3)
    assert len(h)==7 and all(len(cx[v]&h)==2 for v in h)
    hepts.append(h)
assert len(set(hepts))==24
for i,j in combinations(range(24),2):
    shared=hepts[i]&hepts[j]
    shared_edges=sum(len(cx[v]&shared) for v in shared)//2
    assert (j in adj[i])==(len(shared)==3 and shared_edges==2)

# Independently specify the seven toroidal faces by their translated
# explicit 6-cycles (one orientation per face).
faces=[]
for t in range(7):
    point_line=[(t,(t+4)%7),((t+4)%7,(t+4)%7),
                ((t+4)%7,(t+3)%7),((t+6)%7,(t+3)%7),
                ((t+6)%7,(t+6)%7),(t,(t+6)%7)]
    assert all(incident[p][j] for p,j in point_line)
    faces.append(frozenset(point_line))
assert len(set(faces))==7
all_edges={(p,j) for p in range(7) for j in range(7) if incident[p][j]}
assert all(sum(e in f for f in faces)==2 for e in all_edges)
radj=[set() for _ in S]
for i,j in combinations(range(24),2):
    d=frozenset((p,S[i][p]) for p in range(7) if S[i][p]!=S[j][p]) | frozenset(
        (p,S[j][p]) for p in range(7) if S[i][p]!=S[j][p])
    if d in faces:
        radj[i].add(j);radj[j].add(i)
assert sum(map(len,radj))//2==21
assert Counter(map(len,radj))==Counter({0:3,2:21})
seen=set();comps=[]
for i in range(24):
    if i not in seen:
        d=bfs(i,radj);seen.update(d);comps.append(set(d))
assert Counter(map(len,comps))==Counter({1:3,7:3})
# The three elementary translation matchings have constant edge direction.
shift=[tuple((p-t)%7 for p in range(7)) for t in (0,1,3)]
assert set(S[i] for i in range(24) if not radj[i])==set(shift)

def kind(pi):
    return tuple(sum((p-pi[p])%7==d for p in range(7)) for d in (0,1,3))
for c in comps:assert len({kind(S[i]) for i in c})==1
print('PASS independent 7!-permutation enumeration of 24 matchings')
print('PASS all-hexagon trades: 84 edges, Klein distance-regular intersection array')
print('PASS 28 GF(8) hexagons, Coxeter heptagons and shared-two-path criterion')
print('PASS facial trades: 3 K1 + 3 C7, with three pure direction matchings')
