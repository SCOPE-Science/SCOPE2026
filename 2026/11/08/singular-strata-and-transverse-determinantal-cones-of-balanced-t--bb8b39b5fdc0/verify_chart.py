#!/usr/bin/env python3
"""Finite exact Plucker-minor checks for a projected Grassmannian chart.

The all-rank theorem is proved in the accompanying mathematical text;
these finite computations test its local coordinate identities.
"""
from itertools import combinations, permutations
from math import comb


def minors(d):
    a = [f"a{j}" for j in range(2, d+1)]
    b = [f"b{i}" for i in range(2, d+1)]
    z = {(i, j): f"z{i}_{j}" for i in range(2, d+1) for j in range(2, d+1)}
    M = [[None] * (2*d) for _ in range(d)]
    M[0][0] = "1"
    M[0][d] = "c"
    for j in range(2, d+1):
        M[0][j-1] = f"a{j}"
    for i in range(2, d+1):
        M[i-1][d+i-1] = "1"
        M[i-1][d] = f"b{i}"
        for j in range(2, d+1):
            M[i-1][j-1] = z[i,j]

    def det(indices):
        out = {}
        for p in permutations(range(d)):
            vals = [M[r][indices[p[r]]] for r in range(d)]
            if None in vals:
                continue
            mon = tuple(sorted(v for v in vals if v != "1"))
            inv = sum(p[i] > p[j] for i in range(d) for j in range(i+1,d))
            out[mon] = out.get(mon,0) + (-1 if inv%2 else 1)
        return {k:v for k,v in out.items() if v}

    pivot = tuple([0] + list(range(d+1,2*d)))
    hidden = tuple(range(d,2*d))
    assert det(pivot) == {():1}
    assert det(hidden) == {("c",): 1}, (d, det(hidden))
    checks = 0
    for ix in combinations(range(2*d), d):
        if ix == hidden:
            continue
        poly = det(ix)
        assert not any("c" in mon and not any(v.startswith("z") for v in mon) for mon in poly), (d, ix, poly)
        checks += 1

    for j in range(2,d+1):
        ix = tuple(sorted([j-1]+list(range(d+1,2*d))))
        assert det(ix) in ({(f"a{j}",):1}, {(f"a{j}",):-1})
    for i in range(2,d+1):
        ix = tuple(sorted([0,d]+[d+t-1 for t in range(2,d+1) if t!=i]))
        assert det(ix) in ({(f"b{i}",):1}, {(f"b{i}",):-1})
        for j in range(2,d+1):
            ixz = tuple(sorted([0,j-1]+[d+t-1 for t in range(2,d+1) if t!=i]))
            assert det(ixz) in ({(f"z{i}_{j}",):1}, {(f"z{i}_{j}",):-1})
            ixw = tuple(sorted([j-1,d]+[d+t-1 for t in range(2,d+1) if t!=i]))
            poly = det(ixw)
            pair1 = tuple(sorted((f"a{j}",f"b{i}")))
            pair2 = tuple(sorted(("c",f"z{i}_{j}")))
            assert set(poly)=={pair1,pair2} and abs(poly[pair1])==abs(poly[pair2])==1 and poly[pair1]==-poly[pair2], (d,ixw,poly)
    return checks


if __name__ == "__main__":
    for d in range(2, 7):
        num = minors(d)
        k = (d-1)**2
        for r in range(8):
            left = (r+1)*comb(k-1+r,r)
            right = comb(k+r,r)+(k-1)*(comb(k+r-1,r-1) if r else 0)
            assert left == right, (d,r,left,right)
        print(f"d={d} retained={num} transverse_k={k} CHART_AND_HILBERT_OK")
    print("ALL_EXACT_PLUCKER_CHECKS_OK")
    print("CERTIFICATE_OK")
