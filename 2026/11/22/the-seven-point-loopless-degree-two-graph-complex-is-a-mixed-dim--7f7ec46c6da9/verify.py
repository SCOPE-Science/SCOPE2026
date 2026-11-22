#!/usr/bin/env python3
"""Exact finite CW and Morse certificate for the loopless degree-two graph complex on seven vertices.
Only Python standard library required. The sign convention is lexicographic on the graph edges.
"""
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
from itertools import combinations
import json

N=7
E=list(combinations(range(N),2)); m=len(E)
faces={0}

def enum(start,deg,mask):
    for i in range(start,m):
        a,b=E[i]
        if deg[a]<2 and deg[b]<2:
            deg[a]+=1;deg[b]+=1
            s=mask|(1<<i)
            assert s not in faces
            faces.add(s)
            enum(i+1,deg,s)
            deg[a]-=1;deg[b]-=1

enum(0,[0]*N,0)
bydim=Counter(s.bit_count()-1 for s in faces)
assert [bydim[j] for j in range(-1,7)]==[1,21,210,1190,3780,6132,3997,465]
# Lexicographic vertex sweep: on remaining faces pair sigma and sigma U {e}, if both remain.
remaining=set(faces); matched=[]
for i in range(m):
    pair=[(s,s|(1<<i)) for s in remaining if not (s>>i)&1 and (s|(1<<i)) in remaining]
    for lo,hi in pair:
        assert lo in remaining and hi in remaining
        remaining.remove(lo);remaining.remove(hi);matched.append((lo,hi))
assert 0 not in remaining
assert len(remaining)==444 and Counter(s.bit_count()-1 for s in remaining)=={4:132,5:312}
assert len(matched)==7676
# Acyclicity by topological sort on the full Hasse graph: unmatched arrows downward,
# matching arrows upward. This is a finite proof of an acyclic discrete Morse matching.
matched_set=set(matched)
indegree={s:0 for s in faces}; adj=defaultdict(list)
for higher in faces:
    for i in range(m):
        if not ((higher>>i)&1):continue
        lower=higher^(1<<i)
        if (lower,higher) in matched_set:
            adj[lower].append(higher); indegree[higher]+=1
        else:
            adj[higher].append(lower); indegree[lower]+=1
q=deque(x for x,d in indegree.items() if not d);visited=0
while q:
    x=q.popleft();visited+=1
    for y in adj[x]:
        indegree[y]-=1
        if indegree[y]==0:q.append(y)
assert visited==len(faces)
# For ordinary (unaugmented) Forman theory, leave the vertex paired with empty face
# as the single critical vertex; all other matched pairs are legitimate Hasse matches.
base_pair=[p for p in matched if p[0]==0];assert len(base_pair)==1
base_vertex=base_pair[0][1]
pairs=[p for p in matched if p[0]!=0]
assert len(pairs)==7675
active=set(faces);active.remove(0)
cols={};rows=defaultdict(set)
for s in active:
    if s.bit_count()<2:continue
    indices=[i for i in range(m) if s>>i&1]
    col={s^(1<<i):(1 if j%2==0 else -1) for j,i in enumerate(indices)}
    cols[s]=col
    for x in col:rows[x].add(s)

# Any acyclic matching is cancellable over the integers. We explicitly perform
# the resulting unimodular boundary operations and verify every pivot and update.
heap=[]
for lo,hi in pairs:
    d=cols[hi];assert abs(d[lo])==1
    heappush(heap,((len(rows[lo])-1)*(len(d)-1),len(d)+len(rows[lo]),lo,hi))
paired={lo:hi for lo,hi in pairs}
cancelled=0;maxcoeff=1
while heap:
    _cost,_size,lo,hi=heappop(heap)
    if lo not in paired:continue
    if lo not in active or hi not in active:raise AssertionError('lost paired cell')
    d=cols.get(hi)
    if d is None or abs(d.get(lo,0))!=1:raise AssertionError('matched pivot not unit')
    actual=(len(rows[lo])-1)*(len(d)-1)
    if actual>_cost:
        heappush(heap,(actual,len(d)+len(rows[lo]),lo,hi));continue
    sign=d[lo]
    # Schur complement, purely integral elementary basis changes
    for other in list(rows[lo]):
        if other==hi:continue
        dd=cols[other]
        coefficient=dd.pop(lo)
        rows[lo].remove(other)
        for rr,vv in d.items():
            if rr==lo:continue
            before=dd.get(rr,0);after=before-coefficient*sign*vv
            if after:
                dd[rr]=after;maxcoeff=max(maxcoeff,abs(after))
                if not before:rows[rr].add(other)
            elif before:
                del dd[rr];rows[rr].remove(other)
    for rr in d:rows[rr].discard(hi)
    for higher in list(rows[hi]):
        del cols[higher][hi]
    rows[hi].clear()
    del cols[hi]
    if lo in cols:
        for rr in cols[lo]:rows[rr].discard(lo)
        del cols[lo]
    active.remove(hi);active.remove(lo)
    del paired[lo];cancelled+=1
assert cancelled==7675 and not paired
assert Counter(s.bit_count()-1 for s in active)=={0:1,4:132,5:312}
assert base_vertex in active
# Every retained boundary outside dimensions 5 -> 4 is zero.
assert all(not cols.get(x) for x in active if x.bit_count()!=6)
# Compute exact integer Smith invariant factors by successive unit pivots. A non-unit
# remaining pivot would invalidate our claimed integral decomposition.
unit_steps=0
while True:
    candidates=[]
    for c in active:
        if c.bit_count()!=6:continue
        for r,v in cols.get(c,{}).items():
            if abs(v)==1:
                candidates.append(((len(rows[r])-1)*(len(cols[c])-1),r,c))
    if not candidates:break
    _,r,c=min(candidates)
    assert r in active and c in active, (unit_steps,r,c,len(active))
    assert r!=c
    d=cols[c];sg=d[r]
    for other in list(rows[r]):
        if other==c:continue
        dd=cols[other];v=dd.pop(r);rows[r].remove(other)
        for rr,w in d.items():
            if rr==r:continue
            before=dd.get(rr,0);after=before-v*sg*w
            if after:
                dd[rr]=after;maxcoeff=max(maxcoeff,abs(after))
                if not before:rows[rr].add(other)
            elif before:del dd[rr];rows[rr].remove(other)
    for rr in d:rows[rr].discard(c)
    for higher in list(rows[c]):
        del cols[higher][c]
    rows[c].clear()
    del cols[c];active.remove(c)
    if r in cols:
        for rr in cols[r]:rows[rr].discard(r)
        del cols[r]
    active.remove(r);unit_steps+=1
assert unit_steps==131,unit_steps
assert Counter(s.bit_count()-1 for s in active)=={0:1,4:1,5:181}
assert all(not cols.get(c) for c in active)
print('BOUNDED_DEGREE_LOOPLESS_7_OK',flush=True)
print(json.dumps({'face_counts':{str(j):bydim[j] for j in range(-1,7)},'acyclic_matching_pairs':len(pairs),'critical_cells_before_Abelian_reduction':{'0':1,'4':132,'5':312},'unit_pivots':unit_steps,'integer_homology':{'4':'Z','5':'Z^181'},'maximum_intermediate_coefficient':maxcoeff},sort_keys=True))
