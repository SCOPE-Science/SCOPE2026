# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified integral-point census for sixth-power-free Mordell curves with 10001 <= k <= 10032
- **Round:** 2026-09-07-first-light-01
- **Lane:** 825
- **Disposition:** NO_RESULT
- **Domain:** Diophantine Geometry
- **Method:** Baker-Wustholz logarithmic height bounds with 2-descent Selmer rank analysis and lattice-reduction search caps

## Problem

Close the exact integral-point census for all sixth-power-free k with 10001<=k<=10032: for each such k, determine the full finite set {(x,y) in Z^2 : y^2=x^3+k} together with the Mordell-Weil rank and a 2-descent Selmer upper bound.

## Attempted claim

For every sixth-power-free integer k in [10001,10032], the set of integer solutions to y^2=x^3+k is exactly the certified list (to be produced), each list verified below the reduced Baker-Wustholz search bound, with per-k Mordell-Weil rank and 2-Selmer dimension logged; equivalently the union table is complete and no point is missing.

## Research outcome

Target (exact integral-point census with rank and 2-Selmer for sixth-power-free k in 10001..10032) is BLOCKED: completeness needs the descent/height stack absent from this lane. Bounded elementary substitutes provably close nothing: finder to 2e5 gives lower bounds only; single-modulus sieves over m<2000 obstruct 0/25 empty-to-bound curves; an exact stdlib lemma proves tors=0 on all 32 k and rank>=1 on the 7 k with integral witnesses, which is a lower-bound byproduct, not an auditable emergent claim. NOT_PRESET lane with no valuable original increment, so CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No Sage/PARI/mwrank/Magma, no package installs: 2-descent Selmer bounds, rank saturation, Baker-Wustholz caps, LLL reduction, and elliptic-log sieve enumeration were all unimplementable in-lane.', 'Bounded finder to XMAX=200000 yields candidate lower-bound points only, with no completeness content for any of the 32 k.', 'Single-modulus congruence sieves over 3<=m<2000 obstruct 0 of the 25 empty-to-bound curves; no elementary emptiness certificate was found.', 'Proved tors=0 on 32/32 k and rank>=1 on the 7 k with integral witnesses is exact but lower-bound only: no Selmer upper bound, no reduced height cap, no completeness; it does not qualify as an independently valuable emergent finding.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No Sage/PARI/mwrank/Magma, no package installs: 2-descent Selmer bounds, rank saturation, Baker-Wustholz caps, LLL reduction, and elliptic-log sieve enumeration were all unimplementable in-lane.', 'Bounded finder to XMAX=200000 yields candidate lower-bound points only, with no completeness content for any of the 32 k.', 'Single-modulus congruence sieves over 3<=m<2000 obstruct 0 of the 25 empty-to-bound curves; no elementary emptiness certificate was found.', 'Proved tors=0 on 32/32 k and ran…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
