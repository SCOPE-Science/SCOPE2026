from apolar import *
from fractions import Fraction
import sys
sys.path.insert(0, 'output/artifacts')

def show(u, v, label):
    print("=" * 70)
    print(label, "u=", u, "v=", v, "deg=", sum(u))
    F = {tuple(u): Fraction(1), tuple(v): Fraction(-1)}
    d = sum(u)
    # linear annihilator
    ns, src = ann_basis(F, 4, 1, d)
    print("  dim Ann_1 =", len(ns))
    gens = ann_gens_binomial(u, v, 4, maxdeg=d)
    for deg in sorted(gens):
        print(f"  deg {deg}: dim Ann = {len(gens[deg])}")
    kept = min_gens_of_ideal(gens, 4)
    print("  minimal gens (deg, poly):")
    for deg, p in kept:
        print(f"    deg {deg}: {poly_str(p)}")
    print("  mu =", len(kept))

# Type representatives (all homogeneous, Ann_1 = 0 expected)
# (1,1): F = X1^a X2^b (X1^c - X4^d) shape; simplest: disjoint-ish
show((3,1,0,0),(0,0,3,1), "(1,1) CI?")
show((2,2,0,0),(0,0,2,2), "(1,1) equal-exp?")
show((2,1,1,0),(0,0,2,2), "(2,1)?")
show((1,1,1,1),(0,0,0,4), "(3,1)?")
show((2,1,0,1),(0,1,2,0), "(2,2)?")
