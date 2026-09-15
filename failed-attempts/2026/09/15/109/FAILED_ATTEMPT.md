# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Depth-three cohomological-dimension vanishing in ramified mixed characteristic: theorem or counterexample?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20338
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** perfectoid and prismatic envelope construction

## Problem

Let (R,m) be a d-dimensional ramified regular local ring of mixed characteristic (0,p) and I subset R an ideal with depth(R/I) >= 3. Is cd_R(I) := sup{j | H^j_I(R) != 0} <= d-3, i.e. H^j_I(R)=0 for all j >= d-2? Prove the vanishing or construct an explicit counterexample with depth(R/I) >= 3 and H^{d-2}_I(R) != 0 (or H^{d-1}_I(R) != 0).

## Attempted claim

Let (R,m) be a d-dimensional ramified regular local ring of mixed characteristic (0,p) and I subset R an ideal with depth(R/I) >= 3. Is cd_R(I) := sup{j | H^j_I(R) != 0} <= d-3, i.e. H^j_I(R)=0 for all j >= d-2? Prove the vanishing or construct an explicit counterexample with depth(R/I) >= 3 and H^{d-2}_I(R) != 0 (or H^{d-1}_I(R) != 0).

## Research outcome

Target blocked on both routes: the H^{d-2} vanishing proof needs an unestablished ramified prismatic/perfectoid descent lemma, and a counterexample needs local-cohomology certification tooling absent here. A bounded Stanley-Reisner depth proxy confirmed depth>=3 shapes (including the critical non-CM case) exist but cannot decide vanishing. No independently auditable alternative was worthwhile, so the lane exits clean with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The investigation established the exact location of the obstruction but closed neither direction: the H^{d-2} vanishing over a ramified base is neither proved nor disproved, and no certified explicit counterexample was produced. The bounded Stanley-Reisner proxy decides only combinatorial depth, not local-cohomology vanishing, and the environment lacked any Groebner or local-cohomology engine. No emergent finding is claimed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The investigation established the exact location of the obstruction but closed neither direction: the H^{d-2} vanishing over a ramified base is neither proved nor disproved, and no certified explicit counterexample was produced. The bounded Stanley-Reisner proxy decides only combinatorial depth, not local-cohomology vanishing, and the environment lacked any Groebner or local-cohomology engine. No emergent finding is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
