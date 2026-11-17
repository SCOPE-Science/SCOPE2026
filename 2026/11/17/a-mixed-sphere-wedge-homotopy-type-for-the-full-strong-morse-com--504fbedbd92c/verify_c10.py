#!/usr/bin/env python3
"""Independent orientation and exact Morse verification for the full strong complex of C_10.

Run: python3 verify_c10.py gradients.txt
The text file should be produced by enumerate_orders.cpp; no third-party Python packages.
"""
import collections
import functools
import pathlib
import sys

N = 10
MATCH_ORDER = (19, 1, 13, 9, 10, 8, 3, 6, 12, 15, 17, 16, 4, 18, 0, 11, 5, 2, 7, 14)
EXPECTED_F_VECTOR = (20, 160, 660, 1520, 2000, 1470, 560, 90)
EXPECTED_CRITICAL = (70689, 86097, 141864, 524288)  # includes the vertex with incidence label 19

def orientation_gradients():
    output = set()
    for signs in range(1, (1 << N) - 1):  # omit the two directed full cycles
        bits = 0
        for v in range(N):
            e_prev = (signs >> ((v - 1) % N)) & 1
            e_next = (signs >> v) & 1
            if e_prev == e_next:
                bits |= 1 << (2*v + (0 if e_prev else 1))
        output.add(bits)
    return output

def faces_from_gradients(gradients):
    faces = set()
    for g in gradients:
        sub = g
        while sub:
            faces.add(sub)
            sub = (sub-1) & g
    return faces

def boundary(f):
    # Sorted increasing incidence labels give the standard orientation.
    return [(f ^ (1 << j), (-1)**i)
            for i,j in enumerate(k for k in range(2*N) if f & (1<<k))]

def integral_morse_boundary(critical, pairs, upper, cell):
    critical = set(critical)
    @functools.lru_cache(maxsize=None)
    def project(f):
        if f in critical:
            return {f:1}
        if f in upper:
            return {}
        if f not in pairs:
            raise AssertionError(f'unmatched unclassified face {f}')
        u = pairs[f]
        signed_facets = dict(boundary(u))
        assert signed_facets[f] in (-1,1)
        acc = collections.defaultdict(int)
        for sub, coeff in signed_facets.items():
            if sub == f: continue
            for basis, val in project(sub).items():
                acc[basis] -= signed_facets[f] * coeff * val
        return {k:v for k,v in acc.items() if v}
    total = collections.defaultdict(int)
    for facet, coeff in boundary(cell):
        for basis, val in project(facet).items():
            total[basis] += coeff*val
    return {k:v for k,v in total.items() if v}

def original_mod2_homology(faces):
    by_size=collections.defaultdict(list)
    for face in faces:by_size[face.bit_count()].append(face)
    ranks = {1:0}
    for k in range(2, 9):
        domain=by_size[k];codomain=by_size[k-1]
        index={f:i for i,f in enumerate(codomain)}
        pivots={}
        for upper in domain:
            col=0
            for lower,_ in boundary(upper):col ^= 1<<index[lower]
            while col:
                lead=col.bit_length()-1
                if lead not in pivots:
                    pivots[lead]=col
                    break
                col ^= pivots[lead]
        ranks[k]=len(pivots)
    betti={k-1:len(by_size[k])-ranks[k]-ranks.get(k+1,0)
           for k in range(1,9)}
    betti[0]-=1  # reduced homology
    return {k:v for k,v in betti.items() if v},ranks

def main():
    if len(sys.argv)!=2:
        raise SystemExit('usage: python3 verify_c10.py gradients.txt')
    actual=list(map(int,pathlib.Path(sys.argv[1]).read_text().split()))
    assert len(actual)==1021 and len(set(actual))==1021
    gradients=orientation_gradients()
    assert len(gradients)==1021 and set(actual)==gradients
    faces=faces_from_gradients(gradients)
    assert len(faces)==6480
    ordered=sorted(faces,key=lambda f:(f.bit_count(),f))
    by_size=collections.Counter(f.bit_count() for f in faces)
    assert tuple(by_size[k] for k in range(1,9)) == EXPECTED_F_VECTOR
    # Lexicographically staged incidence toggles. Every successful pair is a cover.
    unmatched=set(faces);pairs={}
    for bit_index in MATCH_ORDER:
        bit=1<<bit_index
        for f in ordered:
            if f not in unmatched or f&bit:
                continue
            u=f|bit
            if u in unmatched:
                pairs[f]=u
                unmatched.remove(f)
                unmatched.remove(u)
    critical=unmatched
    assert len(pairs)==3238 and len(critical)==4
    assert set(critical)==set(EXPECTED_CRITICAL), (sorted(critical), EXPECTED_CRITICAL)
    assert collections.Counter(f.bit_count()-1 for f in critical)=={0:1,4:1,5:2}
    # Direct global acyclicity: reverse exactly the matching cover arrows.
    indeg={f:0 for f in faces};arcs=collections.defaultdict(list)
    cover_count=0
    for u in faces:
        for f,_ in boundary(u):
            if not f:continue
            a,b=(f,u) if pairs.get(f)==u else (u,f)
            arcs[a].append(b);indeg[b]+=1;cover_count+=1
    queue=collections.deque(x for x in faces if indeg[x]==0);visited=0
    while queue:
        x=queue.popleft();visited+=1
        for y in arcs[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert visited==6480
    # Exact integer cellular boundary of the two critical five-cells.
    upper=set(pairs.values())
    large=sorted((x for x in critical if x.bit_count()==6))
    boundary_values={x:integral_morse_boundary(critical,pairs,upper,x) for x in large}
    assert all(not b for b in boundary_values.values())
    betti,ranks=original_mod2_homology(faces)
    assert betti=={4:1,5:2},betti
    print('C10_ORIENTATION_AND_PERMUTATION_GRADIENTS',len(gradients))
    print('NONEMPTY_FACES',len(faces),'F_VECTOR',EXPECTED_F_VECTOR)
    print('MATCHED_PAIRS',len(pairs),'CRITICAL',sorted(critical))
    print('HASSE_COVERS',cover_count,'ACYCLIC_VISITED',visited)
    print('INTEGRAL_MORSE_D5',[[boundary_values[x].get(y,0) for x in large]
                                 for y in critical if y.bit_count()==5])
    print('ORIGINAL_F2_BETTI',betti,'BOUNDARY_RANKS',ranks)
    print('FULL_STRONG_C10_WEDGE_PASS')
if __name__=='__main__':main()
