#!/usr/bin/env python3
"""Exact residue and rational verification for the Zumkeller-square density theorem."""
from fractions import Fraction
from math import gcd, isqrt
from itertools import product

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)


def a_of(p):
    a = 1
    while p > 2 ** (a + 1) - 1:
        a += 1
    return a


def g_residues(p):
    # Independent definition-level enumeration: one of p^2 roots must have
    # difference divisible by p but not p^2.
    pp = p * p
    roots = {}
    for x in range(pp):
        r = x * x % pp
        for t in range(1, p):
            roots[(r + p * t) % pp] = True
    return set(roots)


def sq_residues(m):
    return {x*x % m for x in range(m)}


def check_zumkeller(n):
    divs = [d for d in range(1, n+1) if n % d == 0]
    total = sum(divs)
    if total % 2:
        return False
    sums = {0}
    for d in divs:
        sums |= {s+d for s in tuple(sums) if s+d <= total//2}
    return total//2 in sums


def main():
    assert check_zumkeller(70)
    assert 70 + 2 == sum(d for d in range(1,71) if 70 % d == 0) // 2
    for p in PRIMES:
        a = a_of(p)
        assert check_zumkeller((2**a)*p)
    G = {}
    for p in PRIMES:
        G[p] = g_residues(p)
        assert len(G[p]) == (p - 1) * (p + 2) // 2
    A = {p: a_of(p) for p in PRIMES}
    assert [A[p] for p in PRIMES] == [1,2,2,3,3,4,4,4,4,4]
    B = {}
    for a in (1,2,3,4):
        b = Fraction(1)
        for p in PRIMES:
            if A[p] <= a:
                b *= 1 - Fraction(len(G[p]), p*p)
        B[a] = b
    prior_density = 1 - B[1]/2 - B[2]/8 - B[3]/8 - B[4]/4
    assert prior_density == Fraction(63520442937841228526,83108492151210387225)
    # Direct check of the extra classes on the 4*9*25*49 period.
    modulus = 4*9*25*49
    extra = 0
    base70 = 0
    intersection3 = 0
    for n in range(modulus):
        e70 = n % 4 in (2, 3) and n % 25 in G[5] and n % 49 in G[7]
        old3 = n % 9 in G[3]
        base70 += e70
        intersection3 += e70 and old3
        extra += e70 and not old3
    assert (base70, intersection3, extra) == (6804, 3780, 3024)
    assert Fraction(extra,modulus) == Fraction(12,175)
    final_density = prior_density + Fraction(extra,modulus)
    assert final_density == Fraction(2768772438842683346,3324339686048415489)
    # Independently check each q70 local condition directly via square residues.
    good4 = {n for n in range(4) if any((n-x*x)%4 == 2 for x in range(4))}
    assert good4 == {2,3}
    for p in (5,7):
        direct = {n for n in range(p*p) if any((n-x*x)%(p*p) in {p*k for k in range(1,p)} for x in range(p*p))}
        assert direct == G[p]
    # Explicit CRT witness for selected residue classes of the new family.
    # x may be chosen in [1,4900] for any corresponding n.
    for n in (2,3,70,71,122,123,4567,99999):
        if not (n%4 in (2,3) and n%25 in G[5] and n%49 in G[7]):
            continue
        root = next(x for x in range(1,4901)
                    if gcd((n-x*x)//70,70)==1 and (n-x*x)%70 == 0)
        assert root > 0
    print('VERIFY_OK primes=10 local_root_counts=10 mixed_period=44100')
    print('q70_event=6804/44100 intersection_p3=3780/44100 new_classes=3024/44100=12/175')
    print('ten_prime_density=',prior_density)
    print('combined_lower_density=',final_density,'decimal=',float(final_density))
    print('threshold_for_certified_residue_classes=',15376**2+1)

if __name__ == '__main__':
    main()
