"""Exact, finite cross-checks of integer Smith invariants for unit-indexed Ramanujan matrices.
Requires SymPy; this script is finite corroboration, not a proof for all moduli.
"""
from math import gcd
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from sympy import factorint, totient, mobius


def ramanujan(n, t):
    g = gcd(n, t)
    return sum(d * int(mobius(n // d)) for d in range(1, g + 1) if g % d == 0)


def expected(n):
    fs = factorint(n)
    if n == 1:
        return [1]
    rank = 1
    for p, e in fs.items():
        rank *= (p - 1) if e == 1 else p ** (e - 2) * (p - 1) ** 2
    nums = []
    for j in range(1, rank + 1):
        d = 1
        for p, e in fs.items():
            d *= p ** (e - 1 + (j > rank // (p - 1)))
        nums.append(int(d))
    return nums + [0] * (int(totient(n)) - rank)


def check(n):
    units = [a for a in range(n) if gcd(a, n) == 1]
    mat = Matrix([[ramanujan(n, a - b) for b in units] for a in units])
    smith = smith_normal_form(mat, domain=ZZ)
    actual = [abs(int(smith[i, i])) for i in range(len(units))]
    assert actual == expected(n), (n, actual, expected(n))
    assert mat == mat.T
    return len(units)


if __name__ == '__main__':
    sample = list(range(1, 31)) + [32, 36, 40, 45, 48, 49, 50, 60, 72]
    for n in sample:
        d = check(n)
        print(f'n={n}: dim={d} rank={len(expected(n)) - expected(n).count(0)} OK')
    print(f'CHECK_OK {len(sample)} independent Smith forms')
