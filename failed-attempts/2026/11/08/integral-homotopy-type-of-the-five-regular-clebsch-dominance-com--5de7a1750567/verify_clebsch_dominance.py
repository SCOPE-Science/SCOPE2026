#!/usr/bin/env python3
"""Exact finite check of the dominance complex of the 5-regular Clebsch graph.

Run: python3 verify_clebsch_dominance.py
Uses only Python's standard library.
"""
from collections import Counter, deque
from hashlib import sha256

N=16
STEPS=(1,2,4,8,15)
PIVOTS=(10,14,5,1,9,2,3,11,13,7,8,4,0,6,15,12)


def main():
    adjacency=[set() for _ in range(N)]
    for i in range(N):
        for d in STEPS:
            j=i^d
            if i==j:raise AssertionError('loop')
            adjacency[i].add(j)
    assert all(len(a)==5 for a in adjacency)
    assert all(i in adjacency[j] for i in range(N) for j in adjacency[i])
    # The graph is strongly regular (16,5,0,2): an independent model check.
    for i in range(N):
        for j in range(i+1,N):
            assert len(adjacency[i]&adjacency[j])==(0 if j in adjacency[i] else 2)
    closed=[1<<i | sum(1<<j for j in adjacency[i]) for i in range(N)]
    facets=[];faces=[];facemask=[False]*(1<<N)
    for s in range(1,1<<N):
        # direct forbidden closed-neighborhood criterion
        c1=all(s&nb!=nb for nb in closed)
        # independent dominating-set criterion (independently uses complement)
        comp=((1<<N)-1)^s
        c2=all((comp&(1<<i | sum(1<<j for j in adjacency[i])))!=0 for i in range(N))
        assert c1==c2
        if c1:
            facemask[s]=True
            faces.append(s)
    for s in faces:
        if not any(not(s>>i&1) and facemask[s|(1<<i)] for i in range(N)):
            facets.append(s)
    faceset=set(faces)
    low={}; high={}
    for pivot in PIVOTS:
        bit=1<<pivot
        for s in faces:
            u=s|bit
            if s&bit or s in low or s in high or u not in faceset or u in low or u in high:
                continue
            low[s]=u
            high[u]=s
    assert len(low)==len(high)
    assert set(low).isdisjoint(high)
    assert all((b^a).bit_count()==1 and (b&a)==a for a,b in low.items())
    critical=faceset-set(low)-set(high)
    histogram=Counter(s.bit_count()-1 for s in critical)
    assert histogram=={0:1,9:131}, histogram
    assert 2*len(low)+len(critical)==len(faces)
    # For every cover arrow, orient upwards precisely along matched pairs;
    # otherwise orient downwards. A topological-sort certificate exhaustively
    # checks acyclicity of the full directed Hasse diagram.
    indeg={s:0 for s in faces}
    adj={s:[] for s in faces}
    covers=0
    for s in faces:
        for i in range(N):
            if not(s>>i&1):
                continue
            t=s^(1<<i)
            if t==0:continue
            covers+=1
            if low.get(t)==s:
                v,w=t,s
            else:
                v,w=s,t
            adj[v].append(w)
            indeg[w]+=1
    q=deque(s for s in faces if indeg[s]==0)
    count=0
    while q:
        s=q.popleft();count+=1
        for t in adj[s]:
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    assert count==len(faces), (count,len(faces))
    # Independent enumeration checks Euler characteristic and vertex-cover number.
    face_vector=Counter(s.bit_count()-1 for s in faces)
    euler=sum((-1)**d * cnt for d,cnt in face_vector.items())
    assert euler == 1-131, euler
    indepmax=0;maximal_independent_count=0
    for s in range(1<<N):
        if all(not (s & sum(1<<j for j in adjacency[i]))
               for i in range(N) if s & (1<<i)):
            if s.bit_count()>indepmax:
                indepmax=s.bit_count();maximal_independent_count=1
            elif s.bit_count()==indepmax:
                maximal_independent_count+=1
    assert (indepmax,maximal_independent_count)==(5,16)
    print('FACE_VECTOR',dict(sorted(face_vector.items())))
    print('EULER_CHARACTERISTIC',euler)
    print('VERTEX_COVER_NUMBER',N-indepmax)
    print('MAX_INDEPENDENT_SETS',maximal_independent_count)
    print('GRAPH_ORDER',N)
    print('EDGE_COUNT',sum(len(a) for a in adjacency)//2)
    print('FACE_COUNT_NONEMPTY',len(faces))
    print('FACET_COUNT',len(facets))
    print('FACET_DIMENSIONS',dict(sorted(Counter(s.bit_count()-1 for s in facets).items())))
    print('MATCHED_PAIRS',len(low))
    print('CRITICAL_HISTOGRAM',dict(sorted(histogram.items())))
    print('COVER_RELATIONS',covers)
    print('TOPOLOGICALLY_SORTED',count)
    print('FACE_SET_SHA256',sha256(','.join(str(i) for i in faces).encode()).hexdigest())
    print('MATCHING_SHA256',sha256(','.join(f'{s}:{low[s]}' for s in sorted(low)).encode()).hexdigest())
    print('CLEBSCH_DOMINANCE_INTEGRAL_WEDGE_PASS')

if __name__=='__main__':main()
