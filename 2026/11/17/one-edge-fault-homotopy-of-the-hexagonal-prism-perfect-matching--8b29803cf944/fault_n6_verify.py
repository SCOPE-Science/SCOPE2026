"""Reproducible integral Morse certificate for one-edge faults of a hexagonal prism.

Uses only Python's standard library. Graph vertices (layer,column); a face is a
set of edge-indices, represented by a nonnegative integer bit mask. Exact signed
boundaries and all directed face-poset covers are checked independently.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd

N=6

def E(a,b): return tuple(sorted((a,b)))
EDGES = [E((r,i),(r,(i+1)%N)) for r in (0,1) for i in range(N)]+[E((0,i),(1,i)) for i in range(N)]

def perfect_matchings():
    incident=defaultdict(list)
    for j,(a,b) in enumerate(EDGES):
        incident[a].append((b,j));incident[b].append((a,j))
    def rec(unused, mask):
        if not unused:
            yield mask; return
        v=min(unused)
        for w,j in incident[v]:
            if w in unused:yield from rec(unused-{v,w},mask|(1<<j))
    return list(rec({(r,i) for r in (0,1) for i in range(N)},0))

def face_closure(facets):
    out={0}
    for f in facets:
        s=f
        while s:out.add(s);s=(s-1)&f
    return out

def pair_faces(faces):
    unpaired=set(faces); pairs=[]
    for j in range(len(EDGES)):
        for f in sorted(unpaired):
            higher=f|(1<<j)
            if not f&(1<<j) and higher in unpaired:
                pairs.append((f,higher));unpaired.remove(f);unpaired.remove(higher)
    return pairs,unpaired

def acyclic(faces,pairs):
    reversed_pairs={upper:lower for lower,upper in pairs}
    adj={f:[] for f in faces};indeg={f:0 for f in faces}
    for f in faces:
        t=f
        while t:
            b=t&-t;g=f^b
            a,z=(g,f) if reversed_pairs.get(f)==g else (f,g)
            adj[a].append(z);indeg[z]+=1;t-=b
    ready=deque(f for f in faces if not indeg[f]); seen=0
    while ready:
        f=ready.popleft();seen+=1
        for g in adj[f]:
            indeg[g]-=1
            if indeg[g]==0:ready.append(g)
    return seen==len(faces)

def boundary(f):
    bits=[j for j in range(len(EDGES)) if f&(1<<j)]
    return [(f^(1<<b),(-1)**i) for i,b in enumerate(bits)]

def morse_boundary(pairs,critical):
    upward={lo:hi for lo,hi in pairs}; critical=set(critical)
    @lru_cache(None)
    def project(low):
        if low in critical:return {low:1}
        if low not in upward:return {}
        hi=upward[low];unit=dict(boundary(hi))[low]
        result=Counter()
        for f,c in boundary(hi):
            if f==low:continue
            for k,v in project(f).items():result[k]-=unit*c*v
        return {k:v for k,v in result.items() if v}
    matrices={}
    for hi in critical:
        reduced=Counter()
        for f,c in boundary(hi):
            for k,v in project(f).items():
                if k.bit_count()==hi.bit_count()-1:reduced[k]+=c*v
        matrices[hi]={k:v for k,v in reduced.items() if v}
    return matrices

def check_fault(label, fault):
    index=EDGES.index(fault)
    facets=[f for f in perfect_matchings() if not f&(1<<index)]
    faces=face_closure(facets)
    pairs,critical=pair_faces(faces)
    assert acyclic(faces,pairs),f'acyclicity failed for {label}'
    dims=Counter(f.bit_count()-1 for f in critical)
    diff=morse_boundary(pairs,critical)
    bydim={d:sorted(f for f in critical if f.bit_count()-1==d) for d in (1,2,3)}
    d2=[[diff[u].get(l,0) for u in bydim[2]] for l in bydim[1]]
    d3=[[diff[u].get(l,0) for u in bydim[3]] for l in bydim[2]]
    assert all(sum(d2[i][k]*d3[k][j] for k in range(len(bydim[2])))==0
               for i in range(len(bydim[1])) for j in range(len(bydim[3])))
    assert all(f not in critical for f in (0,)), 'empty-face cancellation not observed'
    if label=='rung':
        assert dict(dims)=={1:1,2:3} and len(d2)==1
        assert gcd(*d2[0])==1, 'nonprimitive 2->1 boundary'
    else:
        assert dict(dims)=={1:1,2:4,3:1} and len(d2)==1
        assert gcd(*d2[0])==1 and gcd(*(row[0] for row in d3))==1
    print(f'{label}: facets={len(facets)} faces={len(faces)} pairs={len(pairs)}'
          f' critical={dict(sorted(dims.items()))} d2={d2} d3={d3} DAG=PASS'
          ' integral cancellations=PASS')

if __name__=='__main__':
    check_fault('rung',E((0,0),(1,0)))
    check_fault('rim',E((0,0),(0,1)))
    print('HEXAGON_PRISM_ONE_EDGE_HOMOTOPY_PASS')
