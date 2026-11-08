# Mathematical review

## Correctness: PASS

The conditional-Poisson factorization is exact: the discrepancy in product weights is a margin-only multiplicative factor. The connected support graph supplies a unimodular spanning-tree minor, so the allowed Poisson margin lattice is full. The Fourier integral therefore has a unique dominant torus point and gives both pointwise and uniform local-limit bounds. Dominated convergence over the independent Poisson rare vector yields total-variation convergence. A joint Fourier calculation projects Gaussian fluctuations onto the kernel of the margin map, and establishes independence. The explicit disconnected two-by-two case follows from exact factorial ratios and a dominated series limit. The standalone checker performs 831 finite and algebraic checks; finite enumeration is only supporting evidence, not the infinite proof.

## Originality: PASS (historical-priority risk retained)

The closest 2026 motivating work establishes the conditional-Poisson/Gibbs formalism and bounded-cost, dimension-growing transport/CLT theorems, not this fixed-dimension singular-weight boundary. Zhou's 2017/2018 paper treats a different, coupon-collector table distribution with fixed margins; Chen's 2007 structural-zero work emphasizes valid importance sampling and conditional tests, not a mixed rare-Poisson/Gaussian limit. Exact two-by-two noncentral-hypergeometric weights and the Bessel-series limit are elementary and are not claimed to be independently novel. Literature-index and published-claim searches did not locate a stronger implication, but a general lattice-conditioned rare-event theorem may cover the result under an unrecognized formulation.

## Mathematical value: PASS

The connected-support criterion explains exactly when finitely many suppressed cells can escape global margin dependence and acquire independent Poisson limits while the allowed cells fluctuate normally. The two-by-two Bessel law is a natural sharp boundary, not an arbitrary finite numerical slice. This fills a meaningful singular-prior regime of conditional contingency-table models used in graphical inference and entropy-regularized transport. It does not require a downstream result or larger paper for relevance.

Self-review: passed. Independent audit: not yet performed.
