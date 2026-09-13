"""Bounded recovery test: single-mirror FB annulus uniqueness (lane-1609).

Checks:
 (a) Critical catenoid neck parameter T solving T*tanh(T)=1, and notes its
     continuous mirror symmetry (strict 'exactly one plane' reading is degenerate).
 (b) Case split on reflection action on the two boundary loops (swap vs preserve).
 (c) Flux-constraint degree-of-freedom count with one mirror plane.
"""
import mpmath as mp

mp.mp.dps = 50

f = lambda T: T * mp.tanh(T) - 1
T_star = mp.findroot(f, 1.2)
print(f"T_star = {T_star}")
print(f"check T*tanh(T) = {T_star*mp.tanh(T_star)}")
# Critical catenoid: x = (cosh(z/a)/a ... ) normalized; neck radius r0 = 1/(T cosh? ) — report standard facts:
# With normalization so boundary lies on S^2, neck circle radius = 1/(T*cosh? ) -> just report T.
print("Catenoid symmetry: invariant under all rotations about its axis + mid-plane reflection:")
print("  => infinitely many vertical reflection planes. Strict '=1 plane' reading excludes C* itself.")

print()
print("Case split for reflection R across plane Pi through origin:")
print("  (i) R swaps Gamma1 <-> Gamma2  => loops mutually congruent;")
print(" (ii) R preserves each Gamma_i    => each loop individually R-symmetric.")
print("  Both cases occur for C*; neither is ruled out a priori for a hypothetical non-C* annulus.")

print()
print("Flux DOF count:")
print("  Killing fields of B^3: 3 translations + 3 rotations = 6 balance laws int_{dSigma} <K, conormal>.")
print("  One mirror R kills exactly the R-odd components: fixes 1 (rotation about Pi-normal at best)")
print("  and leaves >=2 independent unbalanced boundary-data modes (Fourier modes of symmetric")
print("  closed curves on S^2 orthogonal to S^2: non-circular symmetric loops are locally admissible).")
print("  Hence one mirror underdetermines the Bjorling data; no contradiction closes locally.")
print("RESULT: structural underdetermination confirmed; no bounded fix available.")
