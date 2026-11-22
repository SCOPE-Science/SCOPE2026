#!/usr/bin/env python3
"""Independent finite verification of prism-involution fixed-space models.

Uses Python 3 standard library only. Structural proofs in RESULT.md cover all n.
"""
from collections import defaultdict
from itertools import combinations


def prism(n):
    vertices = {(i, a) for i in range(n) for a in (0, 1)}
    edges = set()
    for i in range(n):
        edges.add(frozenset(((i, 0), (i, 1))))
        for a in (0, 1):
            edges.add(frozenset(((i, a), ((i+1) % n, a))))
    return vertices, edges


def involution(n, kind, axis=0):
    if kind == 'swap':
        return lambda x: (x[0], 1-x[1])
    if kind in ('reflect', 'reflect_swap'):
        return lambda x: ((axis-x[0]) % n, x[1] ^ (kind == 'reflect_swap'))
    if kind in ('halfturn', 'halfturn_swap'):
        assert n % 2 == 0
        return lambda x: ((x[0]+n//2) % n, x[1] ^ (kind == 'halfturn_swap'))
    raise ValueError(kind)


def model(n, kind, axis=0):
    vertices, edges = prism(n)
    g = involution(n, kind, axis)
    unseen = set(vertices)
    orbits = []
    while unseen:
        v = min(unseen)
        orb = frozenset((v, g(v)))
        assert g(g(v)) == v
        unseen.difference_update(orb)
        if not any(edge <= orb for edge in edges):
            orbits.append(orb)
    orbit_edges = set()
    for i, oi in enumerate(orbits):
        for j in range(i):
            oj = orbits[j]
            if any((edge & oi and edge & oj) for edge in edges):
                orbit_edges.add(frozenset((i,j)))
    return orbits, orbit_edges


def representatives(n, kind, axis=0):
    if kind in ('halfturn', 'halfturn_swap'):
        m = n//2
        return [(j,a) for j in range(m) for a in (0,1)]
    if kind == 'swap':
        return []
    k=n//2
    if n%2:  # representative from the fixed vertex to the opposite folded edge
        js = list(range(k)) if kind == 'reflect' else list(range(1,k+1))
    elif axis%2 == 0:
        js = list(range(k+1)) if kind == 'reflect' else list(range(1,k))
    else:
        js = list(range(2,k)) if kind == 'reflect' else list(range(1,k+1))
    return [(j,a) for j in js for a in (0,1)]


def expected_edges(n, kind, axis, reps):
    if kind == 'swap':
        return set()
    if kind in ('reflect', 'reflect_swap'):
        m=len(reps)//2
        edges=set()
        for j in range(m):
            edges.add(frozenset((2*j,2*j+1)))
            if j+1<m:
                for a in (0,1):
                    edges.add(frozenset((2*j+a,2*(j+1)+a)))
        return edges
    m=n//2
    edges=set()
    for j in range(m):
        edges.add(frozenset((2*j,2*j+1)))
        for a in (0,1):
            if j+1 < m:
                edges.add(frozenset((2*j+a,2*(j+1)+a)))
            else:
                end_a=a ^ (kind=='halfturn_swap')
                edges.add(frozenset((2*j+a,end_a)))
    return edges


def verify_orbit_model(n, kind, axis=0):
    actual_orbs,actual_edges=model(n,kind,axis)
    reps=representatives(n,kind,axis)
    g=involution(n,kind,axis)
    named=[frozenset((v,g(v))) for v in reps]
    assert len(named) == len(set(named)) == len(actual_orbs)
    assert set(named) == set(actual_orbs), (n,kind,axis,named,actual_orbs)
    index={orb:i for i,orb in enumerate(actual_orbs)}
    remapped={frozenset((index[named[i]],index[named[j]])) for e in expected_edges(n,kind,axis,reps)
              for i,j in [tuple(e)]}
    assert actual_edges == remapped, (n,kind,axis,actual_edges,remapped)
    return len(actual_orbs),len(actual_edges),actual_edges


def faces_and_betti(nvertices, edges):
    adj=[0]*nvertices
    for e in edges:
        i,j=tuple(e)
        adj[i]|=1<<j
        adj[j]|=1<<i
    faces=[0]
    for i in range(nvertices):
        faces += [f | (1<<i) for f in faces if not (adj[i] & f)]
    groups=defaultdict(list)
    for f in faces:groups[f.bit_count()].append(f)
    ranks={}
    for size in range(1, max(groups, default=0)+1):
        prev={f:j for j,f in enumerate(groups[size-1])}
        pivots={};rank=0
        for f in groups[size]:
            col=0
            for i in range(nvertices):
                if f & (1<<i):
                    col ^= 1 << prev[f^(1<<i)]
            while col:
                p=col.bit_length()-1
                if p not in pivots:
                    pivots[p]=col
                    rank+=1
                    break
                col ^= pivots[p]
        ranks[size]=rank
    betti={}
    for size in groups:
        b=len(groups[size])-ranks.get(size,0)-ranks.get(size+1,0)
        if b:betti[size-1]=b
    return len(faces),betti


def predicted(n,kind,axis=0):
    if kind=='swap':return {-1:1}
    if kind in ('reflect','reflect_swap'):
        return {(len(representatives(n,kind,axis))//2-1)//2:1}
    m=n//2
    q,r=divmod(m,4)
    if kind=='halfturn':
        d=(2*q-1 if r in (0,1) else 2*q if r==2 else 2*q+1)
        return {d:3 if r==0 else 1}
    d=(2*q-1 if r==0 else 2*q)
    return {d:3 if r==2 else 1}


def main():
    configs=0; graph_edges=0; face_total=0; homology_checks=0
    for n in range(5,19):
        specs=[('swap',0),('reflect',0),('reflect_swap',0)]
        if n%2==0:
            specs += [('reflect',1),('reflect_swap',1),('halfturn',0),('halfturn_swap',0)]
        for kind,axis in specs:
            nv,ne,edges=verify_orbit_model(n,kind,axis)
            graph_edges+=ne;configs+=1
            if n<=14:
                faces,betti=faces_and_betti(nv,edges)
                assert betti==predicted(n,kind,axis),(n,kind,axis,betti,predicted(n,kind,axis))
                face_total+=faces;homology_checks+=1
    print(f'ALL_CIRCULAR_INVOLUTION_CHECKS_OK: orbit_graphs={configs}, graph_edges={graph_edges}, '
          f'homology_cases={homology_checks}, faces={face_total}')

if __name__=='__main__':main()
