# Self-review

## Correctness — PASS

The exact two-point resolvent of the independent-coordinate-flip process gives the unreset hitting-time Laplace transform; the standard renewal calculation then gives the complete mean reset-hitting-time formula. Compact convergence on rates proportional to dimension is proved with dominated convergence, while two separate nonasymptotic inequalities rule out **both** degenerate rate regimes for global minimizers. The fixed-distance assumption, total jump-rate normalization, the unreset endpoint, and the quantifier covering **every** global minimizer are checked in the written proof. A standard-library script independently compares the tridiagonal birth–death equations with the coordinate-product integral and checks numerical optimizer trends; 45 comparisons passed. Computation verifies examples but the infinite assertion is established by the analytic estimates.

## Originality — PASS on examined evidence, not independently certified

Janson–Peres (arXiv:1005.4275) develop state-dependent restart grades on infinite Euclidean lattices. Evans–Majumdar (arXiv:1102.2704 and 1107.4225) establish Poisson restarting and optimize Brownian first passage. Dharmaraja et al. (arXiv:2103.10984; journal 2015) study Ehrenfest catastrophes that return **directly to zero**, and thus a different first-passage mechanism. These results contain ingredients but do not state or imply the rare-corner fixed-distance **hypercube** Poisson optimization. Actual published-result searches and related primary literature were compared for reset aliases and implications. Residual risk: an unindexed exact special case may be in the literature; this is not independent historical certification.

## Mathematical value — PASS

The result identifies the sharp crossover from exponential unaided hitting times to a polynomial optimized search with a nontrivial coefficient and rate law, for a natural high-dimensional physical configuration graph. It solves a complete infinite-family optimization with universal fixed-Hamming-distance constants. No claim about arbitrary restart strategies or growing starting distance is made.

Self-review: passed. Independent audit: not yet performed.
