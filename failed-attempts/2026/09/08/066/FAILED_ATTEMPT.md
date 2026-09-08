# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Hadamard-equivalence census of maximal-determinant (+-1)-matrices at order n=10
- **Round:** 2026-09-07-first-light-01
- **Lane:** 198
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Matrix Theory
- **Method:** branch-and-bound Gram-determinant search with Hadamard/Ehlich-bound certification replay

## Problem

Determine, with exact replayable certificates, the complete Hadamard-equivalence classification of maximal-determinant (+-1)-matrices at order n=10: the exact number of inequivalent extremal classes, one exhibited sign matrix per class attaining the maximum absolute determinant 73728, Gram-determinant certificates, and a branch-and-bound plus Ehlich-bound optimality replay log.

## Attempted claim

At order n=10, the maximum absolute determinant over {+-1}-matrices is 73728, attained by exactly K Hadamard-equivalence classes (signed row/column permutations plus transpose); one explicit 10x10 sign matrix per class is exhibited with exact Gram-determinant certificate det(M M^T)=(det M)^2 and a branch-and-bound plus Ehlich-bound replay log certifying maximality.

## Research outcome

Fallback-plus claim: certified interval 73728<=D(10)<=99840 with two HT-inequivalent extremal witnesses at 73728, exact Gram certs, validated HT decider, stdlib-only full replay passing.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Determinant/interval subclaims verify: independent Fraction-exact Gaussian elimination gives det(W1)=det(W2)=73728; Gram dets re-derived entry-by-entry are 5435817984=73728^2; Lemma 3 (Hadamard, |det|^2<=10^10) and Lemma 4 (2^9=512 divisibility) proofs are sound and interval arithmetic (73728/512=144, 195*512=99840<=100000<99840+512) checks out; verify.py passes. BUT the draft's distinguishing headline inference (2c/2d) is FALSE: W1 and W2 ARE HT-equivalent. Root cause: hteq.py dephases (forcing row 0/col 0 to +1) then compares only the two transpose branches, i.e. it searches only the subgroup of HT-moves that preserve the distinguished row/column (up to transpose). A general HT-move can send any row/column to position 0, and dephase-signs then erase that choice, so completeness requires a further 10x10 (i0,j0) row/col pre-swap search before dephasing. Fuzzing proves incompleteness: genuine random full-HT images of W1 (e.g. seeds 1,2, transpose+arbitrary signed perms, inverse-recovery verified exact) are rejected by ht_equal (false negatives). The complete decider (transpose branch x i0 x j0 pre-swaps + dephase + deph_equal) returns EQUIVALENT for W1 vs W2 at (no-transpose, i0=0, j0=1), with an explicit checkable certificate: dephase(W1) is carried to dephase(colswap(W2,0,1)) by row perm [0,9,8,5,4,1,3,7,6,2] and col perm [0,2,6,3,1,5,4,8,9,7] entry-by-entry, and the signed lift to W1->W2 verifies over all 100 entries. Hence 'W1 vs W2 HT-inequivalent' and 'K_classes_at_max>=2' are refuted for these witnesses. The 'independent brute-force canonical-minimum over 9! column perms' crosscheck shares the same fixed-row0/col0 flaw (both branches differ only because the distinguishing pre-swap j0=1 was never tried) and therefore falsely corroborates. The positive/negative controls in verify.py pass only because the positive control fixes row 0 and column 0 (rows [0,3,1,...] keep 0 at position 0; cols [0,9,4,...] keep 0 at position 0), i.e. it tests inside the decider's limited subgroup. The fallback's promised 'proved Ehlich-bound lemma' is additionally absent (draft states no Ehlich formula is used; upper bound is Hadamard+divisibility only). An essential inference is false, so correctness FAILS despite correct determinant/interval parts. originality: No TRUE new item survives comparison with priors. True subclaims are anticipated: the value 73728 at n=10 is tabulated in OEIS A003433 (b-file: n=10 -> 73728; values proved through n=22); the Hadamard bound n^(n/2) and the 2^(n-1) divisibility argument are classical textbook material (Hadamard 1893; Williamson 1946 relation a(n)=2^(n-1)g(n-1)); the Gram identity det(M M^T)=(det M)^2 is a tautology recomputed, not a finding. The purported novelty (two HT-inequivalent maximizers at n=10, i.e. a partial-census step with K>=2) is false for the exhibited pair, so it contributes no priority; a timestamp or a failed search does not establish priority. Substantive nearest priors structure exactly th…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Optimality of 73728 (D(10)=73728) is not proved -- interval top is 99840; the value match with OEIS A003433 is background, not evidence. Exact census count K is not determined; only >=2 classes attaining 73728 certified. No claim about further classes. A recalled Ehlich closed form was tested, found inconsistent with proved a(22), and discarded. Search code that found witnesses used numpy floats for guidance only; floats never enter certificates.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
