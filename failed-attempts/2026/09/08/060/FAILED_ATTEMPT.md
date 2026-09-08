# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Replayable isotopy census of Latin squares of order 7 with transversal numbers and orthogonal-mate witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 195
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Design Theory
- **Method:** exact-cover DLX search with canonical isotopy labeling replay

## Problem

Produce a replayable isotopy census of Latin squares of order 7 (with sampled order-8 extension): regenerate representatives by DLX exact-cover search, certify isotopy-class distinctness via canonical labeling transcripts, tabulate transversal number and orthogonal-mate existence per class, and exhibit at least one maximal-transversal witness and one orthogonal (Graeco-Latin) pair witness as explicit symbol arrays with replay logs.

## Attempted claim

Complete replayable isotopy census of Latin squares of order 7 via DLX exact-cover regeneration with canonical isotopy transcripts, tabulated transversal number and orthogonal-mate count per isotopy class, exhibiting at least one maximal-transversal witness and one orthogonal Graeco-Latin pair witness as explicit arrays with independently replayable verification logs.

## Research outcome

Certified transversal-count and orthogonal-mate table for the complete group-isomorphism-type stratum: cyclic order-7 table (T=133, mate) and all five order-8 group tables (cyclic C8 T=0/tau=7/no mate; C4xC2, C2^3, D8, Q8 each T=384 with explicit mates), all rebuilt from group laws and verified by a 40-check stdlib-only replay script. Partial theorem toward the order-7 isotopy census topic; full 147/564-class census explicitly not claimed.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline numbers and existence claims are prior published / textbook-implied, not new. OEIS A090741 (Maximum number of transversals) lists a(7)=133 and a(8)=384 with explicit comment that a(7) is from the Z7 group table and a(8) is from the non-cyclic groups of order 8 (see Bedford). Cited reference D. Bedford (1991) 'Transversals in the Cayley tables of the non-cyclic groups of order 8' is exactly the order-8 non-cyclic table the DRAFT recomputes. T=0 for cyclic even order is the well-known transversal-free cyclic principle the DRAFT itself concedes as known. Orthogonal-mate existence for these groups is mechanically implied by the Hall-Paige complete-mapping condition (Sylow 2-subgroups trivial or noncyclic; cyclic C8 fails, all others pass), proved in full by 2009; the B7[i][j]=2i+j mate for odd cyclic and the GF(8) mate for C2^3 are standard constructions. The remaining DFS-found mates are arbitrary explicit instances of a known-existence fact, not a new invariant. The DRAFT's own Section 7 states novelty is only 'the combined certified table + replayable witnesses, not in the well-known group classification or the known principle.' Re-running known counts with a new script plus explicit witness arrays is database recomputation / textbook restatement, not a substantive new claim. The demanded 147/564-class transversal/orthogonality census is explicitly not delivered. value: Even taken as correct, the 6-table group-stratum benchmark is not independently worth retrieving later. It repeats the prior SCOPE-FAIL-20260907-034 arbitrary-slice defect: 1 cyclic order-7 table plus 5 order-8 group tables instead of the admitted headline scope (full order-7 isotopy census) or even the topic fallback (147-class lower-bound table + Graeco-Latin witnesses). The exact values (133/0/384, tau, mate yes/no) are already citable from A090741/Bedford/Hall-Paige and need no new lookup; a future researcher calibrating Ryser-Brualdi-Stein or solver testing gains nothing beyond what those sources plus McKay representatives already give. The narrow-datum exception does not apply because the values were known before computation and are mechanically implied by published theorems, and the explicit mate arrays are arbitrary among many with no pre-computation motivation or canonical identity. Certification/replayability alone does not rescue an arbitrary slice or an explained-but-known number per the audit standard.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial stratum only (6 canonical group tables), not the full 147 main-class / 564 isotopy-class order-7 census. Counts are exact for these squares; no claim about non-group-based classes. Group classification itself is classical; novelty is the combined certified table plus replayable witnesses.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
