#!/usr/bin/env python3
"""Exact, dependency-free certificate for the Wiman quintuple Levi graph.

Constructs the canonical A6 incidence graph of reflection lines and
quintuple-point stabilizers, checks the spectrum and two sink-independent
prime-local Smith computations. Requires only Python 3.8+.
"""
from collections import Counter, deque
from itertools import permutations
from math import prod

IDENTITY = tuple(range(6))

def compose(a, b):
    return tuple(a[b[i]] for i in range(6))

def inverse(a):
    return tuple(a.index(i) for i in range(6))

def power(a, k):
    result = IDENTITY
    for _ in range(k):
        result = compose(result, a)
    return result

def even(a):
    return sum(a[i] > a[j] for i in range(6) for j in range(i+1, 6)) % 2 == 0

def order(a):
    for k in range(1, 6):
        if power(a, k) == IDENTITY:
            return k
    raise AssertionError('unexpected permutation order')

def matmul(A, B):
    n, m, s = len(A), len(B[0]), len(B)
    out = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(s):
            if A[i][k]:
                a = A[i][k]
                for j in range(m):
                    out[i][j] += a * B[k][j]
    return out

def shift(A, d):
    return [[v + (d if i == j else 0) for j, v in enumerate(row)] for i, row in enumerate(A)]

def primary_valuations(R, p, determinant_valuation):
    """Local Smith exponents by legitimate unit-pivot elimination over Z/p^E.

    When no unit remains, all entries are divisible by p and division
    raises the current Smith valuation. E > v_p(det) prevents truncation.
    """
    n = len(R)
    A = [[v for v in row] for row in R]
    modulus = p ** (determinant_valuation + 1)
    exponent = 0
    vals = []
    while n:
        pivot = None
        for i in range(n):
            for j in range(n):
                if A[i][j] % p:
                    pivot = (i, j)
                    break
            if pivot is not None:
                break
        if pivot is None:
            assert modulus % p == 0 and exponent <= determinant_valuation
            assert all(x % p == 0 for row in A for x in row)
            A = [[x // p for x in row] for row in A]
            modulus //= p
            exponent += 1
            continue
        i, j = pivot
        A[0], A[i] = A[i], A[0]
        for row in A:
            row[0], row[j] = row[j], row[0]
        inv = pow(A[0][0], -1, modulus)
        top = A[0]
        B = []
        for row in A[1:]:
            multiplier = row[0] * inv % modulus
            B.append([(row[h] - multiplier * top[h]) % modulus
                      for h in range(1, n)])
        A = B
        n -= 1
        vals.append(exponent)
    assert len(vals) == len(R)
    assert sum(vals) == determinant_valuation
    assert vals == sorted(vals)
    return vals

def main():
    G = [a for a in permutations(range(6)) if even(a)]
    assert len(G) == 360
    involutions = sorted(a for a in G if order(a) == 2)
    fifths = sorted({tuple(sorted(power(a,k) for k in range(1,5)))
                     for a in G if order(a) == 5})
    assert len(involutions) == 45 and len(fifths) == 36
    incidence = [[0] * 36 for _ in range(45)]
    for i, t in enumerate(involutions):
        for j, subgroup in enumerate(fifths):
            a = subgroup[0]
            if compose(compose(t, a), t) == inverse(a):
                incidence[i][j] = 1
            # Independently compare using set-normalization, not just inversion.
            conjugated = {compose(compose(t, b), t) for b in subgroup}
            assert bool(incidence[i][j]) == (conjugated == set(subgroup))
    assert all(sum(row) == 4 for row in incidence)
    assert all(sum(incidence[i][j] for i in range(45)) == 5 for j in range(36))

    N = [[sum(incidence[i][k] * incidence[j][k] for k in range(36))
          for j in range(45)] for i in range(45)]
    assert all(N[i][i] == 4 for i in range(45))
    assert Counter(N[i][j] for i in range(45)
                   for j in range(i+1, 45)) == {0:630, 1:360}
    assert sum(N[i][i] for i in range(45)) == 180
    assert sum(x*x for row in N for x in row) == 1440
    # A polynomial identity verifies all eigenvalues by exact integer arithmetic.
    P = N
    for d in (5, 8, 20):
        P = matmul(P, shift(N, -d))
    assert all(x == 0 for row in P for x in row)
    # Hence the B B^t eigenmultiplicities are 20^1 8^10 5^16 0^18.
    graph = [[] for _ in range(81)]
    for i in range(45):
        for j in range(36):
            if incidence[i][j]:
                graph[i].append(45+j)
                graph[45+j].append(i)
    reached = {0}
    todo = deque([0])
    while todo:
        for v in graph[todo.popleft()]:
            if v not in reached:
                reached.add(v)
                todo.append(v)
    assert len(reached) == 81

    L = [[0] * 81 for _ in range(81)]
    for v in range(81):
        L[v][v] = len(graph[v])
        for w in graph[v]:
            L[v][w] = -1
    tree_valuations = {2:56, 3:24, 5:25}
    answer = None
    for sink in (0, 80):
        R = [[L[i][j] for j in range(81) if j != sink]
             for i in range(81) if i != sink]
        parts = {p:primary_valuations(R,p,e)
                 for p,e in tree_valuations.items()}
        assert Counter(parts[2]) == {0:52,1:8,2:12,3:8}
        assert Counter(parts[3]) == {0:64,1:8,2:8}
        assert Counter(parts[5]) == {0:63,1:9,2:8}
        factors = [prod(p**parts[p][k] for p in (2,3,5))
                   for k in range(80)]
        assert factors == sorted(factors)
        assert all(factors[k+1] % factors[k] == 0 for k in range(79))
        assert Counter(factors) == {1:52,2:8,4:3,20:1,60:8,1800:8}
        assert prod(factors) == (2**56)*(3**24)*(5**25)
        if answer is None:
            answer = factors
        else:
            assert factors == answer
    print('WIMAN_QUINTUPLE_LEVI_CRITICAL_GROUP_OK')
    print('vertices=81 edges=180 degrees=4x45,5x36')
    print('B_Bt_spectrum=20^1,8^10,5^16,0^18')
    print('tree_number=2^56*3^24*5^25')
    print('Smith_factors=1^52,2^8,4^3,20,60^8,1800^8')
    print('verified_reduced_laplacian_sinks=0,80')

if __name__ == '__main__':
    main()
