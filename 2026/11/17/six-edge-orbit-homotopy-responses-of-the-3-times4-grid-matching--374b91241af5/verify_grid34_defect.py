#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse certificates for P3 x P4 matching complexes.

A correction to the intact-grid pivot order is supplied. The six deletion
complexes, their links, the graph incidence convention and the theorem are
unchanged. Only standard-library Python is required.
"""
from itertools import product
from collections import Counter, deque
from functools import lru_cache

V = list(product(range(3), range(4)))
E = ([(V.index((r,c)), V.index((r+1,c))) for r in range(2) for c in range(4)]
     + [(V.index((r,c)), V.index((r,c+1))) for r in range(3) for c in range(3)])
REPRESENTATIVES = (0, 1, 8, 9, 11, 12)
# All pivot orders index the remaining edges, not the original graph edges.
# The corrected base order leaves exactly nine dimension-three critical faces.
ORDERS = {
 'base':[8,5,13,7,6,9,16,15,11,1,14,3,12,2,4,0,10],
 'deletion_0':[14,0,8,11,9,3,4,2,7,15,5,6,1,12,10,13],
 'deletion_1':[11,0,7,13,4,10,5,9,2,6,8,15,3,14,12,1],
 'deletion_8':[0,12,9,8,6,10,13,2,5,4,11,15,1,3,14,7],
 'deletion_9':[6,15,9,4,14,10,12,3,2,13,8,11,1,7,0,5],
 'deletion_11':[3,5,8,13,1,15,14,9,12,7,10,2,6,0,4,11],
 'deletion_12':[12,15,13,1,7,11,8,4,5,0,9,3,6,14,2,10],
 'link_0':[5,0,11,1,6,8,9,10,12,2,7,4,3],
 'link_1':[1,10,5,7,9,6,4,8,0,2,3],
 'link_8':[4,8,0,6,3,10,1,9,11,2,12,5,7],
 'link_9':[3,4,10,2,0,11,5,8,1,7,6,9],
 'link_11':[2,8,3,10,6,1,7,9,0,4,5],
 'link_12':[8,9,4,2,6,7,1,3,5,0]
}
DEL_RANKS={0:5,1:7,8:7,9:5,11:7,12:8}

def enumerate_faces(remaining):
    occupancy=[(1<<u)|(1<<v) for u,v in remaining]
    faces={0}
    def extend(start, used, mask):
        for k in range(start,len(remaining)):
            if not used&occupancy[k]:
                extension=mask|(1<<k)
                assert extension not in faces
                faces.add(extension)
                extend(k+1, used|occupancy[k], extension)
    extend(0,0,0)
    return faces

def certificate(name, edges, degree, rank):
    faces=enumerate_faces(edges)
    order=ORDERS[name]
    assert sorted(order)==list(range(len(edges)))
    unpaired=set(faces)
    matched=set()
    for k in order:
        t=1<<k
        for f in sorted(unpaired):
            g=f|t
            if f in unpaired and not(f&t) and g in unpaired:
                unpaired.remove(f)
                unpaired.remove(g)
                matched.add((f,g))
    assert 0 not in unpaired
    assert Counter(f.bit_count()-1 for f in unpaired)=={degree:rank}, (name,unpaired)
    assert 2*len(matched)+len(unpaired)==len(faces)
    # Every augmented simplicial Hasse cover is used exactly once.
    successors={x:[] for x in faces}
    indegree={x:0 for x in faces}
    cover_count=0
    for top in faces:
        bits=top
        while bits:
            bit=bits&-bits;bits-=bit
            low=top^bit
            assert low in faces
            src,dst=(low,top) if (low,top) in matched else (top,low)
            successors[src].append(dst);indegree[dst]+=1
            cover_count+=1
    pending=deque(x for x in faces if indegree[x]==0)
    seen=0
    while pending:
        x=pending.popleft();seen+=1
        for y in successors[x]:
            indegree[y]-=1
            if indegree[y]==0:pending.append(y)
    assert seen==len(faces), (name,'directed cycle')
    # Alternating matching polynomial, computed from the graph, not the face set.
    footprint=[(1<<u)|(1<<v) for u,v in edges]
    @lru_cache(None)
    def euler(k,used):
        if k==len(edges):return 1
        z=euler(k+1,used)
        if not used&footprint[k]:z-=euler(k+1,used|footprint[k])
        return z
    assert euler(0,0)==(-1)**(degree+1)*rank
    print(f'{name}: faces={len(faces)}, covers={cover_count}, pairs={len(matched)}, critical_{degree}={rank}; DAG=PASS; Euler=PASS')

def main():
    assert len(E)==17
    certificate('base',E,3,9)
    orbits=[]
    for k in REPRESENTATIVES:
        u,v=E[k]
        certificate(f'deletion_{k}',[e for i,e in enumerate(E) if i!=k],3,DEL_RANKS[k])
        certificate(f'link_{k}',[e for e in E if u not in e and v not in e],2,9-DEL_RANKS[k])
        orb=set()
        for row_flip in (False,True):
            for col_flip in (False,True):
                reflected=[((2-r) if row_flip else r,(3-c) if col_flip else c) for r,c in (V[u],V[v])]
                target=tuple(sorted(V.index(z) for z in reflected))
                orb.add(next(j for j,e in enumerate(E) if tuple(sorted(e))==target))
        orbits.append(orb)
    assert len(set().union(*orbits))==sum(map(len,orbits))==17
    assert sorted(map(len,orbits))==[1,2,2,4,4,4]
    print('edge_orbits='+str(tuple(sorted(map(len,orbits)))))
    print('GRID34_ALL_EDGE_DELETION_HOMOTOPY_PASS')

if __name__=='__main__': main()
