#!/usr/bin/env python3
"""Exact finite simplicial-Morse checks for two edge faults in C3 square C4.

Standard-library-only.  Faces are indexed by lexicographically ordered graph edges.
The empty face is included to compute reduced homology.  Every Morse step
is either an elementary free-face collapse or deletion of a maximal cell.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations
import heapq
import random


def graph_edges():
    edges = set()
    for i in range(3):
        for j in range(4):
            v = 4*i+j
            for w in (4*((i+1) % 3)+j, 4*i+(j+1) % 4):
                if v != w:
                    edges.add(tuple(sorted((v,w))))
    return sorted(edges)


def matching_faces(edges):
    occupied = [((1 << u) | (1 << v)) for u,v in edges]
    faces = []
    def visit(k, used, face):
        if k == len(edges):
            faces.append(face)
            return
        visit(k+1, used, face)
        if not (used & occupied[k]):
            visit(k+1, used | occupied[k], face+(k,))
    visit(0,0,())
    assert len(faces) == len(set(faces))
    return set(faces)


def morse_matching(faces, seed, free_order):
    assert free_order in ('high', 'low')
    all_faces = sorted(faces)
    rng = random.Random(seed)
    tie = {f:rng.random() for f in all_faces}
    below = {f:set() for f in faces}
    above = {f:set() for f in faces}
    for f in faces:
        for i in range(len(f)):
            g=f[:i]+f[i+1:]
            assert g in faces
            below[f].add(g)
            above[g].add(f)
    active=set(faces)
    heap=[]
    def enqueue(g):
        if g in active and len(above[g]) == 1:
            h=next(iter(above[g]))
            if len(above[h]) == 0:
                key= -len(g) if free_order=='high' else len(g)
                heapq.heappush(heap,(key,tie[g],g))
    for f in all_faces:
        enqueue(f)
    def remove(f):
        assert f in active
        for g in below[f]:
            above[g].remove(f)
        for h in above[f]:
            below[h].remove(f)
        active.remove(f)
    log=[]
    while active:
        pair=None
        while heap:
            _,_,g=heapq.heappop(heap)
            if g not in active or len(above[g])!=1:
                continue
            h=next(iter(above[g]))
            if h in active and not above[h]:
                pair=(g,h)
                break
        if pair:
            g,h=pair
            assert len(h)==len(g)+1 and g in below[h]
            assert above[g]=={h} and not above[h]
            touched=below[g]|below[h]|above[g]|above[h]
            log.append(('pair',g,h))
            remove(g)
            remove(h)
        else:
            f=max(active,key=lambda t:(len(t),tie[t]))
            assert not above[f]
            touched=below[f]|above[f]
            log.append(('critical',f))
            remove(f)
        for f in touched:
            enqueue(f)
    assert len(log) + sum(rec[0]=='pair' for rec in log)==len(faces)
    # Independent acyclicity check: orient every cover downward except pairs.
    paired = {(g,h) for typ,*other in log if typ=='pair' for g,h in [other]}
    out={f:[] for f in faces}
    indeg={f:0 for f in faces}
    for h in faces:
        for i in range(len(h)):
            g=h[:i]+h[i+1:]
            x,y=(g,h) if (g,h) in paired else (h,g)
            out[x].append(y)
            indeg[y]+=1
    q=deque(f for f in faces if indeg[f]==0)
    seen=0
    while q:
        f=q.popleft();seen+=1
        for h in out[f]:
            indeg[h]-=1
            if indeg[h]==0:
                q.append(h)
    assert seen==len(faces),('cyclic Morse matching',len(faces),seen)
    return log


def integer_morse_boundary(faces,log):
    # Oriented simplicial boundary: delete the i-th vertex with sign (-1)^i.
    B=defaultdict(dict)
    for f in faces:
        B[len(f)-1][f]={f[:i]+f[i+1:]:(-1)**i for i in range(len(f))}
    # The standard integer unit cancellation formula is an exact chain
    # equivalence.  Coefficient of g in any other d-cell is eliminated by
    # subtracting the appropriate multiple of the upper matched h-cell.
    paircount=0
    for rec in log:
        if rec[0] != 'pair':
            continue
        _,g,h=rec
        d=len(h)-1
        assert h in B[d] and g in B[d-1]
        row=B[d][h]
        pivot=row.get(g,0)
        assert pivot in (-1,1),('nonunit',g,h,pivot)
        for k,col in list(B[d].items()):
            if k==h:
                continue
            alpha=col.get(g,0)
            if alpha:
                factor=alpha*pivot
                for w,val in row.items():
                    updated=col.get(w,0)-factor*val
                    if updated:
                        col[w]=updated
                    else:
                        col.pop(w,None)
        B[d].pop(h)
        B[d-1].pop(g)
        for col in B[d+1].values():
            col.pop(h,None)
        paircount+=1
    critical=Counter({d:len(cols) for d,cols in B.items() if cols})
    expected=Counter(len(rec[1])-1 for rec in log if rec[0]=='critical')
    assert critical==expected,(critical,expected)
    n_nonzero=0
    for d,cols in B.items():
        lower=B.get(d-1,{})
        for f,col in cols.items():
            for g,v in col.items():
                assert g in lower and v!=0
                n_nonzero+=1
                assert all(sum(v*c.get(w,0) for g,v in col.items()
                               for c in [lower[g]])==0 for w in B.get(d-2,{})), 'boundary squared'
    return critical,n_nonzero,paircount


def rank_mod_two(cols):
    piv={}
    for c in cols:
        while c:
            b=c.bit_length()-1
            if b not in piv:
                piv[b]=c
                break
            c ^= piv[b]
    return len(piv)


def betti_mod_two(faces):
    bydim=defaultdict(list)
    for f in faces:
        bydim[len(f)-1].append(f)
    rank={}
    for d in range(0,max(bydim)+1):
        rows={f:i for i,f in enumerate(bydim[d-1])}
        cols=[sum(1<<rows[f[:i]+f[i+1:]] for i in range(len(f)))
              for f in bydim[d]]
        rank[d]=rank_mod_two(cols)
    return {d:len(bydim[d])-rank.get(d,0)-rank.get(d+1,0)
            for d in bydim}, {d:len(z) for d,z in bydim.items()}


def edge_orbits(E):
    all_edges=set(E)
    e3=(0,4)
    e4=(0,1)
    orbits=[]
    for rep in (e3,e4):
        image=set()
        for perm in permutations(range(3)):
            for sign in (-1,1):
                for shift in range(4):
                    mp=lambda v:4*perm[v//4]+((sign*(v%4)+shift)%4)
                    assert {tuple(sorted((mp(a),mp(b)))) for a,b in E}==all_edges
                    image.add(tuple(sorted((mp(rep[0]),mp(rep[1])))))
        assert len(image)==12
        orbits.append(image)
    assert orbits[0].isdisjoint(orbits[1]) and orbits[0]|orbits[1]==all_edges
    return e3,e4


def main():
    E=graph_edges()
    assert len(E)==24
    e3,e4=edge_orbits(E)
    cases=[
        ('intact',E,25,'low',{3:44},2764),
        ('C4_edge_deleted',[e for e in E if e!=e4],1,'high',{3:44},2308),
        ('C3_edge_deleted',[e for e in E if e!=e3],6,'high',{3:36},2344),
        ('C4_edge_link',[e for e in E if not(set(e)&set(e4))],0,'high',{2:2,3:2},456),
        ('C3_edge_link',[e for e in E if not(set(e)&set(e3))],0,'high',{2:8},420),
    ]
    for name,edges,seed,order,expected,nfaces in cases:
        faces=matching_faces(edges)
        assert len(faces)==nfaces,(name,len(faces))
        log=morse_matching(faces,seed,order)
        critical,nz,pairs=integer_morse_boundary(faces,log)
        assert dict(critical)==expected, (name,critical,expected)
        assert nz==0, (name,'nonzero Morse differential',nz)
        betti,fvector=betti_mod_two(faces)
        assert {d:b for d,b in betti.items() if b}==expected,(name,betti)
        assert pairs*2+sum(critical.values())==nfaces
        print('%s: faces=%d, pairs=%d, critical=%s, Morse_differential_nonzero=%d, fvector=%s, PASS' %
              (name,nfaces,pairs,dict(sorted(critical.items())),nz,dict(sorted(fvector.items()))))
    # The deletion--link cofibration determines the inclusion maps integrally:
    # C3 fault: Z^36 -> Z^44 has free cokernel Z^8.
    # C4 fault: Z^44 -> Z^44 has kernel and cokernel Z^2.
    print('TWO_EDGE_ORBITS_INTEGRAL_RELATIVE_HOMOTOPY_PASS')

if __name__=='__main__':
    main()
