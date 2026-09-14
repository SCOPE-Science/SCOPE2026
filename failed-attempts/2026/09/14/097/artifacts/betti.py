import sys; sys.path.insert(0, 'output/artifacts')
from apolar import ann_gens_binomial, min_gens_of_ideal, mons
from fractions import Fraction

def hilbert_A(u, v, deg):
    from apolar import ann_basis
    import sympy as sp
    F = {tuple(u): Fraction(1), tuple(v): Fraction(-1)}
    d = sum(u)
    out = []
    for j in range(deg + 1):
        ns, src = ann_basis(F, 4, j, d) if j <= d else ([], mons(4, j))
        # dim A_j = dim S_j - dim Ann_j
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
    print(name, "hilb:", hilbert_A(u, v, sum(u)))
    gens = ann_gens_binomial(u, v, 4, maxdeg=sum(u))
    kept = min_gens_of_ideal(gens, 4)
    from collections import Counter
    print("   mu-types:", Counter(d for d, p in kept))
