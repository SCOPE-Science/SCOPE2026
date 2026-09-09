"""Step I: correct E2 induced ranks + Lee homology dimension for 10_124.
induced_rank(h,q): let K = matrix whose rows span ker(d_{h,q}) (nk x cs),
  Pmat = Phi as rows? Compute S = K*Phi (nk x rt): rows = Phi(ker). Then
  induced rank = rank(stack(S; D)) - rank(D), D = rows of d_{h+1,q+4}... careful:
  D: C(h+1,q+4) -> C(h+2,q+4): im rows live in C(h+1) (rt-dim vectors). S rows also rt-dim. Good.
Lee homology: full d_Lee = d + Phi (filtered); compute total homology dim over Fp
  (rank-nullity over whole complex, ignoring gradings) — expect 2 for a knot.
"""
import json, sys
sys.path.insert(0, 'output/artifacts')
from kh_stepD import parse_pd, smoothing_data
from kh_stepG import build_differentials
from collections import defaultdict

P = 1000000007

def mat_rank_rowdicts(rows, P):
    piv = {}
    r = 0
    for row in rows:
        row = {c: v % P for c, v in row.items() if v % P != 0}
        for pc in sorted(piv):
            if pc in row:
                f = row[pc] * pow(piv[pc][0], P - 2, P) % P
                if f:
                    for cc, vv in piv[pc][1].items():
                        row[cc] = (row.get(cc, 0) - f * vv) % P
                    row.pop(pc, None)
        row = {c: v % P for c, v in row.items() if v % P != 0}
        if not row:
            continue
        c0 = min(row)
        inv = pow(row[c0], P - 2, P)
        piv[c0] = (1, {c: v * inv % P for c, v in row.items()})
        r += 1
    return r

def ker_basis(d, cols, P):
    # d: col->[(row,val)]; rows as dicts
    R = defaultdict(dict)
    for col, lst in d.items():
        for (rw, v) in lst:
            R[rw][col] = (R[rw].get(col, 0) + v) % P
    rows = [R[r] for r in sorted(R)]
    # row-echelon with pivot tracking
    piv = {}
    echel = []
    for row in rows:
        row = dict(row)
        for pc in sorted(piv):
            if pc in row:
                f = row[pc] * pow(piv[pc][0], P - 2, P) % P
                if f:
                    for cc, vv in piv[pc][1].items():
                        row[cc] = (row.get(cc, 0) - f * vv) % P
                    row.pop(pc, None)
        row = {c: v % P for c, v in row.items() if v % P != 0}
        if not row:
            continue
        c0 = min(row)
        inv = pow(row[c0], P - 2, P)
        row = {c: v * inv % P for c, v in row.items()}
        piv[c0] = (1, row)
        echel.append(row)
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for c0 in sorted(piv, reverse=True):
            s = 0
            for cc, vv in piv[c0][1].items():
                if cc != c0:
                    s = (s + vv * v[cc]) % P
            v[c0] = (-s) % P
        basis.append(v)
    return basis
