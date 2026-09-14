import sys; sys.path.insert(0, 'output/artifacts')
from apolar import *
from fractions import Fraction

def show(u, v, label, maxdeg=None):
    print("=" * 70)
    print(label, "u=", u, "v=", v, "deg=", sum(u))
    F = {tuple(u): Fraction(1), tuple(v): Fraction(-1)}
    d = sum(u)
    ns, src = ann_basis(F, 4, 1, d)
    print("  dim Ann_1 =", len(ns))
    gens = ann_gens_binomial(u, v, 4, maxdeg=(maxdeg or d))
    for deg in sorted(gens):
        print(f"  deg {deg}: dim Ann = {len(gens[deg])}")
    kept = min_gens_of_ideal(gens, 4)
    print("  minimal gens:")
    for deg, p in kept:
        print(f"    deg {deg}: {poly_str(p)}")
    print("  mu =", len(kept))

# (2,2) with disjoint-ish supports: F = X^a(X^b - X^c) style
show((3,0,1,0),(1,0,0,3), "(2,2)?")
show((2,0,2,0),(0,2,0,2), "(2,2) disjoint?")
show((3,1,0,0),(1,0,1,2), "(2,1) sharing?")
show((4,1,0,0),(0,0,4,1), "(1,1) deg5?")
show((2,2,2,0),(0,0,0,6), "(3,1) deg6?")
