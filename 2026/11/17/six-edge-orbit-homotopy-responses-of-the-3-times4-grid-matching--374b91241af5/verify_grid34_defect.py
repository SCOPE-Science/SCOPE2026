#!/usr/bin/env python3
"""Exact finite matching-complex certificate for single-edge faults in a 3 by 4 grid.

Only Python standard library is required. All graph edges, faces, acyclic
matching pairs and cover relations are rebuilt from the definitions.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import product

ROWS, COLS = 3, 4
VERTICES = list(product(range(ROWS), range(COLS)))
EDGES = ([(VERTICES.index((r,c)), VERTICES.index((r+1,c)))
          for r in range(ROWS-1) for c in range(COLS)]
         + [(VERTICES.index((r,c)), VERTICES.index((r,c+1)))
            for r in range(ROWS) for c in range(COLS-1)])
REPRESENTATIVES = (0,1,8,9,11,12)
# Original 17-edge ordering is vertical first (in row and column order),
# followed by horizontal edges (in row and column order).
ORDERS = {
 'base': [0,4,15,11,9,16,12,10,14,8,2,7,1,5,6,3,13],
 'deletion_0': [14,0,8,11,9,3,4,2,7,15,5,6,1,12,10,13],
 'deletion_1': [11,0,7,13,4,10,5,9,2,6,8,15,3,14,12,1],
 'deletion_8': [0,12,9,8,6,10,13,2,5,4,11,15,1,3,14,7],
 'deletion_9': [6,15,9,4,14,10,12,3,2,13,8,11,1,7,0,5],
 'deletion_11': [3,5,8,13,1,15,14,9,12,7,10,2,6,0,4,11],
 'deletion_12': [12,15,13,1,7,11,8,4,5,0,9,3,6,14,2,10],
 'link_0': [5,0,11,1,6,8,9,10,12,2,7,4,3],
 'link_1': [1,10,5,7,9,6,4,8,0,2,3],
 'link_8': [4,8,0,6,3,10,1,9,11,2,12,5,7],
 'link_9': [3,4,10,2,0,11,5,8,1,7,6,9],
 'link_11': [2,8,3,10,6,1,7,9,0,4,5],
 'link_12': [8,9,4,2,6,7,1,3,5,0]
}
DELETE_RANKS={0:5,1:7,8:7,9:5,11:7,12:8}
LINK_RANKS={i:9-DELETE_RANKS[i] for i in REPRESENTATIVES}


def face_set(excluded):
    remaining=[edge for i,edge in enumerate(EDGES) if i not in excluded]
    faces=set()
    def rec(next_i, mask, used):
        assert mask not in faces
        faces.add(mask)
        for i in range(next_i,len(remaining)):
            u,v=remaining[i]
            if (used & (1<<u | 1<<v)) == 0:
                rec(i+1,mask | (1<<i),used | (1<<u) | (1<<v))
    rec(0,0,0)
    return faces,remaining


def check_matching(name, excluded, target_degree, target_rank):
    faces,remaining=face_set(excluded)
    size=len(remaining); order=ORDERS[name]
    assert sorted(order)==list(range(size))
    available=set(faces)
    up=set()
    # An augmented acyclic discrete Morse matching; the empty face is paired.
    for bit_index in order:
        toggle=1<<bit_index
        for face in sorted(available):
            if face in available and not face&toggle and face|toggle in available:
                available.remove(face)
                available.remove(face|toggle)
                up.add((face,face|toggle))
    assert 0 not in available
    assert Counter(x.bit_count()-1 for x in available)=={target_degree:target_rank}, (name,available)
    assert 2*len(up)+len(available)==len(faces)
    # Globally check every Hasse cover, reversing precisely the matched covers.
    indegree={f:0 for f in faces}
    outgoing={f:[] for f in faces}
    covers=0
    for higher in faces:
        bits=higher
        while bits:
            b=bits & -bits; bits-=b
            lower=higher-b
            assert lower in faces
            if (lower,higher) in up: source,dest=lower,higher
            else:source,dest=higher,lower
            outgoing[source].append(dest); indegree[dest]+=1
            covers+=1
    q=deque(sorted(f for f in faces if indegree[f]==0))
    visited=0
    while q:
        f=q.popleft();visited+=1
        for g in outgoing[f]:
            indegree[g]-=1
            if indegree[g]==0:q.append(g)
    assert visited==len(faces), (name,'cyclic orientation')
    # Independent signed Euler-characteristic count by the matching-polynomial recurrence.
    n=len(remaining)
    incidence=[(1<<u)|(1<<v) for u,v in remaining]
    @lru_cache(None)
    def matching_sum(start,used):
        if start==n:return 1
        z=matching_sum(start+1,used)
        if not used&incidence[start]:z-=matching_sum(start+1,used|incidence[start])
        return z
    # Sum of (-1)^number_of_edges on all faces = (-1)^{d+1} rank on criticals.
    assert matching_sum(0,0)==(-1)**(target_degree+1)*target_rank
    return len(faces),covers,len(up),len(available)


def main():
    assert len(EDGES)==17
    results=[]
    results.append(('base',check_matching('base',set(),3,9)))
    fullorbits=[]
    for k in REPRESENTATIVES:
        u,v=EDGES[k]
        bad={j for j,(a,b) in enumerate(EDGES) if u in (a,b) or v in (a,b)}
        a=check_matching(f'deletion_{k}',{k},3,DELETE_RANKS[k])
        b=check_matching(f'link_{k}',bad,2,LINK_RANKS[k])
        results.extend(((f'deletion_{k}',a),(f'link_{k}',b)))
        # The rectangular graph's four coordinate reflections exhaust its edge orbits.
        orbit=set()
        for reflect_row in (False,True):
            for reflect_col in (False,True):
                new=[(ROWS-1-rr if reflect_row else rr,
                      COLS-1-cc if reflect_col else cc)
                     for rr,cc in (VERTICES[u],VERTICES[v])]
                mapped=tuple(sorted((VERTICES.index(new[0]),VERTICES.index(new[1]))))
                orbit.add(next(j for j,edge in enumerate(EDGES) if tuple(sorted(edge))==mapped))
        fullorbits.append(orbit)
    assert len(set().union(*fullorbits))==17
    assert sum(map(len,fullorbits))==17
    assert sorted(map(len,fullorbits))==[1,2,2,4,4,4]
    for name,(f,c,p,r) in results:
        print(f'{name}: faces={f}, covers={c}, pairs={p}, critical_{"3" if name=="base" or name.startswith("deletion") else "2"}={r}; DAG=PASS; Euler=PASS')
    print(f'edge_orbits={tuple(sorted(map(len,fullorbits)))}')
    print('GRID34_ALL_EDGE_DELETION_HOMOTOPY_PASS')

if __name__=='__main__':main()
