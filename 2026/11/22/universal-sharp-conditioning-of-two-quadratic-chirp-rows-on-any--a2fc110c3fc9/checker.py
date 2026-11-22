"""Finite diagnostic checks for three-site quadratic-chirp row conditioning.

The all-prime assertion is proved analytically; these checks only test examples.
Run with: python checker.py
"""
import cmath
import itertools
import math

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
TOL = 2e-9
comparisons = 0
for p in PRIMES:
    w = cmath.exp(2j * math.pi / p)
    roots = [w ** i for i in range(p)]
    k = (p + 1) // 3
    rho = abs(1 + 2 * math.cos(2 * math.pi * k / p))
    tau = math.sqrt(5 + 4 * math.cos(2 * math.pi / p))
    values = {}
    for u in range(p):
        for v in range(p):
            if u == v == 0:
                continue
            val = abs(1 + roots[u] + roots[v])
            assert rho - TOL <= val <= tau + TOL
            values[u, v] = val
            comparisons += 1
    best = [(u, v) for (u, v), val in values.items() if abs(val - rho) < TOL]
    worst = [(u, v) for (u, v), val in values.items() if abs(val - tau) < TOL]
    assert len(best) == len(worst) == 6, (p, best, worst)
    assert set(worst) == {(0,1), (0,p-1),(1,0),(p-1,0),(1,1),(p-1,p-1)}
    # Test quadratic-phase difference maps on all supports in small dimensions,
    # and strategically selected supports at larger dimensions.
    supports = list(itertools.combinations(range(p), 3)) if p <= 13 else [
        (0, 1, 2), (0, 1, p - 1), (1, 3, p - 2), (2, p // 2, p - 1)]
    for x0, x1, x2 in supports:
        assert len({x0, x1, x2}) == 3
        uvs = set()
        for da in range(p):
            for db in range(p):
                if da == db == 0:
                    continue
                u = (da*(x1*x1-x0*x0)+db*(x1-x0))%p
                v = (da*(x2*x2-x0*x0)+db*(x2-x0))%p
                uvs.add((u,v))
        assert len(uvs) == p*p-1
        assert sum(abs(values[uv]-rho)<TOL for uv in uvs)==6
        assert sum(abs(values[uv]-tau)<TOL for uv in uvs)==6
    # Direct row-Gram eigenvalues for two label pairs.
    x = supports[0]
    for da, db in [(1,0),(0,1),(1,1)]:
        rows = [[cmath.exp(2j*math.pi*((a*j*j+b*j)%p)/p) for j in x]
                for a,b in [(0,0),(da,db)]]
        inner = sum(rows[0][j].conjugate()*rows[1][j] for j in range(3))
        eigen = (3+abs(inner),3-abs(inner))
        assert eigen[1]>TOL
        u = (da*(x[1]**2-x[0]**2)+db*(x[1]-x[0]))%p
        v = (da*(x[2]**2-x[0]**2)+db*(x[2]-x[0]))%p
        assert abs(abs(inner)-values[u,v])<TOL
    print(f'p={p:3d} best={rho:.11f} worst={tau:.11f} min-count={len(best)} max-count={len(worst)}')
print(f'CHECK_PASS primes={len(PRIMES)} phasor_comparisons={comparisons}; all support and Gram checks passed')
