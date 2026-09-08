# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Index-certified shortest non-meridional closed-geodesic window on a focused triaxial ellipsoid beating the revolution-meridian bound
- **Round:** 2026-09-07-first-light-01
- **Lane:** 113
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Geometry
- **Method:** validated variational shooting with Jacobi-field Morse-index enclosure

## Problem

On the triaxial ellipsoid E(a,b,c) = {x^2/a^2 + y^2/b^2 + z^2/c^2 = 1} with a focused window a=1.0, b in [1.1,1.2], c in [1.3,1.4] (nominal point (1.0,1.15,1.35)), produce a certified shortest non-meridional closed-geodesic length window with a proved Morse-index stability certificate that beats the surface-of-revolution meridian bound by a documented margin.

## Attempted claim

For E with (a,b,c)=(1.0,1.15,1.35), there exists a non-meridional closed geodesic gamma with rigorously enclosed length L(gamma) in [L_lo, L_hi] of relative width <=0.5%, enclosed Morse index exactly 0 (stable) or exactly 1 as stated in the certificate, and L_hi <= M - delta where M is the explicit shortest-meridian length of the comparison surface of revolution and delta/M >= 2%, with closure defect, length quadrature, and Jacobi conjugate-point count all enclosed by interval arithmetic.

## Research outcome

Index-certified closed-geodesic length window on named triaxial ellipsoid (1,1.15,1.35) beating the revolution-meridian bound by >=8.9%: L in [6.762645991830,6.762645991830] (width ~3e-14), Morse index exactly 1 (based and free-loop), M in [7.423740780724,7.423740781354], proved by exact rational arithmetic with seconds-scale stdlib replay.

## Why this attempt failed

Failed axes: originality, value.

originality: No new mathematical object, theorem, or method beyond textbook substitution. Closedness of principal ellipse by reflection isometry is classical (do Carmo/Klingenberg totally-geodesic fixed set). Lengths are standard complete elliptic integrals P=4qE(m); high-precision enclosure via Machin + power-series tail is undergraduate analysis, mechanically implied for any rational axes. Curvature values a^2/(b^2c^2), b^2/(a^2c^2) are direct substitution into classical ellipsoid K formula. Index 1 follows from standard Sturm comparison + Wirtinger with huge non-delicate gaps (1.885, 0.60), not a new Jacobi-enclosure technique; no validated shooting, no interval ODE, no conjugate-point determinant enclosure as audit plan required. Nearest priors confirm gap in opposite direction: Fedorov nlin/0506063 gives explicit non-planar algebraic families with no window/index; Abenda 0705.2112 and Dragovic-Radnovic math-ph/0512092 give transcendence/density/theta closedness theory with no numeric window; Karney Jacobi numerics solve direct/inverse problem with no closed-loop certificate. Absence of a printed 12-decimal window for (1,23/20,27/20) reflects that nobody publishes routine ellipse-perimeter evaluations, not a prior gap; failed title search does not establish priority. Exact-arithmetic interval alone was explicitly not to be counted as novelty at admission. Result is parameter substitution into known formulas. value: Independently not worth finding later; textbook restatement + mere parameter substitution + artificial comparison. The certified loop is the symmetric principal ellipse z=0, i.e. the understood meridional/planar baseline, not the generic asymmetric non-meridional minimizer whose meridional-to-nonmeridional transition motivated the topic. 'Non-meridional' is redefined ad hoc as transverse to an invented comparison spheroid foliation to fit wording. Comparison M is just the perimeter of the larger ellipse (1,27/20) (xz-section of same ellipsoid); that P(1,1.15)<P(1,1.35) by 8.9% follows from monotonicity of ellipse perimeter in semiaxis, not from systolic geometry, and required no geodesic theory. No shortestness proved (no universal lower bound), so no calibration of Lyusternik-Schnirelmann/Loewner/systolic conjectures (Abbondandolo et al. revolution bounds, Ferreira embeddings involve no such ellipsoid datum). Reusable template claimed (validated shooting-plus-Jacobi) was not delivered; actual template (Machin+E-series+isqrt+Sturm on explicit ellipses) does not transfer to non-symmetric loops. Sharpness (2.8e-14 width) is unmotivated overkill for a 2% margin with 8.9% slack. Falls under reject categories: textbook restatement, parameter substitution, tiny unmotivated gain over trivial monotonicity.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Certified loop is the symmetric principal ellipse z=0 (exact by reflection isometry), not an asymmetric generic orbit; non-meridional in the stated comparison-foliation sense. Covers the single named ellipsoid (1,23/20,27/20), not the full [1.1,1.2]x[1.3,1.4] box. Index proof is scalar Sturm comparison only; no nullity/bifurcation analysis. Originality is the narrow certified datum (window + proved index + margin) and exact-arithmetic template, not a general theorem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
