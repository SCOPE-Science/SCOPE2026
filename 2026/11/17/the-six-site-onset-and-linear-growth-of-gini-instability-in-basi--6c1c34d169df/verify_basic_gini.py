"""Exact exhaustive certificate for the two-input Gini modulus of Basic Chebyshev isotonic regression on chains of length 2 through 6.

Every differentiability chamber is indexed by a permutation of the input ranks.
Every Gini-operator norm is attained by a two-level indicator direction.
The proof of these reductions is given in RESULT.md.
No external libraries or floating-point arithmetic are used.
"""

from itertools import permutations
from fractions import Fraction


def gini(v):
    return sum(abs(v[i] - v[j]) for i in range(len(v)) for j in range(i + 1, len(v)))


def selector_indices(rank):
    n = len(rank)
    prefix = [0] * n
    suffix = [0] * n
    best = 0
    for i in range(n):
        if rank[i] > rank[best]:
            best = i
        prefix[i] = best
    best = n - 1
    for i in range(n - 1, -1, -1):
        if rank[i] < rank[best]:
            best = i
        suffix[i] = best
    return prefix, suffix


def certify(n):
    assert 2 <= n <= 6
    max_num, max_den = 0, 1
    witness = None
    examined = 0
    for rank in permutations(range(n)):
        p, q = selector_indices(rank)
        for mask in range(1, 1 << (n - 1)):
            h = tuple((mask >> j) & 1 for j in range(n))
            k = sum(h)
            # Twice the Jacobian response: exactly integer values 0, 1, 2.
            twice_response = [h[p[i]] + h[q[i]] for i in range(n)]
            numerator = gini(twice_response)
            denominator = 2 * k * (n - k)
            examined += 1
            if numerator * max_den > max_num * denominator:
                max_num, max_den = numerator, denominator
                witness = (rank, h, twice_response)
    maximum = Fraction(max_num, max_den)
    expected = Fraction(9, 8) if n == 6 else Fraction(1, 1)
    assert maximum == expected, (n, maximum, expected)
    assert examined == __import__('math').factorial(n) * ((1 << (n - 1)) - 1)
    return maximum, examined, witness


def main():
    checks = 0
    for n in range(2, 7):
        maximum, examined, witness = certify(n)
        checks += examined
        print(f'N={n} EXACT_GINI_LIPSCHITZ_MODULUS={maximum} CHAMBER_CUT_PAIRS={examined}')
    a = (0, 1, 2, 5, 4, 3)
    h = (1, 1, 1, 0, 1, 0)
    assert gini(h) == 8
    p, q = selector_indices(a)
    doubled = tuple(h[p[i]] + h[q[i]] for i in range(6))
    assert doubled == (2, 2, 2, 0, 0, 0)
    assert gini(doubled) == 18
    for denom in (2, 3, 7, 11):
        eps = Fraction(1, denom)
        b = tuple(Fraction(a[i]) + eps * h[i] for i in range(6))
        assert sorted(b) == sorted(set(b)), 'distinct entries required'
        def basic(v):
            return tuple((max(v[:i+1]) + min(v[i:])) / Fraction(2) for i in range(len(v)))
        gain = gini(tuple(basic(b)[i] - basic(a)[i] for i in range(6)))
        loss = eps * gini(h)
        assert gain / loss == Fraction(9, 8)
    # The two-block witness gives a linear-in-size lower bound in every dimension.
    for n in range(6, 31):
        k = n // 2
        a = tuple(range(k)) + tuple(range(n - 1, k - 1, -1))
        h = (1,) * k + (0,) + (1,) * (n - k - 2) + (0,)
        eps = Fraction(1, 3)
        b = tuple(Fraction(a[i]) + eps * h[i] for i in range(n))
        def basic(v):
            return tuple((max(v[:i + 1]) + min(v[i:])) / Fraction(2) for i in range(len(v)))
        output = tuple(basic(b)[i] - basic(a)[i] for i in range(n))
        assert output == (eps,) * k + (Fraction(0),) * (n-k)
        assert gini(h) == 2 * (n - 2)
        assert gini(output) / (eps * gini(h)) == Fraction(k * (n-k), 2 * (n-2))
    print('GENERAL_DIMENSION_LOWER_WITNESSES_PASS_N6_TO30')
    print(f'ALL_EXACT_CHAMBERS_AND_CUTS_PASS {checks}')
    print('STRICT_SIX_SITE_WITNESS_PASS')


if __name__ == '__main__':
    main()
