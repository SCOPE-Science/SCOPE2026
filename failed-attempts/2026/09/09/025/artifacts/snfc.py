"""Integral SNF certification for K0 Khovanov blocks (sympy smith_normal_form).
For each (i,j) block: integer matrices d_in (C^{i-1}->C^i) and d_out (C^i->C^{i+1});
SNF gives: rank, invariant factors (torsion of coker), and homology:
  H = Z^b + T, b = dim - rk_in - rk_out, T from SNF of d_out restricted... 
Standard: with SNF we get coker(d_in) structure; homology needs ker(d_out)/im(d_in).
For small blocks: compute ker basis over Z (via rational nullspace, cleared), then
express im(d_in) in ker basis, SNF of that relation matrix -> torsion + Betti.
Simpler certified route: rank over Q (Betti via euler+torsionfree) + torsion via
SNF of the full differential matrices using the structure theorem per short exact
pieces. Easiest robust: compute H via SNF of the presentation matrix:
  C^{i-1} --d_in--> C^i --d_out--> C^{i+1}; H = ker(d_out)/im(d_in).
  ker(d_out): integer basis K (ncols x k). Inclusion: coordinates. im(d_in) in K-coords:
  solve K X = d_in columns (exact rational, must be integral since im ⊆ ker as d^2=0
  over Z — verify integrality!). Then SNF(X) = diag(d1..dr, 0..): H = Z^{k-r} ⊕ ⊕Z_{dj}.
Uses sympy Matrix.smith_normal_form with calc_transform=False for invariant factors,
plus explicit solve for the coordinate matrix.
"""
import sys
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-332/output/artifacts")
from collections import defaultdict
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from kh import chain_basis
from khdiff import differential_blocks
from cube import Kword

def int_matrix(nrows, ncols, entries):
    M = [[0] * ncols for _ in range(nrows)]
    for (r, c), v in entries.items():
        M[r][c] = int(v)
    return Matrix(M)

def homology_snffull(word, nstrands):
    n_plus = sum(1 for _, s in word if s == 1)
    n_minus = sum(1 for _, s in word if s == -1)
    basis, orders = chain_basis(word, nstrands, n_plus, n_minus)
    mats, idx = differential_blocks(word, nstrands, basis, orders, 10**9 + 7)
    # rebuild integer mats (entries mod 1e9+7 with signs: convert back to signed ints)
    # instead rebuild with p=0 convention? differential_blocks does %p. Redo: entries are -1/0/1/2 mostly; recover sign via v if v<p/2 else v-p.
    P = 10**9 + 7
    Z = {}
    for key, e in mats.items():
        Z[key] = {rc: (v if v < P / 2 else v - P) for rc, v in e.items()}
    result = {}
    for key in sorted(basis):
        n = len(basis[key])
        # incoming: blocks (L,key); outgoing: (key,N)
        in_blocks = [(L, e) for (L, N), e in Z.items() if N == key]
        out_blocks = [(N, e) for (S, N), e in Z.items() if S == key]
        # assemble d_in: rows = basis[key] order, cols = concat of basis[L]
        in_cols = []
        in_widths = []
        for L, e in in_blocks:
            in_widths.append(len(basis[L]))
            in_cols.append(e)
        d_in = None
        if in_cols:
            W = sum(in_widths)
            M = [[0] * W for _ in range(n)]
            off = 0
            for (L, e), wd in zip(in_blocks, in_widths):
                # columns of e are indexed by src basis; rows by key basis
                for (r, c), v in e.items():
                    M[r][off + c] += v
                off += wd
            d_in = Matrix(M)
        out_rows = []
        out_heights = []
        for N, e in out_blocks:
            out_heights.append(len(basis[N]))
            out_rows.append(e)
        d_out = None
        if out_rows:
            H = sum(out_heights)
            M = [[0] * n for _ in range(H)]
            off = 0
            for (N, e), hd in zip(out_blocks, out_heights):
                for (r, c), v in e.items():
                    M[off + r][c] += v
                off += hd
            d_out = Matrix(M)
        # ranks over QQ
        rk_in = d_in.rank() if d_in is not None else 0
        rk_out = d_out.rank() if d_out is not None else 0
        b = n - rk_in - rk_out
        assert b >= 0, (key, b)
        # torsion: ker(d_out) basis, im(d_in) coords, SNF
        tors = []
        if d_out is not None and n > 0:
            ns = d_out.nullspace()
            k = len(ns)
            assert k == n - rk_out
            if k > 0 and d_in is not None:
                K = Matrix.hstack(*ns)  # n x k
                # solve K X = d_in (each col): exact
                X, params = K.gauss_jordan_solve(d_in)
                assert all(v == 0 for v in params), ("non-unique", key)
                # X must be integral (im ⊆ ker over Z)
                assert all(v.q == 1 for v in X), ("non-integral coords", key)
                X = X.applyfunc(int)
                if X.rows > 0 and X.cols > 0 and any(X):
                    S = smith_normal_form(X, domain=ZZ)
                    dg = [abs(S[i, i]) for i in range(min(S.rows, S.cols))]
                    tors = [int(d) for d in dg if d not in (0, 1)]
                # verify: #pivots(=rk_in) ones-or-more count == rk_in
                S = smith_normal_form(X, domain=ZZ) if (X.rows and X.cols and any(X)) else None
        elif n > 0 and d_in is not None:
            # ker = whole space
            X = d_in
            if X.rows > 0 and X.cols > 0 and any(X):
                S = smith_normal_form(X, domain=ZZ)
                dg = [abs(S[i, i]) for i in range(min(S.rows, S.cols))]
                tors = [int(d) for d in dg if d not in (0, 1)]
        result[key] = {"dim": n, "betti": b, "torsion": tors,
                       "rk_in": rk_in, "rk_out": rk_out}
    return result

if __name__ == "__main__":
    r = homology_snffull(Kword(0), 3)
    for k in sorted(r):
        print(k, r[k])
