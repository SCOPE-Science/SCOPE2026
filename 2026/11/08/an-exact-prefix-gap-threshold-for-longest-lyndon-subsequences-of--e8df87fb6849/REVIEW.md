# Self-review

**Correctness — PASS.** The proof is an exhaustive lower-bound case split by indices of the first and last retained marker ones, paired with an explicit construction deleting exactly the first threshold number of marker ones. Its critical nonstandard comparison is the final-zero-run constraint for Lyndon words; this follows directly from the lexicographic proper-suffix definition. The finite checker independently enumerates 201 words and tests 72 patterned examples; the proof establishes the infinite quantification. The positivity and nondecreasing conditions, including equality and the single-gap boundary, are used explicitly.

**Originality — PASS, qualified.** Bannai et al., arXiv:2201.06773 (2022) and the full open-access Algorithmica version (2023 online), establish general computational algorithms, not the exact monotone binary marker threshold. The inspected general and special-case sections do not subsume the claimed closed-form law. Searches for longest Lyndon subsequences, monotone gaps, binary run lengths, and deletion thresholds, together with comparisons against mathematical records and accessible prior claims, found no equivalent or stronger structural classification. A hidden or unindexed equivalent remains possible; search absence is not proof of uniqueness.

**Value — PASS.** The result identifies a natural compressed-word family on which a general longest Lyndon subsequence optimization has an exact linear-time threshold formula and a concrete optimal certificate. Its distinct constant, triangular, and geometric asymptotic deletion regimes expose a structural dependence on gap growth. The result does not claim a new polynomial-time solution for unrestricted inputs.

**Closest source:** Bannai et al. (2022), https://arxiv.org/abs/2201.06773; open-access complete follow-up at https://doi.org/10.1007/s00453-023-01125-z.

**Limits and remaining risk:** No independent scientific audit; possible unindexed equivalent; finite verification alone cannot establish the infinite identity. The proof has been checked with its precise edge cases and quantifiers.

Self-review: passed. Independent audit: not yet performed.
