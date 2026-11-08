"""Supplementary finite checks for the exact parallel Haar-subspace score theorem.

Run with Python 3 standard library: python3 verify_parallel_haar.py.
Finite enumeration is not a proof of the theorem for all parameters.
"""
import math


def b(p):
    return math.exp(math.lgamma((p + 1) / 2) - math.lgamma(p / 2))


def score(p, c):
    if p == 1:
        return b(1) / 1.5
    return b(p) / ((p + c - 1) // c + 1)


def expected(d, c):
    if c == 1:
        return {1}
    if c == 2 and d >= 4:
        return {2, 4}
    return {min(d, c)}


def main():
    checks = 0
    for d in range(2, 120):
        for c in range(1, 65):
            values = [score(p, c) for p in range(1, d + 1)]
            best = max(values)
            maximizers = {p for p, val in enumerate(values, 1)
                          if abs(val - best) <= 1e-11 * max(1, best)}
            assert maximizers == expected(d, c), (d, c, maximizers)
            checks += d

    for c in range(1, 501):
        # Exact identity by Gamma recurrence; floating-point check only.
        h_c = b(c) / (2 * c)
        h_c2 = b(c + 2) / (2 * c + 2)
        assert math.isclose(h_c, h_c2, rel_tol=2e-12)
        checks += 1

    for c in range(2, 101):
        for k in range(2, 31):
            lhs = b(k * c) / (k + 1)
            rhs = b(c) / 2
            assert lhs <= rhs + 2e-12
            if c == 2 and k == 2:
                assert math.isclose(lhs, rhs, rel_tol=2e-12)
            else:
                assert lhs < rhs - 1e-13
            checks += 1

    print('PASS; supplementary comparisons:', checks)


if __name__ == '__main__':
    main()
