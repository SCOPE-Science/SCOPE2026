# Mathematical assessment: alternating delayed long–short steps

## Correctness — PASS
The exact step multipliers yield the forced log-weight recurrence. Its period-two particular orbit is incompatible with the first undelayed long step when the two eigenvalues differ. Every nonzero homogeneous solution has complex characteristic roots of modulus \(\sqrt2\). A four-phase angular covering lemma forces both spectral components to suffer exponentially large cumulative log losses, establishing sharp two-sided double-exponential bounds. Exact-rational replay of the actual update rule and a separate recurrence verifier produced `VERIFY_OK 2256 exact-rational and independent recurrence checks`. This is an analytic infinite-step proof supplemented by finite tests; the result is limited to exact arithmetic and two spectral values.

## Originality — PASS with historical-priority risk
Barzilai–Borwein (1988) and Friedlander et al. (1999) already give individual delayed-step rules and convergence, and classical two-dimensional BB superlinearity is expressly acknowledged. Yang–Yuan (arXiv:2609.12100) gives R-linear behavior for **fixed** spectral weights; it does not cover time-alternating BB1/BB2. Li–Jiang–Hong (arXiv:2607.21579) establishes higher-dimensional open sets of failure for fixed BB1. Gu (arXiv:2610.32705) studies cyclic reuse of historical Ritz values, a different algorithm. Xu (arXiv:2611.02743, published after the source-window anchor) treats delayed residual rules one at a time and does not assert this alternating exception-elimination result. Search results and accessible full-text comparisons identified no directly covering alternating all-start two-mode theorem. Older analyses of alternating spectral steps may contain equivalent specialized formulas; expert priority review is recommended.

## Value — PASS
The two-eigenvalue balanced orbit is a real worst-case obstruction to generic superlinear claims. The theorem supplies a minimal, low-storage alternation that provably removes that obstruction from all initializations and gives the sharp root-exponential scaling. This is a concrete method-design result for numerical quadratic optimization and a useful test case for handling historical steps; it is not a general multidimensional convergence theorem.

## Limits and closest literature
Historical fixed-BB and delayed methods are not novel. The exact conclusion relies on alternating parity and the initial undelayed long step. The BB literature has numerous variants, so unindexed specialized priority remains a risk. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
