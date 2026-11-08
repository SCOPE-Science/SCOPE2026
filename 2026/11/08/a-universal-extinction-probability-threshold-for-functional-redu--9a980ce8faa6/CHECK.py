"""Exact checks for independent-loss functional-group variance comparisons.

Uses only Python's standard library. Finite enumeration corroborates the
all-size analytic proof; it is not substituted for that proof.
"""
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache


def var(profile, q):
    return sum((q ** n - q ** (2 * n) for n in profile), Q(0))


def mean_retained(profile, q):
    return sum((1 - q ** n for n in profile), Q(0))


def direct_moments(profile, q):
    n = sum(profile)
    tags = tuple(i for i, k in enumerate(profile) for _ in range(k))
    result0 = result1 = Q(0)
    for bits in product((0, 1), repeat=n):
        lost = sum(bits)
        mass = q ** lost * (1 - q) ** (n - lost)
        alive = sum(any(bits[j] == 0 for j in range(n) if tags[j] == i)
                    for i in range(len(profile)))
        result0 += mass * alive
        result1 += mass * alive ** 2
    assert sum(q ** sum(bits) * (1 - q) ** (n-sum(bits))
               for bits in product((0, 1), repeat=n)) == 1
    return result0, result1 - result0 ** 2


def polynomial_product(*polys):
    result = {0: 1}
    for poly in polys:
        d = {}
        for a, ca in result.items():
            for b, cb in poly.items():
                d[a+b] = d.get(a+b, 0) + ca*cb
        result = {k: v for k, v in d.items() if v}
    return result


def polynomial_sum(*polys):
    d = {}
    for poly in polys:
        for k, v in poly.items():
            d[k] = d.get(k, 0) + v
    return {k: v for k, v in d.items() if v}


def neg(p):
    return {k: -v for k, v in p.items()}


def h_poly(n):
    return {n: 1, 2*n: -1}


def verify_polynomial_identity(a, b):
    # h(a)+h(b)-h(a+1)-h(b-1)
    lhs = polynomial_sum(h_poly(a),h_poly(b), neg(h_poly(a+1)),neg(h_poly(b-1)))
    # (1-q)(q^a-q^(b-1))(1-(1+q)(q^a+q^(b-1)))
    rhs = polynomial_product({0:1,1:-1}, {a:1,b-1:-1},
                             polynomial_sum({0:1},
                                 neg(polynomial_product({0:1,1:1}, {a:1,b-1:1}))))
    assert lhs == rhs, (a,b,lhs,rhs)


@lru_cache(None)
def partitions(n, k, least=1):
    if k == 0:
        return ((),) if n == 0 else ()
    return tuple((j,)+tail for j in range(least,n//k+1)
                 for tail in partitions(n-j,k-1,j))


def main():
    identities = 0
    for a in range(1, 21):
        for b in range(a+2, 31):
            verify_polynomial_identity(a, b)
            identities += 1

    for profile in ((1,3),(2,2),(1,3,5),(2,2,5),(2,4,3),(3,3,3)):
        m, v = direct_moments(profile, Q(1,2))
        assert m == mean_retained(profile,Q(1,2))
        assert v == var(profile,Q(1,2))
    assert var((1,3,5), Q(1,2))-var((2,2,5), Q(1,2)) == -Q(1,64)
    assert var((2,4,3), Q(1,2))-var((3,3,3), Q(1,2)) == Q(7,256)

    # Exact sign enclosure for the unique root of q(1+q)^2=1.
    lo, hi = Q(46557123187676,10**14), Q(46557123187678,10**14)
    f = lambda q: q*(1+q)**2-1
    assert f(lo) < 0 < f(hi)

    n_cases = 0
    for n in range(2, 17):
        for k in range(2, min(n,6)+1):
            profiles = partitions(n,k)
            balanced = (n//k,)*(k-(n%k)) + (n//k+1,)*(n%k)
            for q in (Q(1,5),Q(2,5)):
                vb = var(balanced,q)
                assert all(vb <= var(p,q) for p in profiles)
                n_cases += len(profiles)
    print('PASS: polynomial transfer identities', identities)
    print('PASS: six direct 2^n extinction-pattern enumerations, n<=9')
    print('PASS: exact nine-species variance contrasts and root enclosure')
    print('PASS: low-extinction balanced-minimum partition comparisons', n_cases)
    print('LIMIT: finite tests do not establish the universal inequalities')

if __name__ == '__main__':
    main()
