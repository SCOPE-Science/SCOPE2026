"""Observed blow-up stability of the corrected ledger (downgraded claim).

Attaches a (-1)-leaf to the center of each graph, recomputes the corrected
two-sided fiber minima, and reports the S0/S1 run shapes. This is an
observed stability datum, NOT a proof of the blow-up/surgery exact sequence.
"""
import sys
sys.path.insert(0, "output/artifacts")
from laufer import (build_star, canon_vec, fiber_min, is_closed,
                    arm_chains, rhs_vec, certify_fiber, total_w2,
                    real_min_quad, tail_window)

def blowup_center(M):
    n = len(M)
    N = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            N[i][j] = M[i][j]
    N[0][0] -= 1; N[0][n] = N[n][0] = 1; N[n][n] = -1
    return N

def ledger(M, mc, N):
    rhs = rhs_vec(M); arms = arm_chains(M)
    A, B, C = real_min_quad(M, rhs)
    lo, hi = tail_window(A, B, C, N)
    ws, xms = {}, {}
    for i in range(lo, hi+1):
        w, xm = fiber_min(M, mc, i)
        assert is_closed(M, xm)
        certify_fiber(M, mc, rhs, arms, i, xm)
        assert total_w2(M, rhs, arms, i, xm) == 2*w
        ws[i] = w; xms[i] = xm
    return ws, (lo, hi)

def runs(ws, n):
    S = sorted(i for i, w in ws.items() if w <= n)
    R = []
    for i in S:
        if R and i == R[-1][-1]+1: R[-1].append(i)
        else: R.append([i])
    return R

for name, M in (("G7", build_star(-1, [[-2],[-3],[-7]])),
                ("G11", build_star(-2, [[-2],[-2,-2],[-2,-2,-2,-2,-3]]))):
    mc = canon_vec(M)
    ws, win = ledger(M, mc, 1)
    print(f"{name}: window {win} S0={runs(ws,0)} S1={runs(ws,1)}")
    B = blowup_center(M); mB = canon_vec(B)
    wB, winB = ledger(B, mB, 1)
    K2s = sum(mB[i]*B[i][j]*mB[j] for i in range(len(B)) for j in range(len(B))) + len(B)
    print(f"{name}+(-1): window {winB} K2s={K2s} min={min(wB.values())} "
          f"S0={runs(wB,0)} S1={runs(wB,1)}")
print("STABILITY_OK")
