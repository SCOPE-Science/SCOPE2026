#!/usr/bin/env python3
"""Exact rational checks for quadratic Walsh tight sampling on Hamming layers."""
from fractions import Fraction
from itertools import combinations, product
from math import isqrt


def shells(n):
    return [s for s in range(n % 2, n + 1, 2)]


def moments(n, s):
    u = s * s
    return (Fraction(u - n, n * (n - 1)),
            Fraction(u * u - (6 * n - 8) * u + 3 * n * (n - 2),
                     n * (n - 1) * (n - 2) * (n - 3)))


def two_shell_pairs(n):
    for a in shells(n):
        u = a * a
        if u >= n:
            break
        t = 2 * n * (n - 1)
        if t % (n - u):
            continue
        v = n + t // (n - u)
        b = isqrt(v)
        if b <= n and b*b == v and (b - n) % 2 == 0:
            yield (a, b)


def weights(n, a, b):
    return (Fraction(b * b - n, b * b - a * a),
            Fraction(n - a * a, b * b - a * a))


def exact_gram(n, shells_and_weights):
    # All vertices are treated individually, with exact per-vertex probabilities.
    pairs = list(combinations(range(n), 2))
    gram = [[Fraction(0) for _ in pairs] for _ in pairs]
    for s, mass in shells_and_weights:
        vertices = [x for x in product((-1, 1), repeat=n) if sum(x) == s]
        assert vertices
        for x in vertices:
            values = [x[i] * x[j] for i,j in pairs]
            factor = mass / len(vertices)
            for i in range(len(pairs)):
                for j in range(len(pairs)):
                    gram[i][j] += factor * values[i] * values[j]
    assert all(gram[i][j] == (1 if i==j else 0)
               for i in range(len(pairs)) for j in range(len(pairs)))


# Newton identities for each shell, tested directly, including all signs.
for n in range(4, 11):
    for s in range(-n, n+1, 2):
        xs = [x for x in product((-1, 1), repeat=n) if sum(x) == s]
        m2, m4 = moments(n, s)
        assert Fraction(sum(x[0]*x[1] for x in xs), len(xs)) == m2
        assert Fraction(sum(x[0]*x[1]*x[2]*x[3] for x in xs), len(xs)) == m4

# Exact min-two-shell criterion and positive weights at representative orders.
examples = [(6, 0, 4), (6, 2, 6), (8, 2, 6), (11, 3, 11),
            (18, 4, 18), (22, 0, 8), (27, 1, 9), (33, 3, 11),
            (34, 0, 10), (96, 4, 18)]
for n, a, b in examples:
    assert (a,b) in list(two_shell_pairs(n))
    wa, wb = weights(n,a,b)
    assert wa>0 and wb>0 and wa+wb==1
    m2a,m4a = moments(n,a)
    m2b,m4b = moments(n,b)
    assert wa*m2a+wb*m2b == 0
    assert wa*m4a+wb*m4b == 0

for n, a, b in [(6,0,4),(8,2,6)]:
    wa,wb = weights(n,a,b)
    exact_gram(n,[(a,wa),(b,wb)])

# Mod-8 no-two-shell families are checked across a substantial finite range.
for n in range(4, 3001):
    cases = list(two_shell_pairs(n))
    assert (n%8 in (4,5,7)) <= (not cases)

# Infinite constructive families: exact rational identities at sampled indices.
for m in range(2,51):
    n=m*m+2; a=m; b=n
    assert (a,b) in list(two_shell_pairs(n))
for b in range(4,101,2):
    if b%3==0:continue
    n=(b*b+2)//3
    assert (0,b) in list(two_shell_pairs(n))

print('QUADRATIC_WALSH_TWO_SHELL_PASS moments=4..10 exact_gram=6,8 modular_orders=4..3000 infinite_families=checked')
