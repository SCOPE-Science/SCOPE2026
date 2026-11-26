"""Exact finite checks for typical digit frequencies of the 3-adic triple sum."""

from collections import Counter
from fractions import Fraction
from itertools import product


raw = Counter(map(sum, product((0, 1), repeat=3)))
carry = [[0, 0], [0, 0]]
digits = [[0, 0, 0], [0, 0, 0]]
for c in (0, 1):
    for s, weight in raw.items():
        next_carry, digit = divmod(s + c, 3)
        carry[c][next_carry] += weight
        digits[c][digit] += weight
assert carry == [[7, 1], [4, 4]]
assert digits == [[2, 3, 3], [3, 2, 3]]
pi = [Fraction(4, 5), Fraction(1, 5)]
assert [sum(pi[c] * carry[c][j] / 8 for c in range(2)) for j in range(2)] == pi
freq = [sum(pi[c] * digits[c][d] / 8 for c in range(2)) for d in range(3)]
assert freq == [Fraction(11, 40), Fraction(14, 40), Fraction(15, 40)]

# Compare the one-position marginal obtained by iterating the carry chain
# with one obtained by extracting digits of ordinary (unreduced) sums.
hist = Counter({0: 1})
carry_probability = [Fraction(1), Fraction(0)]
for j in range(8):
    expanded = Counter()
    for n, count in hist.items():
        for s, weight in raw.items():
            expanded[n + s * 3**j] += count * weight
    hist = expanded
    marginal_counts = [0, 0, 0]
    for n, count in hist.items():
        marginal_counts[(n // 3**j) % 3] += count
    marginal = [Fraction(count, 8**(j+1)) for count in marginal_counts]
    assert marginal == [sum(carry_probability[c] * digits[c][d] / 8
                            for c in range(2)) for d in range(3)]
    carry_probability = [sum(carry_probability[c] * carry[c][i] / 8
                             for c in range(2)) for i in range(2)]

print('Exact digit-table, stationary-frequency and eight finite-marginal checks passed.')
