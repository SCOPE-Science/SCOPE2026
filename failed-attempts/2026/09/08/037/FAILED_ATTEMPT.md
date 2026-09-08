# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Wilf-class census for length-4 pattern pairs at n=9-12 with a collapse bijection and a growth-rate separation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 133
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Combinatorics
- **Method:** insertion-encoding transfer-matrix enumeration with exact backtracking and bijective replay

## Problem

Complete the Wilf-class census for symmetry-reduced unordered pairs of length-4 patterns at lengths n=9,10,11,12: compute exact avoidance counts, exhibit one explicit Wilf-collapse bijection, and prove one growth-rate separation interval.

## Attempted claim

For the symmetry-reduced set of unordered pairs of length-4 patterns, the exact counts |S_n(P)| for n=9,10,11,12 partition the pairs into the stated Wilf-classes (table committed by Research); at least one non-symmetry Wilf-collapse is proved by an explicit bijection verified on all counted permutations through n=12, and at least one pair of classes is proved to have separated growth by a disjoint interval: an insertion-encoding upper bound U for one class and an explicit-construction-family lower bound L>U for the other, both replayable from committed logs.

## Research outcome

Resumed empty lane; reconstructed and re-verified the full 56-class symmetry-reduced census of unordered length-4 pattern pairs at n=9..12 (224 exact counts) with two-method agreement, proved Erdos-Szekeres finiteness with the exact n=9 RSK count 1764 and a Catalan separation interval {0} vs [208012,inf) at n=12, and documented the stable empirical Wilf-grouping as conjecture only. Artifacts and DRAFT.md written.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Symmetry partition verified independently: 56 pair-classes covering 276 unordered distinct pairs, all reps lex-min (recomputed orbits match). Theorem 1 (Erdos-Szekeres finiteness of Av(1234,4321), n=9 count 1764=42^2) is correct: ES bound (4-1)(4-1)+1=10 gives emptiness for n>=10; RSK+hook-length verified (hooks 5,4,3,4,3,2,3,2,1 product 8640, 9!/8640=42, 42^2=1764; partitions of 9 fitting 3x3 admit only (3,3,3) so theory alone predicts 1764; enumerator and stdlib verifier agree Av_8=1764). DRAFT table internally consistent with counts_n*.txt (56 rows x 4 n, zero mismatches). Theorem 2 is FALSE as stated and refuted by the candidate's own data. Claim: every non-ES class satisfies |S_12|>=C_12=208012 via a contained length-3 pattern q with Av(q) subset Av(P). This inference is invalid for pairs: Av(q) subset Av(p1) does not imply Av(q) subset Av(p1) cap Av(p2); a Catalan floor requires a COMMON length-3 subpattern q contained in BOTH patterns. Independent check shows 20 of 56 reps have NO common length-3 subpattern at all (22 lack a common 123/132/321), e.g. (1234,1432): subs {123} vs {132,321}; (1234,3421): {123} vs {231,312}; (1234,4321): {123} vs {321}. The '0 of 56 lack one' machine check tested union, not intersection. Empirically refuted: candidate reports minimum over nontrivial classes at n=12 is 100728 for (1234,3421), which is < 208012, contradicting the claimed universal floor. CENSUS_NOTE p.75 claim that 100728 is 'comfortably above' 208012 is arithmetically false. Hence the proved disjoint interval {0} vs [208012,inf) fails; many classes lie strictly inside the alleged gap. The promised growth-rate separation (insertion upper bound vs explicit-family lower bound) was not delivered; ES finiteness vs positivity at fixed n is not a Stanley-Wilf growth-constant separation. The Wilf-collapse bijection was explicitly abandoned to conjecture ('No bijection is claimed'). Table entries beyond spot checks are machine-certified only (no per-entry proof; full n=12 replay not independently rerun here). originality: The claimed new boundary (complete symmetry-reduced (4,4) pair census at n=9-12 with proved collapse bijection plus growth separation) was not achieved: no bijection is proved (reported only as empirical grouping/conjecture) and no valid growth separation is proved (Theorem 2 false). What remains is a recomputation of pair-avoidance counts already published. Nearest prior art directly covers the pair window: Kremer-Shiu 'Finite transition matrices for permutations avoiding pairs of length four patterns' (Discrete Math 268 (2003), Table 1, cited from OEIS A165542/A165543 links) studies exactly pairs of length-4 patterns; OEIS pair sequences give counts to n>>12 matching DRAFT exactly, e.g. A165542 Av(4231,4123) a9=34676/a10=160808/a11=752608/a12=3548325 equals DRAFT (1324,1432) row 34676/160808/752608/3548325 (symmetry-equivalent pair); A165543 Av(1234,1342) a9=34875/a10=162560/a11=766124/a12=3644066 equals DRAFT (1234,1342…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Table entries are machine-certified exact counts (no per-entry hand proof); the original Wilf-collapse bijection goal is NOT proved and is reported only as a stable empirical grouping (conjecture); loop pairs (P,P) and ordered pairs are excluded; n=12 rows cost ~1-18s each in optimized C (Python-only replay is limited to n<=8 plus spots); FAIL-036 single-pair equality uses labellings outside the unordered-canonical frame and is neither confirmed nor contradicted.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
