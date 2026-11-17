#!/usr/bin/env python3
"""Exact checks of four-column Walsh row-subset rank formulas.

Requires only the Python standard library. Arithmetic is integer-only.
The modular rank test agrees with real rank: every 4x4 sign determinant
has absolute value <=16, so the prime 101 cannot divide a nonzero minor.
"""
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def rank_mod(rows, p=101):
    a = [list(row) for row in rows]
    if not a:
        return 0
    ncol = len(a[0]); r = 0
    for j in range(ncol):
        pivot = next((i for i in range(r, len(a)) if a[i][j] % p), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j] % p, -1, p)
        for i in range(r + 1, len(a)):
            if a[i][j] % p:
                scale = a[i][j] * inv % p
                for c in range(j, ncol):
                    a[i][c] = (a[i][c] - scale * a[r][c]) % p
        r += 1
        if r == ncol: break
    return r


def walsh_row(t, T):
    return tuple(-1 if (t & j).bit_count() % 2 else 1 for j in T)


def fail_count(N, m, parallel):
    b = choose
    if parallel:
        return 4*b(3*N//4,m)-6*b(N//2,m)+4*b(N//4,m)
    return 12*b(N//2,m)+8*b(3*N//8,m)-68*b(N//4,m)+72*b(N//8,m)


def exhaustive(N, T):
    family = (T[0] ^ T[1] ^ T[2] ^ T[3]) == 0
    rows = [walsh_row(t,T) for t in range(N)]
    results = {}
    for m in range(4,N+1):
        failed = sum(rank_mod([rows[i] for i in inds]) < 4
                     for inds in combinations(range(N),m))
        wanted = fail_count(N,m,family)
        assert failed == wanted, (N,T,m,failed,wanted)
        results[m] = failed
    return family,results


def run():
    assertions = 0
    N=8
    orbit_counts={True:0,False:0}
    for T in combinations(range(N),4):
        family, res = exhaustive(N,T)
        orbit_counts[family]+=1
        assertions += len(res)
        assert res[4] in [54,12]
        assertions += 1
    assert orbit_counts == {True:14,False:56},orbit_counts
    assertions += 1
    print('N=8: all 70 four-column supports and all sample sizes 4..8 verified')
    print('N=8: affine-plane support count 14, affine-independent count 56')
    N=16
    for T in [(0,1,2,3),(0,1,2,4)]:
        f, res = exhaustive(N,T)
        assertions += len(res)
        print('N=16:', 'affine plane' if f else 'affine independent', 'm=4:',res[4],'/1820')
    # Algebraic group-incidence certificate for the independent case:
    from itertools import product
    pts=list(product((-1,1),repeat=3))
    coplanar = sum(rank_mod([(1,)+pts[i] for i in inds]) <4
                     for inds in combinations(range(8),4))
    assert coplanar == 12
    assertions += 1
    # Exact benchmark
    assert fail_count(8,4,True)==54 and fail_count(8,4,False)==12
    assertions += 2
    print('3-cube: exactly 12 coplanar four-vertex subsets')
    print('N=8,m=4: exact singularity counts 54/70 vs 12/70')
    print('PASSED',assertions,'assertions')

if __name__ == '__main__': run()
