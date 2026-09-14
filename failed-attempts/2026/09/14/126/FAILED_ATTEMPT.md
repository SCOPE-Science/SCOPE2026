# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp toroidal-toroidal distance for hyperbolic manifolds with totally geodesic boundary
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20122
- **Disposition:** NO_RESULT
- **Domain:** Low-Dimensional Topology
- **Method:** character variety and Culler-Shalen norm techniques

## Problem

Let M be a compact, connected, orientable hyperbolic 3-manifold with chi(M)<0 containing a torus boundary component T_0 and a connected totally geodesic boundary component Sigma_g, g>=2. Call a slope r on T_0 of type T if M(r) contains an essential torus. Determine Delta_neg(T,T) = max{Delta(r,s): M,T_0 as above, r,s both type T} and whether the bound is realized; in particular decide whether the large-manifold bound Delta<=4 stays sharp under chi<0 or drops to 3 or lower, using SL(2,C) character variety and Culler-Shalen norm techniques.

## Attempted claim

Let M be a compact, connected, orientable hyperbolic 3-manifold with chi(M)<0 containing a torus boundary component T_0 and a connected totally geodesic boundary component Sigma_g, g>=2. Call a slope r on T_0 of type T if M(r) contains an essential torus. Determine Delta_neg(T,T) = max{Delta(r,s): M,T_0 as above, r,s both type T} and whether the bound is realized; in particular decide whether the large-manifold bound Delta<=4 stays sharp under chi<0 or drops to 3 or lower, using SL(2,C) character variety and Culler-Shalen norm techniques.

## Research outcome

Target not established: universal bound Delta_neg(T,T) <= 4 holds via largeness, but whether distance 4 is realized under chi(M)<0 with a genus>=2 totally geodesic boundary component remains undecided after bounded SnapPy heuristic scans and literature upper-bound work.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Upper bound Delta_neg(T,T) <= 4 was secured via the large-manifold corollary, but sharpness (4 vs <=3) was not decided. SnapPy solution_type scans are only hyperbolicity heuristics: framing conversion to the documented Gordon/Teragaito toroidal slopes was unresolved, verify_hyperbolicity needs unavailable Sage, and the arc-drilling retention plus hyperbolization and essential-torus survival were never constructed or certified. No complete proof or counterexample exists in the artifacts.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Upper bound Delta_neg(T,T) <= 4 was secured via the large-manifold corollary, but sharpness (4 vs <=3) was not decided. SnapPy solution_type scans are only hyperbolicity heuristics: framing conversion to the documented Gordon/Teragaito toroidal slopes was unresolved, verify_hyperbolicity needs unavailable Sage, and the arc-drilling retention plus hyperbolization and essential-torus survival were never constructed or certified. No complete proof or counterexample exists in the artifacts.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
