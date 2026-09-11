# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit size-depth tradeoff for Tseitin on the LPS(5,q) Ramanujan family via restriction bottleneck and interpolation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 692
- **Disposition:** NO_RESULT
- **Domain:** Proof Complexity
- **Method:** random-restriction bottleneck counting with feasible-interpolation transfer from circuit lower bounds

## Problem

Fix the explicit 6-regular LPS Ramanujan family G_q=X^{5,q} and odd-charge Tseitin formulas T(G_q). Prove a new resolution size-depth tradeoff with explicit constants via a random-restriction width bottleneck transferred to depth through feasible interpolation — or refute the conjectured tradeoff by exhibiting a short narrow refutation trace.

## Attempted claim

For G_q = LPS X^{5,q} (6-regular Ramanujan, n=q(q^2-1)/2 vertices, q prime =1 mod 4, q != 5) with any odd charge, every resolution refutation Pi of Tseitin(G_q) satisfies log2 S(Pi) + D(Pi)/100 >= n/200, where S is size (number of clauses) and D is depth.

## Research outcome

Target size-depth inequality log2 S+D/100>=n/200 for Tseitin on LPS X^{5,q} is BLOCKED with quantified constant shortfall (closed bound 0.00390 vs required 0.005 per-n; need_beta 0.288 vs proved 0.2546). Preset fallback P_{1/2}[width>=n/40]>=1-exp(-n/100) was attempted via three bounded analytic routes (Chernoff+union, Karger, matrix Bernstein) and is BLOCKED (15.5x entropy gap; others vacuous). Scripts log both blocks. No independently valuable original increment; CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Target constant 1/200 exceeds closed BSW+Cheeger certification (0.00390 per-n, 22% shortfall) at every family member; optimistic 4N denominator unproven.', 'Fallback union-bound entropy exceeds per-set Chernoff tail by 15.5x; Karger/Bernstein structurally vacuous at linear thresholds.', 'Width fragment w>=(3-sqrt(5))n/3 is routine textbook combination, not independently valuable; no emergent finding claimed.', 'LPS Ramanujan expansion used as black box; no independent expansion certificate computed.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Target constant 1/200 exceeds closed BSW+Cheeger certification (0.00390 per-n, 22% shortfall) at every family member; optimistic 4N denominator unproven.', 'Fallback union-bound entropy exceeds per-set Chernoff tail by 15.5x; Karger/Bernstein structurally vacuous at linear thresholds.', 'Width fragment w>=(3-sqrt(5))n/3 is routine textbook combination, not independently valuable; no emergent finding claimed.', 'LPS Ramanujan expansion used as black box; no independent expansion certificate co…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
