#!/usr/bin/env python3
"""Independent replay verifier for the frozen Mordell-family boundary at p*=73.
Stdlib only (fractions). Re-checks:
  (A) primality + completeness of 1-mod-4 primes below 73,
  (B) parametric coverage of each by frozen family M = {F3,F5,F17},
  (C) finite non-membership (elimination) certificates for 73,
  (D) explicit witness triple for 4/73.
"""
from fractions import Fraction

def check(n, x, y, z):
    return Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

# ---- frozen family M (fixed before computation) ----
def F3(n):
    """Mordell n=4k+3: (k+1, 2n(k+1), 2n(k+1))."""
    assert n % 4 == 3, n
    k = (n - 3) // 4
    A = k + 1
    return (A, 2 * n * A, 2 * n * A)

def F5(n):
    """Mordell n=8M-3: (2M, nM, 2nM)."""
    assert (n + 3) % 8 == 0, n
    M = (n + 3) // 8
    return (2 * M, n * M, 2 * n * M)

def F17(n):
    """Mordell n=24M-7: (6M, nM, 6nM)."""
    assert (n + 7) % 24 == 0, n
    M = (n + 7) // 24
    return (6 * M, n * M, 6 * n * M)

# (A) completeness of 1-mod-4 primes below 73
cands = [m for m in range(5, 73) if m % 4 == 1]
primes = [m for m in cands if is_prime(m)]
assert primes == [5, 13, 17, 29, 37, 41, 53, 61], primes
assert is_prime(73) and 73 % 4 == 1
print("primes 1mod4 below 73:", primes)

# (B) coverage table
expected = {
    5: ("F5", F5(5)), 13: ("F5", F5(13)), 17: ("F17", F17(17)),
    29: ("F5", F5(29)), 37: ("F5", F5(37)), 41: ("F17", F17(41)),
    53: ("F5", F5(53)), 61: ("F5", F5(61)),
}
for p, (tag, t) in expected.items():
    assert check(p, *t), (p, tag, t)
    print(f"  {p}: {tag} {t}  OK")

# (C) elimination certificates for 73
p = 73
assert (p - 3) % 4 != 0          # F3 needs p=3 mod 4; 73=1 mod 4
assert (p + 3) % 8 == 4 and (p + 3) % 8 != 0  # F5 needs (p+3)%8==0; 76%8=4
assert (p + 7) % 24 == 8 and (p + 7) % 24 != 0  # F17 needs (p+7)%24==0; 80%24=8
# residue-class form: 1-mod-4 primes split 5,13,29,37,53,61 (8M-3, F5) vs 17,41 (24M-7, F17);
# 73 = 8*9+1 = 24*3+1 hits neither admissible class.
print("elimination certs: F3 fails (73=1mod4), F5 fails (76mod8=4), F17 fails (80mod24=8)  OK")

# (D) witness triple
w = (20, 292, 730)
assert check(73, *w), w
print("witness 4/73 = 1/20+1/292+1/730  OK")
# show the divisor structure
assert 292 == 4 * 73 and 730 == 10 * 73
assert Fraction(4, 73) - Fraction(1, 20) == Fraction(7, 1460) == Fraction(1, 292) + Fraction(1, 730)
print("ALL CHECKS PASSED")
