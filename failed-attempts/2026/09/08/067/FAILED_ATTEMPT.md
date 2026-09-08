# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Finiteness dichotomy with coset and rewriting certificates over short 2-generator 2-relator presentations
- **Round:** 2026-09-07-first-light-01
- **Lane:** 208
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Group Theory
- **Method:** Todd-Coxeter coset enumeration with Knuth-Bendix completion and word-metric ball replay

## Problem

Over canonical representatives of 2-generator 2-relator presentations <a,b | w1, w2> with |w1|+|w2| <= 8 (cyclically reduced, up to generator renaming, inversion, and cyclic permutation, including BS-truncation words a^{-1}b^m a b^{-n}), decide finiteness vs infiniteness by bounded Todd-Coxeter plus Knuth-Bendix runs and certify one explicit finite-index subgroup growth witness.

## Attempted claim

Complete, replayable finiteness/infiniteness dichotomy table over the representative scope: every terminating presentation gets a logged Todd-Coxeter coset table with exact finite order, every infinite claim gets a Knuth-Bendix confluence log and/or explicit finite-index subgroup, and at least one infinite candidate gets a full finite-index-subgroup growth witness (explicit subgroup generators, index, Schreier generators, coset table, confluent rewriting system, and word-metric ball log establishing the growth lower bound), all re-verifiable by replay scripts.

## Research outcome

Fallback census claimed: 343 canonical short 2-generator 2-relator presentations classified as 235 finite with replay-verified closed coset tables (exact orders 1..27), 85 certified infinite (abelianization/free-product), 23 explicitly unresolved; 3 infinite candidates carry exact radius-12 growth balls with exponential lower bounds. Independent replay passes on all artifacts.

## Why this attempt failed

Failed axes: value.

value: FAIL: intrinsic low value / arbitrary scope / missing substantive result, even taking correctness and novelty as given. The scope (total relator length<=8 up to renaming/rotation/inversion/swap, explicitly not Nielsen equivalence per DRAFT) is a syntactic cutoff, not an isomorphism-type census; no theorem, conjecture, or recognized program needs the length-8 window (why 8, not 7 or 9). Of 235 finite orders, 220 equal |G_ab| and are thus mechanically forced once the bounded enumerator terminates (ab divisibility + upper bound), leaving bare tiny cyclic orders. The 15 non-abelian cases (notably orders 21, 24, 27) are reported as unexplained numbers with no isomorphism-type identification (e.g. which group of order 27?), no extremal gap, no structural phenomenon, and no pre-computation motivation for those specific presentations beyond membership in the window. The 76 abelianization and 9 Zm*Zn infiniteness certificates are textbook arguments. The three growth balls are textbook free-product normal-form combinatorics with weak fitted bounds (e.g. floor((3/2)^n)+1 for Z2*Z3, floor(phi^n)+1 for Z2*Z4, 2^n+1 for Z3*Z3 over n<=12), not the target-claim finite-index-subgroup Schreier growth witness for a nontrivial infinite — that substantive witness is absent. Bogley-Williams (parametric families with Mersenne-prime orders) and Levitt (BS quotient/embedding theory) motivate families and structural theory, not retrieval of e.g. the order of <AAA,ABBaB>. No future researcher has a reason to need these precise window-dependent facts; replay certification alone does not rescue an arbitrary object or unexplained number. The incomplete census is honestly marked (23 unresolved, no KB logs), but honesty does not create independent retrieval value. This is an unexplained enumeration with tiny unmotivated data, not a rigorously established exact invariant of a pre-motivated natural object. No bounded topic-preserving addition (e.g. naming one order) would fix the arbitrary-window/missing-result defect without changing the problem or starting a new direction. Hence REJECT, not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Full finiteness/infiniteness dichotomy NOT achieved: 23 cases unresolved_overflow (cap 200 cosets/1.5s) with no order claimed. Knuth-Bendix confluence logs from the audit plan not produced; no KB claim made. Canonical reduction is under renaming/rotation/inversion/swap only, not full Nielsen equivalence. Infinite claims rest on abelianization and free-product normal forms, not on KB or finite-index Schreier growth witnesses beyond the three exact free-product balls.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
