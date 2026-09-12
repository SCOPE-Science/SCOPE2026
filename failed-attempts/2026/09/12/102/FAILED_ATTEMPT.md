# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sakuma-Weeks crossing-arc fragment over Montesinos knots to 12 crossings
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1328
- **Disposition:** NO_RESULT
- **Domain:** hyperbolic 3-manifolds / canonical decompositions
- **Method:** tilt-verified Epstein-Penner canonical cellulation

## Problem

Let H be the set of hyperbolic alternating Montesinos knots with crossing number at most 12, each equipped with a reduced alternating Montesinos diagram D. For each crossing of D let a(D) be the associated crossing arc (polar axis) in M_K = S^3 \ K. Is a(D) isotopic to an edge of the Epstein-Penner canonical polyhedral decomposition of M_K for every crossing of every diagram in H (the Sakuma-Weeks crossing-arc fragment)? Decide by exact tilt-verified canonical cellulations (e.g. SnapPy/tilt certificates): either prove the property for all of H or exhibit one explicit knot, diagram, and crossing whose arc is provably not a canonical edge, with the tilt signs and canonical cells listed.

## Attempted claim

Let H be the set of hyperbolic alternating Montesinos knots with crossing number at most 12, each equipped with a reduced alternating Montesinos diagram D. For each crossing of D let a(D) be the associated crossing arc (polar axis) in M_K = S^3 \ K. Is a(D) isotopic to an edge of the Epstein-Penner canonical polyhedral decomposition of M_K for every crossing of every diagram in H (the Sakuma-Weeks crossing-arc fragment)? Decide by exact tilt-verified canonical cellulations (e.g. SnapPy/tilt certificates): either prove the property for all of H or exhibit one explicit knot, diagram, and crossing whose arc is provably not a canonical edge, with the tilt signs and canonical cells listed.

## Research outcome

Target blocked: exact tilt-verified Epstein-Penner certificates require Sage, which is unavailable; unverified numerics cannot decide the Sakuma-Weeks crossing-arc claim, so clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No tilt-verified canonical cellulation could be produced because every certified SnapPy path requires the absent Sage interval engine; unverified canonize() output is documented as possibly wrong, so no crossing-arc verdict was drawn and no partial table is claimed as evidence.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No tilt-verified canonical cellulation could be produced because every certified SnapPy path requires the absent Sage interval engine; unverified canonize() output is documented as possibly wrong, so no crossing-arc verdict was drawn and no partial table is claimed as evidence.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
