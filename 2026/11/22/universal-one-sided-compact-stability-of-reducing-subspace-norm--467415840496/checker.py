"""Supplementary finite block and sign-tail diagnostics (not an infinite proof)."""
import math

checks = 0
last_plus, last_minus = float('inf'), float('inf')
for n in range(1, 301):
    eps = 1.0 / (4 * n)
    delta = math.sqrt(1 + 4 * eps * eps)
    plus = (3 + 2 * eps + delta) / 2
    minus = (3 + 2 * eps - delta) / 2
    assert plus > 2 and 1 < minus < 2
    checks += 1
    assert plus < last_plus and minus < last_minus
    checks += 1
    assert abs((plus + minus) - (3 + 2 * eps)) < 1e-12
    checks += 1
    assert abs(plus * minus - (2 + 3 * eps)) < 1e-12
    checks += 1
    last_plus, last_minus = plus, minus

for n in range(1, 301):
    t = 2.0 ** (-n) if n < 1020 else 0.0
    if n < 40:
        assert 0 < 1 - t < 1
        checks += 1
    if n < 40:
        assert 1 - 2**(-(n + 1)) > 1 - 2**(-n)
        checks += 1

print('ONE_SIDED_COMPACT_STABILITY_DIAGNOSTIC_OK', checks)
