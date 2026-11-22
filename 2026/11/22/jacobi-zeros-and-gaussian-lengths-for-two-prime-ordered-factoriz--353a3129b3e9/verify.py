"""Exact arithmetic checks for the two-prime ordered-factorization length theorem.

Requires Python 3.9+ standard library; no external packages.
This is a finite reproducibility check, not a proof of all exponents.
"""
from functools import lru_cache
from math import comb


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return tuple(c)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return tuple(c)


def power_plus_one(k):
    return tuple(comb(k, j) for j in range(k + 1))


def predicted(a, b):
    big, small = max(a, b), min(a, b)
    jac = (0,)
    for j in range(small + 1):
        term = (0,) * j + (comb(big, j) * comb(small, j),)
        jac = add(jac, mul(term, power_plus_one(small - j)))
    return mul((0, 1), mul(power_plus_one(big - 1), jac))


@lru_cache(None)
def direct(a, b):
    if a == 0 and b == 0:
        return (1,)
    # Choose the first nontrivial factor's two prime exponents.
    ans = (0,)
    for i in range(a + 1):
        for j in range(b + 1):
            if i + j:
                ans = add(ans, mul((0, 1), direct(a - i, b - j)))
    return ans


def check():
    num = 0
    for a in range(1, 13):
        for b in range(1, 13):
            got = direct(a, b)
            exp = predicted(a, b)
            assert got == exp, (a, b, got, exp)
            assert got[0] == 0 and got[1] == 1
            assert len(got) == a + b + 1
            num += 1
    for a, b, answer in [(1, 1, (0, 1, 2)),
                          (2, 2, (0, 1, 7, 12, 6)),
                          (3, 2, (0, 1, 10, 27, 28, 10)),
                          (3, 3, (0, 1, 14, 55, 92, 70, 20))]:
        assert predicted(a, b) == answer
    print(f"PASS: {num} pairs of exponents, 4 illustrative coefficient vectors")
    print("All comparisons are exact integer arithmetic; root and limit claims are proved analytically.")


if __name__ == '__main__':
    check()
