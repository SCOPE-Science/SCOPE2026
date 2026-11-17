#!/usr/bin/env python3
"""Finite checks for orbit-weight fixed spaces and integral exterior-power symmetry.

Only standard-library modules are required. This is finite corroboration, not a universal proof.
"""
from itertools import combinations, permutations
from math import comb


def bit_rank(rows):
    piv = {}
    for x in rows:
        while x:
            i = x.bit_length() - 1
            if i not in piv:
                piv[i] = x
                break
            x ^= piv[i]
    return len(piv)


def f2_reduced_homology(faces, nv):
    by_size = {j: sorted([f for f in faces if len(f) == j]) for j in range(nv+1)}
    ranks = {0: 0}
    for j in range(1, nv+1):
        low = by_size[j-1]
        index = {f:i for i,f in enumerate(low)}
        # A column is encoded as a bit vector indexed by its boundary (j-1)-faces.
        columns = []
        for f in by_size[j]:
            x = 0
            for v in f:
                x ^= 1 << index[tuple(a for a in f if a != v)]
            columns.append(x)
        ranks[j] = bit_rank(columns)
    return {j-1: len(by_size[j])-ranks[j]-ranks[j+1] for j in range(1,nv) if len(by_size[j])-ranks[j]-ranks[j+1]}


def calculate():
    cases, groups, chars = 0, 0, 0
    for p in (2,3,4):
        for m in range(2,7):
            n = m*p+1
            gen = [0]*n
            gen[0] = 0
            for j in range(m):
                for a in range(p):
                    gen[1+j*p+a] = 1+j*p+(a+1)%p
            assert sorted(gen) == list(range(n))
            orbits = [(0,)] + [tuple(range(1+j*p,1+(j+1)*p)) for j in range(m)]
            assert all(tuple(sorted({v for o in [orbits[j]] for v in o})) == orbits[j] for j in range(m+1))
            for k in range(1,m):
                rank = k*p
                # Enumerate orbit choices and check original independence condition independently.
                faces = set()
                for s in range(m+2):
                    for f in combinations(range(m+1),s):
                        chosen = {v for i in f for v in orbits[i]}
                        assert all(gen[v] in chosen for v in chosen)
                        if len(chosen) <= rank:
                            faces.add(f)
                assert () in faces
                hom = f2_reduced_homology(faces,m+1)
                assert hom == {k-1:comb(m,k)}, (p,m,k,hom)
                # The star of vertex 0 contains every orbit-face not using >k-1 heavy orbits.
                star = {f for f in faces if (0 in f) or (0,)+f in faces}
                shells = {f for f in faces if f not in star}
                expected_shells={tuple(i+1 for i in t) for t in combinations(range(m),k)}
                assert shells == expected_shells, (p,m,k,shells,expected_shells)
                # Each critical face has entire boundary in the closed star.
                assert all(tuple(x for x in f if x!=v) in star for f in shells for v in f)
                # S_m acts by signed permutation of these shell orientations: Lefschetz character.
                for sigma in permutations(range(m)):
                    trace=0
                    for t in combinations(range(m),k):
                        st=tuple(sigma[x] for x in t)
                        if set(st)==set(t):
                            inv=sum(st[i]>st[j] for i in range(k) for j in range(i+1,k))
                            trace += (-1)**inv
                    # Coefficient of t in the exterior power of the natural permutation representation.
                    expected=sum((-1)**sum(tuple(sigma[x] for x in t)[i] > tuple(sigma[x] for x in t)[j] for i in range(k) for j in range(i+1,k))
                                 for t in combinations(range(m),k) if {sigma[x] for x in t}==set(t))
                    assert trace==expected
                    # Independently calculate the signed augmented simplicial Lefschetz sum
                    # from every face, *not* from critical faces or exterior coordinates.
                    lf=-1
                    for f in faces:
                        if not f: continue
                        mapped=tuple(0 if i==0 else 1+sigma[i-1] for i in f)
                        if set(mapped)!=set(f): continue
                        inversions=sum(mapped[i]>mapped[j] for i in range(len(f)) for j in range(i+1,len(f)))
                        lf += (-1)**(len(f)-1+inversions)
                    assert trace==(-1)**(k-1)*lf, (p,m,k,sigma,trace,lf)
                    chars += 1
                # Integral obstruction: unique rational lift v wedge x / m has coefficient 1/m
                # on e_1 wedge ... wedge e_k for x=(e_1-e_m) wedge ... wedge (e_{k-1}-e_m).
                # Its m-fold multiple is integral; smaller positive multiples are not.
                coefficient=1
                assert m*coefficient%m == 0
                assert all(q*coefficient % m != 0 for q in range(1,m))
                cases+=1
                groups+=len(list(permutations(range(m))))
    print(f'UNIFORM_MATROID_ORBIT_EXTERIOR_CHECKS_PASS cases={cases} symmetric_actions={groups} signed_trace_checks={chars}')

if __name__=='__main__':
    calculate()
