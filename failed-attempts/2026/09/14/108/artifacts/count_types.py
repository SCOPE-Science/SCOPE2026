"""Bounded recovery test for lane-20108.

Question: for H^4(M;Z) = Z_n (n != 0), how many Crowley diffeomorphism types
must a complete TARGET proof cover (or exclude), and what do the known
sec>=0 constructions provably realise?

Part 1 (exact, local): number of isomorphism classes of nonsingular linking
forms b on Z_n.  For cyclic Z_n, b(x,y) = u*x*y/n with u a unit mod n, and
b_u ~= b_v iff u*v^{-1} is a square in (Z_n^x) modulo the standard
identification (per prime power; exact for odd n, heuristic label for 2-powers).
Part 2 (estimate, labelled): each (b) admits >= 1 quadratic refinement q, and
each almost-diffeomorphism class carries up to |bP_8| = 28 smooth refinements
distinguished by the (generalised) Eells-Kuiper invariant mu.
Part 3 (realised side): Grove-Ziller linear S^3-bundles M_{m,n} and the
Goette-Kerin-Shankar 6-parameter cohomogeneity-one family provably realise
specific subfamilies; the exact parameter->(b,q,p,mu) image is NOT derivable
locally (it is the content of Goette JEMS 2014 adiabatic/Dedekind-sum
computation + GKS Annals 2020). Recorded here as UNKNOWN.
"""
import math
from itertools import product


def units(n):
    return [a for a in range(n) if math.gcd(a, n) == 1]


def squares(n):
    U = units(n)
    return {a * a % n for a in U}


def linking_form_classes(n):
    U = units(n)
    S = squares(n)
    reps = []
    for a in U:
        coset_a = {(a * s) % n for s in S}
        if not any(r in coset_a for r in reps):
            reps.append(a)
    return reps


print(f"{'n':>4} | {'#linking-form classes':>22} | {'reps u':>14} | {'admissible-type lower bound (classes x 28)':>44}")
print("-" * 95)
for n in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27, 32]:
    reps = linking_form_classes(n)
    print(f"{n:>4} | {len(reps):>22} | {str(reps):>14} | {len(reps) * 28:>44}")
print()
print("Realised side (sec>=0, from literature triage):")
print("  Grove-Ziller 2000 : linear S^3-bundles over S^4, all (m,n); covers 20/28 homotopy spheres.")
print("  GKS Annals 2020   : 6-parameter cohomogeneity-one family; infinitely many (q,mu) combos;")
print("                      contains all linear S^3-bundles + all exotic 7-spheres.")
print("  Exact image of construction parameters in Crowley (b,q,p,mu) coordinates: UNKNOWN locally.")
print("Conclusion: even for n=2 (lower bound 28+ types across >=1 linking class with q/mu")
print("refinements), closing 'realised == admissible' requires the full Goette-type EK/Dedekind-sum")
print("formulae plus a surjectivity proof - a research-program-scale gap, not a session-scale computation.")
