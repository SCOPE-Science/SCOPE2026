#!/usr/bin/env python3
"""Exact rational certificate and direct finite checks for a binomial-sum residue theorem."""
from fractions import Fraction
from math import comb

P = 5
W = (1, 2, 1, 0, 0)
CUM = (0, 1, 3, 4, 4)
ACTIVE = [(u, a) for u in range(P) for a in range(1, P)]
INDEX = {state: j for j, state in enumerate(ACTIVE)}


def step(state, digit):
    u, a = state
    return ((4 * u + CUM[digit] * a) % P, (W[digit] * a) % P)


def apply_b(v):
    out = [0] * 20
    for j, state in enumerate(ACTIVE):
        for digit in range(3):
            out[INDEX[step(state, digit)]] += v[j]
    return out


def apply_c(v):
    out = [0] * P
    for j, state in enumerate(ACTIVE):
        for digit in (3, 4):
            dest = step(state, digit)
            assert dest[1] == 0
            out[dest[0]] += v[j]
    return out


# The row index is u=0,...,4; the column index is a=1,...,4.
# This integer array is 100800*(I - B^2/25)^(-1)*e_(0,1).
CERT = [
    [110373, 5561, 689, 877],
    [373, 5561, 689, 5877],
    [4973, 961, 689, 877],
    [4973, 5561, 689, 1277],
    [373, 5561, 289, 1277],
]
T = [CERT[u][a - 1] for u, a in ACTIVE]
B2T = apply_b(apply_b(T))
e = [1 if st == (0, 1) else 0 for st in ACTIVE]
assert all(25 * T[j] - B2T[j] == 25 * 100800 * e[j] for j in range(20))

ct = apply_c(T)
cbt = apply_c(apply_b(T))
q = [Fraction(ct[(-y) % 5] * 5 + cbt[y], 25 * 100800) for y in range(5)]
q_even = [Fraction(v, 14) for v in (1, 8, 2, 1, 2)]
q_odd = [q_even[(-y) % 5] for y in range(5)]
assert q == q_even
assert sum(q) == 1
assert q_odd == [Fraction(v, 14) for v in (1, 2, 1, 2, 8)]


def digit_product(n):
    a = 1
    while n:
        a = a * W[n % 5] % 5
        n //= 5
    return a


# Verify Lucas' digit product against direct integer binomials.
for n in range(201):
    assert digit_product(n) == comb(2 * n, n) % 5

# Independently accumulate the original partial sums and check all five residues.
expected = {
    1: [1, 1, 0, 1, 2],
    2: [3, 14, 3, 2, 3],
    3: [9, 19, 8, 19, 70],
    4: [47, 358, 87, 46, 87],
    5: [221, 451, 220, 451, 1782],
    6: [1123, 8934, 2223, 1122, 2223],
    7: [5569, 11179, 5568, 11179, 44630],
}

# Second implementation: state transition for every n, rather than only the digit product.
def recursive_state(n):
    digits = []
    while n:
        digits.append(n % 5)
        n //= 5
    state = (0, 1)
    for d in reversed(digits):
        state = step(state, d)
    return state

for r in range(1, 8):
    freq = [0] * P
    partial = 0
    for n in range(5 ** r):
        freq[partial] += 1
        if r <= 4:
            assert recursive_state(n) == (partial, digit_product(n))
        partial = (partial + digit_product(n)) % 5
    assert freq == expected[r], (r, freq)
    assert partial == pow(4, r, 5)
    Q = q_even if r % 2 == 0 else q_odd
    for y in range(5):
        assert abs(Fraction(freq[y], 5 ** r) - Q[y]) <= Fraction(3 ** r, 5 ** r)

print('PASS: 20 exact matrix equations; 5 rational limiting frequencies;')
print('      201 direct binomial congruences; 7 complete block histograms;')
print('      transition checks and rigorous finite-depth error bounds.')
print('even:', ', '.join(map(str, q_even)))
print('odd: ', ', '.join(map(str, q_odd)))
