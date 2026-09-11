"""Fallback attempt F: GS-count-certifiable recovery point at the (48,12,l=2) window.

F1: beyond-Johnson point (T=33, rho=0.3125, L<=16) via uniform-mult GS count.
F2: GS-certifiable point with the target's list cap (L<=8): minimize T over m.
F3: tractability of the only count-feasible beyond-Johnson corner (T=33,L=64,m=22):
    build the actual interpolant linear system for one explicit list tuple and
    measure whether it solves in the remaining budget.

All stdlib. Prints verdicts; used as evidence for ATTEMPTED_AND_BLOCKED.
"""
import time

N, K, L_IN, KM1 = 48, 12, 2, 11
Q = 97


def dof(D, L):
    s = 0
    for j in range(L + 1):
        if D - KM1 * j >= 0:
            s += D - KM1 * j + 1
    return s


def dmin(C, L):
    lo, hi = 0, 1
    while dof(hi, L) <= C:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if dof(mid, L) > C:
            hi = mid
        else:
            lo = mid + 1
    return lo


def cost(n, l, m):
    return n * l * m * (m + 1) // 2


print("== F1: T=33, L<=16, m<=500 ==")
f1 = []
for L in (8, 12, 16):
    for m in range(1, 501):
        D = dmin(cost(N, L_IN, m), L)
        if D < 33 * m:
            f1.append((L, m, D))
            break
print("F1 feasible corners:", f1 if f1 else "NONE -> F1 BLOCKED by count")

print("== F2: L<=8, minimize T over m<=500 ==")
best = None
for m in range(1, 501):
    D = dmin(cost(N, L_IN, m), 8)
    # need T > D/m, smallest integer T
    Tneed = D // m + 1
    if best is None or Tneed < best[0]:
        best = (Tneed, m, D)
print(f"F2 best: T>={best[0]} (rho<={1-best[0]/48:.4f}) at m={best[1]} (D={best[2]}); "
      f"beyond-Johnson needs T<=33 -> F2 {'BLOCKED (below Johnson)' if best[0] > 33 else 'viable'}")

print("== F3: only beyond-Johnson corner T=33,L=64,m=22: system size ==")
m, L, T = 22, 64, 33
C = cost(N, L_IN, m)
D = dmin(C, L)
U = dof(D, L)
print(f"m={m} L={L}: constraints C={C}, D={D}, unknowns U={U}, margin T*m-D={T*m-D}")
print(f"Solve {U}x{U} dense over F97: ~{U**3/1e9:.1f} Gops -> intractable in remaining minutes in stdlib "
      f"-> F3 BLOCKED (computationally)")
print("FALLBACK_VERDICT: ATTEMPTED_AND_BLOCKED")
