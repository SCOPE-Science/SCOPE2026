# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Tighter certified two-sided enclosure for the first Dirichlet eigenvalue of the standard L-shaped membrane via conforming FEM with Lehmann-Goerisch lower bound
- **Round:** 2026-09-07-first-light-01
- **Lane:** 20
- **Disposition:** NO_RESULT
- **Domain:** Spectral Geometry
- **Method:** certified conforming FEM eigenvalue enclosure with Lehmann-Goerisch lower bound and explicit a posteriori majorant

## Problem

Let Omega_L be the L-polygon with CCW vertices (0,0),(2,0),(2,1),(1,1),(1,2),(0,2) (area 3, one 270-degree reentrant corner at (1,1), congruent to (-1,1)^2 minus [0,1]^2). Let lambda1 be the lowest eigenvalue of -Delta on H0^1(Omega_L). Survey published numerical values versus certified enclosures for lambda1 on triangles/quadrilaterals/L-shapes, then prove a new rigorous two-sided enclosure [L,U] with L <= lambda1 <= U, width U-L <= 5e-4, via P2-conforming FEM Rayleigh-quotient upper bound plus Lehmann-Goerisch lower bound with explicit a posteriori majorant, all linear-algebra and quadrature steps interval-verified, with meshes, stiffness/mass matrices and bound scripts stored and rerunnable in <10 minutes.

## Attempted claim

Exhibit explicit rationals/decimal intervals L<U with U-L <= 5e-04 such that L <= lambda1(Omega_L) <= U is rigorously verified by the audit plan, [L,U] contains the Betcke-Trefethen MPS reference 9.63972384402, and [L,U] is strictly narrower than the best prior rigorous two-sided enclosure for the same normalization re-checked in the survey (prior rigorous widths >= ~2e-03 / one-sided only). Upper bound from P2-conforming Ritz value plus bounded variational crime; lower bound from Lehmann-Goerisch with a crude verified shift rho (Crouzeix-Raviart/Faber-Krahn) and explicit residual majorant on a corner-graded mesh.

## Research outcome

No certifiable tightening: proved rigorous wide enclosure [6.0561, 9.643856] for lambda1 of the size-2 L-membrane (exact-rational Faber-Krahn floor + P1-conforming N=256 Rayleigh upper with explicit rounding bound), verified MPS 9.63972384402 containment, plus convergence table to 9.64385398, self-contained Kato H^{-1} lemma with honest negative flux test, square gap nu=12.33, and <1s rerunnable certificate. Width 3.59 misses 5e-04/5e-03 gates; prior FHM widths remain tighter.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Two-sided width 3.5878 >> 5e-04 target and >> 5e-03 fallback; no tightening over Fox-Henrici-Moler O(1e-02) widths is claimed.', 'Lower bound is only the exact-rational Faber-Krahn floor 6.0561; Kato flux lemma proved but vacuous with tested averaged flux (eta 2.3-3.3, e2 diverging); equilibrated RT flux / CR verification / Trefftz-Lehmann not completed.', 'Upper bound U=9.643856 is rigorous (dyadic-exact stiffness + Higham rounding 1.42e-06) and within 0.00413 of MPS, but MPS containment uses quoted non-rigorous value as reference only.', 'Graded-mesh tests did not beat uniform at equal dofs in the time budget; P2 not implemented; convergence table is non-rigorous except the N=256 upper.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Two-sided width 3.5878 >> 5e-04 target and >> 5e-03 fallback; no tightening over Fox-Henrici-Moler O(1e-02) widths is claimed.', 'Lower bound is only the exact-rational Faber-Krahn floor 6.0561; Kato flux lemma proved but vacuous with tested averaged flux (eta 2.3-3.3, e2 diverging); equilibrated RT flux / CR verification / Trefftz-Lehmann not completed.', 'Upper bound U=9.643856 is rigorous (dyadic-exact stiffness + Higham rounding 1.42e-06) and within 0.00413 of MPS, but MPS containment use…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
