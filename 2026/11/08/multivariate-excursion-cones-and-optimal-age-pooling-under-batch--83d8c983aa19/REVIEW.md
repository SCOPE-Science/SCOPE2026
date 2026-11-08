# Scientific review: multivariate excursion cones and optimal age pooling

## Correctness

**PASS.** For every stated finite \(N,m,k\), the admissibility condition makes each single-tag reset mark avoiding any previously specified tags have strictly positive rate. The exact marked-Poisson joint age survival has increments \(d_j\); strict-order local lower bounds are obtained from disjoint finite-width marked-event windows, and ties from continuity. Conditional Gaussian tails and compact exponential truncation give the full logarithmic excursion limit. Rearrangement, strict convexity, the PAV KKT multipliers and the four explicit three-tag configurations establish the rate, uniqueness and curvature boundary. The independent numerical minimizer agreed in 1,500 randomized cases; the packaged standard-library verifier passed 29,382 deterministic checks. Neither finite test establishes the general theorem.

## Originality

**PASS, qualified.** The closest source, de Mauro, Majumdar and Schehr (arXiv:2601.20077), establishes the partially resetting Brownian model, arbitrary-order stationary marginal recursions and pair correlations. Their general characteristic-function equations are not attributed to the present result. The exact \(k\ge3\) directional positive-excursion logarithmic rate, its weighted-PAV optimizer and four distinct three-age partitions were not identified in the inspected primary main text, supplemental equations or the relevant search results. Classical multivariate Marshall–Olkin survival and known bivariate Gaussian-shock tail formulas provide input identities, not the stated general \(k\)-coordinate constrained age optimization. Work on simultaneous resetting (arXiv:2509.06658) concerns a fully common clock, not intermediate batches; only its abstract and substantive overview were accessible. The exact publication-priority comparison remains subject to broader literature, especially any general theorem for Marshall–Olkin Gaussian scale mixtures. A failed textual search is not a novelty certificate.

## Value

**PASS.** Extreme displacements probe joint fluctuations that second-moment correlations cannot resolve. The result yields a complete computable directional rate for every admissible observed set of at least three tags, with no numerically fitted constants. The four attainable age-pooling regimes and their second-derivative phase boundaries show how one, two or three effective reset histories dominate different angles. The equal-level formula gives a concise \(k\)-way tail diagnostic of the batch size; finite-order data can therefore distinguish differences invisible in one-particle Laplace tails. This is a natural multivariate large-deviation classification, rather than a parameter substitution or a new notation for an old pair result.

## Closest literature and limitations

De Mauro–Majumdar–Schehr, arXiv:2601.20077 (first posted 2026-01-27), is the direct source for the process and stationary marginal recursion. De Mauro–Biroli–Majumdar–Schehr, arXiv:2509.06658, covers fully synchronous renewal resetting. Classical Marshall–Olkin exponential shocks give the tagged-age distribution. Existing two-coordinate angular rates and tagged-age gap limits are acknowledged as prior special-case information, not counted as new. No claim is made for larger tagged sets \(k>N-m+1\), finite-threshold asymptotic prefactors, or microscopic interactions. Independent priority and proof audits are still absent.

Self-review: passed. Independent audit: not yet performed.
