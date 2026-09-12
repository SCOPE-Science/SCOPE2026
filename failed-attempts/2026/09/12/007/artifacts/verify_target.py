"""Replayable certificate: corrected R7 vs R11 reduced graded-root verdict.

Single consistent Nemethi sign chi(x)=-(x^T M x + m^T M x)/2. Two-sided
Laufer + per-arm exact DP optimality certificates; rigorous real tail
windows (exact Schur complement) prove no fiber outside the window can
meet the verdict levels. Prints VERIFY_OK on success.
"""
from fractions import Fraction
import sys
sys.path.insert(0, "output/artifacts")
from laufer import (build_star, canon_vec, fiber_min, chi_of, is_closed,
                    arm_chains, rhs_vec, certify_fiber, total_w2,
                    real_min_quad, tail_window)

def check_graph(M, name):
    import numpy as np
    det = round(float(np.linalg.det(np.array(M, float))))
    ev = sorted(np.linalg.eigvalsh(np.array(M, float)))
    assert all(e < 0 for e in ev), (name, ev)
    return det

M7 = build_star(-1, [[-2],[-3],[-7]])
M11 = build_star(-2, [[-2],[-2,-2],[-2,-2,-2,-2,-3]])
m7 = canon_vec(M7); m11 = canon_vec(M11)
assert check_graph(M7, "G7") == 1 and check_graph(M11, "G11") == -1

def K2s(M, m):
    return sum(m[i]*M[i][j]*m[j] for i in range(len(M)) for j in range(len(M))) + len(M)
k7, k11 = K2s(M7, m7), K2s(M11, m11)
assert k7 == 0 and k11 == 8, (k7, k11)

def ledger(M, mc, N):
    rhs = rhs_vec(M); arms = arm_chains(M)
    A, B, C = real_min_quad(M, rhs)
    lo, hi = tail_window(A, B, C, N)
    ws, xms = {}, {}
    for i in range(lo, hi+1):
        w, xm = fiber_min(M, mc, i)
        assert is_closed(M, xm), f"fiber {i} not two-sided closed"
        certify_fiber(M, mc, rhs, arms, i, xm)  # exact per-arm DP optimality
        assert total_w2(M, rhs, arms, i, xm) == 2*w
        ws[i] = w; xms[i] = xm
    return ws, xms, (lo, hi), (A, B, C)

def runs(ws, n):
    S = sorted(i for i, w in ws.items() if w <= n)
    R = []
    for i in S:
        if R and i == R[-1][-1]+1: R[-1].append(i)
        else: R.append([i])
    return R

w7, x7, win7, q7 = ledger(M7, m7, 4)
w11, x11, win11, q11 = ledger(M11, m11, 4)
print("windows N<=4:", {"G7": win7, "G11": win11})
print("realmin G7: A=%s B=%s C=%s" % q7)
print("realmin G11: A=%s B=%s C=%s" % q11)
assert min(w7.values()) == 0 and min(w11.values()) == 0
d7 = Fraction(k7, 4) - 2*min(w7.values())
d11 = Fraction(k11, 4) - 2*min(w11.values())
assert (d7, d11) == (0, 2), (d7, d11)

R70, R110 = runs(w7, 0), runs(w11, 0)
R71, R111 = runs(w7, 1), runs(w11, 1)
R72, R112 = runs(w7, 2), runs(w11, 2)
print("S0 G7:", R70, " S0 G11:", R110)
print("S1 G7:", R71, " S1 G11:", R111)
print("S2 G7:", R72, " S2 G11:", R112)
# Corrected verdict: S0 both split (5+5 vs 1+1); S1: 1 vs 1 (merge heights differ);
# distinguishing data: S0 left-run widths 5 vs 1, gap structure, and d=0 vs 2.
assert [len(r) for r in R70] == [5, 5], R70
assert [len(r) for r in R110] == [1, 1], R110
assert len(R71) == 1 and len(R111) == 1
assert len(R72) == 1 and len(R112) == 1
assert R70 != R110, "S0 run shapes coincide?!"
assert d7 != d11
print(f"d(G7)={d7} d(G11)={d11} K2s=({k7},{k11})")
print("minimizers G7 S0-gap: i=1 w=%s x=%s" % (w7[1], x7[1]))
print("minimizers G11 S0-runs: i=0 w=%s x=%s; i=6 w=%s x=%s" % (w11[0], x11[0], w11[6], x11[6]))
print("VERIFY_OK")
