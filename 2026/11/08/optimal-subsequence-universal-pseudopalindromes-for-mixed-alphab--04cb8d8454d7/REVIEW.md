# Self-review

## Correctness
**PASS.** The proof uses the exact complete-alphabet-factor characterization of scattered-subsequence universality and distinguishes even from odd symmetric words. In the odd mixed case, the central fixed letter occurs exactly once in each of the \(2r+1\) complete-alphabet factors. Matching minimal prefix/suffix requirements force \(r\) permutation blocks on each side and an orbit transversal in the center. The independent finite checker confirms the claimed factorial counts and structure across 1,385,969 candidate symmetric words, including 79,828 direct full-pattern comparisons. The proof, not the finite test, supports all \(k\).

## Originality
**PASS (qualified).** Barker et al. (2020) prove a palindrome midpoint-index statement (Proposition 15) and a word/permutation concatenation criterion (Proposition 18); Adamson (2023) counts general universal words. The fixed-point-free and identity-involution boundary cases have existing separate treatments and are expressly excluded from the new claim. The mixed case \(p\ge1,f\ge1\) has a different exact parity penalty and center-transversal enumeration, not directly entailed by the stated predecessor formulas. Searches for mixed-involution universality, theta-palindromes, and reverse-complement universal words did not identify an equivalent result. An unindexed equivalent remains a risk; no independent literature certification is asserted.

## Mathematical value
**PASS.** The simultaneous presence of swapped and fixed letters is a natural gap between ordinary palindrome and Watson–Crick reverse-complement symmetries. The theorem classifies every shortest universal word for all alphabet orbit profiles and every positive universality order, with a sharp fixed-point-dependent length penalty and exact enumeration. The central orbit-transversal structure offers constructive extremizers, rather than an ad hoc finite calculation.

## Closest sources and limits
Relevant sources: Barker et al., arXiv:2003.04629 (2020), Section 4, particularly Propositions 15 and 18; Adamson, arXiv:2304.04583 (2023), Sections 2–3; Zhang and Wu, DOI:10.1016/j.csbj.2023.11.035 (2023), reverse-complement sequence motivation. Results do not cover words longer than the optimum or arbitrary noninvolutive alphabet symmetries.

Self-review: passed. Independent audit: not yet performed.
