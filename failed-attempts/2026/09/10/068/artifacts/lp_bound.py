"""Delsarte-LP upper bound for N_{1/5}(14), stdlib exact rational vertex enumeration.

Antipodal-code LP: M=2N points, f(t)=1+sum_{k>=1} f_k P_k(t), P_k normalized
Gegenbauer (d=14). Variant A: f(s)<=0 for s in {1/5,-1/5,-1} => M<=f(1).
Variant B: f(s)<=0 for s in {+-1/5} only => N <= 1+sum_{even k} f_k.
Reports LP optimum per degree m=2..12 and implied N bound.
"""
from fractions import Fraction as Q

D = 14
LAM = Q(D - 2, 2)  # 6

def gegenbauer_vals(t, m):
    # returns [C_0(t),...,C_m(t)] exact
    C = [Q(0)] * (m + 1)
    C[0] = Q(1)
    if m >= 1:
        C[1] = 2 * LAM * t
    for k in range(1, m):
        # (k+1) C_{k+1} = 2(k+lam) t C_k - (k+2lam-1) C_{k-1}
        C[k + 1] = (Q(2) * (k + LAM) * t * C[k] - (k + 2 * LAM - 1) * C[k - 1]) / (k + 1)
    return C

def norm_P(s, m):
    Ct = gegenbauer_vals(s, m)
    C1 = gegenbauer_vals(Q(1), m)
    return [Ct[k] / C1[k] for k in range(m + 1)]

def solve_lin(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, n) if M[i][c] != 0), None)
        if p is None:
            return None
        M[r], M[p] = M[p], M[r]
        piv.append(c)
        div = M[r][c]
        M[r] = [x / div for x in M[r]]
        for i in range(n):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * bb for a, bb in zip(M[i], M[r])]
        r += 1
        if r == n:
            break
    if r < n:
        return None
    x = [Q(0)] * n
    for i, c in enumerate(piv):
        x[c] = M[i][n]
    # verify
    for i in range(n):
        if sum(A[i][j] * x[j] for j in range(n)) != b[i]:
            return None
    return x

from itertools import combinations

def lp_min(m, constraints_pts, obj_mode):
    # variables f_1..f_m. constraints: sum_k P_k(s) f_k <= -1 for s in pts; f_k>=0.
    # objective variant A: sum f_k (then N<=(1+obj)/2). variant B handled post-hoc.
    P = {s: norm_P(s, m) for s in constraints_pts}
    Arows, bvec = [], []
    for s in constraints_pts:
        Arows.append([P[s][k] for k in range(1, m + 1)])
        bvec.append(Q(-1))
    for k in range(m):
        row = [Q(0)] * m
        row[k] = Q(-1)
        Arows.append(row)
        bvec.append(Q(0))
    nc = len(Arows)
    best = None
    for combo in combinations(range(nc), m):
        A = [Arows[i] for i in combo]
        b = [bvec[i] for i in combo]
        x = solve_lin(A, b)
        if x is None:
            continue
        if any(v < 0 for v in x):
            continue
        ok = True
        for i in range(nc):
            if sum(Arows[i][j] * x[j] for j in range(m)) > bvec[i]:
                ok = False
                break
        if not ok:
            continue
        o = sum(x)
        if best is None or o < best[0]:
            best = (o, x)
    return best

if __name__ == "__main__":
    ptsA = [Q(1, 5), Q(-1, 5), Q(-1)]
    ptsB = [Q(1, 5), Q(-1, 5)]
    print("m | variantA: sumf -> N<=(1+sumf)/2 | variantB: opt N<=1+sum_even")
    for m in range(2, 13):
        rA = lp_min(m, ptsA, 'A')
        rB = lp_min(m, ptsB, 'B')
        sA = f"{float(rA[0]):.6f} -> N<={(1 + rA[0]) / 2} = {float((1 + rA[0]) / 2):.4f}" if rA else "INFEASIBLE"
        if rB:
            seven = sum(rB[1][k - 1] for k in range(1, m + 1) if k % 2 == 0)
            sB = f"N<={1 + seven} = {float(1 + seven):.4f} (sumf={float(rB[0]):.4f})"
        else:
            sB = "INFEASIBLE"
        print(f"{m} | A: {sA} | B: {sB}")
