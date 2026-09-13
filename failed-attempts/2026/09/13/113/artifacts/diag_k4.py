"""Diagnose l=3,k=4 FULL: tabulate chi(p) vs expected (p-1)(p-24)^3."""
import sys
sys.path.insert(0, '.')
from chi_count import chi_at_p
l, k = 3, 4
print('p chi_got chi_expected_aff grounded?')
for p in [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 97]:
    got = chi_at_p(l, k, p, None)
    exp = (p - 1) * (p - 24) ** 3
    print(p, got, exp, 'OK' if got == exp else 'DIFF')
