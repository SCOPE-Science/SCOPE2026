#!/usr/bin/env python3
"""Exact finite-state majority dynamics, using a pole-and-two-rings icosahedron.
Standard library only. Run: python3 check_finite.py
All 4096 binary configurations are enumerated, with complete functional-graph search.
"""
from collections import Counter
from math import comb

N = 12
edges = set()
def add(u,v):
    assert u!=v
    edges.add(tuple(sorted((u,v))))
for i in range(5):
    a,b=1+i,6+i
    add(0,a); add(11,b)
    add(a,1+(i+1)%5); add(b,6+(i+1)%5)
    add(a,b);add(a,6+(i-1)%5)
assert len(edges)==30
neighbors=[set() for _ in range(N)]
for u,v in edges: neighbors[u].add(v);neighbors[v].add(u)
assert [len(k) for k in neighbors]==[5]*N
mask=[sum(1<<j for j in ns) for ns in neighbors]

def step(x):
    return sum((1<<i) for i in range(N) if (mask[i]&x).bit_count()>=3)
F=tuple(map(step,range(1<<N)))
fixed=set(x for x in range(1<<N) if F[x]==x)
recurrent={x for x in range(1<<N) if F[F[x]]==x}
cycles={tuple(sorted((x,F[x]))) for x in recurrent if F[x]!=x}
assert len(fixed)==14 and len(cycles)==156 and len(recurrent)==326
# Finite certificate of the sharp global entry bound and eventual period two.
def iterate(x,t):
    for _ in range(t): x=F[x]
    return x
assert all(iterate(x,7)==iterate(x,5) for x in range(1<<N))

entry={} ; destiny={}
for x in range(1<<N):
    y=x; t=0
    while y not in recurrent:
        y=F[y];t+=1
        assert t<=5
    entry[x]=t
    destiny[x]=(y,) if F[y]==y else tuple(sorted((y,F[y])))

B=Counter(destiny.values())
E=Counter(entry.values())
assert sum(B.values())==1<<N
assert E=={0:326,1:986,2:984,3:1080,4:480,5:240},E
assert Counter(B.values())=={1:12,2:16,4:60,6:60,14:20,1586:2}
cap={sum(1<<j for j in ({i}|neighbors[i])) for i in range(N)}
assert fixed==cap|{0,(1<<N)-1},(len(cap), len(fixed))
assert all(B[(x,)]==1 for x in cap)
assert all(sum(F[y]==x for y in range(1<<N))==1 for x in cap)
assert B[(0,)]==B[((1<<N)-1,) ]==1586
# Hamming weight profiles for attraction class and recurrent classes.
profile=tuple(tuple(sum(1 for x in range(1<<N)
    if x.bit_count()==k and (len(destiny[x])==j))
    for j in (1,2)) for k in range(13))
assert profile==((1,0),(12,0),(66,0),(220,0),(495,0),
    (732,60),(132,792),(732,60),(495,0),(220,0),(66,0),(12,0),(1,0))
wcycles=Counter(tuple(sorted((x.bit_count(),y.bit_count()))) for x,y in cycles)
assert wcycles=={(5,5):30,(6,6):96,(7,7):30}
print('MODEL vertices=12 edges=30 degree=5 initial_states=4096')
print('FIXED',len(fixed),'PRIMITIVE_TWO_CYCLES',len(cycles),'PERIODIC_STATES',len(recurrent))
print('CAPS',len(cap),'ISOLATED_CAP_BASINS',12,'CONSENSUS_BASIN_EACH',1586)
print('ENTRY_TIME_HISTOGRAM',sorted(E.items()))
print('BASIN_SIZE_HISTOGRAM',sorted(Counter(B.values()).items()))
print('TWO_CYCLE_WEIGHTS',sorted(wcycles.items()))
print('INITIAL_WEIGHT_BY_EVENTUAL_PERIOD',list(enumerate(profile)))
print('CHECK F^7=F^5 FOR ALL 4096: PASS')
