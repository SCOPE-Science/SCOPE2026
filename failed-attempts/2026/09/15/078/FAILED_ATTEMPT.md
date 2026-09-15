# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Extending the length vs. Culler-Shalen norm inequality to hyperbolic alternating knot exteriors
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20288
- **Disposition:** NO_RESULT
- **Domain:** Low-Dimensional Topology
- **Method:** character variety deformation and Dehn surgery estimates

## Problem

Let M be the exterior of a hyperbolic alternating knot in S^3. Let ||.|| be the total Culler-Shalen norm on H_1(partial M;R) and, for any horotorus T in M, let length_T(r) be the Euclidean length of a slope r on partial M. Does ||r|| >= (2/3) length_T(r) hold for every slope r and every horotorus T? In particular, does the uniform bound hold for the bounded-volume subfamily vol(M) <= V (equivalently, bounded twist number)?

## Attempted claim

Let M be the exterior of a hyperbolic alternating knot in S^3. Let ||.|| be the total Culler-Shalen norm on H_1(partial M;R) and, for any horotorus T in M, let length_T(r) be the Euclidean length of a slope r on partial M. Does ||r|| >= (2/3) length_T(r) hold for every slope r and every horotorus T? In particular, does the uniform bound hold for the bounded-volume subfamily vol(M) <= V (equivalently, bounded twist number)?

## Research outcome

Target blocked: universal length-vs-Culler-Shalen-norm inequality for alternating knot exteriors could be neither proved nor disproved. Executed a maximal-cusp length survey, exact Riley-curve elimination for 4_1/5_2, and heuristic multi-slope lower-bound ratio tests (all passing with margin), but certification tooling was unavailable and bounded volume still leaves an infinite family, so no auditable claim resulted.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No certified result is claimed: SnapPy cusp translations and normal-surface boundary slopes are uncertified floating-point numerics, Sage-dependent verification entry points were unavailable, the Riley-curve elimination was left un-normalized, and only 13 small alternating knots were surveyed, so nothing here establishes or refutes the universal inequality.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No certified result is claimed: SnapPy cusp translations and normal-surface boundary slopes are uncertified floating-point numerics, Sage-dependent verification entry points were unavailable, the Riley-curve elimination was left un-normalized, and only 13 small alternating knots were surveyed, so nothing here establishes or refutes the universal inequality.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
