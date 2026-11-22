# Review: exact excess-summand statistics for nonunique Lucas partitions

## Correctness — PASS

The canonical-interval induction proves that each nonnegative integer has exactly one normal-form expansion, and specifies the cutoff range. The independent-tail maximum recurrence establishes injectivity among redundant representations. The unique initial even run yields the exact replacement \(\{0,2,\ldots,2j+2\}\mapsto\{1,2j+3\}\), preserving the integer and changing the number of summands by exactly \(j\). The remaining admissible tail has an exact Fibonacci independent-set count; the empty-tail boundary is addressed separately. The rational bivariate generating function, parity-dependent totals, probability normalization and moment convergence follow algebraically. Direct exhaustive independent-subset tests for all 22 index cutoffs from 3 to 24 agreed with every fiber formula. The finite computations do not substitute for the unrestricted proof.

## Originality — PASS on inspected evidence

Brown's 1969 full text proves uniqueness under the canonical constraint. Chu–Luo–Miller, arXiv:2004.08316, full text Sections 3–5 and appendix, already give the at-most-two fact, redundant-partition table, unweighted Beatty enumeration, and density. These are explicitly credited. Shallit, arXiv:2305.02672, Section 5, Theorem 5.2, proves an automaton recognition equivalence for the unweighted double-representation set, not the difference of the two summand counts. OEIS A342089 similarly indexes the unweighted support. Neither the complete finite-cutoff weighted distribution nor its bivariate generating function or geometric normalization-cost law was found in the inspected primary sources or relevant indexed-results comparisons. The known normal-form statements are ingredients; a hidden equivalent weighted derivation remains a genuine priority risk.

## Mathematical value — PASS

Two different nonconsecutive Lucas partitions can represent the same number. Their discrepancy in *number of summands* is an intrinsic normalization cost, not captured by the known unweighted existence/density theorems. The result gives the full finite-size law for every allowed excess, proves that arbitrarily large excess is possible, and identifies an exact geometric limiting cost distribution, including a nontrivial moment identity with variance one. This is a motivated structural refinement and complete classification, not an arbitrary finite census or routine reindexing of a single count.

## Closest sources and limits

The most relevant previous work is Chu–Luo–Miller (2020/2022), Brown (1969), Shallit (2023), and OEIS A342089. Similar Fibonacci/Zeckendorf digit-count studies and phi-expansion counts concern different objects and do not directly state this paired-Lucas-length law. The comparison cannot exclude unindexed manuscripts or reductions requiring nontrivial unpublished arguments. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
