# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Complete lex shape-position stratification of sparse {+-1} quadratic pairs in Q[x,y] with box-minimal non-shape witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 277
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Computational Algebra
- **Method:** exhaustive Buchberger shape-stratification over finite sparse coefficient box with elimination and variety-count replay

## Problem

Let U be the complete finite set of unordered pairs {f,g} in Q[x,y], each of total degree exactly 2 with 2 or 3 nonzero terms and all nonzero coefficients in {+1,-1}. For every pair with I=<f,g> zero-dimensional, compute reduced Groebner bases under lex (both variable orders) and grevlex, decide shape position under each lex order, record elimination generator degrees (resultant cross-checked) and exact affine complex variety counts. Report the full shape/non-shape stratification table over U and exhibit the lex-least pair failing shape position under both orders, with box-minimality certified by the completed enumeration.

## Attempted claim

The shape/non-shape stratification table over the complete {+1,-1} sparse-quadratic box U is exactly table T (one row per zero-dimensional pair: shape verdicts, basis sizes, elimination degrees, variety counts as replayed), and the named pair P* fails lex shape position under both variable orders and is lex-least such in U, establishing the box-minimal shape-failing witness.

## Research outcome

Certified the box-minimal double lex-non-shape witness P*={-y^2-y-1,-x^2-x-1} (indices 0,60) over the complete 200-poly/19900-pair sparse {+-1} quadratic box in Q[x,y]: both reduced lex bases are {x^2+x+1,y^2+y+1}, quot-dim 4, eliminant degs 2/2, resultant degs 4/4 with squared (t^2+t+1) factors, 4 distinct complex zeros; 59-pair prefix audit proves box-least minimality. Replay: python3 output/artifacts/check_pstar.py -> VERIFY_OK (~0.2s). Full-census table explicitly NOT claimed (inherited census artifacts buggy).

## Why this attempt failed

Failed axes: value.

value: Headline P* alone, judged separately from the unfinished full census per standard, is a textbook restatement wrapped in an order-artifact enumeration, not an independently retrievable invariant. P*={-y^2-y-1,-x^2-x-1} is decoupled univariate quadratics: reduced lex bases {x^2+x+1,y^2+y+1}, double-non-shape, quot-dim 4, eliminants degree 2 vs resultants (y^2+y+1)^2/(x^2+x+1)^2 degree 4, 4-point variety — all visible by inspection/hand algebra (Res_x = f^{deg_x g} for x-constant f) with discriminants -3; no computation needed and known to anyone knowing the Shape Lemma. It fails the narrow-datum exception: value IS mechanically implied, not unknown before computation, and no future researcher would query index '(0,60)' — minimality is relative to the candidate's implementation sort key (support-tuple, coefficient-tuple sign order), not a natural mathematical order (degree, sparsity, Bezout number). A different sign ordering gives a different 'first' decoupled pair (e.g. {x^2-1,y^2-1} equally simple). The 59-row prefix is a cutoff artifact, and the full 19900-row stratification that might have constituted a citable finite classification is explicitly NOT claimed (inherited files disclaimed as corrupted). Certification (VERIFY_OK) alone does not rescue an arbitrary object/unexplained number. Intrinsic low value + arbitrary scope + missing substantive result.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Claims ONLY the box-minimal double-non-shape witness and its invariants, not the full 19900-row stratification census. Inherited stratification.csv/summary.json have corrupted eliminant/resultant columns (Poly.resultant tuple-vs-Poly misuse, univariate-extraction bugs) and a swapped-variable shape_yx column (identically 0; e.g. pair (0,16) is in fact shape in y>x order) and are NOT relied upon; they plus other exploratory scripts/logs remain in output/artifacts/ as superseded working notes. Min…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
