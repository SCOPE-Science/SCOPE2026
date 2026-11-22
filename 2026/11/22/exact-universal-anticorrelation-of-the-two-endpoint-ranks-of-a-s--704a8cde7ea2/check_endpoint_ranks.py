"""Exact finite sign-permutation tests for endpoint rank covariance identities.

Only a finite check: the proof for arbitrary continuous symmetric increments
uses the two- and three-block sign identities given in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def endpoint_ranks(increments):
    positions = [0]
    for x in increments:
        positions.append(positions[-1] + x)
    assert len(set(positions)) == len(positions)
    return (1 + sum(x < positions[0] for x in positions),
            1 + sum(x < positions[-1] for x in positions))


def check(n):
    first = second = square_first = square_second = mixed = 0
    count = 0
    for magnitudes in permutations(1 << j for j in range(n)):
        for signs in product((-1, 1), repeat=n):
            r, s = endpoint_ranks([a * z for a, z in zip(magnitudes, signs)])
            first += r
            second += s
            square_first += r*r
            square_second += s*s
            mixed += r*s
            count += 1
    assert count == factorial(n) * 2**n
    E = Fraction(n+2, 2)
    var = Fraction(n*(n+1),8)
    cov = -Fraction((n+1)*(n+2),24)
    checks = [Fraction(first,count)==E, Fraction(second,count)==E,
              Fraction(square_first,count)-E*E==var,
              Fraction(square_second,count)-E*E==var,
              Fraction(mixed,count)-E*E==cov,
              cov/var == -Fraction(n+2,3*n)]
    assert all(checks), (n,checks)
    print(f'n={n}: {count} exact paths; mean={E}; variance={var}; covariance={cov}; correlation={cov/var}; 6 identities passed')
    return len(checks)


def block_sign_identities():
    def sign(x):
        return (x > 0) - (x < 0)
    total = 0
    for a, b in product((0, 1, 2, 4, 8), repeat=2):
        if a != b:
            s = sum(sign(x*a+y*b) * (sign(x*a)+sign(y*b))
                    for x, y in product((-1, 1), repeat=2))
            assert s == 4
            total += 1
    for a, b, c in product((0, 1, 2, 4, 8), repeat=3):
        positive = [v for v in (a,b,c) if v]
        if not positive or len(positive) != len(set(positive)):
            continue
        s = 0
        for x, y, z in product((-1, 1), repeat=3):
            p, q, r = sign(x*a+y*b), sign(y*b+z*c), sign(x*a+z*c)
            s += p*q + p*r + q*r
        assert s == 8, (a,b,c,s)
        total += 1
    print(f'{total} finite magnitude sign-identity cases passed')
    return total


if __name__ == '__main__':
    assert sum(check(n) for n in range(1,7)) == 36
    block_sign_identities()
    print('36 exact moment identities and finite sign tests passed; finite examples only, not a general theorem proof.')
