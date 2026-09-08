# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing the live-open binary [36,11] interval via residual MacWilliams classification
- **Round:** 2026-09-07-first-light-01
- **Lane:** 196
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Coding Theory
- **Method:** residual classification with MacWilliams/Krawtchouk integer feasibility chained to Heijnen shortening cascade

## Problem

Decide the live-open binary BKLC interval at (n,k)=(36,11): determine whether a binary linear [36,11,13] code exists. Either (A) prove nonexistence via residual-with-respect-to-a-minimum-weight-word plus MacWilliams/Krawtchouk integer-feasibility elimination chained by shortening/puncturing to the Heijnen [33,9,13]-nonexistence anchor, establishing d(36,11)=12; or (B) exhibit an explicit generator matrix of a [36,11,13] code with exact weight enumerator, establishing d(36,11)=13. In either branch the artifact closes the interval Lb=Ub with a checkable certificate.

## Attempted claim

The binary BKLC interval at (36,11) is closed: either (A) no binary linear [36,11,13] code exists — proved by enumerating all MacWilliams/Krawtchouk-compatible weight enumerators for the putative code and eliminating each by the residual-plus-shortening cascade to the Heijnen [33,9] nonexistence bound, so d(36,11)=12; or (B) an explicit [36,11,13] generator matrix with exact weight enumerator is exhibited, so d(36,11)=13. The delivered certificate determines which value holds and closes Lb=Ub.

## Research outcome

Live-open cell (36,11) not closed; delivered fallback-grade partial theorem: new certified [36,11,12] witness + proved residual classification (d* in {7,8}, d*>=9 eliminated) + new (36,11)->(36,10) even-subcode reduction, all stdlib-replayable, with honestly logged LP failure and hunt.

## Why this attempt failed

Failed axes: value.

value: Strongest headline judged separately from unfinished survey; still fails independent-retrievability. (a) Witness re-proves known Lb=12 via different route, no new table value; exact enumerator is invariant of investigator-chosen arbitrary representative, not of natural cell object d(36,11), no pre-computation motivation for this distribution, no downstream need; certification alone does not rescue arbitrary object. (b) Lemma B is textbook first-order residual + single Griesmer lookup G(10,9)=25>23, recomputable in seconds, leaves two subfamilies, promised MacWilliams/Krawtchouk feasible-enumerator table missing (float LP failed 195.06 vs 306.34 and removed) and promised Heijnen-cascade kill explicitly reports 'consistent, no contradiction'. (c) Lemma D is elementary parity-kernel + G(10,18)=42 corollary leaving both (36,11) and (36,10) open, no exact order/constant/value determined, tiny gain recomputable instantly. No rigorously established exact invariant of natural object whose value was unknown and reusable (d(36,11) remains 12-vs-13 open). This is textbook restatement / tiny unmotivated gain / unexplained enumeration case: correct and new yet not worth finding later. Missing substantive result is intrinsic, not a bounded presentation gap.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The (36,11) interval is NOT closed: no [36,11,13] witness and no [36,11,13]-nonexistence proof. No MacWilliams/Krawtchouk enumerator-table certificate is claimed (the float LP branch failed with 195.06-vs-306.34 inconsistency and was removed; logged in WORKLOG). The [36,11,12] witness re-establishes the known Lb=12 via a new matrix, not a new table value. Lemma D reduces (36,11) to (36,10) but (36,10) itself remains open, so no cell falls. Heijnen [33,9] anchor cited from tables, not re-proved.…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
