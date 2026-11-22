# Scientific review of the two-tail triangle-free stick theorem

## Correctness — PASS

The claim concerns iid positive lengths with a strictly positive continuous log-density having two finite positive pointwise logarithmic tail slopes. The proof identifies the no-triangle event with every consecutive Fibonacci inequality and establishes the pairwise Fibonacci lower bound. For each threshold-occupancy count, that bound forces the quadratic cost \((\log\varphi)[\beta m^2+\alpha(n-m)^2]/2+O(n)\). Global upper and lower exponential envelopes for the log density turn this deterministic cost into an upper probability bound after reserving an integrable fraction of the density. A family of disjoint geometric-length rectangles with ratio arbitrarily near \(\varphi\) gives a matching lower bound for each integer count, including zero and all. Completing the square gives the full conditional large-deviation principle; all limits and quantifiers, including the fixed-threshold condition, are explicit. Exact finite calculations certify the geometric rectangles and quadratic identity but are not treated as infinite proofs.

## Originality — PASS on inspected evidence

The motivating 2026 Barczy–Lovas paper studies exponential and one-sided Pareto-I lengths, not two-sided power tails, and contains finite-sample integrals instead of the proposed sharp two-sided logarithmic exponent and conditioned rank rate function. Brennan–Callow–Lin's 2026 paper has a general-density **integral representation** for polygon avoidance; the formula does not evaluate this two-tail asymptotic, let alone the conditional threshold-occupancy large deviations. Sudbury–Sun–Treeby–Wang's product is specific to bounded uniform lengths. An indexed November 2026 note already gives the quadratic coefficient for the one-sided Pareto family; this known special support class is explicitly not asserted new and does not imply the positive two-tail harmonic-mean coefficient. Searches for two-sided, asymmetric log-Laplace, double-Pareto, rank-occupancy and Fibonacci alternatives did not identify a stronger covering theorem. Search failure alone is not a novelty proof.

## Mathematical value — PASS

The theorem resolves a motivated distributional gap in a recently studied random-stick problem: when both unusually short and unusually long sticks are possible, how does a rare triangle-free configuration allocate its geometric separation across the two tails? The full quadratic occupancy-rate function quantitatively identifies the rare-event mass balance, and the marginal cost depends on the harmonic mean of the two tail exponents, unlike the one-sided Pareto rate. This is a natural joint probability and conditional shape result under a broad family of distributions, not merely a renamed special case or finite diagnostic.

## Inspected sources and limitations

Primary full text inspected: Barczy and Lovas, *Pick-up sticks problems for exponential and Pareto distributions*, arXiv:2611.04436v1, Introduction, Theorem 3.2, Lemma 3.1, Corollary 3.3, and ratio constraints. Primary full text inspected: Brennan, Callow and Lin, *Fibonacci numbers and the probability of polygon formation using random length sticks*, arXiv:2604.27573v1, Sections 3.2–3.3, especially its general-density formula. Additional comparison: Sudbury et al., *Pick-up Sticks and the Fibonacci Factorial*, 2026, main theorem. An indexed summary of *Sharp quadratic decay for triangle-free Pareto stick samples* (2026-11-08) was read; its full-text retrieval was unavailable, and this is retained as a residual priority risk rather than described as a complete inspection. Further specialized asymptotics not identified by searches remain a general historical-priority risk.

The result has only logarithmic \(n^2\)-accuracy and requires log-density rather than merely distribution-tail slopes. There is no claim of an exact finite-sample formula or moving-threshold uniformity. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
