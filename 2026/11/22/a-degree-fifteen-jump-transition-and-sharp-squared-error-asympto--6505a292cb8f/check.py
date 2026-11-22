"""Exact rational finite-degree checks for the Bernstein jump L2 theorem.

Python 3 standard library only.  Infinite-dimensional and asymptotic
proof steps are mathematical, not certified by this finite checker.
"""
from fractions import Fraction
from math import comb


def coefficients(n, j):
    if j == 0:
        return [1]
    if j == n + 1:
        return [0]
    return [0] * j + [(-1) ** (r-j) * comb(n, r) * comb(r-1, j-1)
                          for r in range(j, n+1)]


def primitive(a, t):
    return sum((Fraction(c, r+1) * t**(r+1)
                for r, c in enumerate(a)), Fraction(0))


def energy(n, k, j):
    t = Fraction(k, n)
    a = coefficients(n, j)
    square = [0] * (2*len(a)-1)
    for r, u in enumerate(a):
        for s, v in enumerate(a):
            square[r+s] += u*v
    return (primitive(square, Fraction(1))
            - 2*(primitive(a, Fraction(1)) - primitive(a, t))
            + 1-t)


def check():
    count = 0
    # Check each power coefficient against the direct Bernstein tail.
    for n in range(1, 16):
        for j in range(0, n+2):
            tail = [0]*(n+1)
            for i in range(j, n+1):
                for r in range(i, n+1):
                    tail[r] += comb(n, i)*comb(n-i, r-i)*(-1)**(r-i)
            a = coefficients(n, j)+[0]*(n+1-len(coefficients(n,j)))
            assert a == tail, (n, j)
            count += 1

    # Exact exhaustion of all cell-boundary one-sided limits.
    for n in range(1, 15):
        endpoint = Fraction(1, 2*n+1)
        for k in range(0, n+1):
            for j in (k, k+1):
                e = energy(n, k, j)
                assert e <= endpoint, (n, k, j, e, endpoint)
                if 0 < k < n:
                    assert e < endpoint, (n, k, j)
                    count += 1
                count += 1
        assert energy(n, n, n) == endpoint
        count += 1

    n = 15
    exact = Fraction(7885956840965217, 239784545898437500)
    maxima = []
    for k in range(n+1):
        for j in (k, k+1):
            e = energy(n, k, j)
            assert e <= exact, (n,k,j,e)
            if e == exact:
                maxima.append((k,j))
            count += 1
    assert maxima == [(6,7),(9,9)], maxima
    assert exact > Fraction(1,31)
    count += 2
    print(f'PASS {count} exact rational comparisons; degree-15 square norm={exact}; exact extremal traces={maxima}')


if __name__ == '__main__':
    check()
