"""Exact arithmetic and independently generated signed-permutation subgroup checks.

Run with Python 3.9+; no third-party libraries.
"""
from fractions import Fraction
from math import factorial
from itertools import permutations, product


def ordinary_classes(limit):
    def product_series(factors):
        a = [0] * (limit + 1)
        a[0] = 1
        for degree, multiplicity in factors:
            for _ in range(multiplicity):
                for i in range(degree, limit + 1):
                    a[i] += a[i-degree]
        return a
    full = product_series([(1, 1), (3, 2), (4, 1), (6, 2), (12, 1)])
    nonfaithful = product_series([(1, 1), (3, 1)])
    return [a-b for a, b in zip(full, nonfaithful)]


def exponential_coefficients(limit):
    # Derive exp(A(z)) from (exp A)' = A' exp A, using exact fractions.
    def exp_series(weights):
        a = [Fraction(0) for _ in range(limit+1)]
        a[0] = 1
        for n in range(1, limit+1):
            a[n] = sum(k*v*a[n-k] for k,v in weights if k <= n)/n
        return a
    full = exp_series([(1, Fraction(1,2)), (3, Fraction(2,3)),
                       (4, Fraction(1,2)), (6, Fraction(1,2)),
                       (12, Fraction(1,24))])
    nonfaithful = exp_series([(1, Fraction(1,2)), (3, Fraction(1,6))])
    values = [Fraction(2**n*factorial(n), 24) * (full[n]-nonfaithful[n])
              for n in range(limit+1)]
    assert all(v.denominator == 1 for v in values)
    return [int(v) for v in values]


def compose(a, b):
    return tuple((1 if v > 0 else -1)*a[abs(v)-1] for v in b)


def inverse(a):
    v = [None] * len(a)
    for i, j in enumerate(a):
        v[abs(j)-1] = (1 if j > 0 else -1) * (i+1)
    return tuple(v)


def signed_group(n):
    for p in permutations(range(1, n+1)):
        for signs in product((1,-1), repeat=n):
            yield tuple(a*b for a,b in zip(p, signs))


def brute_subgroups(n, check_conjugacy=False):
    identity = tuple(range(1,n+1))
    elements = list(signed_group(n))
    of_order_2, of_order_3 = [], []
    for a in elements:
        square = compose(a, a)
        if square == identity and a != identity:
            of_order_2.append(a)
        elif compose(square, a) == identity:
            of_order_3.append(a)
    # The triangle presentation <a,b | a^3=b^2=(ab)^3=1>
    # gives A4, and each actual A4 has 8*3=24 such ordered pairs.
    pairs = 0
    subgroups = set()
    for a in of_order_3:
        for b in of_order_2:
            ab = compose(a,b)
            if compose(compose(ab,ab),ab) != identity:
                continue
            pairs += 1
            if check_conjugacy:
                seen = {identity}
                queue = [identity]
                for x in queue:
                    for g in (a,b):
                        y = compose(x,g)
                        if y not in seen:
                            seen.add(y)
                            queue.append(y)
                assert len(seen) == 12
                subgroups.add(frozenset(seen))
    assert pairs % 24 == 0
    total = pairs//24
    orbit_sizes = None
    if check_conjugacy:
        assert len(subgroups) == total
        inverses = {g:inverse(g) for g in elements}
        missing = set(subgroups)
        orbit_sizes = []
        while missing:
            H = next(iter(missing))
            orbit = {frozenset(compose(compose(g,h),inverses[g]) for h in H)
                     for g in elements}
            assert orbit <= subgroups
            missing.difference_update(orbit)
            orbit_sizes.append(len(orbit))
        orbit_sizes.sort()
    return total, orbit_sizes


def run():
    assert ordinary_classes(15) == [0,0,0,1,2,2,6,8,9,16,21,23,38,46,51,74]
    assert exponential_coefficients(9) == [0,0,0,1,12,50,1500,18795,164136,3878532]
    for n in range(3,7):
        actual, orbits = brute_subgroups(n, check_conjugacy=(n<=4))
        assert actual == exponential_coefficients(n)[n], (n, actual)
        if orbits is not None:
            assert len(orbits) == ordinary_classes(n)[n]
            assert orbits == ({3:[1],4:[4,8]})[n]
    # Check independent profile-to-normalizer formula up to rank 12.
    degrees = (1,3,3,4,6,6,12)
    factors = (2,6,2,2,4,4,24)
    for n in range(13):
        profiles = []
        def visit(j,left,ms):
            if j == len(degrees):
                if left == 0 and sum(ms[2:]) > 0:
                    profiles.append(tuple(ms))
                return
            d=degrees[j]
            for k in range(left//d+1):
                visit(j+1,left-k*d,ms+[k])
        visit(0,n,[])
        assert len(profiles) == ordinary_classes(n)[n]
        predicted = 0
        for ms in profiles:
            cent = 1
            for c,m in zip(factors,ms):
                cent *= c**m*factorial(m)
            assert (2**n*factorial(n)) % (24*cent) == 0
            predicted += (2**n*factorial(n))//(24*cent)
        assert predicted == exponential_coefficients(n)[n]
    print('A4_HYPEROCTAHEDRAL_PROFILE_NORMALIZER_AND_SUBGROUP_CENSUS_VERIFIED n<=12; brute B_n n<=6')


if __name__ == '__main__':
    run()
