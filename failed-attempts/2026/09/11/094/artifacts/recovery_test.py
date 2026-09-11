"""Bounded recovery test for lane-951 target.

Naive decategorified counts for C0=2Vect_{Z/2} vs C1=2Rep(Z/2) on T*:
- |Hom(pi1(T*), Z/2)| with pi1(T*)=F2 free on 2 generators (A/B cycles).
- Loop-level ranks: Omega(C0)=Vect (rank 1), Omega(C1)=Rep(Z/2) (rank 2).
- Simple counts of C0/C1 as fusion 2-categories (2 vs 2: C0 has 2 components
  x Vect; C1 has 2 simples: Vect and Vect^sign module).
- Double-braiding / twist eigenvalues on generating loop objects (both +1:
  Vect trivial; Rep(Z/2) symmetric bosonic).

Conclusion: no certified torus-level Hom-rank or twist mismatch follows from
these counts; a genuine completed-excision certificate is missing. BLOCKED.
Stdlib only.
"""
import itertools

G = [0, 1]

def hom_F2_to_Z2():
    # F2 = <a,b>; hom determined by images of a,b
    return list(itertools.product(G, G))

homs = hom_F2_to_Z2()
n_loc = len(homs)
print("Hom(F2,Z/2) count (naive Bun_{Z/2}(T*) points):", n_loc)
assert n_loc == 4

# Loop-level Grothendieck ranks
rank_Omega_C0 = 1  # Vect
rank_Omega_C1 = 2  # Rep(Z/2): 1 + sign
print("rank Omega(C0) =", rank_Omega_C0)
print("rank Omega(C1) =", rank_Omega_C1)

# Fusion 2-category simple/component counts
simples_C0 = 2  # two graded components, each ~Vect
simples_C1 = 2  # Vect-mod simples for Rep(Z/2): trivial + sign-twisted
print("simples/components C0 =", simples_C0, " C1 =", simples_C1)

# Twist eigenvalues on loop generators (both symmetric/trivial => +1)
twists_C0 = [1]
twists_C1 = [1, 1]  # trivial rep and sign rep both bosonic, twist +1
print("twists C0 =", twists_C0, " C1 =", twists_C1)
assert all(t == 1 for t in twists_C0 + twists_C1)

print("RESULT: naive counts coincide at torus level (4 local systems, "
      "trivial twists); no certified Hom-rank/twist mismatch. BLOCKED.")
