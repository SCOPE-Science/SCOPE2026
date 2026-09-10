# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Bounded-coefficient Cutting Planes length threshold for Tseitin on the 60-vertex LPS Ramanujan expander via Prover-Delayer lifting
- **Round:** 2026-09-07-first-light-01
- **Lane:** 490
- **Disposition:** NO_RESULT
- **Domain:** Proof Complexity
- **Method:** communication-complexity lifting with expander isoperimetry and Prover-Delayer plus feasible-interpolation comparison

## Problem

Fix the explicit 3-regular Ramanujan graph G=LPS(2,5) on 60 vertices with a fixed odd charge tau_odd. Transfer its certified vertex-isoperimetric profile to a bounded-coefficient Cutting Planes length threshold for the Tseitin contradiction T(G,tau_odd) via one Prover-Delayer Resolution-width step plus one feasible-interpolation clause-count conversion, or isolate one short CP* upper-bound refutation as a lifting-tightness witness.

## Attempted claim

Every Cutting Planes refutation of T(T(G,tau_odd)) with all coefficients bounded in absolute value by 60^3 (CP* regime) requires length at least 4096 = 2^12, shown by chaining (i) the certified vertex-expansion profile of G=LPS(2,5), (ii) a logged Delayer strategy forcing Resolution width >=9, and (iii) one stated lifting-plus-feasible-interpolation conversion with explicit constants; a single CP* refutation with <=4095 lines counts as a tightness witness disproving the threshold.

## Research outcome

Target chain broken with replayable evidence: concrete 60-vertex 3-regular Ramanujan instance certified (lambda*=2.732051<=2sqrt2, trA^2=180), Tseitin params fixed (90 vars, 240 width-3 clauses), exact small-set boundaries computed, but the constructed Delayer provably scores only 4 against an explicit 5-query trap order on all 90 edges (below the required 9), and standard width-to-length conversion cannot reach 4096 from width 9 (BSW gives ~1.03; 2^9=512). No fallback or emergent claim met the auditable value bar. Artifacts replay via verify.py -> VERIFY_OK.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Naive Delayer R defeated by uniform 5-query edge-trap (score 4 < 9 on all 90 edges); BSW conversion width-9 -> ~1.03, far from 4096 (needs width >= ~112); textbook LPS(2,5) quotient identity ambiguous ((2/5)=-1); no bound on true game value, Resolution width, or CP* length; no short refutation exhibited.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Naive Delayer R defeated by uniform 5-query edge-trap (score 4 < 9 on all 90 edges); BSW conversion width-9 -> ~1.03, far from 4096 (needs width >= ~112); textbook LPS(2,5) quotient identity ambiguous ((2/5)=-1); no bound on true game value, Resolution width, or CP* length; no short refutation exhibited.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
