# Scientific review

## Correctness: PASS

The source strings, independent deletion channel and distance normalization are fixed precisely. The proof derives the two trace masses and their likelihood ratio, including zero-probability boundaries; the ratio cancels the retention parameter for any finite number of independent traces. The binomial-expectation formula follows by changing to a common product-binomial reference measure. A separate coupling moves a single additional zero retention from one side of the marker to the other; conditioning on the total count yields an explicitly unimodal hypergeometric law, whose distance to its one-step shift is its largest point mass. This proves the new all-position maximum formula with no computational assumption. The central expression follows by exchangeability and binomial convolution, and a local central limit theorem plus a controlled Taylor expansion proves the fixed-retention asymptotic constants. A standalone exact-rational checker enumerates every deletion mask for 108 adjacent-source pairs and verifies the formulas and likelihood ordering, supplemented by central affinity checks. These finite tests do not certify the infinite statements; their mathematical proofs are given separately.

## Originality: PASS, with known overlapping ingredients and residual risk

The closest established predecessor is McGregor, Price and Vorotnikova (2014), Section 3.3/Lemma 11. It explicitly introduces the *central* shifted-single-marker pair and its binomial-product laws, obtaining an order \(r^{-1}\) Hellinger bound. That central distribution and an implied exact central affinity are prior art; neither is independently claimed as new. The accepted contribution instead treats every adjacent pair, exhibits a rate-independent optimal hypothesis test for any number of traces, and proves an exact **off-center** total-variation formula as a weighted hypergeometric maximum-coefficient sum. Neither the 2014 central bound nor the inspected 2024 generalized-trace manuscript states or directly covers this all-position maximum identity. The half-retention central value at short lengths may already be known from a reported finite trace comparison, so its numerical cases are not asserted as original. The checked indexed results contained relevant deletion-sphere and Bernoulli-distance work, but no equivalent off-center theorem. A closer unpublished or unindexed characterization is still possible.

## Value: PASS

For adjacent-location discrimination, a practical question is the minimum testing error at each position and its dependence on deletion rate. An exact profile for all lengths and positions, computable through unimodal hypergeometric maxima, is a natural complete characterization rather than a selected numeric example. More unexpectedly, the Bayes-optimal classification rule requires no knowledge or estimation of the retention probability, even from multiple traces. The central sharp constants quantify the transition between one-trace error and many-trace indistinguishability. These facts are useful as exact local benchmarks in noisy synchronization and trace reconstruction without purporting to solve arbitrary-string reconstruction.

## Closest literature and limitations

A. McGregor, E. Price, S. Vorotnikova, *Trace Reconstruction Revisited* (2014), Lemma 11, author PDF: https://people.cs.umass.edu/~mcgregor/papers/14-esa.pdf. This is decisive prior coverage of the central product-binomial law, not of the off-center maximum theorem.

J. Rivkin, G. Valiant, P. Valiant, *A Generalized Trace Reconstruction Problem: Recovering a String of Probabilities* (arXiv:2412.00674v1, 2024-12-01): https://arxiv.org/html/2412.00674v1. Its source model includes deterministic single-marker strings, but its lower bounds and recovery algorithms do not assert the claimed local exact test.

A 2026 public summary reports exhaustive one-trace total-variation comparison through length ten at half-retention and a central-marker extremizer; it does not establish all-length off-center likelihood identities. Primary coverage of any unpublished detailed calculations remains an explicit priority risk. Only constant homogeneous retention and adjacent single markers are covered; no independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
