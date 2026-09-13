"""Bounded recovery check for lane-1776 (referenced by WORKLOG.md).

Computes p_c(3), the n^{-0.10} revealment targets, and the uniform
annulus-circuit constant required to drive a dyadic one-arm upper bound
with exponent 0.10. Shows the gap is the missing explicit RSW constant.
"""
import math

pc = math.sqrt(3) / (1 + math.sqrt(3))
print(f"p_c(3) = {pc:.12f}")
for n in [64, 128, 256, 512, 1024, 10**6]:
    print(f"n={n:>8d}  n^(-0.10)={n**(-0.10):.6f}")

c2 = 1 - 2 ** (-0.10)
c4 = 1 - 4 ** (-0.10)
print(f"required dyadic (factor-2) circuit constant c* = {c2:.6f}")
print(f"required factor-4 circuit constant c* = {c4:.6f}")
for c in [0.01, 0.02, 0.05, c2]:
    exp2 = -math.log(1 - c) / math.log(2)
    print(f"illustrative c={c:.5f} -> dyadic one-arm exponent {exp2:.5f} "
          f"({'BELOW' if exp2 < 0.10 else 'MEETS'} 0.10)")
