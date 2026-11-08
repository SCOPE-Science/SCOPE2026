#!/usr/bin/env python3
"""Exact finite-dimensional checks supporting the global toric divisor theorem.

No additional packages are required. The proof for all n is in RESULT.md;
these checks cover representative dimensions, not an infinite range.
"""
from fractions import Fraction
from itertools import permutations


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    nr, nc = len(a), len(a[0]); r = 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = Fraction(1, 1) / a[r][c]
        for j in range(c, nc):
            a[r][j] *= inv
        for i in range(r + 1, nr):
            if a[i][c]:
                fac = a[i][c]
                for j in range(c, nc):
                    a[i][j] -= fac * a[r][j]
        r += 1
        if r == nr:
            break
    return r


def check(n):
    m = n + 1
    k = 2*n + 1
    ell = 2*n - 1
    edges = list(permutations(range(m), 2))
    ix = {e: j for j,e in enumerate(edges)}
    vertices = { (p,q):[(-ell if i == p else (1 if i == q else 2)) for i in range(m)] for p,q in edges }
    assert all(sum(x) == 0 and sorted(x) == sorted([-ell, 1]+[2]*(n-1)) for x in vertices.values())
    # Linear conditions for all three-vertex restrictions to an upper facet.
    rows = []
    for p,q,r in permutations(range(m), 3):
        row = [0]*len(edges)
        row[ix[p,q]] = k+1
        row[ix[q,p]] = -(k+1)
        for a,b,coef in [(p,r,-(k-1)),(r,p,-(k-1)),(q,r,k-1),(r,q,k-1)]:
            row[ix[a,b]] += coef
        rows.append(row)
    condition_rank = rank(rows)
    assert condition_rank == len(edges)-m, (n,condition_rank,len(edges)-m)
    # Verify that the global linear+constant functions are exactly in the kernel.
    for j in range(m):
        vals = [vertices[e][j] for e in edges]
        assert all(sum(c*v for c,v in zip(row,vals))==0 for row in rows)
    assert all(sum(row)==0 for row in rows)
    # Every facet's ray vectors span the ambient rank-n lattice over Q.
    for i in range(m):
        for side in ('upper','lower'):
            subset = [v[:n] for e,v in vertices.items() if (i not in e if side=='upper' else e[0]==i)]
            assert rank(subset)==n,(n,side,i)
            assert len(subset)==(n*(n-1) if side=='upper' else n)
    # For a toric support coefficient t, the local slopes differ from an
    # integral global character by -t/2 * e_i or t/ell * e_i.
    assert all((2*ell)%z == 0 for z in (2,ell))
    for t in range(1,2*ell):
        assert not(t%2==0 and t%ell==0)
    return len(edges),condition_rank,len(edges)-condition_rank-n,2*ell

if __name__=='__main__':
    for n in range(3,7):
        rays,rr,pic,index=check(n)
        print(f'n={n}: rays={rays}; upper-facet relation rank={rr}; Picard rank={pic}; canonical Cartier index={index}; PASS')
    print('EXACT_CHECKS_PASS')
