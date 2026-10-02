#!/usr/bin/env python3
"""Numerical checks for the reciprocal polylogarithmic smoothing threshold."""
import mpmath as mp

mp.mp.dps = 60
N = 100000

def B_bounds(s):
    s = mp.mpf(s)
    partial = mp.fsum(
        1 / (mp.mpf(m) * mp.power(m + 2, 2 * s))
        for m in range(1, N + 1)
    )
    # For m>N,
    # 1/[m(m+2)^(2s)] < m^(-2s-1), and the decreasing-tail
    # integral gives sum_{m>N} m^(-2s-1) <= N^(-2s)/(2s).
    upper = partial + mp.power(N, -2 * s) / (2 * s)
    return partial, upper

def H_bounds(s):
    lo, hi = B_bounds(s)
    first = mp.power(2, 1 - mp.mpf(s))
    return first + mp.sqrt(lo), first + mp.sqrt(hi)

for s in ("1.413519", "1.413520"):
    lo, hi = H_bounds(s)
    print(s, "H lower - 1 =", mp.nstr(lo - 1, 25),
          "H upper - 1 =", mp.nstr(hi - 1, 25))

lo_a, _ = H_bounds("1.413519")
_, hi_b = H_bounds("1.413520")
assert lo_a > 1
assert hi_b < 1

# Elementary majorant used for the U-functional estimate at sigma >= 7/5:
# sum_{n>=2} n^(-9/5)
# <= 2^(-9/5)+3^(-9/5)+integral_3^infty x^(-9/5) dx.
C_majorant = (
    mp.power(2, -mp.mpf(9)/5)
    + mp.power(3, -mp.mpf(9)/5)
    + mp.mpf(5)/4 * mp.power(3, -mp.mpf(4)/5)
)
print("C majorant at 7/5 =", mp.nstr(C_majorant, 30))
assert C_majorant < 1

print("all checks passed")
