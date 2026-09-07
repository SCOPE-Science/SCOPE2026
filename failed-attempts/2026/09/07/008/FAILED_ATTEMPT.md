# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified ultra-flat Littlewood witness in degree 28: joint sup-norm and merit-factor record with reciprocal-symmetry sieving gap
- **Round:** 2026-09-07-first-light-01
- **Lane:** 8
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Number Theory
- **Method:** FFT-accelerated exhaustive sieving with exact algebraic norm verification

## Problem

Let L_28={P(z)=sum_{i=0}^{28} a_i z^i : a_i in {+1,-1}, a_0=+1} modulo G={P -> -P, P(z) -> z^28 P(1/z)} with lexicographically minimal canonical representative per orbit (134217728 orbits). Define M(P)=max_{|z|=1}|P(z)| and merit F(P)=29^2/(2*sum_{k=1}^{28} C_k^2) with C_k=sum_{i=0}^{28-k} a_i a_{i+k} in integers. Pin published records R28_sup,R28_F from Borwein-Choi/Mossinghoff table snapshot stored in audit/record_table.json. Problem: by FFT-prefiltered (16384/65536-grid) pruned sieving of the canonical space with exact integer-autocorrelation merit verification and Lipschitz-certified sup bounds (L=406), either produce an explicit canonical witness P28 with certified M(P28) <= R28_sup-0.03 or F(P28) >= R28_F+0.20 while the other metric is within 3% of its record, or certify a non-existence gap B28 such that min_{L_28} M >= B28 with B28 >= min(R28_sup,5.95) via exhaustive pruning logs.

## Attempted claim

Exhibit one explicit reciprocal-canonical P28 in {+1,-1}^29 (bitstring published) with machine-checkable certificate that either (A) certified sup M(P28) <= R28_sup-0.03 with merit F(P28) within 3% of R28_F, or (B) exact merit F(P28) >= R28_F+0.20 with certified sup within 3% of R28_sup, where R28_sup/R28_F are the pinned Borwein-Choi/Mossinghoff degree-28 records loaded at runtime; sup certification is dense-FFT-grid max plus Lipschitz remainder <=0.02 recomputed by verifier, merit is exact integer Fraction. Success strictly improves the published joint ultra-flat record for degree 28.

## Research outcome

Explicit reciprocal-canonical degree-28 Littlewood witness +---++++---+---+---+--+-++-++ with certified two-sided sup interval sqrt(45)<=M<=sqrt(45)+0.00487 (N=262144; +0.00122 at N=2^20) and exact merit 841/124≈6.7823; proves max merit over the full skew-symmetric subspace (16384 exhaustive integer scan) and upper/lower bounds min M<=6.7095, max F>=841/124. No published-record-beating claim (offline, records unpinned; no 134M sweep).

## Why this attempt failed

Failed axes: value.

value: Even taking correctness and certificate-novelty as given, the result is not independently worth finding later under SCOPE value filters. Target claim (topic.json) required a joint record-beater: certified M<=R28_sup-0.03 or F>=R28_F+0.20 with 3% non-regression vs pinned Borwein-Choi/Mossinghoff records. DRAFT §5(i) explicitly states this is 'unassessed, not achieved' (offline, records unpinned). Fallback required (a) certified complete census over canonical representatives (134M orbits) plus extension to degrees 24-27 and (b) certified non-existence gap B28>=min(R28_sup,5.95). Delivered is only a 16384-row skew census (0.012% of canonical space, 2^14 vs 2^28/2), no full sweep, no gap, no 24-27 extension. What IS delivered — single-witness one-sided bounds min_{L28}M<=6.7095 and max_{L28}F>=841/124 plus exact optimum over the tiny skew subspace — leaves global interval [5.385,6.7095] for min M wide (L2 lower bound sqrt(29)=5.385) with unknown distance to true optimum, and no record context to show 6.708/6.782 is globally good (random-polynomial sup ~9-10, random merit ~1, so better than random but unquantified vs optimum; heuristic non-beating searches are explicitly non-proofs). This collapses to a degree-28-specific single example (mere parameter instantiation) plus a <1s trivial enumeration (16384 integer sums) without theoretical insight, i.e. tiny unmotivated enumeration and textbook Lipschitz+autocorrelation exercise applied to one bitstring. A later researcher seeking flat polynomials would not cite this as a record, gap, or method; at most as one heuristic example among many. Hence correct and arguably new, but must be rejected per 'reject textbook restatements, mere parameter substitutions, tiny unmotivated gains, and unexplained enumerations even if correct and new.'

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No R28_sup/R28_F pinning (offline workspace; Borwein-Choi/Mossinghoff not live-verified) so joint record-beating criterion unassessed. No exhaustive 134M canonical sweep; no certified non-existence gap B28. Sup upper bound uses FFT doubles + 1e-6 margin, not interval arithmetic; exact equality M=sqrt(45) suggested by grids but unproved. Global optimality of P* in L28 conjectured only. Skew count 2^14 with a0=+1 (2^15 counting both signs) — terminology disambiguated in DRAFT.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
