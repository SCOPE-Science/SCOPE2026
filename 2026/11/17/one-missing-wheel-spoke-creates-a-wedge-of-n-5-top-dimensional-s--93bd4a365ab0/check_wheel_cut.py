"""Finite exact checks for the three-cut complex of a wheel with one missing spoke.

Only the finite instances are computationally checked; the unrestricted theorem
rests on the separate combinatorial and homotopy proof.
"""
from collections import defaultdict
from itertools import combinations


def down_closure(facets):
    faces = set()
    for f in facets:
        for k in range(len(f)+1):
            faces.update(combinations(sorted(f), k))
    return faces


def cut_facets(n, removed_spoke=True, removed_rim=False):
    hub = n
    vertices = set(range(n+1))
    adj = {v: set() for v in vertices}
    for i in range(n):
        j = (i+1) % n
        if removed_rim and i == 0:
            continue
        adj[i].add(j); adj[j].add(i)
    for i in range(n):
        if removed_spoke and i == 0:
            continue
        adj[i].add(hub); adj[hub].add(i)
    facets = []
    for triple in combinations(sorted(vertices), 3):
        seen = {triple[0]}
        queue = [triple[0]]
        while queue:
            u = queue.pop()
            for v in adj[u].intersection(triple) - seen:
                seen.add(v); queue.append(v)
        if len(seen) < 3:
            facets.append(tuple(sorted(vertices.difference(triple))))
    return facets


def mod2_reduced_betti(faces):
    by_dim = defaultdict(list)
    for f in faces:
        if f:
            by_dim[len(f)-1].append(f)
    pivots = {}
    for d, ff in by_dim.items():
        if d == 0:
            continue
        lower = {f: i for i, f in enumerate(by_dim[d-1])}
        basis = {}
        for f in ff:
            vec = 0
            for g in combinations(f, d):
                vec ^= (1 << lower[g])
            while vec:
                pivot = vec.bit_length()-1
                if pivot in basis:
                    vec ^= basis[pivot]
                else:
                    basis[pivot] = vec
                    break
        pivots[d] = len(basis)
    result = {}
    for d, ff in sorted(by_dim.items()):
        b = len(ff)-pivots.get(d,0)-pivots.get(d+1,0)-(d==0)
        if b:
            result[d] = b
    return result


def verify(n):
    vertices = set(range(n+1))
    hub = n
    # A: cut facets arising from a triple entirely in the rim.
    rim = set(range(n))
    all_facets = cut_facets(n)
    A = [f for f in all_facets if hub in f]
    B = [f for f in all_facets if hub not in f]
    nonneighbors = set(range(2,n-1))
    expected_B = {tuple(sorted(rim - {0,z})) for z in nonneighbors}
    assert set(B) == expected_B
    assert set(A)|set(B) == set(all_facets)
    Afaces = down_closure(A)
    Bfaces = down_closure(B)
    I = Afaces & Bfaces
    Y = set(range(1,n))
    expected_I = {f for f in Bfaces if len(f) <= n-4}
    bad1 = tuple(sorted(Y-{1,2}))
    bad2 = tuple(sorted(Y-{n-1,n-2}))
    expected_I.update(f for f in Bfaces if len(f)==n-3 and f not in {bad1,bad2})
    assert I == expected_I
    assert bad1 not in I and bad2 not in I
    for bad, z in [(bad1,2),(bad2,n-2)]:
        upper = tuple(sorted(Y-{z}))
        assert sum(set(bad).issubset(set(f)) for f in B) == 1
        assert set(bad).issubset(upper)
    actual_betti = mod2_reduced_betti(down_closure(all_facets))
    expected_betti = ({n-3:n-5} if n>=6 else {})
    assert actual_betti == expected_betti, (n,actual_betti)
    intact = mod2_reduced_betti(down_closure(cut_facets(n,False)))
    rim_fault = mod2_reduced_betti(down_closure(cut_facets(n,False,True)))
    assert intact == {} and rim_fault == {}
    print('n', n, 'facets',len(all_facets),'betti',actual_betti,'intersection_facets_removed',2,'intact/rim_fault_acyclic',True)


if __name__=='__main__':
    for n in range(5,13):
        verify(n)
    print('WHEEL_CUT_FINITE_CHECK_PASS')
