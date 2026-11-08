# Self-review

## Correctness (PASS)
The proof is finite and combinatorial up to the asymptotic step: forbidding a set of source vertices leaves a smaller uniform map on the complement; this gives the exact factorial identity and covariance formula without assumptions about conditional cycle independence. The product monotonicity proves the complete sign law. For the mesoscopic limit, the logarithmic product expansion is uniform when the length is proportional to the square root of the vertex count; the explicit telescoping Gaussian majorant justifies the two whole-spectrum sums. The included standard-library verifier checks every map through seven vertices with exact rational arithmetic, and supplies numerical convergence diagnostics. Finite tests alone would not establish the all-size law.

## Originality (PASS, with material priority risks)
The inspected 1996 Soria seminar presents general symbolic constructions for leaves and for cycles, not the computed cycle-length-resolved source-vertex covariance, the all-length sign split, or the mesoscopic Gaussian-profile correction. The 1998 Pitman forest multinomial law and the 2006 Hansen–Jaworski indegree-driven mapping calculus do not directly state these evaluated mixed results in the inspected materials. Comparable indexed work on Cayley-tree degrees and on permutation cycles involves different observables and does not imply the claim. An early general generating function may encode this statistic; deriving an observable from a general framework is not automatically new, so historical implicit coverage is explicitly reserved as a priority risk. Two plausible broad mapping articles were available only at abstract/bibliography level, not as inspected full texts.

## Value (PASS)
The finite covariance profile answers a natural dependence question between feed-in/source structure and feedback cycles of a functional graph. It isolates an exact zero at self-loops from strict negative dependence at every longer length, and identifies the square-root cycle-length window in which the correction accumulates to limiting aggregate covariances. It quantifies a nontrivial finite-size effect missed by separate leading-order source-count and cycle-count limits. It does not assert a general functional central limit theorem.

Self-review: passed. Independent audit: not yet performed.
