# Verify the Ann(F) minimal generators are CORRECT (not just greedy): check Hilbert function of S/I equals Macaulay-dual prediction.
import sys; sys.path.insert(0, 'output/artifacts')
from apolar import *
from fractions import Fraction
import sympy as sp
from apolar import mons

def hilb_quotient(kept, nvars, dmax):
    out = []
    for d in range(dmax + 1):
        ms = mons(nvars, d)
        rows = []
        for dg, g in kept:
            if dg > d: continue
            for m in mons(nvars, d - dg):
                row = [Fraction(0)] * len(ms)
                for e, c in g.items():
                    ne = tuple(a + b for a, b in zip(e, m))
                    row[ms.index(ne)] += c
                rows.append(row)
        M = sp.Matrix(rows) if rows else sp.zeros(0, len(ms))
        out.append(len(ms) - M.rank())
    return out

def hilb_dual(u, v, dmax):
    from apolar import ann_basis
    F = {tuple(u): Fraction(1), tuple(v): Fraction(-1)}
    d = sum(u)
    out = []
    for j in range(dmax + 1):
        ns, src = ann_basis(F, 4, j, d) if j <= d else ([], mons(4, j))
        out.append(len(mons(4, j)) - len(ns))
    return out

CASES = {
 "T111a": ((3,1,0,0),(0,0,3,1)),
 "T111b": ((2,2,0,0),(0,0,2,2)),
 "T21a": ((2,1,1,0),(0,0,2,2)),
 "T31a": ((1,1,1,1),(0,0,0,4)),
 "T22disj": ((2,0,2,0),(0,2,0,2)),
 "T21b": ((3,1,0,0),(1,0,1,2)),
 "T15": ((4,1,0,0),(0,0,4,1)),
}
for name, (u, v) in CASES.items():
    gens = ann_gens_binomial(u, v, 4, maxdeg=sum(u))
    kept = min_gens_of_ideal(gens, 4)
    h1 = hilb_quotient(kept, 4, sum(u))
    h2 = hilb_dual(u, v, sum(u))
    print(name, "quot:", h1, "dual:", h2, "MATCH" if h1 == h2 else "MISMATCH")
