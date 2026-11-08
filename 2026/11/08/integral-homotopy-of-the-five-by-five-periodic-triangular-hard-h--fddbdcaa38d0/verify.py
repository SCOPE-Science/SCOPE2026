#!/usr/bin/env python3
"""Exact standalone certificate for the 5-by-5 periodic triangular independence complex.

Python 3 standard library only. All masks are vertex subsets, with vertex 5*i+j.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from heapq import heappush, heappop

W = H = 5
N = W * H
STEP = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
nei = [0] * N
for i in range(H):
    for j in range(W):
        v = W*i+j
        for di,dj in STEP:
            u = W*((i+di)%H)+(j+dj)%W
            if u != v:
                nei[v] |= (1 << u)
assert all(nei[v].bit_count()==6 for v in range(N))
assert all(((nei[v]>>u)&1)==((nei[u]>>v)&1) for v in range(N) for u in range(N))

# Independent enumeration A: extend sets by increasing vertex indices.
faces = {0}
stack = [(0,0)]
while stack:
    s, start = stack.pop()
    for v in range(start,N):
        if not (nei[v] & s):
            t=s|(1<<v)
            assert t not in faces
            faces.add(t)
            stack.append((t,v+1))
assert len(faces)==4216
cnt = Counter(s.bit_count() for s in faces)
assert tuple(cnt[k] for k in range(8))==(1,25,225,900,1600,1140,300,25)

# Independent enumeration B: compatible independent 5-cycle row patterns.
rows=[r for r in range(1<<W) if not(r & ((r<<1)|(r>>(W-1))))]
assert len(rows)==11
rot=lambda r:(r>>1)|((r&1)<<(W-1))
def compatible(a,b):
    return not (a&b or a&rot(b))
other=set()
for rs in product(rows,repeat=H):
    if all(compatible(rs[i],rs[(i+1)%H]) for i in range(H)):
        other.add(sum(rs[i] << (W*i) for i in range(H)))
assert other==faces
print('FACES',len(faces),'NONEMPTY',len(faces)-1,'FACE_VECTOR',tuple(cnt[k] for k in range(1,8)))

# Deterministic vertex-by-vertex matching, restricted to NONEMPTY faces.
nonempty=faces-{0}
remaining=nonempty.copy()
paired={}
pairs=[]
for v in range(N):
    b=1<<v
    low=sorted(s for s in remaining if not(s&b) and (s|b) in remaining)
    for s in low:
        t=s|b
        assert s in remaining and t in remaining
        remaining.remove(s)
        remaining.remove(t)
        paired[s]=(t,0) # lower
        paired[t]=(s,1) # upper
        pairs.append((s,t))
crit=Counter(s.bit_count()-1 for s in remaining)
assert crit=={0:1,3:51,4:15}
assert len(pairs)==2074
assert 2*len(pairs)+len(remaining)==len(nonempty)
print('MATCHING_PAIRS',len(pairs),'CRITICAL',dict(sorted(crit.items())))

# Exhaustive Hasse orientation test. Matched covering relations point up,
# every other covering relation points down. Kahn sorting proves acyclicity.
indegree={s:0 for s in nonempty}
out=defaultdict(list)
incidences=0
for s in nonempty:
    t=s
    while t:
        v=t&-t
        t-=v
        q=s^v
        if q==0:
            continue
        if paired.get(q)==(s,0):
            a,b=q,s
        else:
            a,b=s,q
        out[a].append(b)
        indegree[b]+=1
        incidences+=1
assert incidences==17225
ready=[]
for s,d in indegree.items():
    if d==0:heappush(ready,s)
seen=0
while ready:
    a=heappop(ready)
    seen+=1
    for b in out[a]:
        indegree[b]-=1
        if indegree[b]==0:heappush(ready,b)
assert seen==len(nonempty)
print('HASSE_INCIDENCES',incidences,'ACYCLIC_SORTED',seen)

# Signed integral Morse differential in degree 4 to degree 3.
# For a 3-cell matched upward to a 4-cell, eliminate the 3-cell from
# the cellular boundary of the 4-cell; matched upper 3-cells vanish.
def signed_boundary(s):
    k=0
    t=s
    while t:
        v=t&-t
        t-=v
        yield s^v, (1 if k%2==0 else -1)
        k+=1
critical3=sorted(s for s in remaining if s.bit_count()==4)
critical4=sorted(s for s in remaining if s.bit_count()==5)
critical3idx={s:i for i,s in enumerate(critical3)}
@lru_cache(maxsize=None)
def projection(s):
    if s in remaining:
        assert s.bit_count()==4
        return {s:1}
    mate,is_upper=paired[s]
    if is_upper:
        return {}
    assert mate.bit_count()==5
    boundary=list(signed_boundary(mate))
    incidence=next(c for t,c in boundary if t==s)
    answer=defaultdict(int)
    for t,c in boundary:
        if t==s:continue
        for v,a in projection(t).items():
            answer[v]-=incidence*c*a
    return {v:a for v,a in answer.items() if a}

matrix=[[0 for _ in critical4] for _ in critical3]
for j,s in enumerate(critical4):
    for t,c in signed_boundary(s):
        for v,a in projection(t).items():
            matrix[critical3idx[v]][j]+=c*a
assert all(a==0 for row in matrix for a in row)
print('SIGNED_MORSE_BOUNDARY_4_TO_3',len(matrix),'x',len(matrix[0]),'NONZERO',0,
      'PROJECTION_STATES',projection.cache_info().currsize)

# Separate GF(2) simplicial boundary ranks; these calculations do NOT use matching.
bydim={d:sorted(s for s in nonempty if s.bit_count()==d+1) for d in range(7)}
ranks={0:0,7:0}
for d in range(1,7):
    idx={s:i for i,s in enumerate(bydim[d-1])}
    pivots={}
    for s in bydim[d]:
        x=0
        for t,c in signed_boundary(s):
            x ^= 1<<idx[t]
        while x:
            pivot=x.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=x
                break
            x ^= pivots[pivot]
    ranks[d]=len(pivots)
assert tuple(ranks[d] for d in range(1,7))==(24,201,699,850,275,25)
betti=tuple(len(bydim[d])-ranks[d]-ranks[d+1] for d in range(7))
assert betti==(1,0,0,51,15,0,0)
print('BOUNDARY_RANKS_MOD2',tuple(ranks[d] for d in range(1,7)))
print('BETTI_MOD2',betti)
print('MORSE_HOMOTOPY_WEDGE_51_S3_AND_15_S4_CHECKED')
print('ALL_CHECKS_PASS')
