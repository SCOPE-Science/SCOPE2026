"""Exact checks for an ordered geometric pollen-transfer counterexample.
Run using Python 3 with no nonstandard dependencies: python verify.py
"""
from math import comb
from fractions import Fraction

A = '110001001'
B = '011100100'
N = 9
P = [1,0,0,-2,-1,0,-1,1,0,1]
TRANSFORM = [1,9,36,82,113,91,33,-6,-9,-1]


def lag_profile(word):
    return tuple(sum(word[i] == word[i + d]
                     for i in range(len(word) - d))
                 for d in range(1, len(word)))


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out


def success_polynomial(word):
    # One distinct plant per visit; recipient i gets independent donor attempts.
    total = [0]
    for i, species in enumerate(word):
        failed = [1]
        for j in range(i):
            if word[j] == species:
                factor = [1] + [0] * (i-j-1) + [-1]
                failed = mul(failed, factor)
        success = add([1], [-x for x in failed])
        total = add(total, success)
    return total


def eval_poly(a, x):
    z = 0
    for c in reversed(a): z = z*x + c
    return z


def canonical(word):
    flip = ''.join('0' if c == '1' else '1' for c in word)
    return min(word, flip, word[::-1], flip[::-1])


def check():
    assert A.count('1') == B.count('1') == 4
    assert lag_profile(A) == lag_profile(B) == (4,2,3,3,2,0,1,1)
    assert canonical(A) != canonical(B)
    poly_a, poly_b = success_polynomial(A), success_polynomial(B)
    difference = add(poly_a, [-z for z in poly_b])
    predicted = mul([0]*6+[1], mul([-1,1], mul([1,1,1], P)))
    assert difference == predicted, (difference, predicted)
    transform = [sum(P[j]*comb(9-j, k-j) for j in range(k + 1))
                 for k in range(10)]
    # Coefficients of (1+t)^9 P(t/(1+t)):
    assert transform == TRANSFORM
    signs = [1 if x > 0 else -1 for x in transform if x]
    assert sum(u != v for u,v in zip(signs,signs[1:])) == 1
    assert eval_poly(P,0) == 1 and eval_poly(P,1) == -1
    assert eval_poly(P,Fraction(7,10)) > 0
    assert eval_poly(P,Fraction(3,4)) < 0
    assert eval_poly(difference,Fraction(1,2)) < 0
    assert eval_poly(difference,Fraction(9,10)) > 0
    # Independent exhaustive eight-and-below binary lag-equivalence census.
    # Only reflection and species exchange are allowed trivial ambiguities.
    for n in range(1,9):
        seen = {}
        for j in range(1<<n):
            word = format(j, '0%db' % n)
            profile = lag_profile(word)
            orbit = canonical(word)
            assert profile not in seen or seen[profile] == orbit
            seen[profile] = orbit
    # At nine, the full lag-profile (4,2,3,3,2,0,1,1) has two
    # nontrivial symmetry classes, and all nine-word profiles have at most two.
    buckets = {}
    for j in range(1<<9):
        word = format(j, '09b')
        buckets.setdefault(lag_profile(word),set()).add(canonical(word))
    assert sum(len(v)==2 for v in buckets.values()) == 1
    assert max(map(len,buckets.values())) == 2
    assert len(buckets[lag_profile(A)]) == 2
    # Exactly equal every linear pairwise pollen-transfer score for all q.
    assert lag_profile(A)==lag_profile(B)
    print('PASS: exact pollen-score polynomial, unique crossover, full lag homometry, 1..9 exhaustive binary census')

if __name__ == '__main__':
    check()
