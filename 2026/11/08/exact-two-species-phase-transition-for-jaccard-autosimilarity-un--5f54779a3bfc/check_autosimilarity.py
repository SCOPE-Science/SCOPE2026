"""Exact finite checks for two-species iid Jaccard autosimilarity.

This checker verifies finite identities and examples; the all-parameter
phase theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import sqrt


def j_formula(p, n):
    q = 1 - p
    return 1 - p**n - q**n + p**(2*n) + q**(2*n)


def j_enumerated(p, n):
    q = 1 - p
    # Enumerate all sample sequences and their probabilities exactly.
    rows = []
    for sequence in product((0, 1), repeat=n):
        weight = p**sequence.count(0) * q**sequence.count(1)
        mask = (1 if 0 in sequence else 0) | (2 if 1 in sequence else 0)
        rows.append((mask, weight))
    return sum((a & b).bit_count() * wa * wb /
               (a | b).bit_count()
               for a, wa in rows for b, wb in rows)


def j_general(probabilities, n):
    # Dynamic exact distribution of observed-species sets; independent replicates.
    states = {0: Fraction(1)}
    for _ in range(n):
        nxt = {}
        for mask, weight in states.items():
            for i, probability in enumerate(probabilities):
                new_mask = mask | (1 << i)
                nxt[new_mask] = nxt.get(new_mask, Fraction(0)) + weight*probability
        states = nxt
    return sum(wa*wb*Fraction((ma & mb).bit_count(), (ma | mb).bit_count())
               for ma, wa in states.items() for mb, wb in states.items())


def check():
    checks = 0
    probabilities = [Fraction(a, b) for a, b in
                     [(1, 2), (2, 3), (3, 4), (4, 5),
                      (9, 10), (19, 20), (49, 50)]]
    for p in probabilities:
        q = 1 - p
        t = p*q
        for n in range(1, 9):
            assert j_formula(p, n) == j_enumerated(p, n)
            checks += 1
        assert j_formula(p, 2) - j_formula(p, 1) == 2*t*t
        checks += 1
        assert j_formula(p, 3) - j_formula(p, 2) == t*(-2*t*t + 7*t - 1)
        checks += 1
        for n in range(1, 60):
            delta = j_formula(p, n+1) - j_formula(p, n)
            delta_by_parts = (q*p**n*(1-(1+p)*p**n) +
                              p*q**n*(1-(1+q)*q**n))
            assert delta == delta_by_parts
            checks += 1
    p = Fraction(9, 10)
    assert j_formula(p, 1) == Fraction(41, 50)
    assert j_formula(p, 2) == Fraction(4181, 5000)
    assert j_formula(p, 3) == Fraction(400721, 500000)
    assert j_formula(p, 6) > j_formula(p, 7)
    assert j_formula(p, 7) < j_formula(p, 8)
    checks += 5
    # Parameter threshold: exact algebraic root of p*(1-p)=(7-sqrt(41))/4.
    pc = (1 + sqrt(sqrt(41) - 6))/2
    assert 0.81745 < pc < 0.81747
    checks += 1
    # The factor identity used for strict increase of the normalized
    # increment on the upper-abundance branch.
    for p in probabilities:
        lhs = (1+p)*p**4 - (2*p-1)
        rhs = (p*p+p-1)*(p**3+p-1)
        assert lhs == rhs
        checks += 1
    for number_species in (3, 4, 5, 7):
        epsilon = Fraction(1, 10000*number_species)
        remaining = 1 - (number_species-2)*epsilon
        abundances = [remaining*Fraction(9,10), remaining*Fraction(1,10)]
        abundances += [epsilon]*(number_species-2)
        j = {n: j_general(abundances, n) for n in (1,2,3,6,7,8)}
        assert j[2] > j[1]
        assert j[2] > j[3]
        assert j[6] > j[7]
        assert j[8] > j[7]
        checks += 4
    print(f'PASS: {checks} exact/equality and witness checks')


if __name__ == '__main__':
    check()
