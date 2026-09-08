# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified limit-cycle census for five committed quadratic Lienard boxes: Dulac exclusion, trapping annuli, and interval Poincare returns
- **Round:** 2026-09-07-first-light-01
- **Lane:** 265
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Ordinary Differential Equations
- **Method:** Dulac trapping-region construction with Poincare-return interval-enclosure and Floquet-interval replay

## Problem

Certified limit-cycle census over 5 fixed quadratic Lienard-type boxes: family dx/dt = y - (a*x + b*x^2), dy/dt = -x + c*y + d*x*y with boxes B1..B5 of radius <=0.02 around centers (a,c,b,d) = (1.0,0.5,0.3,0.0), (1.5,0.8,0.2,0.1), (0.8,0.3,0.5,-0.1), (2.0,1.0,0.1,0.0), (0.5,0.1,0.4,0.2). For each box state rectangle R, annulus A, section Sigma. Prove by interval-checked inequalities: Dulac exclusion on part of R, inward trapping on A edges, and validated Poincare return enclosing exactly one hyperbolic cycle where claimed.

## Attempted claim

For each of boxes B1..B4 the field has exactly one limit cycle, enclosed in the stated annulus A with inward-pointing vector field on both boundaries, with interval-enclosed Poincare return satisfying P(I) subset I and derivative interval excluding 1 (hyperbolic, Floquet-multiplier interval bounded away from 1); box B5 is cycle-free by a Dulac-function divergence-sign certificate on its stated rectangle. All inequalities replay from the committed coefficients.

## Research outcome

Pivoted from the admitted B1-B4 existence census (refuted by simulation + linear census: stable foci/saddles, no cycles) to a rigorous uniform-over-box exclusion fragment: Lyapunov no-cycle discs for B1/B3/B5, equilibrium census incl. B3 whole-plane uniqueness and B2/B4 saddle certification, and Dulac half-plane logs for all five boxes, all replayable stdlib-only via output/artifacts/verify_basins.py (VERIFY_OK).

## Why this attempt failed

Failed axes: correctness, value.

correctness: Replayed inputs/artifacts/verify_basins.py: VERIFY_OK. Exact-rational check A^T P+P A+I==0 holds for B1/B3/B5 P (det>0, P>0). Lyapunov logic Vdot<=-1+spread+K|z| is sound; KAPPA upper bounds valid (B1 0.6403<=0.641, B3 1.0469<=1.048, B5 0.8683<=0.869); spread<1, R<r* and V(R)<Vsafe hold with large margins even with 1e-9 padding, so Part A conclusion true. Equilibrium sup-g bounds (-0.3746/-0.6700/-0.8321) verified from box corners; B2/B4 saddle ac ranges [1.1544,1.2464]/[1.9404,2.0604] correct; Dulac base/slope logs for all five boxes and B5 slab -0.63 correct. ESSENTIAL DEFECT in B3 whole-plane uniqueness log: script/DRAFT claim bd in [-0.0576,-0.0416] and disc<=0.0108-0.1227<0. True box product range is [-0.0624,-0.0384] (b in [0.48,0.52], d in [-0.12,-0.08]); true min 4|bd||ac-1|=0.11329 not 0.1227, and true max s^2=0.010816 not 0.0108. Hence two printed intermediate inequalities are false as stated. Final conclusion disc<0 remains true (0.010816-0.11329=-0.10247<0) but the logged derivation is inaccurate. Additional rigor gap: spread/K/eigs use floats not intervals (margins >> eps so conclusion robust, but not formal interval proof as claimed). RK4 survey correctly excluded from proof. value: Strongest honestly-claimed headline is a partial exclusion fragment: tiny Lyapunov no-cycle discs (R=0.02/0.04/0.06), uniqueness in [-0.5,0.5]^2 / B3 whole-plane via quadratic discriminant, B=1 divergence sign on x>=0. No limit cycle, trapping annulus, Poincare return, or Floquet interval is claimed; full cycle-freeness open for every box; B2/B4 basins open. This is textbook linear stability + one-line algebra (Lyapunov equation at stable focus, quadratic g(x) bound, div=(c-a)+(d-2b)x sign from box corners with c-a<0, d-2b<0 by construction). Radii and half-plane logs are mechanically implied, not hard invariants; five boxes are arbitrary regime samples with no pre-existing identity as natural objects, and no future researcher would need R=0.02 or div<0 on x>=0 at these points. Gasull-Giacomini-Grau precedent (precise existence/location of detected cycles) does not transfer to tiny stable-focus discs plus open existence. DRAFT honestly flags incompleteness, but honesty does not create substantive result. Certification alone does not rescue arbitrary scope. Fails independent-retrieval test.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial theorem only: no full cycle-freeness for any box (outer-equilibrium counts for B1/B5 open; B2/B4 separatrix/basin structure open); no trapping annuli, Poincare returns, or hyperbolicity/Floquet intervals; KAPPA/BDC constants are crude-but-rigorous upper bounds checked against box corners; numerical non-existence survey is evidence only, not part of the proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
