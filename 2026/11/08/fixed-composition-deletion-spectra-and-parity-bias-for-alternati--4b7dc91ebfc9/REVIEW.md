# Scientific review

## Correctness — PASS
The asserted identity \(v\preceq A_{m+t}\iff v_1+\#\{i:v_i=v_{i+1}\}\le t\) follows from the unique earliest embedding of any query in a binary alternating host. Its equality-indicator encoding is a bijection, establishing the total distinct-output count. Weight tracking in the two-state transition matrix yields the rational generating function with correctly normalized empty-length boundary. The exact support follows from maximum run counts with fixed ones/zeros. The complement difference is a cancellation of paired words away from the exact penalty boundary; run-composition binomials give the signed formula. The independent run-sum formula supplies a second derivation of every coefficient. Verifier: direct deletion-output sets through host length \(17\), transfer-vs-run census through output length \(64\), all checks passed. The infinite case is proved symbolically, not extrapolated.

## Originality — PASS (best-knowledge review)
Flaxman–Harrow–Sorkin (2004) prove the alternating host maximizes total distinct subsequences and give a bivariate enumeration in host/output lengths. Those established results have been removed from the novelty claim. Alon et al. (2022) focus on deletion codes and common subsequences of two words, and Menon–Singh (2023) count occurrence multiplicities of specified patterns across hosts. The inspected statements do not imply the fixed-Hamming-composition trivariate enumerator or signed binomial complement defect without a new refinement. Searches across research records and literature for aliases and composition/weight terms did not identify equivalent results. Residual risk: an unindexed prior multivariate refinement could cover the formula; searches do not prove uniqueness.

## Mathematical value — PASS
The question is naturally motivated by deletion channels with constrained received-word composition: the total deletion-ball cardinality does not identify which constant-composition output classes occur or their sizes. The exact support threshold and parity-sensitive skew classify every class, including saturation boundaries, for an infinite host family. The complement-bias factorization is structural and not an arbitrary small numerical increment. No claim about all hosts or general coding-capacity improvements is made.

## Closest sources and limitations
- Flaxman, Harrow, Sorkin (2004), DOI: https://doi.org/10.37236/1761: the unweighted precursor and greedy matching, not the weight spectrum.
- Alon et al. (2022), https://arxiv.org/abs/2209.11882: deletion codes and longest-common-subsequence multiplicity.
- Menon and Singh (2023), https://arxiv.org/abs/2306.07870: frequency of prescribed subsequences in collections of binary words.
- Indexed research records on deletion-ball variance, deletion reconstruction, and subsequence universality address different counts.

The proof covers a single binary alternating source phase only. The unweighted statement is known; the novelty judgment for the exact weight refinement is necessarily bibliographic and not an independent certification.

Self-review: passed. Independent audit: not yet performed.
