"""Exact certificate for a four-prime squarefree divisor-sum classification.

Requires only Python 3 and the standard library. This program complements,
but does not replace, the algebraic exhaustive-bound proof in RESULT.md.
"""
from fractions import Fraction
from math import isqrt, prod


def is_prime(n):
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, isqrt(n) + 1))


def R(p):
    return Fraction(p + 1, p - 1)


# Monotonic bounds used in the infinite reduction; these are exact fractions.
assert R(13)**4 < 2
assert R(11) * R(13)**3 < 2
assert R(5) * R(23)**3 < 2
assert R(5) * R(19) * R(23)**2 < 2
assert R(7) * R(17)**3 < 2
assert R(7) * R(13) * R(17)**2 < 2
for (p, q), excluded_r in [
    ((5, 11), 41), ((5, 13), 31),
    ((5, 17), 29), ((7, 11), 19),
]:
    assert R(p) * R(q) * R(excluded_r)**2 < 2

# Complete finite list left by the proved monotonic bounds.
triples = {}
for p, q in ((5, 11), (5, 13), (5, 17), (7, 11)):
    triples[(p, q)] = []
    for r in range(q + 1, 41):
        if not is_prime(r):
            continue
        A = R(p) * R(q) * R(r)
        if A < 2 and A * R(r) > 2:
            triples[(p, q)].append(r)

expected_triples = {
    (5, 11): [23, 29, 31, 37],
    (5, 13): [17, 19, 23, 29],
    (5, 17): [19, 23],
    (7, 11): [13, 17],
}
assert triples == expected_triples, (triples, expected_triples)

# The fourth prime s must solve A(s+1)=2(s-1), hence s=(2+A)/(2-A).
expected_candidates = {
    (5, 11, 23): Fraction(109),
    (5, 11, 29): Fraction(55),
    (5, 11, 31): Fraction(49),
    (5, 11, 37): Fraction(39),
    (5, 13, 17): Fraction(127),
    (5, 13, 19): Fraction(71),
    (5, 13, 23): Fraction(43),
    (5, 13, 29): Fraction(31),
    (5, 17, 19): Fraction(31),
    (5, 17, 23): Fraction(169, 7),
    (7, 11, 13): Fraction(29),
    (7, 11, 17): Fraction(19),
}
candidates = {}
solutions = []
for (p, q), rs in triples.items():
    for r in rs:
        A = R(p) * R(q) * R(r)
        s = (2 + A) / (2 - A)
        candidates[(p, q, r)] = s
        if s.denominator == 1 and s.numerator > r and is_prime(s.numerator):
            t = (p, q, r, s.numerator)
            assert prod(v + 1 for v in t) == 2 * prod(v - 1 for v in t)
            solutions.append(t)
assert candidates == expected_candidates
expected_solutions = [
    (5, 11, 23, 109),
    (5, 13, 17, 127),
    (5, 13, 19, 71),
    (5, 13, 23, 43),
    (5, 13, 29, 31),
    (5, 17, 19, 31),
    (7, 11, 13, 29),
    (7, 11, 17, 19),
]
assert solutions == expected_solutions, solutions
numbers = sorted(prod(t) for t in solutions)
assert numbers == [24871, 29029, 50065, 58435, 64285, 87685, 137885, 140335]
print('VERIFY_OK complete_prefix_cases=4 candidate_prime_triples=12 solutions=8')
print('numbers=' + ','.join(map(str, numbers)))
