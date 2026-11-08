"""Independent exact checks for conditional crossing degrees in uniform matchings.

Run: python3 verify.py. Uses only the Python standard library.
"""
import math
from fractions import Fraction
from functools import lru_cache


def double_factorial(k):
    product = 1
    for j in range(k, 0, -2):
        product *= j
    return product


def law(n, a):
    """Crossing-degree law of a chord with shorter arc of a endpoints."""
    b = 2 * n - 2 - a
    return {k: Fraction(
        math.comb(a, k) * math.comb(b, k) * math.factorial(k)
        * double_factorial(a-k-1) * double_factorial(b-k-1),
        double_factorial(2*n-3)
    ) for k in range(a+1) if (a-k) % 2 == 0}


@lru_cache(None)
def pairings(points):
    """All perfect matchings of a tuple of ordered endpoint indices."""
    if not points:
        return ((),)
    first, *rest = points
    output = []
    for index, partner in enumerate(rest):
        remaining = tuple(rest[:index] + rest[index+1:])
        for suffix in pairings(remaining):
            output.append(((first, partner),) + suffix)
    return tuple(output)


def enumerate_law(n, a):
    """Direct enumeration after fixing the distinguished chord (0, a+1)."""
    other = tuple(i for i in range(2*n) if i not in (0, a+1))
    observed = {}
    total = 0
    for matching in pairings(other):
        crossings = sum((x < a+1) != (y < a+1) for x, y in matching)
        observed[crossings] = observed.get(crossings, 0) + 1
        total += 1
    return {k: Fraction(v, total) for k, v in observed.items()}


def tail(d, t):
    return sum((p for k, p in d.items() if k >= t), Fraction(0))


def check():
    assertions = 0
    def require(test):
        nonlocal assertions
        assertions += 1
        assert test, ('failure on assertion', assertions)

    # Count the distribution directly, without invoking the mass formula.
    for n in range(2, 8):
        for a in range(n):
            require(law(n, a) == enumerate_law(n, a))

    # Check normalization, expected degree, support, and likelihood ratios.
    for n in range(3, 42):
        for a in range(n):
            p = law(n, a)
            b = 2*n-2-a
            require(sum(p.values()) == 1)
            require(set(p) == set(range(a % 2, a+1, 2)))
            require(sum(k*v for k, v in p.items()) == Fraction(a*b, 2*n-3))
            if a+2 < n:
                q = law(n, a+2)
                factor = Fraction((a+1)*(a+2), b*(b-1))
                ratios = []
                for k in sorted(p):
                    predicted = factor * Fraction(b-k, a+2-k)
                    require(Fraction(q[k],p[k]) == predicted)
                    ratios.append(predicted)
                require(all(x < y for x,y in zip(ratios, ratios[1:])))
                require(q.get(a+2,0) > 0)
                for threshold in range(1,a+3):
                    require(tail(q, threshold) >= tail(p, threshold))
                require(tail(q, a+1) > tail(p, a+1))

            if a+1 < n:
                q = law(n,a+1)
                if a == 0:
                    require(tail(q,1) > tail(p,1))
                elif a % 2 == 1:
                    require(p.get(0,0) == 0 and q.get(0,0) > 0)
                    require(tail(p,1) > tail(q,1))
                    require(tail(q,a+1) > tail(p,a+1))
                else:
                    require(q.get(1,0) == (a+1)*p[0])
                    require(tail(p,2) > tail(q,2))
                    require(tail(q,a+1) > tail(p,a+1))

    print('PASS:', assertions, 'exact assertions; all matchings checked through n=7.')

if __name__ == '__main__':
    check()
