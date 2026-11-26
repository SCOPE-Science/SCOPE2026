"""Reproducible finite checks for one-perfect flag-rank-metric codes.

The proof for arbitrary finite fields is algebraic and does not depend on this
program. The executable uses prime fields, constructs parity-check maps,
checks every possible weight-1/2 obstruction, and independently enumerates
all binary low-band matrices at the smallest perfect parameter pair.
"""
from itertools import combinations, product
from math import factorial


def points(q, a):
    out = {}
    for v in product(range(q), repeat=a):
        if not any(v):
            continue
        pivot = next(z for z in v if z)
        key = tuple((x * pow(pivot, -1, q)) % q for x in v)
        out[key] = key
    return sorted(out)


def add(q, *vecs):
    return tuple(sum(v[j] for v in vecs) % q for j in range(len(vecs[0])))


def scale(q, v, s):
    return tuple((s * x) % q for x in v)


def choose_check(q, a):
    P = points(q, a)
    n = len(P)
    nonzero = [v for v in product(range(q), repeat=a) if any(v)]
    F = []
    for i in range(n-1):
        span = {add(q, scale(q, P[i], x), scale(q, P[i+1], y))
                for x in range(q) for y in range(q)}
        choices = [v for v in nonzero if v not in span]
        assert len(choices) == q**a - q**2
        F.append(choices[0])
    return P, F


def syndrome(q, a, P, F, M):
    n = len(P)
    res = [0] * a
    for i in range(n):
        for k in range(a):
            res[k] = (res[k] + M[i][i] * P[i][k]) % q
    for i in range(n-1):
        for k in range(a):
            res[k] = (res[k] + M[i][i+1] * F[i][k]) % q
    return tuple(res)


def rank_prime(q, rows):
    if not rows:
        return 0
    B = [list(row) for row in rows]
    h, w = len(B), len(B[0])
    rank = 0
    for col in range(w):
        pivot = next((i for i in range(rank, h) if B[i][col] % q), None)
        if pivot is None:
            continue
        B[rank], B[pivot] = B[pivot], B[rank]
        inv = pow(B[rank][col], -1, q)
        B[rank] = [(v * inv) % q for v in B[rank]]
        for j in range(h):
            if j != rank and B[j][col]:
                z = B[j][col]
                B[j] = [(x - z*y) % q for x, y in zip(B[j], B[rank])]
        rank += 1
        if rank == h:
            break
    return rank


def weight(q, M):
    n = len(M)
    return sum(rank_prime(q, [row[i:] for row in M[:i+1]]) for i in range(n))


def verify_case(q, a):
    P, F = choose_check(q, a)
    n = (q**a - 1) // (q-1)
    assert len(P) == n
    zeros = tuple([0]*a)
    syndromes = {zeros}
    for i in range(n):
        for z in range(1, q):
            syndromes.add(scale(q, P[i], z))
    assert len(syndromes) == q**a
    checked = 0
    # Exhaustively test the classified weight-one and weight-two families.
    for i in range(n):
        for z in range(1, q):
            M = [[0]*n for _ in range(n)]
            M[i][i] = z
            assert weight(q, M) == 1
            assert syndrome(q, a, P, F, M) != zeros
            checked += 1
    for i, j in combinations(range(n), 2):
        for x in range(1, q):
            for y in range(1, q):
                M = [[0]*n for _ in range(n)]
                M[i][i], M[j][j] = x, y
                assert weight(q, M) == 2
                assert syndrome(q, a, P, F, M) != zeros
                checked += 1
    for i in range(n-1):
        for x in range(q):
            for y in range(q):
                for z in range(1, q):
                    M = [[0]*n for _ in range(n)]
                    M[i][i], M[i][i+1], M[i+1][i+1] = x, z, y
                    assert weight(q, M) == 2
                    assert syndrome(q, a, P, F, M) != zeros
                    checked += 1
    # Three diagonal positions already realize weight three in the kernel.
    triple = None
    for i, j in combinations(range(n), 2):
        u = add(q, P[i], P[j])
        if any(u):
            for k, pk in enumerate(P):
                if k in (i, j):
                    continue
                for s in range(1, q):
                    if scale(q, pk, s) == u:
                        triple = (i, j, k, s)
                        break
                if triple:
                    break
        if triple:
            break
    assert triple is not None
    i, j, k, s = triple
    M = [[0]*n for _ in range(n)]
    M[i][i], M[j][j], M[k][k] = 1, 1, -s % q
    assert syndrome(q, a, P, F, M) == zeros
    assert weight(q, M) == 3
    return checked, triple, P, F


def binary_full_band_test(P, F):
    q, a, n = 2, 3, 7
    positions = [(i,i) for i in range(n)] + [(i,i+1) for i in range(n-1)]
    counts = {0:0, 1:0, 2:0}
    for mask in range(1 << len(positions)):
        M = [[0]*n for _ in range(n)]
        for k, (i,j) in enumerate(positions):
            M[i][j] = (mask >> k) & 1
        w = weight(q, M)
        if w <= 2:
            counts[w] += 1
            if w > 0:
                assert syndrome(q, a, P, F, M) != (0,0,0)
    assert counts == {0:1, 1:7, 2:45}, counts
    # Every omitted higher superdiagonal elementary matrix has weight >= 3.
    for i in range(n):
        for j in range(i+2,n):
            M = [[0]*n for _ in range(n)]
            M[i][j] = 1
            assert weight(2, M) == j-i+1
    return counts


def count_check():
    q, a = 2, 3
    n = (q**a - 1)//(q-1)
    T = n*(n+1)//2
    GL = 1
    for j in range(a):
        GL *= (q**a-q**j)
    num_maps = factorial(n)*(q-1)**n*(q**a-q**2)**(n-1)*q**(a*(T-2*n+1))
    assert num_maps % GL == 0
    num_codes = num_maps//GL
    assert num_codes == 30*(4**6)*(2**45)
    return num_codes


if __name__ == '__main__':
    totals = 0
    for q, a in [(2,3), (2,4), (3,3), (5,3)]:
        count, triple, P, F = verify_case(q, a)
        totals += count
        print('FIELD',q,'CODIM',a,'LENGTH',len(P),'LOW_WEIGHT_TESTS',count,'TRIPLE',triple)
        if (q, a) == (2,3):
            print('BINARY_BAND_WEIGHT_0_1_2',binary_full_band_test(P, F))
    print('EXACT_BINARY_DIMENSION3_CODE_COUNT',count_check())
    print('TOTAL_LOW_WEIGHT_TESTS',totals)
    print('VERIFY_OK')
