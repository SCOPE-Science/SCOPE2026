#!/usr/bin/env python3
"""Exact finite checks for the length-five non-overlapping-code theorem."""


def objective(a, b, c, d, e):
    p = a * b
    q3 = a * (p - c) + c * b
    r4 = a * (q3 - d) + c * (p - c) + d * b
    assert 0 <= c <= p and 0 <= d <= q3 and 0 <= e <= r4
    return a * (r4 - e) + c * (q3 - d) + d * (p - c) + e * b


def brute(q):
    best = -1
    for a in range(1, q):
        b = q - a
        p = a * b
        for c in range(p + 1):
            q3 = a * (p - c) + c * b
            for d in range(q3 + 1):
                r4 = a * (q3 - d) + c * (p - c) + d * b
                # The objective is affine in e, so an endpoint is sufficient.
                for e in {0, r4}:
                    best = max(best, objective(a, b, c, d, e))
    return best


def reduced(q):
    """Exact SQN optimum using left-right symmetry and endpoint linearity."""
    best = -1
    witnesses = []
    for a in range(1, q // 2 + 1):
        b = q - a
        p = a * b
        for c in range(p + 1):
            q3 = a * (p - c) + c * b
            e_side = b - a
            for d in {0, q3}:
                r4 = a * (q3 - d) + c * (p - c) + d * b
                e = r4 if e_side >= 0 else 0
                value = objective(a, b, c, d, e)
                if value > best:
                    best = value
                    witnesses = [(a, b, c, d, e)]
                elif value == best:
                    witnesses.append((a, b, c, d, e))
    return best, sorted(set(witnesses))


def theorem_value(q):
    if q == 2:
        return 2
    if q == 3:
        return 17
    ell = (4 * q + 2) // 5
    return (q - ell) * ell**4


for q in range(2, 8):
    assert brute(q) == theorem_value(q)

for q in range(2, 61):
    best, witnesses = reduced(q)
    assert best == theorem_value(q), (q, best, theorem_value(q), witnesses)
    if q >= 4:
        ell = (4 * q + 2) // 5
        a, b = q - ell, ell
        p = a * b
        q3 = a * (p - p) + p * b
        r4 = a * (q3 - q3) + p * (p - p) + q3 * b
        assert witnesses == [(a, b, p, q3, r4)], (q, witnesses)

for q in range(4, 1001):
    ell = (4 * q + 2) // 5
    target = (q - ell) * ell**4
    assert target == max(a * (q - a)**4 for a in range(1, q))

print("verified full SQN endpoint enumeration for 2 <= q <= 7")
print("verified reduced exact SQN and unique orientation for 2 <= q <= 60")
print("verified integer maximizer formula for 4 <= q <= 1000")
