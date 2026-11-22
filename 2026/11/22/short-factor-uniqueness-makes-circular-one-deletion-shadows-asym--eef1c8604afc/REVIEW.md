# Scientific review

## Correctness
PASS. The critical source-location anchoring lemma is proved directly: at least one length-\(\ell\) output factor is intact in both deletion presentations, its origin must agree because the cyclic source has unique factors, and the resulting linearly rooted deletion equality forces the removed positions into the same cyclic run. For the random bound, a complete shift-orbit cannot fit in a consecutive block of at most half the cyclic positions, so the factor-matching constraints form a forest and have probability \(q^{-\ell}\). The exact chromatic-cycle count and pairwise edge independence establish the cyclic run law, moments and CLT. The verifier passed exhaustive finite checks; no finite computation is used as a proof of an infinite assertion.

## Originality
PASS on inspected published and indexed evidence, with a priority qualification. Sloane's 2002 full text, especially Section 5, treats linear one-deletion descendants by ordinary runs; Liron and Langberg's 2012 full text treats linear deletion-subsequence counts and extremizers. The closest published circular result determines the maximum shadow size, not the source-wise short-factor guarantee or random full distribution. A special de Bruijn-cycle run-exact theorem does not provide the all-source short-factor criterion or q-ary random law. The 2025 circular trace reconstruction paper concerns sample complexity for an unknown source under repeated probabilistic deletions. Unindexed antecedents may exist, and independent priority review has not been performed.

## Value
PASS. Arbitrary cyclic quotienting can merge deletions from distinct runs, so transfer of the familiar linear run law is invalid without an additional synchronizing property. A general finite-window criterion turns a nontrivial circular deletion statistic into the explicitly enumerated cyclic-transition law with an algebraic total-variation error, a usable approximation for any fixed alphabet and all sufficiently large lengths. This distinguishes deterministic collision prevention from an exact average-source output-count approximation and supplies the correct parity-constrained finite reference law in the binary case, beyond a mere central limit calculation.

## Closest comparisons and limitations
Relevant: Sloane (2002, https://arxiv.org/html/math/0207197v1), Liron–Langberg (2012, https://arxiv.org/html/1202.1644v1), sharp circular support maximum (https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-one-deletion-outdegree-of-binary-necklaces--2341722fce11/RESULT.md), and circular trace reconstruction (https://arxiv.org/html/2512.02412v1). The theorem does not enumerate exact short-length shadow-size frequencies, deletion probabilities, or outputs under more than one deletion. Novelty is not established as a theorem by database searches.

Self-review: passed. Independent audit: not yet performed.
