# Scientific review: reversed permutation powers and maximal subsequences

## Correctness — PASS
For any nonempty candidate, greedy matching in the two opposite permutation blocks proves the exact feasibility inequalities in the proof: the rise and fall budgets, including the extra cost of equal adjacent letters, must each be at most one less than the repetition exponent. A repeated-letter edge can be replaced by a two-edge rise/fall at unchanged budget. For adjacent-distinct candidates, if either budget is still available, the insertion argument constructs a strictly longer common word; the only nontrivial boundary case is discharged by the telescoping equation on alphabet indices. Therefore every maximal word has exactly one less than twice the repetition exponent in length. The exact Smirnov generating function follows from the finite end-letter recurrence; the palindrome count follows from mirroring. Actual `verify.py` checks passed: 17 exhaustive input pairs, 8,323 common words, 3,228 maximal words, and 816 generating-function coefficient identities. Finite checks are supportive rather than logical proof.

## Originality — PASS, with residual bibliographic risk
- Hirota and Sakai, arXiv:2307.10552, Sections 1–5, develop general MCS enumeration algorithms and explicitly distinguish MCS from LCS. No theorem for reverse permutation powers or the absence of shorter MCS appears in the examined mathematical material.
- Conte, Grossi, Punzi and Uno, arXiv:2307.13695 / ISAAC 2023, Introduction, Sections 2–4 and Theorem 13, give polynomial-size DAG representations for general MCS languages. This machinery can calculate a finite instance, but does not imply a symbolic, all-parameter saturation theorem by itself.
- Ellzey and Wachs, arXiv:1901.01591, equation (1.7), already prove a Smirnov-word descent generating function. The rational series itself is **not** claimed new; its precise MCS interpretation in the two reversed strings is the additional result.
- Bukh and Cox, arXiv:1912.03510, study common subsequences of a periodic word against a random word, not deterministic opposite-order powers.
- Accessible prior findings on ternary powers against \((021)^s\), the general palindrome length for run-power words, and palindromic subsequence spectra cover different questions or only the optimal length/palindromic subcounts. They do not imply the full MCS= LCS rigidity and complete nonpalindromic optimizer language for full reversal.
- OEIS A396530 contains an initially matching coefficient segment but differs at the next checked term (26,334 versus 26,312); it is not an exact table of this parameter family.

The comparisons assess implication, not merely matching titles. No directly dominating statement was found in the accessible searches or inspected source material. A specialized unindexed theorem or an equivalent formulation in a source not retrieved remains possible; lack of a search result is not a proof of novelty.

## Mathematical value — PASS
General maximal-common-subsequence languages can include arbitrarily shorter maximal elements, so an infinite input family where maximality **forces** optimal length is a meaningful structural distinction. The theorem identifies the full downward language basis, gives exact enumerative coefficients for all alphabet sizes and exponents, and separates palindromic from nonpalindromic optima. This classification is more than a routine numerical table: the completion lemma is global and uses an obstruction equation that treats all alphabet sizes and boundary cases.

## Scientific limits
Equal exponents, opposite block orders and pairwise distinct letters are essential assumptions. This is a self-review only. The Smirnov GF is known independently, and publication-equivalent variants might be unindexed. The verifier checks only finite sizes; the general argument is contained in the proof.

Self-review: passed. Independent audit: not yet performed.
