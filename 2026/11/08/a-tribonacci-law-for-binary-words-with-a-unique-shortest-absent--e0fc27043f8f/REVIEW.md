# Mathematical review

## Correctness — PASS
The claim is the exact bivariate count of *distinct binary source words* having exactly one shortest absent subsequence. Its proof handles the empty suffix separately, partitions absent subsequences by first letter, establishes the first-occurrence length/count recurrence, and derives an exhaustive and nonoverlapping first-arch grammar. Weighted enumeration proves the rational generating function, with binomial extraction and standard singularity analysis giving the remaining consequences. Two different exhaustive computations agree with the all-length formula at every coefficient through length \(22\); no finite check is used as an infinite proof.

## Originality — PASS (qualified)
The original omnibus-word paper studies full universality and expected missing-pattern counts, not the exact unique-shortest-absent source-word census. The previously published characterization of 1-nearly \(k\)-universal words already covers the **membership question** and must be credited: the present counting assertion does not claim an unknown characterization of that class. The exact bivariate length/index enumeration is not stated by the inspected membership, universality-index, extremal-count or shortest-absent algorithms. A complete characterization could facilitate an alternative derivation, but an explicit all-length weighted count is an additional enumerative result. The scalar tribonacci numbers are **already tabulated** for unrelated interpretations; only their here-proved SAS interpretation and refinement are advanced. An unindexed equivalent enumeration remains a historical risk.

## Value — PASS
The exact abundance of source strings with only one minimal-length missing subsequence is a natural precision measure for near-universal sequence design: it distinguishes the exceptional one-missing level from the much larger classes of k-universal or other deficient words. The index-refined rational series and the exponentially decaying probability provide quantitative answers for every length, not a selected numerical instance or a mere restatement of a membership algorithm. The binary first-arch decomposition explains structurally why the count has a tribonacci recurrence.

## Closest literature and limits
Theorem 16 of Fleischmann et al. (2022) is the closest **strong** result: full general-alphabet membership characterization, but not word-count enumeration by length. Abraham et al. (2009) and the later exact universality-index formula count related but different objects. Earlier extremal work on SAS counts and the independently known OEIS scalar sequence constrain any novelty assertion. This proof is binary-specific and has not had independent scientific review.

Self-review: passed. Independent audit: not yet performed.
