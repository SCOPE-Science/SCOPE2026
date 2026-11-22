# Assessment: sparse non-overlapping code capacity

## Correctness — PASS

The finite-alphabet quantifiers and the exact definition of overlap, including self-overlap, are explicit. The upper bound is not inferred from experiments: cyclic rotation gives at most one representative per primitive weight-two necklace; unequal zero gaps account for \(\lfloor(n-1)/2\rfloor(q-1)^2\) necklace classes. At even blocklengths, equal zero gaps imply that the set of first-marker colors is disjoint from the set of last-marker colors, so at most \(\lfloor(q-1)^2/4\rfloor\) such codewords exist. The construction uses every unequal-gap representative with the larger gap preceding the first marker, and a balanced first/last alphabet partition for equal-gap words. Its proper prefix/suffix proof checks all ordered pairs, including equal words.

The supplied executable directly checks 91 parameter pairs and 438,536 ordered pairs of constructed words. An independently built full conflict graph was optimized to a zero-gap integer optimum in 20 small parameter instances, agreeing with the theorem. Finite tests are corroboration, not proof of the unbounded result. The empty boundary case at alphabet size two and blocklength two is included.

## Originality — PASS, qualified

The inspected articles of Wang and Wang (2021, arXiv:2108.06934), Qin, Chen and Luo (2023, arXiv:2309.08915), and Stanovnik, Moškon and Mraz (2024, DOI 10.1007/s10623-023-01344-z) treat general construction families, non-expandability, and global optimization, rather than an exact fixed-two-nonzero-symbol optimum at every alphabet and blocklength. Stanovnik et al. (2024/2025, arXiv:2410.18458) study run-length and near-balance constraints, but not this particular support restriction. Indexed exact weight-three and weight-four binary non-overlapping results do not determine the colored weight-two formula by specialization. The familiar length-two bipartition is an ingredient, not a proof of the arbitrary-length necklace bound. No inspected implication supplies the even-blocklength deficit or the odd-blocklength saturation.

Searches used the equivalent terms *non-overlapping*, *cross-bifix-free*, *mutually uncorrelated*, *two nonzero positions*, *two colored markers*, *constant weight two*, and *primitive necklace*. Equivalent unindexed claims, a general theorem with unnoticed stronger implications, or an overlooked appendix remain residual historical-priority risks; no claim of independently certified novelty is made.

## Value — PASS

The exact all-parameter capacity is a natural sparse synchronization-code invariant. It separates the finite-length effect of sparsity from the unrestricted code-size problem, explains a parity transition by a complete-bipartite marker-color obstruction, gives explicit maximum codebooks, and precisely measures the first strict failure of the usual primitive-necklace packing bound at four alphabet symbols. This is not an arbitrary short lookup table or a change of notation: it is a structural bound and matching construction for an infinite family.

## Sources and limitations

- G. Wang and Q. Wang, *Q-ary non-overlapping codes: a generating function approach*, arXiv:2108.06934v1, 2021-08-16, https://arxiv.org/pdf/2108.06934 .
- C. Qin, B. Chen and G. Luo, *On non-expandable cross-bifix-free codes*, arXiv:2309.08915v1, https://arxiv.org/pdf/2309.08915 .
- L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, https://doi.org/10.1007/s10623-023-01344-z .
- L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, https://arxiv.org/abs/2410.18458 .

The theorem does not address higher weights, noise correction, or mixed lengths. The numerical checks use finite instances only. Independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
