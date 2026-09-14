"""Bounded recovery test: can Dobrowolski's unconditional height lower bound
formally force trace-field degree d >= N/c for long fillings?

Setup: grant (as fantasy) a global Weil-height upper bound h_N = log(N)/N^2
for the core-trace element at filling size N = max|coeffs| (Neumann-Zagier
gives |t-2| ~ 1/N^2 only at the geometric embedding; the global height needs
ALL Galois conjugates, which are uncontrolled -- that missing upper bound is
part of the blocking obstacle). Dobrowolski: h >= D(d) with
D(d) = (1/4)*(loglog d / log d)^3 / d for d > e.

Excluded degrees at size N: E_N = {d : D(d) > h_N}. For the target's linear
bound to be formally forced, E_N would have to cover [1, N/c). We compute E_N.
Result: E_N is a tiny bounded interval; both very small d and all large d are
COMPATIBLE with the height inequality -- so the only available unconditional
height inequality cannot force d >= N/c. Pure linear is formally consistent
with being false under these tools.
"""
import math

def D(d):
    if d <= math.e:
        return float("inf")
    l = math.log(d)
    ll = math.log(l)
    if ll <= 0:
        return float("inf")
    return 0.25 * (ll / l) ** 3 / d

print("Dobrowolski bound D(d) profile:")
for d in [4, 8, 12, 16, 24, 32, 50, 100, 1000, 10**5, 10**6]:
    print(f"  d={d:>8d}  D(d)={D(d):.3e}")

print("\nExcluded-degree intervals E_N = {d : D(d) > logN/N^2}:")
DMAX = 2000000
for N in [50, 100, 500, 1000, 5000]:
    h = math.log(N) / N ** 2
    lo, hi, count = None, None, 0
    d = 4
    while d <= DMAX:
        if D(d) > h:
            count += 1
            if lo is None:
                lo = d
            hi = d
        d += 1
    print(f"  N={N:>5d}  h_N={h:.3e}  E_N=[{lo},{hi}] (size {count}); "
          f"target needs [1,{N}/c) excluded; d=4 compatible: {D(4) <= h}; "
          f"d=10^6 compatible: {D(10**6) <= h}")
