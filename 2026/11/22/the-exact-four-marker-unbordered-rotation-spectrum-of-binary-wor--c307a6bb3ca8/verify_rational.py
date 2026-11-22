#!/usr/bin/env python3
"""Exact four-one unbordered-rotation enumerator using integer polynomial arithmetic."""
from itertools import product

EXPECTED = {
    0: (1, -1, 1, -2, 1, -1, 1),
    2: (0, 4, 4, 0, -8, -8, 8),
    3: (0, 0, 0, 8, 8, 8, -24),
    4: (0, 0, 0, 0, 4, 4, 16),
}

def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return trim(out)

def one_minus_power(m):
    p = [0] * (m+1)
    p[0] = 1
    p[m] = -1
    return p

def rotation_count(g):
    """The proven 1-start and 0-start border criteria, evaluated at four starts."""
    answer = 0
    for i in range(4):
        a, b, c, d = [g[(i+j) % 4] for j in range(4)]
        if a < d and not (a == c and b >= d): answer += 1
        if a > d and not (b == d and c >= a): answer += 1
    return answer

def calculate():
    P = {k: [0] for k in EXPECTED}
    seen = 0
    rank_cases = {k: 0 for k in EXPECTED}
    for g in product(range(4), repeat=4):
        k = max(g) + 1
        if set(g) != set(range(k)):
            continue  # a strict weak ordering requires every rank to occur
        seen += 1
        m = [g.count(i) for i in range(k)]
        suffix_sums = {sum(m[i:]) for i in range(k)}
        term = [0] * (1 + sum(i * m[i] for i in range(k)))
        term[-1] = 1
        for j in range(1, 5):
            if j not in suffix_sums:
                term = mul(term, one_minus_power(j))
        count = rotation_count(g)
        assert count in EXPECTED
        rank_cases[count] += 1
        P[count] = add(P[count], term)
    assert seen == 75, seen
    for label, target in EXPECTED.items():
        assert tuple(trim(P[label])) == target, (label, P[label])
    total = [0]
    for p in P.values(): total = add(total, p)
    d = [1]
    for j in range(1,5): d = mul(d, one_minus_power(j))
    # The 4-variable unrestricted gap series is (1-z)^(-4).
    q = mul(mul([1, 2, 1], [1, 0, 1]), [1, 1, 1])
    assert total == q, (total, q)
    assert d == mul(q, mul(mul([1,-1],[1,-1]),mul([1,-1],[1,-1])))
    return P, rank_cases, d

if __name__ == '__main__':
    p, cases, d = calculate()
    print('75 ordered equality patterns; exact integer numerator identities PASS')
    print('weak-order classes by rotation count:', cases)
    print('common denominator coefficients:', d)
    for k in sorted(p): print('numerator', k, ':', p[k])
