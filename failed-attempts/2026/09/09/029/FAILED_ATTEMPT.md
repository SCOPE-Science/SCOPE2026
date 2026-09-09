# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First certified upper bounds for girth-5 extremal numbers at n=54-56 with improved explicit witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 340
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Extremal Graph Theory
- **Method:** combined pair-counting / neighborhood-independence / anchored induction / spectral ceiling with explicit witness check

## Problem

For each n in {54,55,56}, prove a finite certified integer upper bound U(n) on ex_{C3,C4}(n), the maximum edges in an n-vertex graph of girth at least 5, via a combined replayable certificate (C4 pair-counting sharpened by triangle-free neighborhood independence, monotone induction anchored at exact a(53)=181, and a Nikiforov-type spectral ceiling, taking the minimum), and exhibit explicit girth>=5 witnesses with machine-checked edge counts meeting or beating the recorded lower bounds.

## Attempted claim

For each n in {54,55,56}, ex_{C3,C4}(n) <= U(n) for a stated finite integer U(n) at or below the best previously recorded (i.e., currently nonexistent) upper bound, proved by the combined certificate replayed from committed integer inputs, together with an explicit girth-at-least-5 graph on n vertices with machine-checked C4/C3-freeness and L(n) edges with L(54)>=185, L(55)>=189, L(56)>=193.

## Research outcome

Proved replay-verified girth>=5 extremal ceilings at n=54,55,56: unconditional Cauchy ceilings a(n)<=196/202/207 from a self-contained neighborhood-disjointness proof, tightened to 187/194/201 conditional on the published exact anchor a(53)=181 via monotone induction, plus explicit machine-checked C3/C4-free witnesses with 184/188/188 edges (1/1/5 short of recorded lower bounds 185/189/193, so no new lower bound claimed). verify.py replays all arithmetic and graph audits: VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: Strongest self-contained headline (unconditional 196/202/207; conditional 187/194/201; sub-record witnesses 184/188/188) is correct and narrowly new but not independently worth retrieving: textbook restatement + mere parameter substitution. Unconditional ceilings are direct substitution of n=54,55,56 into classical 4m^2<=n^2(n-1), reproducible by integer sqrt in seconds with no new method (research_report admits 'Method is classical; contribution is only the instantiated numeric ceilings'). Conditional ceilings are three integer divisions from the published anchor a(53)=181 via folklore averaging lemma, equally seconds-scale for any reader with the anchor. Witnesses at 184/188/188 fall short of already-recorded 185/189/193 by 1/1/5, so no new lower bound, no exact value, no structural claim; sub-record graphs have no retrieval need when better existence is already recorded. Target_claim promised L>=185/189/193 and audit-plan fallback required witnesses 'at least matching recorded lower bounds' — both unmet on the delivered artifacts. Remaining intervals ([185,187]/[189,194]/[193,201] conditional; wider unconditional) are loose one-sided textbook corollaries with no demonstrated downstream use requiring these precise loose numbers; 'Moore stability / LDPC benchmarks' is generic motivation, not a use of these widths. Exact-invariant carve-out does not rescue: result is not an exact invariant (loose upper bounds + sub-record witnesses), values ARE mechanically implied once anchor/formula known, and certification (VERIFY_OK) alone does not rescue a trivial instantiation. This is the 'correct and new but tiny unmotivated / parameter-substitution' rejection class.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Conditional ceilings depend on trusted external anchor a(53)=181 (OEIS A006856/McKay, not re-derived). Method (neighborhood-disjointness + Cauchy + deletion induction) is classical; contribution is only the instantiated numeric ceilings plus replay package, not a new method. Own witnesses fall short of recorded lower bounds 185/189/193; no exact values, no structural claims, no results outside n=54,55,56. Generic analytic families already implied some finite ceiling, so 'first finite' is NOT cl…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
