"""Exact elementary checks for alternating space-filling cones.

Recompute the rank census and characteristic-p polar identities over finite
ranges. These checks supplement, and do not replace, the general proof.
"""
from fractions import Fraction
from math import prod
from collections import Counter
from itertools import combinations


def gaussian(n, k, q):
    z = Fraction(1)
    for i in range(k):
        z *= Fraction(q**(n-i)-1, q**(k-i)-1)
    assert z.denominator == 1
    return z.numerator


def rank_count(n, r, q):
    return gaussian(n, n-2*r, q) * q**(r*(r-1)) * prod(
        q**(2*j-1)-1 for j in range(1, r+1)
    )


def polar_test(p, q, r):
    """Verify partial derivatives mod p by sparse monomial arithmetic."""
    assert q % p == 0
    dimension = 2*r
    monomials = {}
    for j in range(r):
        a, b = 2*j, 2*j+1
        for exponents, coeff in [((a,q,b,1), 1), ((a,1,b,q), -1)]:
            e = [0] * dimension
            e[exponents[0]] = exponents[1]
            e[exponents[2]] = exponents[3]
            e = tuple(e)
            monomials[e] = (monomials.get(e, 0) + coeff) % p
    monomials = {k: v for k,v in monomials.items() if v}
    assert all(any(v >= p for v in exp) for exp in monomials)
    for d in range(dimension):
        derivative = {}
        for e, a in monomials.items():
            if e[d]:
                new = list(e)
                new[d] -= 1
                new = tuple(new)
                derivative[new] = (derivative.get(new,0) + a*e[d]) % p
        derivative = {k:v for k,v in derivative.items() if v}
        e = [0]*dimension
        e[d ^ 1] = q
        expected_coeff = (-1 if d%2==0 else 1) % p
        assert derivative == {tuple(e): expected_coeff}, (p,q,r,d,derivative)


def exhaustive_binary_rank_five():
    # Enumerate the entire 10-dimensional space of alternating 5-by-5 matrices.
    n = 5
    pairs = list(combinations(range(n), 2))
    out = Counter()
    for mask in range(1 << len(pairs)):
        rows = [0] * n
        for k, (a,b) in enumerate(pairs):
            if (mask >> k) & 1:
                rows[a] ^= 1 << b
                rows[b] ^= 1 << a
        pivots = {}
        rank = 0
        for x in rows:
            while x:
                i = x.bit_length() - 1
                if i in pivots:
                    x ^= pivots[i]
                else:
                    pivots[i] = x
                    rank += 1
                    break
        out[rank] += 1
    assert dict(out) == {0: 1, 2: 155, 4: 868}


def main():
    for p, qs in ((2,(2,4,8)),(3,(3,9)),(5,(5,))):
        for q in qs:
            for n in range(5,9):
                counts = [rank_count(n,r,q) for r in range(n//2+1)]
                assert sum(counts) == q**(n*(n-1)//2)
                for r in range(2,n//2+1):
                    if n-2*r > 0:
                        polar_test(p,q,r)
                        a = 2*r-q-2
                        assert (a>=-1) == (q<=2*r-1)
                        assert (a>=0) == (q<=2*r-2)
                        assert (a>0) == (q<=2*r-3)
    exhaustive_binary_rank_five()
    assert rank_count(5,2,2) == 868
    assert rank_count(5,2,3) == 56628
    assert 2**4 == 16
    assert 3**4 == 81
    print('PASS: exhaustive binary rank census, general rank-count sums, sparse polar identities, wall inequalities')


if __name__ == '__main__':
    main()
