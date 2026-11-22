#!/usr/bin/env python3
"""Exact finite checks for two-step Hamming random graphs.

Run: python3 checker.py
All comparisons use integers or fractions, with no Monte Carlo sampling.
"""
from fractions import Fraction
from itertools import product
from math import comb

CHECKS = 0


def check(test, label):
    global CHECKS
    if not test:
        raise AssertionError(label)
    CHECKS += 1


def parameters(q, d):
    b = q - 1
    N = q ** d
    A = d * b + comb(d, 2) * b * b
    c1 = (d - 1) * b * b + d * b - 1
    c2 = b * b + 2 * (d - 1) * b - 1
    B = d * b * c1 + comb(d, 2) * b * b * c2
    p = Fraction(A, N)
    delta = Fraction(B, A * N) - p * p
    return N, A, c1, c2, B, p, delta


def distance(u, v):
    return sum(a != b for a, b in zip(u, v))


def cube(q, d):
    return list(product(range(q), repeat=d))


def enumerate_moments(q, d, n):
    vertices = cube(q, d)
    N = len(vertices)
    edge = [[int(1 <= distance(x, y) <= 2) for y in vertices]
            for x in vertices]
    hist = [0] * (comb(n, 2) + 1)
    for sequence in product(range(N), repeat=n):
        count = sum(edge[sequence[i]][sequence[j]]
                    for i in range(n) for j in range(i + 1, n))
        hist[count] += 1
    total = N ** n
    mean = sum(k * c for k, c in enumerate(hist))
    var2 = sum(k * k * c for k, c in enumerate(hist))
    third = sum(k**3 * c for k, c in enumerate(hist))
    mu = Fraction(mean, total)
    k3 = Fraction(third, total) - 3 * mu * Fraction(var2, total) + 2 * mu**3
    return mu, k3



def joint_degrees(q, d, n):
    from collections import Counter
    v = cube(q, d)
    N, A, c1, c2, B, p, delta = parameters(q, d)
    adjacency = [[int(1 <= distance(x, y) <= 2) for y in v] for x in v]
    hist = Counter()
    num_conditioned = 0
    for seq in product(range(N), repeat=n):
        if not adjacency[seq[0]][seq[1]]:
            continue
        num_conditioned += 1
        du = 1 + sum(adjacency[seq[0]][seq[j]] for j in range(2, n))
        dv = 1 + sum(adjacency[seq[1]][seq[j]] for j in range(2, n))
        hist[(du, dv)] += 1
    observed = {key: Fraction(count, num_conditioned) for key, count in hist.items()}

    expected = Counter()
    for h, weight, c in [(1, d*(q-1), c1),
                         (2, comb(d,2)*(q-1)**2, c2)]:
        if weight == 0:
            continue
        p11 = Fraction(c, N)
        p10 = p - p11
        p00 = 1 - 2*p + p11
        transitions = {(0,0):p00, (1,0):p10,
                       (0,1):p10, (1,1):p11}
        current = {(1,1):Fraction(1)}
        for _ in range(n-2):
            nxt = Counter()
            for (a,b),pa in current.items():
                for (u,v),pv in transitions.items():
                    nxt[(a+u,b+v)] += pa*pv
            current = nxt
        for key, probability in current.items():
            expected[key] += Fraction(weight, A)*probability
    return observed, expected


def main():
    for q, d in [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                 (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (5, 3)]:
        v = cube(q, d)
        N, A, c1, c2, B, p, delta = parameters(q, d)
        check(len(v) == N, 'vertex number')
        for index in range(N):
            near = [y for y in range(N) if 1 <= distance(v[index], v[y]) <= 2]
            check(len(near) == A, f'degree q={q},d={d},v={index}')
            if index == 0:
                for j in near:
                    h = distance(v[index], v[j])
                    common = sum(1 for k in range(N)
                                 if 1 <= distance(v[index], v[k]) <= 2
                                 and 1 <= distance(v[j], v[k]) <= 2)
                    check(common == (c1 if h == 1 else c2),
                          f'common neighbor q={q},d={d},h={h}')
        check(sum(1 for y in range(N) if distance(v[0], v[y]) == 1) == d * (q-1),
              'distance-one count')
        check(sum(1 for y in range(N) if distance(v[0], v[y]) == 2)
              == comb(d, 2) * (q-1)**2, 'distance-two count')
        check(delta == Fraction(N*B-A**3, A*N*N), 'signed-triangle algebra')
    for q, d, n in [(2, 2, 4), (2, 3, 4), (2, 5, 3),
                    (3, 2, 4), (3, 3, 4), (4, 3, 3)]:
        observed, expected = joint_degrees(q,d,n)
        check(all(observed.get(key,0)==expected.get(key,0)
                  for key in observed.keys() | expected.keys()),
              f'conditional joint degree PGF q={q},d={d},n={n}')
    for q, d, n in [(2, 2, 4), (2, 3, 4), (2, 4, 4),
                    (2, 5, 3), (2, 6, 3), (3, 2, 4), (3, 3, 3),
                    (3, 4, 3), (4, 3, 3), (5, 3, 3)]:
        N, A, c1, c2, B, p, delta = parameters(q, d)
        mu, k3 = enumerate_moments(q, d, n)
        expected_mu = comb(n, 2) * p
        expected_k3 = (comb(n, 2) * p * (1-p) * (1-2*p)
                       + 6*comb(n, 3)*p*delta)
        check(mu == expected_mu, f'edge mean q={q},d={d},n={n}')
        check(k3 == expected_k3, f'edge third cumulant q={q},d={d},n={n}')
    for q in range(2, 15):
        for d in range(1, 21):
            N, A, c1, c2, B, p, delta = parameters(q, d)
            predicted_positive = ((q == 2 and d >= 5)
                                  or (q == 3 and d >= 4)
                                  or (q >= 4 and d >= 3))
            check((delta > 0) == predicted_positive and delta != 0,
                  f'phase q={q},d={d}')
    for n in range(3, 17):
        for d in range(1, 18):
            for q in range(2, 11):
                N, A, c1, c2, B, p, delta = parameters(q, d)
                k3 = (comb(n, 2)*p*(1-p)*(1-2*p)
                      + 6*comb(n, 3)*p*delta)
                positive = ((q == 2 and d >= 5)
                            or (q == 3 and d >= 4)
                            or (q >= 4 and d >= 3))
                exception = (q == 4 and d == 3 and n == 3)
                check((k3 > 0) == (positive and not exception) and k3 != 0,
                      f'skewness q={q},d={d},n={n}')
    print(f'PASS: {CHECKS} exact assertions; direct independent moment enumeration and parameter sweeps')


if __name__ == '__main__':
    main()
