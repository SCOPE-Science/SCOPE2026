# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Shifting-monotone variance stability lemma for C4-free near-extremals with below-record upper bounds at open orders
- **Round:** 2026-09-07-first-light-01
- **Lane:** 253
- **Disposition:** NO_RESULT
- **Domain:** Extremal Combinatorics
- **Method:** shifting-monotone degree-variance-capped Kovari-Sos-Turan inequality with monotone induction

## Problem

Prove a quantitative shifting-monotone degree-variance stability lemma for C4-free near-extremal graphs and apply it, via monotone induction from the exact base a(40)=127, to narrow genuinely open C4-extremal intervals: explicit improved upper bounds strictly below the recorded maxima at two orders in 41..49.

## Attempted claim

Stability lemma: every C4-free graph on n vertices with m edges near the KST pair-count ceiling satisfies an explicit shifting-monotone degree-variance cap V(n,m). Corollaries: improved upper bounds ex(42,C4)<=138 (recorded <=139) and ex(43,C4)<=144 (recorded <=145), each proved by the lemma combined with the monotone induction a(n)<=floor(a(n-1)*n/(n-2)) anchored at exact a(40)=127, with all arithmetic replayable from committed integer inputs.

## Research outcome

Target route fails on three verified grounds. (1) Chain audit: recorded induction 127->133->139->145 replays byte-exact, and yields ex(42)<=138 iff ex(41)<=132, i.e. it needs the open width-one exact decision. (2) Degree-cap non-exclusion: balanced graphic sequences (Erdos-Gallai checked) at (41,133),(42,139),(43,145) satisfy sum-to-2m, KST pair-count with slack 66-85, and variance far below the KST-implied cap V, so no variance/pair-count cap excludes the targets. (3) Shifting unsound: explicit 6-vertex C4-free graph whose standard S_01 shift contains a C4 (exhaustive 2^15 check). Hence neither the two-order claim (138/144) nor the single-order fallback is provable by this lemma+chain route. No verified new upper bound obtained.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No strict improvement over recorded maxima (133/139/145) was proved; ex(41) decision remains open. Negative findings are route-specific barriers, not lower bounds or exact values: (a) degree-cap non-exclusion does not exhibit any C4-free graph with 133/139/145 edges; (b) shifting counterexample is on 6 vertices and only refutes the shifting-monotonicity step, not the numerical bounds themselves; (c) no polarity-subgraph search or exhaustive elimination was attempted. All positive statements are classical re-derivations (KST, convexity floor, recorded induction), claimed only as verified background, not as original results.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No strict improvement over recorded maxima (133/139/145) was proved; ex(41) decision remains open. Negative findings are route-specific barriers, not lower bounds or exact values: (a) degree-cap non-exclusion does not exhibit any C4-free graph with 133/139/145 edges; (b) shifting counterexample is on 6 vertices and only refutes the shifting-monotonicity step, not the numerical bounds themselves; (c) no polarity-subgraph search or exhaustive elimination was attempted. All positive statements are…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
