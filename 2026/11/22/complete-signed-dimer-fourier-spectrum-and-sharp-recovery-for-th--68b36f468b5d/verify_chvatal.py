#!/usr/bin/env python3
"""Exact matching-incidence Walsh checker for the Chvatal graph. Python 3 stdlib only."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

EDGES = (
(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),
(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),
(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))
N=12; M=len(EDGES); SIZE=1<<N
ADJ = [[] for _ in range(N)]
for i, (u,v) in enumerate(EDGES):
    ADJ[u].append((v,i));ADJ[v].append((u,i))
assert M==24 and all(len(a)==4 for a in ADJ)
assert not any(len({u,v,w})==3 and (v in {z for z,_ in ADJ[u]}) and
               (w in {z for z,_ in ADJ[u]}) and
               (w in {z for z,_ in ADJ[v]})
               for u in range(N) for v in range(u+1,N) for w in range(v+1,N))

def k_colorable(k):
    color=[-1]*N
    order=sorted(range(N), key=lambda u:(-len(ADJ[u]),u))
    def visit(j):
        if j==N:return True
        u=order[j]
        used={color[v] for v,_ in ADJ[u] if color[v]>=0}
        for c in range(k):
            if c not in used:
                color[u]=c
                if visit(j+1):return True
        color[u]=-1
        return False
    return visit(0)
assert not k_colorable(3) and k_colorable(4)

def all_matchings(remaining):
    if remaining==0:
        yield 0
        return
    v=(remaining & -remaining).bit_length()-1
    rest=remaining^(1<<v)
    for w,e in ADJ[v]:
        if (rest>>w)&1:
            for tail in all_matchings(rest^(1<<w)):
                yield tail | (1<<e)

MATCHINGS=tuple(all_matchings(SIZE-1))
assert len(MATCHINGS)==52 and len(set(MATCHINGS))==52
assert all(m.bit_count()==6 for m in MATCHINGS)
assert all(sum((mask>>e)&1 for mask in MATCHINGS) in (12,14) for e in range(M))
assert sum(sum((mask>>e)&1 for mask in MATCHINGS) for e in range(M))==52*6

# Fix a canonical BFS spanning tree with increasing edge-index order.
used={0}; tree=set()
while len(used)<N:
    incoming = next((e,u,v) for e,(u,v) in enumerate(EDGES)
                    if (u in used)^(v in used))
    e,u,v=incoming;tree.add(e);used.add(u);used.add(v)
assert len(tree)==N-1
C=tuple(e for e in range(M) if e not in tree)
R=len(C);Q=1<<R
assert R==13 and Q==8192

def fwt(a):
    a=list(a)
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

reduced=[sum(((mask>>e)&1)<<j for j,e in enumerate(C)) for mask in MATCHINGS]
pop=Counter(reduced)
multipliers=fwt([pop.get(i,0) for i in range(Q)])
expected={0:2536,4:2864,8:1708,12:574,16:304,20:120,24:52,28:24,32:8,52:2}
assert dict(Counter(map(abs,multipliers)))==expected

# Independent calculation: signed matching recursion for each assignment,
# without using the matching list or its Fourier transform.
@lru_cache(maxsize=None)
def dp(remaining, signing):
    if not remaining: return 1
    u=(remaining&-remaining).bit_length()-1
    rem=remaining^(1<<u)
    total=0
    for v,e in ADJ[u]:
        if (rem>>v)&1:
            sign=-1 if (signing>>e)&1 else 1
            total+=sign*dp(rem^(1<<v),signing)
    return total

for s in range(Q):
    signature=sum(((s>>j)&1)<<e for j,e in enumerate(C))
    assert multipliers[s]==dp(SIZE-1,signature), ('dp',s)
    dp.cache_clear()

edge_count=[sum((x>>e)&1 for x in MATCHINGS) for e in range(M)]
assert Counter(edge_count)=={12:12,14:12}
for v in range(N):
    assert sorted(edge_count[e] for _,e in ADJ[v])==[12,12,14,14]
zeros=[]
for e,f in combinations(range(M),2):
    co=sum(((mask>>e)&1)*((mask>>f)&1) for mask in MATCHINGS)
    val=52-2*edge_count[e]-2*edge_count[f]+4*co
    adjacent=bool(set(EDGES[e]) & set(EDGES[f]))
    if not adjacent and edge_count[e]!=edge_count[f]: assert co>=2
    if not adjacent and edge_count[e]==edge_count[f]==14: assert co>=3
    if not val:zeros.append((e,f))
    assert (val==0)==(adjacent and edge_count[e]!=edge_count[f])
assert len(zeros)==48
assert all(52-2*c for c in edge_count)

support=[int(x!=0) for x in multipliers]
inverse=fwt(support)
assert sum(abs(z) for z in inverse)==162144
assert Fraction(sum(abs(z) for z in inverse),Q)==Fraction(5067,256)
assert Q-len([x for x in multipliers if x])==2536
assert sum(expected.values())==Q
assert 5656*2048==11583488
assert 2536*2048==5193728
print('PASS: matching count, two independent signed spectra, low-degree cancellation, projection norm')
print('spectrum', sorted(expected.items()))
print('projection',Fraction(5067,256),'full rank',5656*2048,'nullity',2536*2048)
