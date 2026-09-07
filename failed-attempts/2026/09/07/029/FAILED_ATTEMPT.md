# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact toroidal queen domination for the 11x11 wrap-around board via symmetry-broken SAT
- **Round:** 2026-09-07-first-light-01
- **Lane:** 46
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Games
- **Method:** symmetry-broken SAT-based domination search with board-automorphism reduction and neighbourhood-coverage verification

## Problem

Determine the exact toroidal queen domination number gamma_T(11) for the 11x11 board T_11 = Z_11 x Z_11 where a queen on (x,y) attacks its row, column, and both diagonals modulo 11. Deliver: (i) explicit dominating-set witness coordinates for the optimum k, (ii) full 121-cell attack-coverage table under wrap-around diagonals stating covering queen and line type per cell, and (iii) symmetry-broken SAT unsatisfiability certificate (DRAT log) for k-1 queens using toroidal-automorphism reduction (translations x D4, order 968), all rerunnable in minutes.

## Attempted claim

Close the 11x11 toroidal stratum: exhibit an explicit 4-queen set dominating all 121 cells of T_11 under modulo-11 rows/columns/diagonals and a machine-checkable SAT UNSAT proof that no 3 toroidal queens dominate, hence gamma_T(11)=4. If search instead finds a 3-dominating set, the symmetric success criterion is a verified 3-witness plus UNSAT for k=2, hence gamma_T(11)=3; either way the stratum is closed exactly with witness + coverage table + DRAT log.

## Research outcome

Closed the 11x11 toroidal queen domination stratum exactly: gamma_T(11)=5 with explicit 5-witness, full 121-cell coverage table, and translation-reduced exhaustive UNSAT for k=3 (7140 sets, max 92) and k=4 (280840 sets, max 108), replayable in <1s stdlib-only. Counting bound gives k>=3; enumeration lifts to k>=5.

## Why this attempt failed

Failed axes: value.

value: FAIL: single-stratum n=11 exact number by 0.17s trivial exhaustive search is a mere parameter substitution and unexplained enumeration, not independently worth finding later. Method (neighbourhood size 4n-3 for odd n, translation reduction to C(n^2-1,k-1), bitmask enumeration) is generic for any n and textbook group action; no new encoding, canonicalization beyond fixing (0,0), structural theorem, classification, uniqueness/census of 5-dominators (explicitly disclaimed), frequency table, or general gamma_T(n) formula is given. Optimality rests solely on 'checked 280840 cases, none dominate, max 108' without structural reason why 4 insufficient beyond overlap observation (~12 per pair). Result is trivially recomputable by anyone in <1s, so archival value is minimal. Equals long-known planar gamma(11)=5 (Bozoki et al.), so hoped-for planar/toroidal separation does not occur; contribution is one data point coinciding with planar value, not a separation or general bound. Analogous single-parameter SAT+DRAT exact number RT(30,K4,6) was previously AUDIT_REJECT on value despite heavier machinery; this 280k brute-force single number is thinner. Closing one n in infinite family gamma_T(n) without table for 9-12, without general insight, and without hard-to-reproduce artefact falls under 'mere parameter substitution / unexplained enumeration even if correct and new' and 'tiny unmotivated gain'. Correct and new, but not worth finding later as standalone finding.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Single stratum n=11 only; no general gamma_T(n) formula. Optimality via translation-reduced brute force (280840 cases), not DRAT/SAT log. No census/uniqueness of 5-dominators. Correctness depends on hand proof of translation invariance plus stdlib itertools and mod-11 line generation (two code paths agree). Value equals planar gamma(11)=5, so no planar/toroidal separation at n=11.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
