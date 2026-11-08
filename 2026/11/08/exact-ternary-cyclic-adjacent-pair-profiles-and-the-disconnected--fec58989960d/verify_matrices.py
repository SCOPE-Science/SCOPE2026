#!/usr/bin/env python3
"""Independent matrix test of balanced/connected profiles and the exact GF."""
from math import comb


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for rest in compositions(n - a, k - 1):
                yield (a,) + rest


def is_balanced(m):
    return all(sum(m[3*i+j] for j in range(3)) ==
               sum(m[3*j+i] for j in range(3)) for i in range(3))


def connected_nonisolated(m):
    active = {i for i in range(3) if
              any(m[3*i+j] or m[3*j+i] for j in range(3))}
    if not active:
        return False
    seen = {next(iter(active))}
    frontier = list(seen)
    while frontier:
        i = frontier.pop()
        for j in active - seen:
            if m[3*i+j] or m[3*j+i]:
                seen.add(j)
                frontier.append(j)
    return seen == active


def reciprocal_product(factors, limit):
    out = [1] + [0] * limit
    for period, multiplicity in factors:
        for _ in range(multiplicity):
            for n in range(period, limit + 1):
                out[n] += out[n - period]
    return out


def expected_all(limit):
    # (1+z^3)/[(1-z)^3(1-z^2)^3(1-z^3)].
    a = reciprocal_product([(1, 3), (2, 3), (3, 1)], limit)
    return [a[n] + (a[n-3] if n >= 3 else 0) for n in range(limit+1)]


def expected_disconnected(limit):
    a = reciprocal_product([(1, 2)], limit)
    b = reciprocal_product([(1, 3)], limit)
    c = reciprocal_product([(1, 3), (2, 1)], limit)
    return [(3*a[n-2] if n>=2 else 0) +
            (b[n-3] if n>=3 else 0) +
            (3*c[n-3] if n>=3 else 0) for n in range(limit+1)]


def main():
    limit = 12
    total, feasible = [0] * (limit+1), [0] * (limit+1)
    for n in range(1, limit+1):
        for m in compositions(n, 9):
            if not is_balanced(m):
                continue
            total[n] += 1
            feasible[n] += connected_nonisolated(m)
    all_formula = expected_all(limit)
    bad_formula = expected_disconnected(limit)
    for n in range(1, limit+1):
        assert total[n] == all_formula[n], (n,total[n],all_formula[n])
        assert total[n]-feasible[n] == bad_formula[n], (n,total[n],feasible[n],bad_formula[n])
    want = [3,6,11,24,48,95,174,306,510,819,1266,1901]
    assert feasible[1:] == want, feasible
    print('MATRICES_VERIFY_OK n=1..12')


if __name__ == '__main__':
    main()
