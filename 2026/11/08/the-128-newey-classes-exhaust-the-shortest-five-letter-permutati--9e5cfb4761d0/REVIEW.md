# Scientific review

## Correctness — PASS

The statement concerns all length-\(19\) words over five labeled symbols containing all \(120\) permutations as scattered subsequences, modulo the explicitly defined group actions. Consecutive equal letters are removable. First-appearance normalization loses no class and is unique. For each \(t\)-pattern, the earliest embedding must finish at most \(L-m_{5-t}\) because its suffix must embed all permutations of the complementary alphabet. The needed smaller-alphabet minima \(1,3,7,12\) were independently checked. This lemma justifies *every* pruning deadline in the exhaustive canonical search. Two separate state constructions—greedy matching of the 120 full permutations and explicit distinct-letter-subsequence languages—give identical results at lengths 18 and 19, including the exact 128-word file. Direct permutation tests, free relabeling, and a complete reversal-orbit partition verify the remaining consequences. There is no use of finite samples to infer an unbounded claim: the claimed domain is completely enumerated.

## Originality — PASS, with residual historical priority risk

Newey (March 1973, Section 9, printed page 12) **already reported 128 distinct construction classes**, and stated that they *may or may not be all of them*. The novelty assessed here is the previously unproved global upper bound and resulting exact equality-case census; the construction, numerical lower bound, and minimum length 19 are expressly credited. Newey fully settled the nine four-letter classes. Radomirović (2012) and Engen–Vatter (2018) treat constructions and universal-word lengths but provide no exact exhaustive five-letter class count in the inspected material. The OEIS entries give lengths and examples, not the upper bound. Search comparisons found no published assertion settling the 1973 uncertainty; this is best-knowledge priority, not an independent certification. A later, unindexed census remains a risk.

## Value — PASS

This closes the explicit 1973 equality-class completeness question in the first alphabet size where the known 128-class construction was not asserted exhaustive. It determines all optimal words, establishes that every optimum starts with a permutation, and gives exact labeled and reversal-symmetry spectra. The invariant is the natural number of minimal universal words, rather than an arbitrary slice or a small numerical improvement. The result is a meaningful self-contained finite classification with complete reproducibility.

## References and scope boundaries

Newey, *Notes on a Problem Involving Permutations as Subsequences*, STAN-CS-73-340 (March 1973), Sections 5, 7 and 9; Radomirović, *Electronic Journal of Combinatorics* 19(4), P31 (2012); Engen–Vatter, arXiv:1810.08252, Section 4 (2018); OEIS A062714 and A351468. No classification is claimed for six or more letters. Earlier March 1973 source has no verified exact day; the exact day in metadata identifies a later day-verified primary publication and does not erase or redate the original source.

Self-review: passed. Independent audit: not yet performed.
