# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** New large-determinant record for {+-1}-matrices at open order n=29 via 3-normalized bordering and excess-guided search
- **Round:** 2026-09-07-first-light-01
- **Lane:** 238
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Matrix Theory
- **Method:** 3-normalized Hadamard bordering with maximal-excess-guided stochastic local search and Bareiss exact verification

## Problem

Construct a new world-record large-determinant {+-1}-matrix at the open 4k+1 order n=29 via 3-normalized Hadamard bordering with Farmakis-Kounias maximal-excess-guided stochastic local search, with exact Bareiss determinant verification strictly exceeding the posted Orrick-Solomon record lower bound.

## Attempted claim

Let R29 be the largest |det| for 29x29 {+-1}-matrices posted in Orrick et al. math/0304410 and the Orrick-Solomon maxdet tables as retrieved and committed at run start. Exhibit an explicit 29x29 matrix M* with entries +-1 whose exact Bareiss determinant D*=|det M*| (integer fixed by the run) satisfies D* > R29 strictly, with Gram matrix G*=M*M*^T and row-excess search log; report the ratio of D* to the Ehlich/Barba upper bound at n=29.

## Research outcome

No new n=29 world record (D*>R29 NOT found; exhaustive H1 sweep proves posted record is a strict single-flip local optimum). Consolidated to the admissible fallback: four exact (+-1) witnesses at open 4k+1 orders n=29/33 strictly beating classical pre-2003 baselines (W29,W29b>Koukouvinos K29; W33,W33b>Farmakis-Kounias FK33), all verified by exact stdlib-only Bareiss+Gram replay (verify.py -> results.json, ALL CHECKS PASSED).

## Why this attempt failed

Failed axes: originality, value.

originality: No new inequality over best-known is established; primary target D*>R29 was NOT achieved by admission. The fallback 'beats classical baseline' inequalities were already published in the cited prior itself: Orrick et al. math/0304410 (2003) reports n=29 and n=33 matrices as new world records explicitly superseding the Farmakis-Kounias/Koukouvinos values (posted R29 at 86.5% of Barba vs Koukouvinos 81.4%; n=33 record vs FK value). Hence R29>K29 and D33>FK33 are prior results, not new. W29 (det=R29) and W33 (det=D33) are signed-permutation copies of those published records — verified same |det| and identical absolute Gram-entry multisets — so they contribute no new object, value, or method; equality is implied by signed-permutation invariance. The only distinct determinants, W29b (H=1 neighbor, 1.9% BELOW R29) and W33b (H=2 neighbor, ~7% BELOW D33), are sub-record single/double-flip degradations of the published records that beat only the long-superseded baseline while losing to the current posted record at the same order. They do not improve any best-known lower bound, use no 3-normalized-bordering construction (artifacts: permutation / flip logs), and are trivial variations obtainable by anyone holding the posted matrix. A timestamp or exact Bareiss certificate does not establish priority over the 2003 record that already implies the baseline comparison. value: Independently worth retrieving? No. The program's benchmark form is a strict improvement over best-known (D*>R29 / new D33 record); none is delivered — best-known values R29, D33 are merely replayed. Remaining witnesses fail the narrow-datum rescue test: W29/W33 values are mechanically implied by Hadamard equivalence to the known records (not unknown before computation), and W29b/W33b are arbitrary 1-2-flip neighbors below best-known with no motivated identity (why (6,6) / (21,0),(0,24)?), no mathematical interpretation, and no downstream use — D-optimal tables and construction-boundary calibration cite best-known extremals, not sub-record neighbors that are 2-7% worse at the same order while +4.3%/+0.49% above an obsolete pre-2003 baseline. W33b's +0.49% over FK33 while ~7% below D33 is a tiny unmotivated gain against a superseded comparator; certification (Bareiss+Gram) alone does not rescue an arbitrary object or unexplained number. The fallback as executed is a bare failed-record log plus repackaged record copies and degraded neighbors, not two new benchmark lower bounds.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Primary target (strict n=29 world record D*>R29) FAILED: no such matrix found; not claimed. Live Indiana maxdet tables unreachable (404/site migration), so baselines are pinned to arXiv math/0304410v1 text; a newer unpublished record would supersede benchmark comparisons but not the exact determinant equalities. W29/W33 are Hadamard-equivalent (signed row/col permutations) to posted records, so their determinant equalities are expected; their value is as distinct design-table objects with indep…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
