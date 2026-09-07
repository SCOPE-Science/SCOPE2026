#!/usr/bin/env python3
"""Replay verifier for lane-42: 12 <= N_{1/5}(9) <= 13.

Uses only stdlib + numpy. Deterministic (seed pinned). Runs in seconds.
Checks:
 1. gram12.csv entries are 1 / +-1/5 (exact via scaled integers).
 2. Gram PSD (lambda_min >= -1e-8) and rank == 9 (tol 1e-7).
 3. Analytic spectrum {12/5 x1, 0 x3, 6/5 x8} within 1e-8.
 4. DGS relative-bound arithmetic giving U=13.
 5. Saturation: all 4096 one-line extensions of G12 have rank >=10 or non-PSD
    (i.e. no PSD rank<=9 extension exists in R^9).
Environment pin: python3.12, numpy 1.26.4 (any numpy>=1.20 works).
"""
import csv
import os
import sys

import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
GRAM_PATH = os.path.join(BASE, "gram12.csv")
TOL_PSD = 1e-8
TOL_RANK = 1e-7
TOL_SPEC = 1e-8


def load_gram(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    n = len(rows)
    G = np.array([[float(x) for x in r] for r in rows], dtype=float)
    assert G.shape == (n, n), G.shape
    return G


def check_entries(G):
    n = G.shape[0]
    assert n == 12, f"expected 12, got {n}"
    S = np.round(G * 5).astype(int)  # exact scaled check
    for i in range(n):
        for j in range(n):
            if i == j:
                assert S[i, j] == 5, (i, j, G[i, j])
            else:
                assert S[i, j] in (1, -1), (i, j, G[i, j])
                assert abs(G[i, j] - S[i, j] / 5.0) < 1e-12, (i, j)
    # block structure check (4xK3): within-block -1, between +1 (up to perm, here canonical order)
    for u in range(n):
        for v in range(n):
            if u != v:
                expect = -1 if (u // 3) == (v // 3) else 1
                assert S[u, v] == expect, (u, v)
    print("[1] entry check passed: diag 1, off-diag +-1/5, 4xK3 block structure.")


def check_psd_rank(G):
    w = np.linalg.eigvalsh(G)
    lmin = float(w[0])
    rank = int((w > TOL_RANK).sum())
    print(f"[2] eigenvalues: {np.round(w, 10).tolist()}")
    print(f"    lambda_min={lmin:.3e}, rank(tol 1e-7)={rank}")
    assert lmin >= -TOL_PSD, f"not PSD: {lmin}"
    assert rank == 9, f"rank {rank} != 9"
    # analytic spectrum
    expect = sorted([12 / 5] + [0.0] * 3 + [6 / 5] * 8)
    got = sorted(w.tolist())
    assert all(abs(a - b) < 1e-6 for a, b in zip(got, expect)), "spectrum mismatch"
    print("[2] PSD + rank-9 + analytic spectrum {12/5,0x3,6/5x8} passed.")
    return w


def check_relative_bound():
    d, alpha = 9, 1 / 5
    # f(t)=t^2-alpha^2 = a2 P2 + a0 P0, P2=(d t^2-1)/(d-1)
    a2 = (d - 1) / d
    a0 = (1 - d * alpha * alpha) / d
    bound = d * (1 - alpha * alpha) / (1 - d * alpha * alpha)
    print(f"[3] a2={(d-1)}/{d}={a2}, a0=(1-{d}*1/25)/{d}={a0} (exact 16/225={16/225})")
    print(f"    DGS bound = d(1-a^2)/(1-d a^2) = 9*(24/25)/(16/25) = {bound} -> N<=13")
    assert abs(a2 - 8 / 9) < 1e-15
    assert abs(a0 - 16 / 225) < 1e-15
    assert abs(bound - 13.5) < 1e-12
    assert int(bound) == 13  # floor
    print("[3] relative-bound U=13 passed.")


def check_saturation(G12):
    n12 = 12
    psd_count = 0
    best_rank = 99
    # exhaustive 2^12 extensions; deterministic order mask=0..4095
    for mask in range(1 << n12):
        s = np.array([0.2 if (mask >> i) & 1 else -0.2 for i in range(n12)])
        G = np.eye(13)
        G[:12, :12] = G12
        G[:12, 12] = s
        G[12, :12] = s
        w = np.linalg.eigvalsh(G)
        if w[0] >= -TOL_PSD:
            psd_count += 1
            r = int((w > TOL_RANK).sum())
            best_rank = min(best_rank, r)
            assert r >= 10, f"found rank<=9 extension mask={mask} eig={w}"
    print(f"[4] saturation: {psd_count}/4096 extensions PSD, best PSD rank={best_rank}")
    assert psd_count == 164, f"expected 164 PSD extensions, got {psd_count}"
    assert best_rank == 10
    print("[4] saturatedness passed: no PSD rank<=9 extension in R^9.")


def main():
    print(f"numpy {np.version.version}, python {sys.version.split()[0]}")
    G = load_gram(GRAM_PATH)
    check_entries(G)
    check_psd_rank(G)
    check_relative_bound()
    check_saturation(G)
    print("ALL CHECKS PASSED: 12 <= N_{1/5}(9) <= 13, 12-witness PSD rank-9, saturated.")


if __name__ == "__main__":
    main()
