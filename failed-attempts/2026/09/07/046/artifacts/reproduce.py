#!/usr/bin/env python3
"""Lane-87 single-script reproducer (stdlib + numpy only).

Claim under test: for every real x in [1e7, 1e8], [x, x + x/30000] contains a prime.

Legs:
  A. Explicit Dusart-type theta-difference margin m(x) on a grid (documents FAILURE:
     margins are negative by ~20x, so no analytic leg in this range).
  B. Segmented-sieve gap closure of [1e7,1e8] (the actual proof).
  C. Exact-rational Selberg-weight upper-bound spot checks (one-sided consistency).

Outputs (written next to this script): margin_table.csv, gap_table.csv,
selberg_table.csv, summary.json. Exits 0 iff all asserts hold.
"""
import csv
import json
import math
import os
import time
from fractions import Fraction

import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
LO = 9_900_000          # sieve low (below 1e7 to capture the preceding prime)
HI = 100_100_000        # sieve high (> 1e8 + 1e8/30000, with margin)
XL = 10_000_000
XR = 100_000_000
DELTA = 30000
SEG = 1 << 20
T0 = time.time()
TIM = {}


def phase(name):
    TIM[name] = round(time.time() - T0, 2)


# ---------------- Leg A: analytic margin (expected to FAIL) ----------------
def theta_margin_table():
    # E(t) = 0.2 t / log^2 t  (Dusart-type psi/theta error shape, valid t >= 3.6e6)
    # E2(t) = 0.35 t / log^3 t (decade-sharper modern shape, for robustness of failure)
    # U(t) = 1.000081 * sum_{k=2}^{floor(log2 t)} t^{1/k}  bounds psi(t)-theta(t),
    #        using theta(s) < 1.000081 s (Rosser--Schoenfeld).
    # m(x) = h(x) - E(x+h) - E(x) - U(x+h); analytic leg needs m(x) > 0.
    grid = sorted(set(
        [round(XL * (10.0) ** (i / 160)) for i in range(161)]
        + [30_000_000, 40_000_000, 50_000_000]
    ))
    rows = []
    for x in grid:
        h = x / DELTA
        t2 = x + h
        E = lambda t: 0.2 * t / (math.log(t) ** 2)
        E2 = lambda t: 0.35 * t / (math.log(t) ** 3)
        U = 1.000081 * sum(t2 ** (1.0 / k) for k in range(2, int(math.log2(t2)) + 1))
        m = h - E(t2) - E(x) - U
        m2 = h - E2(t2) - E2(x) - U
        rows.append((x, h, E(x), E(t2), U, m, m2))
    with open(os.path.join(OUT, "margin_table.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["x", "h_x", "E_x", "E_xh", "U_psith_xh", "margin_m", "margin_m_sharp"])
        for r in rows:
            w.writerow([r[0], f"{r[1]:.6f}", f"{r[2]:.3f}", f"{r[3]:.3f}",
                        f"{r[4]:.3f}", f"{r[5]:.3f}", f"{r[6]:.3f}"])
    worst = max(r[5] for r in rows)
    worst2 = max(r[6] for r in rows)
    assert worst < 0, "unexpected: Dusart-type margin went positive"
    assert worst2 < 0, "unexpected: sharper margin went positive"
    return {"n_grid": len(rows), "worst_margin": round(worst, 1),
            "worst_margin_sharp": round(worst2, 1)}


# ---------------- Leg B: segmented sieve + gap closure ----------------
def base_primes(limit):
    bs = bytearray(b"\x01") * (limit + 1)
    bs[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if bs[p]:
            bs[p * p:limit + 1:p] = b"\x00" * ((limit - p * p) // p + 1)
    return [i for i in range(2, limit + 1) if bs[i]]


def segmented_sieve():
    blim = math.isqrt(HI) + 1  # >= ceil(sqrt(HI)); audit said 1e4 but sqrt(HI) > 1e4
    while True:  # ensure the largest base *prime* squares past HI (blim itself may be composite)
        bp = base_primes(blim)
        if max(bp) ** 2 >= HI:
            break
        blim += 100
    assert max(bp) ** 2 >= HI
    parts = []
    witnesses = []  # per-segment (block) witness rows
    seg_lo = LO
    while seg_lo < HI:
        seg_hi = min(seg_lo + SEG, HI)
        n = seg_hi - seg_lo
        arr = np.ones(n, dtype=bool)
        for p in bp:
            start = max(p * p, ((seg_lo + p - 1) // p) * p)
            if start < seg_hi:
                arr[start - seg_lo::p] = False
        idx = np.flatnonzero(arr).astype(np.int64) + seg_lo
        idx = idx[idx >= 2]
        parts.append(idx.astype(np.uint32))
        witnesses.append((seg_lo, seg_hi, int(idx[0]), int(len(idx))))
        seg_lo = seg_hi
    P = np.concatenate(parts)
    assert np.all(np.diff(P.astype(np.int64)) > 0)
    # correctness anchors: known pi values. Our array covers [LO, HI), so add pi(LO-1).
    assert int(P[0]) < XL  # first sieved prime precedes the claim range
    n_le_1e7 = int(np.searchsorted(P, 10_000_000, side="right"))
    # pi(LO-1): sieve [2, LO) quickly with numpy
    q = np.ones(LO - 2 + 1, dtype=bool)
    for p in base_primes(math.isqrt(LO) + 1):
        st = max(p * p, 2)
        q[st - 2::p] = False
    pi_LOm1 = int(q.sum())
    assert n_le_1e7 + pi_LOm1 == 664579, (n_le_1e7 + pi_LOm1,)  # pi(1e7)
    n_le_1e8 = int(np.searchsorted(P, 100_000_000, side="right"))
    assert n_le_1e8 + pi_LOm1 == 5761455, (n_le_1e8 + pi_LOm1,)  # pi(1e8)
    return P, witnesses, {"base_limit": blim, "n_base": len(bp)}


def gap_closure(P):
    p = P.astype(np.int64)
    q = p[1:]
    p = p[:-1]
    touch = (q >= XL) & (p <= XR)
    pt, qt = p[touch], q[touch]
    a = np.maximum(pt, XL)
    lhs = DELTA * (qt - a)  # integer arithmetic; need lhs <= a
    ok = np.all(lhs <= a)
    worst = int(np.min(a - lhs))
    k = int(np.argmin(a - lhs))
    gaps = qt - pt
    mg_all = int(gaps.max())
    # global maximal gap over whole sieved array
    mg_global = int(np.max(q - p))
    assert ok, "gap closure FAILED"
    # endpoint safety: sieve extends past XR + XR/DELTA and below XL
    assert int(P[0]) < XL and int(P[-1]) > XR + XR / DELTA + 1000
    return {"n_gaps_touching": int(touch.sum()), "max_gap_touching": mg_all,
            "max_gap_global": mg_global,
            "worst_slack": worst, "worst_at_p": int(pt[k]), "worst_gap": int(qt[k] - pt[k])}


# ---------------- Leg C: exact Selberg upper-bound spot checks ----------------
def selberg_checks(P):
    # Selberg upper sieve for the sifted set {n in [X,X+y): (n,30)=1}, i.e. sieve
    # primes P_s = {2,3,5}. Support: all squarefree d < D=36 with prime factors in
    # P_s -> {1,2,3,5,6,10,15,30}. Optimal weights solve M v = e_1 exactly over
    # QQ (M[d,e] = 1/lcm(d,e)); lambda = v/v_1, main term Q = 1/G with
    # G = v_1, remainder R = (sum |lambda_d|)^2 (each |r_lcm| <= 1).
    sup = [1, 2, 3, 5, 6, 10, 15, 30]
    D = 36
    n = len(sup)
    M = [[Fraction(1, sup[i] * sup[j] // math.gcd(sup[i], sup[j]))
          for j in range(n)] for i in range(n)]
    A = [row[:] + [Fraction(1 if i == 0 else 0, 1)] for i, row in enumerate(M)]
    for c in range(n):
        piv_row = max(range(c, n), key=lambda r: abs(A[r][c]))
        A[c], A[piv_row] = A[piv_row], A[c]
        piv = A[c][c]
        assert piv != 0
        A[c] = [a / piv for a in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    v = [A[i][n] for i in range(n)]
    G = v[0]
    lam = [x / G for x in v]
    assert lam[0] == 1
    Q = sum(lam[i] * lam[j] * M[i][j] for i in range(n) for j in range(n))
    assert Q == 1 / G, (Q, 1 / G)  # exact diagonalized-identity self-check
    R = sum(abs(lam[i] * lam[j]) for i in range(n) for j in range(n))
    Xs = [10_000_000, 12_500_000, 15_000_000, 20_000_000, 25_000_000, 32_000_000,
          40_000_000, 50_000_000, 63_000_000, 75_000_000, 88_000_000, 100_000_000]
    rows = []
    for X in Xs:
        y = X // DELTA
        S = sum(1 for nn in range(X, X + y) if nn % 2 and nn % 3 and nn % 5)
        # exact sieve identity: S == sum lam lam count(lcm | block)
        exact = sum(lam[i] * lam[j] * Fraction(
            (X + y - 1) // (sup[i] * sup[j] // math.gcd(sup[i], sup[j]))
            - (X - 1) // (sup[i] * sup[j] // math.gcd(sup[i], sup[j])), 1)
            for i in range(n) for j in range(n))
        assert exact == S, (X, S, exact)
        Pc = int(np.searchsorted(P, X + y, side="left") - np.searchsorted(P, X, side="left"))
        assert Pc <= S, (X, Pc, S)
        UB = Fraction(y, 1) / G + R
        assert Fraction(S, 1) <= UB, (X, S, float(UB))
        rows.append((X, y, Pc, S, float(UB)))
    with open(os.path.join(OUT, "selberg_table.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["X", "y", "prime_count", "survivors_coprime_30", "selberg_UB"])
        for r in rows:
            w.writerow([r[0], r[1], r[2], r[3], f"{r[4]:.4f}"])
    return {"sieve_primes": [2, 3, 5], "D": D, "support": sup,
            "weights": [f"{float(x):.4f}" for x in lam],
            "G": f"{float(G):.6f}",
            "remainder_R": f"{float(R):.4f}", "n_blocks": len(rows),
            "max_ratio_count_over_UB": round(max(r[2] / r[4] for r in rows), 4)}


def main():
    m = theta_margin_table()
    phase("margin_s")
    P, wit, s = segmented_sieve()
    phase("sieve_s")
    gc = gap_closure(P)
    phase("gap_s")
    with open(os.path.join(OUT, "gap_table.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["block_start", "block_end_exclusive", "witness_prime", "prime_count"])
        for r in wit:
            w.writerow(r)
    sc = selberg_checks(P)
    phase("selberg_s")
    phase("total_s")
    summary = {
        "params": {"LO": LO, "HI": HI, "XL": XL, "XR": XR, "DELTA": DELTA, "SEG": SEG},
        "legA_analytic_margin": m,
        "legA_conclusion": "infeasible in [1e7,1e8]: best margin < 0 everywhere",
        "legB_sieve": s,
        "legB_gap_closure": gc,
        "legB_conclusion": "every [x,x+x/30000], 1e7<=x<=1e8, contains a prime",
        "legC_selberg": sc,
        "legC_conclusion": "one-sided upper-bound consistency only; not a lower-bound proof",
        "timings_s": TIM,
    }
    assert TIM["total_s"] < 7200
    with open(os.path.join(OUT, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
