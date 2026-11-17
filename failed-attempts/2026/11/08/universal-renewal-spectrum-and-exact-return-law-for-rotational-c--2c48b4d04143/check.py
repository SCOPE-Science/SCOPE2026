"""Exact-arithmetic checks for the rotational connect-the-dots interval family.

Run with: python3 check.py. No external dependencies.
Finite tests support, but do not replace, the all-parameter proof in RESULT.md.
"""
from fractions import Fraction
from math import gcd

checks = 0

def check(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def markov(n, step):
    images = [(i + step) % n for i in range(n)]
    m = n - 1
    matrix = [[0] * m for _ in range(m)]
    for src in range(m):
        low, high = sorted((images[src], images[src + 1]))
        for dst in range(low, high):
            matrix[dst][src] = 1
    return images, matrix

def matmul(A, B):
    d = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(d))
             for j in range(d)] for i in range(d)]

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def det_coeffs_from_traces(matrix):
    # det(I-zA) = sum_{j=0}^m c_j z^j;
    # Newton identities k*c_k = -sum_{i=1}^k c_(k-i)*trace(A^i).
    m = len(matrix)
    P = ident(m)
    traces = [0]
    for k in range(1, m + 1):
        P = matmul(P, matrix)
        traces.append(sum(P[i][i] for i in range(m)))
    coeff = [1]
    for k in range(1, m + 1):
        s = sum(coeff[k - j] * traces[j] for j in range(1, k + 1))
        check(s % k == 0, ('Newton-divisibility', m, k))
        coeff.append(-s // k)
    return coeff

def fixed_by_itineraries(n, step, k):
    images, matrix = markov(n, step)
    m = n - 1
    coefficients = [(images[i + 1] - images[i],
                     images[i] - i * (images[i + 1] - images[i]))
                    for i in range(m)]
    points = set()
    total = 0
    invalid = 0
    def walk(start, now, depth, slope, intercept, path):
        nonlocal total, invalid
        if depth == k:
            if not matrix[start][now]:
                return
            total += 1
            check(slope != 1, ('nonexpanding-cycle', n, step, k, path))
            x = Fraction(intercept, 1 - slope)
            y = x
            for state in path:
                if not (state <= y <= state + 1):
                    invalid += 1
                    return
                a, b = coefficients[state]
                y = a * y + b
            check(y == x, ('affine-root', n, step, k, path))
            points.add(x)
            return
        for nxt in range(m):
            if matrix[nxt][now]:
                a, b = coefficients[nxt]
                walk(start, nxt, depth + 1,
                     a * slope, a * intercept + b, path + (nxt,))
    # Path lists states for each applied map, so transitions in the matrix
    # connect successive states, not the final image of an extra branch.
    def enumerate_states(start, now, path):
        nonlocal total, invalid
        if len(path) == k:
            if not matrix[start][now]:
                return
            s = 1; b = 0
            for state in path:
                a, c = coefficients[state]
                s, b = a * s, a * b + c
            total += 1
            check(s != 1, ('neutral-cycle', n, step, k, path))
            x = Fraction(b, 1 - s)
            y = x
            for state in path:
                if not state <= y <= state + 1:
                    invalid += 1
                    return
                a, c = coefficients[state]
                y = a * y + c
            check(y == x, ('return-root', n, step, k, path))
            points.add(x)
            return
        for nxt in range(m):
            if matrix[nxt][now]:
                enumerate_states(start, nxt, path + (nxt,))
    for start in range(m):
        enumerate_states(start, start, (start,))
    return total, len(points), invalid

def trace_formula(m, k):
    # [z^k] log zeta via the renewal polynomial.
    Q = [0] + [1] * m
    # Newton recurrence for trace from det(I-zA)=1-sum(z^r)
    F = [0] * (k + 1)
    for h in range(1, k + 1):
        # -h*c_h = sum_{j=1}^h c_j*F_(h-j), rearranged
        c_h = -1 if h <= m else 0
        F[h] = -h * c_h + sum(F[h - j] for j in range(1, min(m, h - 1) + 1))
    return F[k]

for n in range(3, 17):
    m = n - 1
    for step in range(1, n):
        if gcd(n, step) != 1:
            continue
        images, M = markov(n, step)
        c = n - step - 1
        for j in range(m):
            column = [M[i][j] for i in range(m)]
            if j == c:
                check(column == [1] * m, ('critical-column', n, step, j))
            else:
                dest = (j + step) % n
                check(dest < m and column == [int(i == dest) for i in range(m)],
                      ('deterministic-column', n, step, j))
        check(det_coeffs_from_traces(M) == [1] + [-1] * m,
              ('integer-characteristic-polynomial', n, step))
        power = ident(m)
        for k in range(1, 2 * m + 3):
            power = matmul(power, M)
            check(sum(power[i][i] for i in range(m)) == trace_formula(m, k),
                  ('fixed-count-recurrence', n, step, k))

for n in range(3, 9):
    for step in range(1, n):
        if gcd(n, step) != 1:
            continue
        for k in range(1, 10):
            t, u, bad = fixed_by_itineraries(n, step, k)
            F = trace_formula(n - 1, k)
            check(bad == 0, ('itinerary-outside-branch', n, step, k, bad))
            check(t == F, ('path-total', n, step, k, t, F))
            check(u == F, ('distinct-fixed-point-count', n, step, k, u, F))
print('VERIFIED exact checks:', checks)
print('Markov matrices: all coprime shifts, n=3..16.')
print('Physical periodic points: all coprime shifts, n=3..8, k=1..9.')
