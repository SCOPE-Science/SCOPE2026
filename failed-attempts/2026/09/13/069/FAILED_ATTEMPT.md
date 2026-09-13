# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Type-3 Wilf gap 3 for multiplicity-6 semigroups
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1616
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** numerical semigroups
- **Method:** type-3 faces of the Kunz polyhedron P_6 and Apery poset maxima

## Problem

Let S be a numerical semigroup of multiplicity m(S) = 6 with Cohen-Macaulay type t(S) = 3, where t(S) is the number of pseudo-Frobenius numbers of S, equivalently the number of maximal elements of Ap(S,6) = {0,w1,...,w5}, wi = 6 ki + i, under the order x precedes_S y iff y - x is in S. Let e(S) be the embedding dimension, c(S) the conductor, n(S) = |S intersect [0, c(S)-1]|, and Wilf number W(S) = e(S) n(S) - c(S). Prove or disprove that every numerical semigroup S with m(S) = 6 and t(S) = 3 satisfies W(S) at least 3. The parameter scope is all Kunz 5-tuples (k1,...,k5) in the Kunz polyhedron P_6 whose Apery poset has exactly three maximal elements. A complete answer is either a proof of the type-conditioned gap W at least 3 covering all such tuples via the type-3 faces of P_6, or an explicit semigroup S* with m(S*) = 6 and t(S*) = 3, given by its minimal generators, its Ap(S*,6) with identified maximal elements and pseudo-Frobenius numbers, and computed (e,c,n,W) with W(S*) at most 2.

## Attempted claim

Let S be a numerical semigroup of multiplicity m(S) = 6 with Cohen-Macaulay type t(S) = 3, where t(S) is the number of pseudo-Frobenius numbers of S, equivalently the number of maximal elements of Ap(S,6) = {0,w1,...,w5}, wi = 6 ki + i, under the order x precedes_S y iff y - x is in S. Let e(S) be the embedding dimension, c(S) the conductor, n(S) = |S intersect [0, c(S)-1]|, and Wilf number W(S) = e(S) n(S) - c(S). Prove or disprove that every numerical semigroup S with m(S) = 6 and t(S) = 3 satisfies W(S) at least 3. The parameter scope is all Kunz 5-tuples (k1,...,k5) in the Kunz polyhedron P_6 whose Apery poset has exactly three maximal elements. A complete answer is either a proof of the type-conditioned gap W at least 3 covering all such tuples via the type-3 faces of P_6, or an explicit semigroup S* with m(S*) = 6 and t(S*) = 3, given by its minimal generators, its Ap(S*,6) with identified maximal elements and pseudo-Frobenius numbers, and computed (e,c,n,W) with W(S*) at most 2.

## Research outcome

Proved the type-conditioned Wilf gap: every numerical semigroup with multiplicity 6 and type 3 satisfies W(S)>=3, via exhaustive exactly-certified enumeration of all 29700 refined cells.

## Why this attempt failed

Failed axes: correctness.

correctness: FAIL: a systematic sign error in the strict non-comparability encoding invalidates the entire certificate corpus. For q<p the positive Apery-order criterion is (k_q-k_p-k_d>=1), whose exact integer negation is (<=0); but rowsutil.rows/sysrows and DRAFT.md impose (<=-2), i.e. RHS -1-off instead of off-1. Submitted cells are therefore strict subsets of the true cells. Independent exact replication of rows(): the genuine type-3 semigroup k=(1,1,2,1,1) with true maxima (3,4,5) lies in 0 of the 29700 submitted cells (e.g. pair (4,2): code demands -1<=-2, false, while true maximality holds), and 487 of the 690 box type-3 tuples fail the submitted strict rows. run_verify.py/run_verify_e5.py pass only because they check internal consistency with the wrong rows, and coverage.py never checks strict rows, so neither detects the hole. All 214 bound, 15 branch-tree, 29471 infeasibility and 800 Lemma-A certificates certify the wrong regions and do not establish W>=3. Route is TARGET with the exact admitted claim; the defect is in research execution, not an ADMISSION_DEFECT.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The certificate set is computer-generated (rational Farkas/duality data found via CBC, then independently verified in exact arithmetic); human readability of individual certificates varies though the two weak families also admit short hand proofs given in DRAFT.md. Sharpness: computed minimum over searched boxes is W=4, so the proved gap 3 has one unit of slack and no extremal semigroup attaining W=3 is exhibited.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
