# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Distance-optimal binary linear [n,k] codes for n=20-24, k=7-12: generator witnesses with weight-enumerator certificates
- **Round:** 2026-09-07-first-light-01
- **Lane:** 59
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Coding Theory
- **Method:** monomial-equivalence canonical reduction with Griesmer-bound pruning and exhaustive weight-enumeration replay

## Problem

For each of the 30 pairs (n,k) with n in {20,21,22,23,24} and k in {7,8,9,10,11,12}, determine d*(n,k) = max minimum distance over binary linear [n,k] codes by enumerating generator matrices up to monomial (permutation plus column-scaling, trivial over GF(2)) equivalence via canonical column-multiset reduction, pruned by Griesmer and Plotkin bounds, with exact d and full weight enumerator per class by exhaustive 2^k enumeration.

## Attempted claim

For every (n,k) in n=20-24 x k=7-12, exhibit one binary k x n generator matrix G_{n,k} in systematic form achieving distance d*(n,k) equal to the Grassl BKLC upper bound, with optimality certified by exhaustive monomial-canonical search with Griesmer/Plotkin pruning logs, plus the exact full weight enumerator W_{n,k}(z) verified by exhaustive codeword enumeration and an independent syndrome-based replay script.

## Research outcome

Independent certified reproduction for all 30 binary [n,k] cells (n=20-24 x k=7-12): one explicit full-support systematic generator per cell attaining the Grassl BKLC optimum d*, with exact distance and full weight enumerator proved by exhaustive 2^k enumeration and an independent stdlib-only replay (30/30 PASS), plus derivation-containment audit against three verified parents and recomputed Griesmer bounds. No new distance records claimed; distances coincide with Brouwer/Grassl.

## Why this attempt failed

Failed axes: originality, value.

originality: Live retrieval decisively anticipates the mathematical facts claimed. DRAFT itself states optimal distances are NOT new and coincide with Brouwer/Grassl tables (LB=UB in all 30 cells). Live inspection confirms: (1) Grassl [24,12] page gives LB=UB=8 via QR with Griesmer UB, anticipating P1 Golay distance and optimality; (2) Grassl [20,10] page gives full construction chain [23,14,5] Wa stored matrix -> extend to [24,14,6] -> shorten to [20,10,6] with UB via one-step Griesmer, and its 14x23 stored matrix is byte-identical to DRAFT P2 rows (e.g. row1 10000000000010000101101), anticipating both distance and derivation route; (3) Grassl [23,7] page gives LB=UB=9 HP with stored 7x23 matrix byte-identical to DRAFT P3, anticipating parent; (4) Grassl [20,8] and [21,9] pages give LB=UB=8 via shortening of Golay [24,12,8], anticipating DRAFT routes for those cells; (5) Golay enumerators reproduced exactly are classical MacWilliams-Sloane facts (extended Golay and punctured [23,12,7] perfect Golay distributions), not new; (6) Griesmer/shortening/puncturing/subcode monotonicity is textbook (Helgert-Stinaff 1973; MacWilliams-Sloane). The only byte-novel data are weight enumerators of arbitrarily resampled subcodes (seed 20260907, e.g. [20,7] subcode of [20,8], [22,7/8/9] subcodes of [22,10]) which DRAFT admits are not cell invariants and vary with random choice, so they constitute no new mathematical fact about (n,k) strata. No timestamp, memory, or failed search was used to establish priority; live pages establish prior disclosure since 2001-2007. Hence no substantively new object, bound, construction, or invariant: originality FAIL. value: Even taking correctness as given, the result is not independently worth finding later. It falls into multiple reject categories: (a) Textbook restatement: shortening the extended Golay [24,12,8], extending/parity-checking Wagner [23,14,5] and Hashim-Pozdniakov [23,7,9], and applying Griesmer/Plotkin bounds are standard exercises in MacWilliams-Sloane Chapter 1, already documented cell-by-cell on codetables.de with identical chains. (b) Mere parameter substitution: the 30-cell grid n=20-24 x k=7-12 varies length/dimension by 1 with the same shortening/subcode recipe, no new phenomenon, threshold, or structural insight, and no distance beats the 2007 Brouwer table. (c) Unexplained enumeration: full weight enumerators for random seed-dependent subcode representatives (explicitly not canonical, other optima in same cell differ) have no interpretation, no downstream use, and no comparison; listing them for 30 cells is an arbitrary census, not a motivated invariant. (d) No method advance: exhaustive 2^k enumeration for k<=12 is trivial Hamming-weight counting; the promised monomial-equivalence canonical reduction with exhaustive search was abandoned as infeasible, leaving no reusable technique. The bundle is a correct reproduction/certificate of 20-year-old table values, useful at most as a classroom replay, not a…

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Optimality for 15/30 non-Griesmer-tight cells is conditional on Brouwer upper-bound proofs cited from Grassl pages, not re-derived here.', 'No exhaustive enumeration over monomial-equivalence classes was attempted (search space infeasible); the audit-plan brute-force route was replaced by constructive derivation, openly disclosed.', 'Weight enumerators are properties of our chosen representatives, not canonical cell invariants; other optimal codes in the same cell may have different enumerato…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
