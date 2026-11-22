#!/usr/bin/env python3
"""Finite checks for pentagonal independence-complex orbit reduction.

The topological theorem is established by the proof.  This script checks
its combinatorial orbit statement in small crosspolytope-boundary fibres,
and verifies the cellular homology predicted for the projective join.
"""
from itertools import product
from collections import defaultdict

def fibre_faces(d):
    # H=(d+1) disjoint edges. Each index has 0, 1, or 2 as choice.
    for choices in product((0,1,2), repeat=d+1):
        yield tuple((i, x-1) for i,x in enumerate(choices) if x)

def encoded_faces(d, shore):
    fs=list(fibre_faces(d))
    zero=((),)
    if len(shore)==1:
        for f in fs:
            if f: yield tuple(sorted((shore[0],j,b) for j,b in f))
    elif len(shore)==2:
        a,b=shore
        for f in fs:
            for g in fs:
                if f or g:
                    yield tuple(sorted([(a,j,v) for j,v in f]+[(b,j,v) for j,v in g]))
    else:
        raise ValueError('shore count')

def dihedral_images(face):
    # rotations and reflections of the five labelled shores
    for sign in (1,-1):
        for shift in range(5):
            yield tuple(sorted(((sign*a+shift)%5,j,b) for a,j,b in face))

def orbit_rep(face): return min(dihedral_images(face))
def stabilizer_rep(face):
    # Stabilizer of unordered shore pair {0,2}: id and i -> 2-i.
    return min(face,tuple(sorted(((2-a)%5,j,b) for a,j,b in face)))

def test(d):
    # Every independent face has outer support contained in one pentagon diagonal.
    supports=[(i,(i+2)%5) for i in range(5)]
    all_faces=set()
    for pair in supports: all_faces.update(encoded_faces(d,pair))
    faces_in_chosen=set(encoded_faces(d,(0,2)))
    orbit_to_stabilizer=defaultdict(set)
    for face in faces_in_chosen:
        orbit_to_stabilizer[orbit_rep(face)].add(stabilizer_rep(face))
    global_orbits={orbit_rep(f) for f in all_faces}
    assert global_orbits==set(orbit_to_stabilizer), (d,'surjection')
    assert all(len(reps)==1 for reps in orbit_to_stabilizer.values()), (d,'injection')
    assert len(global_orbits)==len({stabilizer_rep(f) for f in faces_in_chosen})
    print(f'd={d}: faces={len(all_faces)}, dihedral_orbits={len(global_orbits)}, '
          f'stable_pair_faces={len(faces_in_chosen)}: PASS')

def projective_homology(d):
    # The integral cellular differential for RP^d is multiplication by
    # 0 in odd degrees and 2 in positive even degrees.
    groups={}
    for j in range(1,d+1):
        incoming = 2 if (j+1<=d and (j+1)%2==0) else 0
        outgoing = 2 if (j%2==0) else 0
        if outgoing==2: continue
        if incoming==2: groups[d+1+j]='Z/2'
        else: groups[d+1+j]='Z'
    # Note the degree-0 cell of RP^d is connected, reduced H_0=0.
    expected = {d+1+j:'Z/2' for j in range(1,d,2)}
    if d%2:expected[2*d+1]='Z'
    assert groups==expected, (d,groups,expected)
    print(f'd={d}: reduced integral homology {groups}: PASS')

if __name__=='__main__':
    for d in range(4): test(d)
    for d in range(2,9): projective_homology(d)
    print('FINITE ORBIT / HOMOLOGY CROSS-CHECKS PASS')
