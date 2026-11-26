#!/usr/bin/env python3
"""Reproduce supplementary finite checks for low-band path observation determinants."""
import math

def prod(xs):
    result = 1.0
    for x in xs:
        result *= x
    return result

def ratio(N, m, j):
    if j in (0, N - 1):
        return 1.0
    return (2.0 ** (m / 2.0)) * abs(prod(math.cos(math.pi * j * k / (N - 1)) for k in range(1, m)))

def expected(N, m):
    L = N - 1
    if m == 2:
        return ([0, L] if N == 3 else list(range(N)) if N == 4 else [1, L - 1])
    if m == 3:
        return ([0, L] if N <= 6 else [1, L - 1])
    if N == 4:
        return list(range(N))
    if N in (5, 6, 8):
        return [0, L]
    if N == 7:
        return [0, 2, 4, 6]
    if N == 9:
        return [0, 1, 3, 5, 7, 8]
    return [1, L - 1]

def determinant(rows):
    a = [list(row) for row in rows]
    n = len(a)
    answer = 1.0
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < 1e-14:
            return 0.0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            answer = -answer
        p = a[k][k]
        answer *= p
        for i in range(k + 1, n):
            f = a[i][k] / p
            for j in range(k + 1, n):
                a[i][j] -= f * a[k][j]
    return answer

def psi(N, k, j):
    L = N - 1
    deg = 1 if j in (0, L) else 2
    if k == 0:
        return math.sqrt(deg / (2 * L))
    if k == L:
        return ((-1) ** j) * math.sqrt(deg / (2 * L))
    return math.sqrt(deg / L) * math.cos(math.pi * k * j / L)

def check():
    cases = 0
    for m in (2, 3, 4):
        for N in range(max(3, m), 201):
            ratios = [ratio(N, m, j) for j in range(N)]
            top = max(ratios)
            winners = [j for j, v in enumerate(ratios) if abs(v - top) < 1e-9]
            assert winners == expected(N, m), (N, m, winners)
            for j in range(N):
                assert abs(ratios[j] - ratios[N - 1 - j]) < 1e-10
            cases += 1
    direct = 0
    for m in (2, 3, 4):
        for N in range(max(3, m), 23):
            L = N - 1
            # Heat spectral multiplier; the time step rescales with graph size.
            lam = [math.exp(-0.5 * L * L * (1 - math.cos(math.pi * k / L))) for k in range(m)]
            vander = prod((lam[a] - lam[b]) for a in range(m) for b in range(a + 1, m))
            for j in range(N):
                rows = [[lam[k] ** t * psi(N, k, j) for k in range(m)] for t in range(m)]
                obs_det = determinant(rows)
                identity_det = vander * prod(psi(N, k, j) for k in range(m))
                assert math.isclose(abs(obs_det), abs(identity_det), rel_tol=5e-8, abs_tol=1e-12), (N, m, j, obs_det, identity_det)
                direct += 1
    rt = math.sqrt(7)
    zminus, zplus = (5 - rt) / 12, (5 + rt) / 12
    p = lambda z: z * (2 * z - 1) * (4 * z - 3)
    assert math.isclose(p(zminus), (10 + 7 * rt) / 108, abs_tol=1e-14)
    assert math.isclose(p(zplus), (10 - 7 * rt) / 108, abs_tol=1e-14)
    assert p(7 / 8) == 21 / 64
    assert (10 + 7 * rt) / 108 < 21 / 64
    print(f'VERIFY_OK {cases} optimizer comparisons, {direct} direct heat-Vandermonde determinants, exact stationary identities')

if __name__ == '__main__':
    check()
