# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified Gram-spectrum and Gerzon-gap table for seven committed equiangular configurations in R^4-R^6 with one maximal-cardinality witness and one non-extendability exclusion
- **Round:** 2026-09-07-first-light-01
- **Lane:** 270
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Frame Theory
- **Method:** Gram-matrix positive-semidefinite verification with Gerzon/absolute-bound and angle-set replay

## Problem

From a committed bundle of 7 explicit unit-vector configurations in R^4, R^5, R^6 (6-8 configurations; at least one Gerzon-compared extremal candidate attaining the known maximal cardinality in its dimension and one two-distance near-miss with exactly two distinct off-diagonal |inner-product| values), recompute from scratch: (a) each Gram matrix G_ij=<v_i,v_j> by fresh inner-product evaluation, (b) its spectrum and exact/interval PSD certificate via LDL/Cholesky logs, (c) the common-angle value arccos(alpha) and full inner-product histogram, (d) Gerzon-bound n <= d(d+1)/2 and absolute-bound comparison with explicit gap log, (e) one maximal-cardinality witness via exhibited linear-independence/rank certificate meeting the known maximum for that (d,alpha) slot, and (f) one proven non-extendability exclusion: no additional unit vector extends the designated configuration while preserving its angle set.

## Attempted claim

The replayed table for the 7 committed configurations: each Gram spectrum certified PSD (min eigenvalue >= 0 exactly or by rigorous interval), each off-diagonal histogram tallied entrywise to a single |alpha| for equiangular members (two values for the near-miss), each Gerzon gap n vs d(d+1)/2 explicitly logged, PLUS (i) a maximal-cardinality witness: the designated configuration attains the known maximum for its (d,alpha) slot with a checked rank/independence certificate, and (ii) a non-extendability exclusion: the bordered-Gram PSD/angle feasibility for a (k+1)-st line fails by an auditable interval certificate.

## Research outcome

Certified 7-config Gram-spectrum/histogram/Gerzon-gap table in R^4-R^6 with exact PSD logs, three maximal-cardinality witnesses (N(4)=6, N(5)=10, N_{1/3}(6)=16), and a proved bordered-Gram non-extendability exclusion for C1; verifier replays VERIFY_OK.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Main 7-config table replays: VERIFY_OK reproduced; independent exact Fraction LDL with correct zero-block handling plus exact fraction-rank confirms all 7 PSD claims, ranks (4,4,5,5,6,6,4), stated pivots, histograms (C1-C6 single-|alpha|, C7 {0:12,1/2:16}) and Gerzon gaps (4,5,9,5,15,5,2) are arithmetically correct; relative-bound 16 at (6,1/3) correct. Maximality as 'attains known maximum' is arithmetically correct conditional on cited classical upper bounds (explicitly not re-proved). Section 4 exclusion proof as stated is FALSE in its certificate: DRAFT+script claim '20/64 bordered patterns PSD, all rank 5'. Independent correct PSD test (full-trailing-block zero check), exact rank, and float eigvalsh all agree the true PSD count is 10/64 (bits [1,6,10,20,24,39,43,53,57,62]), not 20. The 10 extra patterns (e.g. bits 7,11,17,21,30,33,42,46,52,56) have min eigenvalue approx -0.50 to -0.53 (indefinite) but candidate ldl_exact misclassifies them as PSD because its zero-pivot branch only checks row/col j instead of the whole trailing block. Final conclusion 'no 7th 1/3-line extends C1 in R4' remains true (0/64 with rank<=4 under both checkers, and also follows from cited N(4)=6), but the logged PSD enumeration and the soundness of the committed prover are wrong. This is an essential evidence defect. originality: No new claim/boundary. DRAFT Sec.5 admits no new upper bound is proved; C1 n=6=N(4), C4 n=10=N(5) appeal to cited van Lint-Seidel/Lemmens-Seidel maxima, and C6 n=16=relative bound at (6,1/3) is the same Clebsch witness already validated as SCOPE023 (N_{1/3}(6)=16 via Clebsch Gram exact LDL rank 6 + relative bound 16). The 7 Gram matrices are standard classical objects (simplexes, Petersen Seidel S=J-I-2A, Clebsch Cayley Seidel, Sylvester-Hadamard MUB pair); their spectra (e.g. C6 0x10/8x6, C4 0x5/6x5, simplex 0/5-6x), single-angle histograms and Gerzon subtractions are mechanically implied by routine exact arithmetic from those matrices, verified by recomputation. The C1 bordered exclusion (no 7th 1/3-line) is mechanically implied by the cited N(4)=6 itself and adds no new boundary. Nearest large-d/SDP priors (Jiang et al. 1907.12466 large-d N_alpha asymptotics; Greaves et al. 1403.2155 d=14,16 bounds; Barg-Yu 1311.3219 n>=24 SDP bounds) indeed lack this bundle, but the relevant low-d classical priors (cited maxima + standard Petersen/Clebsch/simplex/MUB constructions) already record the facts; grouping 7 known facts with fresh LDL logs is textbook/database recomputation, not a new result. A timestamp or failed search does not establish priority. value: Textbook restatement + mechanically implied enumeration, not an independently retrievable new fact. Objects are classical; invariants (LDL pivots in an arbitrary diagonal-pivoted order, float spectra, entrywise |.| tallies, Gerzon subtractions n vs d(d+1)/2) follow by routine arithmetic and are not shown to have been unknown or needed as a precise narrow datum (pivots are order-…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Maximality of the numbers N(4)=6, N(5)=10 appeals to cited classical Lemmens-Seidel/van Lint-Seidel bounds (no new upper-bound proof); C6 attains the relative bound 16, consistent with validated SCOPE023. No exhaustive optimality over all sign patterns for C4/C6. C7 is a two-distance near-miss, not equiangular. Float eigenvalues are cross-checks only; proofs are the exact Fraction LDL logs.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
