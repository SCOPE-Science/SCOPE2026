#!/usr/bin/env python3
"""Exact rational certification of ONE tolerance-1 triple partition.

Config: 13-point moment curve t=-6..6 (integer coords). Partition: ledger
index g with labels L. For the full set and each of the 13 single-point
deletions, finds a float-feasible 9-basis, then re-solves that basis EXACTLY
over Fractions and asserts E*lam=b, lam>=0. Writes witnesses_exact.json.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fractions import Fraction
from audit import build_E, bases, triple_hit, get_partitions, cfg_moment

ART = os.path.dirname(os.path.abspath(__file__))

def exact_solve(A, b):
    """A: n x n int matrix (list of lists), b: len-n. Returns [Fraction] or None."""
    n = len(b)
    M = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(b[i])]
         for i in range(n)]
    piv = [-1] * n
    row = 0
    for col in range(n):
        sel = -1
        for i in range(row, n):
            if M[i][col] != 0:
                sel = i
                break
        if sel == -1:
            return None
        M[row], M[sel] = M[sel], M[row]
        piv[col] = row
        inv = Fraction(1, M[row][col])
        M[row] = [v * inv for v in M[row]]
        for i in range(n):
            if i != row and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * c for a, c in zip(M[i], M[row])]
        row += 1
    return [M[piv[j]][n] for j in range(n)]


def int_E(X, lab, active):
    idx = np.where(active)[0]
    labs = lab[idx]
    m0 = [i for i, l in enumerate(labs) if l == 0]
    m1 = [i for i, l in enumerate(labs) if l == 1]
    m2 = [i for i, l in enumerate(labs) if l == 2]
    order = np.array(m0 + m1 + m2)
    pts = X[idx][order]  # ints
    m = len(idx)
    n0, n1 = len(m0), len(m1)
    E = [[0] * m for _ in range(9)]
    for j in range(n0):
        E[0][j] = 1
    for j in range(n0, n0 + n1):
        E[1][j] = 1
    for j in range(n0 + n1, m):
        E[2][j] = 1
    for k in range(3):
        for j in range(n0):
            E[3 + k][j] = int(pts[j, k])
        for j in range(n0, n0 + n1):
            E[3 + k][j] = -int(pts[j, k])
        for j in range(n0):
            E[6 + k][j] = int(pts[j, k])
        for j in range(n0 + n1, m):
            E[6 + k][j] = -int(pts[j, k])
    return E, (len(m0), len(m1), len(m2))


def main():
    X = cfg_moment(-6)
    P = get_partitions(os.path.join(ART, "partitions13.npy"))
    g = int(sys.argv[1]) if len(sys.argv) > 1 else 57738
    lab = np.asarray(P[g])
    assert set(np.unique(lab)) == {0, 1, 2}
    assert all(int((lab == v).sum()) >= 2 for v in range(3))
    Cf = X.astype(float)
    out = {"config": "moment-6", "partition_index": g,
           "labels": lab.tolist(), "coords": X.tolist(), "systems": []}
    cases = [("full", np.ones(13, dtype=bool))]
    for d in range(13):
        a = np.ones(13, dtype=bool)
        a[d] = False
        cases.append((f"del{d}", a))
    for name, act in cases:
        Ef, sz = build_E(Cf, lab, act)
        E9, sz9 = int_E(X, lab, act)
        assert sz9 == tuple(int_E(X, lab, act)[1])
        Bm = bases(sz)
        feas = None
        for S in Bm:
            S = [int(c) for c in S]
            try:
                w = np.linalg.solve(Ef[:, S], np.array(
                    [1., 1., 1., 0., 0., 0., 0., 0., 0.]))
            except np.linalg.LinAlgError:
                continue
            if w.min() >= 1e-9:
                A = [[E9[i][c] for c in S] for i in range(9)]
                lam = exact_solve(A, [1, 1, 1, 0, 0, 0, 0, 0, 0])
                if lam is not None and all(v >= 0 for v in lam):
                    feas = (S, lam)
                    break
        if feas is None:
            print(f"FAIL: no exactly-certified basis for {name}")
            sys.exit(1)
        S, lam = feas
        # exact residual check
        m = E9 and len(E9[0])
        full = [Fraction(0)] * m
        for c, v in zip(S, lam):
            full[c] = v
        for i in range(9):
            assert sum(Fraction(E9[i][j]) * full[j]
                       for j in range(m)) == (1 if i < 3 else 0), name
        out["systems"].append({
            "case": name, "basis": S,
            "lambda": [str(v) for v in lam],
            "min_lambda": str(min(lam))})
        print(f"{name}: basis ok, min_lambda={min(lam)}", flush=True)
    json.dump(out, open(os.path.join(ART, "witnesses_exact.json"), "w"))
    print("CERTIFY_OK")


if __name__ == "__main__":
    main()
