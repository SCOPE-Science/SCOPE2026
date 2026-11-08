#!/usr/bin/env python3
"""Independent graph update and boundary-record census for 3-state excitation on paths."""
from itertools import product

def step(a):
    out = []
    for j, v in enumerate(a):
        if v == 1:
            out.append(2)
        elif v == 2:
            out.append(0)
        else:
            out.append(int((j > 0 and a[j-1] == 1) or
                           (j+1 < len(a) and a[j+1] == 1)))
    return tuple(out)

def terminal_record(a):
    heights = [0]
    for left, right in zip(a, a[1:]):
        heights.append(heights[-1] + ((left == 0 and right == 1) -
                                      (left == 1 and right == 0)))
    return heights[-1] > max(heights[:-1]) or heights[0] > max(heights[1:])

def exact_coeffs(n):
    # A(z) = sqrt((1+z)/(1-3z)); (1-2z-3z^2) A'(z) = 2 A(z).
    vals=[1,2]
    for k in range(2,n):
        numer=2*k*vals[-1]+3*(k-2)*vals[-2]
        assert numer % k == 0
        vals.append(numer//k)
    return vals[:n]

coeffs=exact_coeffs(13)
for n in range(1,13):
    extreme=0
    records=0
    for a in product(range(3),repeat=n):
        x=a
        for t in range(n+2):
            if not any(x):
                break
            x=step(x)
        else:
            raise AssertionError(('no extinction',n,a))
        # n+1 is the worst possible first-zero entry time
        is_extreme=(t==n+1)
        is_rec=terminal_record(a) if n>1 else (a==(1,))
        assert is_extreme == is_rec,(n,a,t,is_rec)
        extreme+=is_extreme
        records+=is_rec
    assert extreme==coeffs[n-1],(n,extreme,coeffs[n-1])
    print(f'n={n}: maximum-time colorings={extreme}; exact-series coefficient={coeffs[n-1]}; OK')
print('EXHAUSTIVE_OK')
