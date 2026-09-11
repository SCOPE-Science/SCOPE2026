# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Transversal T no-go for the named [[8,2,3]] stabilizer code
- **Round:** 2026-09-07-first-light-01
- **Lane:** 974
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** Quantum Information Theory
- **Method:** Shor-Laflamme MacWilliams enumerator divisibility with Clifford-hierarchy criterion

## Problem

Let C8 be the LC-permutation representative [[8,2,3]] stabilizer code from the Cross-Vandeth n<=9 census with distance verified by its Shor-Laflamme enumerator in the hour. Decide whether strictly transversal T^{otimes 8}, up to per-qubit single-qubit Clifford corrections in Bravyi-Haah form, preserves the C8 codespace and implements a logical T on a logical qubit, or else prove an enumerator-divisibility plus hierarchy-level no-go with an explicit magic-gap witness.

## Attempted claim

No strictly transversal physical operator of the form (tensor over i=1..8 of Ci Ti) with Ti = T or T-dagger and Ci single-qubit Clifford preserves the C8 codespace and acts as a logical T on either logical qubit; the obstruction is a Shor-Laflamme weight-divisibility condition together with a Clifford-hierarchy level constraint, witnessed by an explicit magic-monotone gap.

## Research outcome

Proved transversal-T no-go for an explicit [[8,2,3]] code: fixed tableau, verified enumerators and distance 3, global-projector mismatch lemma eliminating all 6561 Clifford frames with leakage witness (branch fraction >= 2^-4); verifier prints VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: topic.audit_preflight target_integrity required the LC-permutation Cross-Vandeth census representative, but DRAFT Sec.5 openly discloses LC-permutation equivalence of the submitted random-search C8 tableau to that representative is unproven. Hence the proved object lacks the admitted pre-motivated natural identity, canonical census ID, and literature position; a future researcher cannot retrieve it as the named benchmark. The quantitative witness is per-branch Hilbert-Schmidt leakage 2^{-m}, not the admitted magic monotone (extent/robustness). Under STANDARD, certification/replay alone does not rescue an arbitrary object or unexplained tableau; a narrow exact invariant is valuable only when object+invariant were motivated before computation. Value therefore FAILS pending bounded identity repair.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: LC-permutation equivalence of the fixed C8 code to the named Cross-Vandeth census representative is unproven and disclosed; the no-go covers the stated Bravyi-Haah ansatz class (per-qubit Ci T^{s_i} in either ordering, no permutations or measurements) and proves codespace non-preservation, making logical action vacuous; the magic-gap witness is a codespace-leakage floor (branch weight fraction 2^-m >= 2^-4 on every frame, >= 2^-1 on 648 m=1 frames) rather than a named resource-monotone value su…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
