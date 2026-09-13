# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Single-deletion freeness of cone extended Shi type B
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1737
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** hyperplane arrangements
- **Method:** addition-deletion triple and Saito/characteristic-polynomial check

## Problem

Let l with 3<=l<=6 and integer k>=1, with cShi(B_l,k) the cone in C^{l+1} of the type-B extended Shi arrangement with translates m in {-k+1,...,k} for x_i, x_i-x_j, x_i+x_j plus z=0. For each single-hyperplane deletion D=cShi(B_l,k)\{H} where H runs over W(B_l)-orbit representatives (coordinate type x_1=0 or m z, difference type x_1-x_2=m z, sum type x_1+x_2=m z, and infinite type z=0), decide whether D is free, compute its characteristic polynomial chi(D,t), and decide whether chi(D,t) factors as a product of linear terms (t-d_i) over Z with the d_i equal to the derivation exponents when free. A complete answer covers all orbit representatives for 3<=l<=6 and all k>=1, proved by an addition-deletion triple exact sequence and Saito-criterion check when free, or by a proven non-factorization/non-freeness obstruction when not free.

## Attempted claim

Let l with 3<=l<=6 and integer k>=1, with cShi(B_l,k) the cone in C^{l+1} of the type-B extended Shi arrangement with translates m in {-k+1,...,k} for x_i, x_i-x_j, x_i+x_j plus z=0. For each single-hyperplane deletion D=cShi(B_l,k)\{H} where H runs over W(B_l)-orbit representatives (coordinate type x_1=0 or m z, difference type x_1-x_2=m z, sum type x_1+x_2=m z, and infinite type z=0), decide whether D is free, compute its characteristic polynomial chi(D,t), and decide whether chi(D,t) factors as a product of linear terms (t-d_i) over Z with the d_i equal to the derivation exponents when free. A complete answer covers all orbit representatives for 3<=l<=6 and all k>=1, proved by an addition-deletion triple exact sequence and Saito-criterion check when free, or by a proven non-factorization/non-freeness obstruction when not free.

## Research outcome

Certified single-deletion chi table for cone extended Shi type B on six (l,k) blocks over 6k+1 S_l orbit representatives: only the two extreme representatives split; 72 others proved non-free via non-factorization, lifted to all hyperplanes by the coordinate-permutation lemma.

## Why this attempt failed

Failed axes: correctness.

correctness: Independently re-verified the 84-row computational core: all 12 SPLIT identities (t-1)(t-b)^(l-1)(t-b+1) hold symbolically; all 72 NON_SPLIT rows carry valid divisor-exhaustion certificates (66 kind-A, 6 kind-B; nonzero constants; SymPy Z-factor lists confirm no linear factor); spot recomputation with chi_count.py reproduces the full-arrangement formula and deletion fits; the Terao non-freeness direction is valid. FATAL DEFECT: the S_l symmetry lemma (DRAFT 1bis) is FALSE. Counterexample: in cShi(B_3,2) with S={-1,0,1,2}, the swap x1<->x2 sends H={x1-x2=2z} in A to {x1-x2=-2z}, not in A since -2 is not in S (verified: permuted set differs with |B-A|=1). Position dependence confirmed numerically (deleting x1-x3=2z vs x1-x2=2z differs at p=29: 146132 vs 145656). Hence the 6k+1 reps do NOT determine chi/freeness for all 2kl^2+1 hyperplanes, and all 'hence for every H' and l(l-1) count claims are unproven as stated.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The theorem covers only (l,k) in {(3,1),(3,2),(3,3),(3,4),(4,1),(4,2)} and directly computes the 6k+1 S_l orbit representatives per block (x1, x1-x2, x1+x2 translates plus z=0), lifting to all 2kl^2+1 hyperplanes only via the S_l symmetry lemma of DRAFT section 1bis; the S_l statement is not a full W(B_l)-orbit statement and the sign flip x1-x2=kz versus x1+x2=kz is an explicit counterexample; freeness of the 12 splitting representative rows is not claimed since Terao theorem has no converse an…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
