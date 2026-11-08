#!/usr/bin/env python3
"""Exact modular checks for the odd double-factorial residue theorem."""
from collections import Counter

def odd_double_factorial_values(modulus, length):
    a = 1
    values = []
    for n in range(length):
        values.append(a)
        a = a * (2*n + 1) % modulus
    return values

def nu2(x):
    assert x != 0
    return (x & -x).bit_length() - 1

# Verify complete index periods and every fiber for precisions through 15.
case_count = 0
for k in range(1, 16):
    m = 1 << k
    vals = odd_double_factorial_values(m, 2*m)
    predicted_period = 1 if k == 1 else (4 if k == 2 else (1 << (k-1)))
    assert vals[:m] == vals[predicted_period:predicted_period+m], (k, 'period')
    if k > 1:
        # Minimal period: direct scan, with at least two full periods.
        for d in range(1, predicted_period):
            if all(vals[i] == vals[i+d] for i in range(predicted_period)):
                raise AssertionError((k, 'shorter period', d))
    fibers = Counter(vals[:m])
    if k >= 4:
        expected = {
            y: (6 if y%16==1 else 2 if y%8==3 or y%16==9 else 4 if y%16==15 else 0)
            for y in range(m)
        }
        assert all(fibers[y] == c for y,c in expected.items()), (k, 'fiber mismatch')
        assert len(fibers) == 5*(1 << (k-4)), (k,'image')
    elif k == 3:
        assert set(fibers) == {1,3,7}
    elif k == 2:
        assert set(fibers) == {1,3}
    else:
        assert set(fibers) == {1}
    case_count += 1

# Independently check the sharp block-product valuation for all short offsets.
checks = 0
for t in range(2, 11):
    for n in range(0, 80):
        modulus = 1 << (t+8)
        prod = 1
        for j in range(1 << t):
            prod = (prod * (2*(n+j)+1)) % modulus
        assert nu2((prod - 1) % modulus) == t + 1 + (n&1), (t,n)
        checks += 1
print(f'VERIFY_OK levels={case_count} block_valuations={checks} max_modulus=32768')
