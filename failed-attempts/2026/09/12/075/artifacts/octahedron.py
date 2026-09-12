"""Verify octahedron-type recurrence for Z_n(a).
Hypothesis: T_n = Z_n satisfies T_n*T_{n-4} = T_{n-1}*T_{n-3} + (correction)?
Since log T is exactly quadratic per mod-4 class, T_n*T_{n-2}/(T_{n-1}*T_{n-3})... let's find exact relations.
Actually exact per-class quadraticity means: T_{n+4}*T_n / T_{n+2}^2 = e^{8 F0} (constant in n, same all classes?).
And 2nd finite difference in steps of 4 is exactly 8 F0.
"""
import numpy as np, math
from kasteleyn import logZ
for a in [0.3, 0.7]:
    print(f"--- a={a} ---")
    lz={n: logZ(n,a) for n in range(0,25)}
    lz[0]=0.0
    for n in range(1,21):
        d2 = lz[n+4]-2*lz[n+2]+lz[n]
        print(f"n={n:2d} D4^2={d2:.12f}", end="  ")
        if n%4==1: print()
    print()
    # ratio T_{n} T_{n-4} / T_{n-2}^2
    for n in range(4,21):
        r = math.exp(lz[n]+lz[n-4]-2*lz[n-2])
        print(f"n={n} ratio={r:.12f}")
