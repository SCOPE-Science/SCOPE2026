#!/usr/bin/env python3
"""Exact integral homology certificate for polygon noncrossing-matching reflection loci.

Usage: python noncrossing_reflection_verify.py
Dependency: sympy>=1.12. Computational ranges are explicitly finite.
"""
from itertools import combinations
from collections import defaultdict
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def chords_conflict(a, b, n):
    if len(set(a+b)) < 4:
        return True
    x,y=sorted(a);u,v=sorted(b)
    # Independent implementation: endpoints alternate around the boundary.
    return (x<u<y<v) or (u<x<v<y)

def independently_cross(a, b, n):
    if len(set(a+b))<4:
        return True
    x,y=a; u,v=b
    def between(z,p,q):
        return 0 < (z-p)%n < (q-p)%n
    return (between(u,x,y)!=between(v,x,y)) and (between(x,u,v)!=between(y,u,v))

def check_chord_rule():
    count=0
    for n in range(3,13):
        edges=list(combinations(range(n),2))
        for a,b in combinations(edges,2):
            assert chords_conflict(a,b,n)==independently_cross(a,b,n), (n,a,b)
            count+=1
    return count

def orbit_complex(n, k):
    assert n >= 2
    edges=list(combinations(range(n), 2))
    def reflect(edge):
        return tuple(sorted(((k-edge[0])%n,(k-edge[1])%n)))
    seen=set()
    admissible=[]
    for e in edges:
        if e in seen: continue
        orbit=tuple(sorted(set((e, reflect(e)))))
        seen.update(orbit)
        if len(orbit)==2 and chords_conflict(orbit[0],orbit[1],n):
            continue
        admissible.append(orbit)
    conflicts={frozenset((i,j)) for i,j in combinations(range(len(admissible)),2)
      if any(chords_conflict(a,b,n) for a in admissible[i] for b in admissible[j])}
    return admissible, conflicts

def enumerate_faces(orbits, conflicts):
    neighbor=[0]*len(orbits)
    for pair in conflicts:
        a,b=sorted(pair)
        neighbor[a]|=1<<b
        neighbor[b]|=1<<a
    faces=defaultdict(list)
    def recurse(candidate, chosen):
        faces[len(chosen)-1].append(chosen)
        while candidate:
            bit=candidate & -candidate
            i=bit.bit_length()-1
            candidate ^= bit
            recurse(candidate & ~neighbor[i], chosen+(i,))
    recurse((1<<len(orbits))-1, ())
    return dict(faces)

def boundary(faces, dimension):
    lower=faces.get(dimension-1,[])
    higher=faces.get(dimension,[])
    lookup={face:i for i,face in enumerate(lower)}
    entries={}
    for col,face in enumerate(higher):
        for pos in range(len(face)):
            entries[(lookup[face[:pos]+face[pos+1:]],col)]=(-1)**pos
    return SparseMatrix(len(lower),len(higher),entries)

def integral_homology(n,k):
    orbits,conflicts=orbit_complex(n,k)
    faces=enumerate_faces(orbits,conflicts)
    max_d=max(faces)
    ranks={0:1 if faces.get(-1) else 0}
    nonunits=[]
    boundaries={}
    for d in range(1,max_d+1):
        mat=boundary(faces,d)
        boundaries[d]=mat
        diagonal=smith_normal_form(mat,domain=ZZ)
        factors=[abs(int(diagonal[i,i])) for i in range(min(diagonal.shape)) if diagonal[i,i]!=0]
        ranks[d]=len(factors)
        nonunits += [(d,v) for v in factors if v!=1]
    for d in range(2,max_d+1):
        assert boundaries[d-1]*boundaries[d] == SparseMatrix(boundaries[d-1].rows,boundaries[d].cols,{})
    betti={d: len(faces.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)
           for d in range(0,max_d+1)}
    betti={d:b for d,b in betti.items() if b}
    return len(orbits),len(conflicts),[len(faces.get(i,[])) for i in range(0,max_d+1)],ranks,nonunits,betti

def main():
    independent_pairs=check_chord_rule()
    print('INDEPENDENT_CHORD_RULE_PAIRS',independent_pairs)
    tests=0
    print('n axis orbits conflicts nonzero_reduced_betti nonunit_boundary_factors',flush=True)
    for n in range(3,13):
        ks=(0,) if n%2 else (0,1)
        for k in ks:
            orbits,conflicts,fvec,ranks,nonunit,betti=integral_homology(n,k)
            assert not nonunit, (n,k,nonunit)
            if n<=11:
                assert len(betti)<=1,(n,k,betti)
            if (n,k)==(12,0):
                assert betti=={1:3}
            if (n,k)==(12,1):
                assert (orbits,conflicts,fvec)==(21,125,[21,85,100,48,11,1])
                assert ranks=={0:1,1:20,2:61,3:38,4:10,5:1}
                assert betti=={1:4,2:1}
            tests+=1
            print(n,k,orbits,conflicts,betti,len(nonunit),flush=True)
    print('FINAL_N12_EDGE_AXIS_F_VECTOR 21 85 100 48 11 1')
    print('FINAL_N12_EDGE_AXIS_BOUNDARY_RANKS 20 61 38 10 1')
    print('FINAL_N12_EDGE_AXIS_REDUCED_HOMOLOGY H1=Z^4 H2=Z')
    print('FIRST_MIXED_DEGREE_REFLECTION_LOCUS N=12 EDGE_AXIS')
    print('CASES_CHECKED',tests)
    print('NONCROSSING_REFLECTION_INTEGRAL_CERTIFICATE_PASS')
if __name__=='__main__':
    main()
