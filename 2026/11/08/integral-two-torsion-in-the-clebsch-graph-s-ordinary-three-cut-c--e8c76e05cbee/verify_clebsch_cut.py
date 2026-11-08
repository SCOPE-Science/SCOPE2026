#!/usr/bin/env python3
"""Reproduce an integral Morse certificate for the ordinary 3-cut complex
of the 5-regular Clebsch graph, and independent dual field ranks.
Python 3.10+, standard library only; uses exact integer arithmetic.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import gcd

N=16
V=tuple(v for v in range(32) if v.bit_count()%2==0)
ALL=(1<<N)-1
EDGE={(i,j) for i,j in combinations(range(N),2) if (V[i]^V[j]).bit_count()==4}
NEIGH=[0]*N
for i,j in EDGE:
    NEIGH[i]|=1<<j
    NEIGH[j]|=1<<i
assert len(EDGE)==40 and all(a.bit_count()==5 for a in NEIGH)
TRIPLES=[]
for a,b,c in combinations(range(N),3):
    e=((NEIGH[a]>>b)&1)+((NEIGH[a]>>c)&1)+((NEIGH[b]>>c)&1)
    TRIPLES.append(((1<<a)|(1<<b)|(1<<c), e))
CONNECT=tuple(s for s,e in TRIPLES if e>=2)
DISCONNECT=tuple(s for s,e in TRIPLES if e<2)
assert (len(CONNECT),len(DISCONNECT))==(160,400)

# Generate the full face set by downward closure of the 400 facets.
MEMBER=bytearray(1<<N)
for t in DISCONNECT:
    top=ALL^t
    s=top
    while s:
        MEMBER[s]=1
        s=(s-1)&top
    MEMBER[0]=1
FACES=[s for s in range(1<<N) if MEMBER[s]]
assert len(FACES)==65199
assert all(MEMBER[s]==any((t & (ALL^s))==t for t in DISCONNECT)
           for s in range(1<<N))  # independent facet membership rule
FC=Counter(s.bit_count()-1 for s in FACES if s)
expected=(16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1780,400)
assert tuple(FC[i] for i in range(13))==expected

# Staged vertex-toggle matching; remove the augmented empty-vertex pair.
ORDER=(12,5,6,10,1,2,7,8,9,13,3,15,0,11,14,4)
FREE=bytearray(MEMBER)
MATCH=[]
for v in ORDER:
    b=1<<v
    for s in FACES:
        if not s&b and FREE[s] and FREE[s|b]:
            MATCH.append((s,s|b))
            FREE[s]=FREE[s|b]=0
assert len(MATCH)==32591
empty_pair=[(a,b) for a,b in MATCH if a==0]
assert len(empty_pair)==1
MATCH=[(a,b) for a,b in MATCH if a!=0]
CRIT=[s for s in FACES if FREE[s] or s in (0,empty_pair[0][1])]
CRIT=[s for s in CRIT if s]
assert len(MATCH)==32590
assert Counter(s.bit_count()-1 for s in CRIT)=={0:1,11:16,12:1}

# The entire oriented Hasse graph is acyclic; lower->upper for matched edges,
# upper->lower for all other face incidences.
PAIRS=set(MATCH)
OUT=[[] for _ in range(1<<N)]
INDEG=[0]*(1<<N)
incidences=0
for upper in FACES:
    if upper==0:continue
    for j in range(N):
        if (upper>>j)&1:
            lower=upper^(1<<j)
            if lower==0:continue
            start,end=(lower,upper) if (lower,upper) in PAIRS else (upper,lower)
            OUT[start].append(end)
            INDEG[end]+=1
            incidences+=1
queue=deque(s for s in FACES if s and INDEG[s]==0)
visited=0
while queue:
    s=queue.popleft(); visited+=1
    for t in OUT[s]:
        INDEG[t]-=1
        if INDEG[t]==0:queue.append(t)
assert visited==len(FACES)-1
assert incidences==519776

# Signed cellular Morse differential from the unique critical 12-cell to
# the sixteen critical 11-cells.  This is exact gradient-path elimination.
LOW=sorted(s for s in CRIT if s.bit_count()==12)
TOP=[s for s in CRIT if s.bit_count()==13]
assert len(LOW)==16 and len(TOP)==1
LIDX={s:i for i,s in enumerate(LOW)}
LOWER_TO_UPPER=dict(MATCH)

def incidence(lower,upper):
    b=lower^upper
    assert b.bit_count()==1 and lower&upper==lower
    return -1 if (upper&(b-1)).bit_count()%2 else 1

@lru_cache(maxsize=None)
def projection(s):
    if s in LIDX:return {LIDX[s]:1}
    if s not in LOWER_TO_UPPER:return {}
    upper=LOWER_TO_UPPER[s]
    if upper.bit_count()!=13:return {}
    coeff=incidence(s,upper)
    out=defaultdict(int)
    for j in range(N):
        b=1<<j
        if not upper&b:continue
        other=upper^b
        if other==s:continue
        factor=-coeff*incidence(other,upper)
        for i,a in projection(other).items():out[i]+=factor*a
    return {i:a for i,a in out.items() if a}

col=defaultdict(int)
for j in range(N):
    b=1<<j
    if TOP[0]&b:
        t=TOP[0]^b
        for i,a in projection(t).items():
            col[i]+=incidence(t,TOP[0])*a
D=tuple(col[i] for i in range(16))
assert D==(0,0,2,-2,-2,2,-2,0,0,0,0,-2,-2,0,-2,0)
assert gcd(*D)==2
# A 1-by-16 Morse boundary has Smith invariant 2, giving
# 15 infinite cyclic generators and one Z/2 in degree 11.

# Independent small Alexander-dual test: all triples must be connected.
DUAL={0}
for s in range(1<<N):
    bits=[j for j in range(N) if (s>>j)&1]
    if all(sum(int((NEIGH[a]>>b)&1) for a,b in combinations(tr,2))>=2
           for tr in combinations(bits,3)):
        DUAL.add(s)
DBY={i:sorted(s for s in DUAL if s.bit_count()==i+1) for i in range(4)}
assert tuple(len(DBY[i]) for i in range(4))==(16,120,160,40)
assert len(DUAL)==337
# Each dual tetrahedron is an induced four-cycle; every graph edge
# belongs to four distinct such cycles, so the cycles are not edge-disjoint.
SQUARES=DBY[3]
square_edge_counts=Counter(e for s in SQUARES for e in EDGE
                           if (s>>e[0])&1 and (s>>e[1])&1)
assert len(square_edge_counts)==40 and set(square_edge_counts.values())=={4}

def dual_boundary(d):
    rows={s:i for i,s in enumerate(DBY[d-1])}
    cols=[]
    for s in DBY[d]:
        bits=[j for j in range(N) if (s>>j)&1]
        cols.append({rows[s^(1<<b)]:(-1)**i for i,b in enumerate(bits)})
    return cols

def rank_mod(cols,p):
    piv={}
    for vec in cols:
        v={i:a%p for i,a in vec.items() if a%p}
        while v:
            j=min(v)
            if j not in piv:
                z=pow(v[j],-1,p)
                piv[j]={i:(a*z)%p for i,a in v.items() if a%p}
                break
            z=v[j]
            for i,a in piv[j].items():
                w=(v.get(i,0)-z*a)%p
                if w:v[i]=w
                else:v.pop(i,None)
    return len(piv)
RANKS={p:tuple(rank_mod(dual_boundary(d),p) for d in (1,2,3))
       for p in (2,3,5,7,11)}
assert RANKS[2]==(15,104,40)
assert all(RANKS[p]==(15,105,40) for p in (3,5,7,11))
print('graph vertices=16 edges=40 degrees=5 triangles=0')
print('connected triples=160 disconnected triples=400')
print('cut complex f-vector=',expected)
print('cut complex faces including empty=65199 facets=400')
print('Morse pairs=32590 critical by dimension={0:1,11:16,12:1}')
print('Hasse incidences=',incidences,'acyclic=',visited==65198)
print('critical 12-boundary=',D,'Smith invariant=2')
print('reduced integral H11=Z^15 direct-sum Z/2; other reduced H=0')
print('integral homotopy=(wedge of 15 S^11) wedge M(Z/2,11)')
print('Alexander dual f-vector=',tuple(len(DBY[i]) for i in range(4)))
print('four-cycles=40; every graph edge lies in four distinct four-cycles')
for p in (2,3,5,7,11):
    r=RANKS[p]
    b=(16-r[0],120-r[0]-r[1],160-r[1]-r[2],40-r[2])
    print('dual field',p,'boundary ranks=',r,'Betti=',b)
print('ALL CHECKS PASSED')
