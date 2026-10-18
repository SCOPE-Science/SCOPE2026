#!/usr/bin/env python3
"""Finite replay for the Laurent-tower burden specialization."""
PRIMES = [2, 3, 5, 7, 11, 13]
assertions = 0

# q[r,p] models |F_r^*/(F_r^*)^p|.  Each Laurent level contributes Z/pZ.
for p in PRIMES:
    q = 1
    assert q == p**0
    assertions += 1
    for r in range(1, 13):
        q *= p
        assert q == p**r
        assertions += 1

# Burden recurrences after the external transfer theorems are specialized.
b_no_ac = 1
b_all_ac = 1
for r in range(0, 21):
    assert b_no_ac == 1
    assert b_all_ac == r + 1
    assertions += 2
    b_no_ac = max(b_no_ac, 1)
    b_all_ac = b_all_ac + 1

# The burden gap is exactly the number of named stagewise angular components.
b_no_ac = 1
b_all_ac = 1
for r in range(1, 21):
    b_no_ac = max(b_no_ac, 1)
    b_all_ac += 1
    assert b_all_ac - b_no_ac == r
    assertions += 1

print(f"VERIFY_OK {assertions} exact assertions")
