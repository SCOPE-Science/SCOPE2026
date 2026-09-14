"""Sanity checks for the D=178 quartic-slice census.

Verifies: D % 4 == 2, factor-pair parity obstruction, and brute-force
absence of solutions for small y.
"""
import math

D = 178
assert D == 2 * 89 and D % 4 == 2, "D must be 2 mod 4"

# Every factor pair of 178 has mixed parity -> no same-parity pair exists.
pairs = [(d, D // d) for d in range(1, D + 1) if D % d == 0 and d <= D // d]
print("factor pairs:", pairs)
assert pairs == [(1, 178), (2, 89)]
for a, b in pairs:
    assert (a % 2) != (b % 2), "unexpected same-parity pair"
print("parity obstruction confirmed: no same-parity factor pair of 178.")


def is_square(k):
    if k < 0:
        return False
    r = math.isqrt(k)
    return r * r == k


sols = []
for y in range(2, 200):
    for n in (4, 8, 12):
        v = y ** n - D
        if v >= 0 and is_square(v):
            sols.append((math.isqrt(v), y, n))
print("solutions with y<200, n in {4,8,12}:", sols)
assert sols == []

sols4 = []
for y in range(2, 5000):
    if is_square(y ** 4 - D):
        sols4.append(y)
print("solutions with n=4, y<5000:", sols4)
assert sols4 == []
print("OK: brute force consistent with empty list.")
