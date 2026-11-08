# Mathematical review

## Correctness — PASS

The face identity follows from a bijection between crossed simplex faces and section faces under genericity. A projected standard Gaussian is Haar in the simplex tangent space, and shifting through an interior centroid-to-vertex point yields the stated common threshold. The critical formula follows from a uniform local empirical-CDF increment estimate and the CLT for \({\mathbf{1}}_{\{G>0\}}-1/2-\varphi(0)G\), whose variance is exactly \(1/4-1/(2\pi)\). A distinguished independent Gaussian adds the \(c^2/(2\pi)\) term. Uniform empirical convergence gives the other two regimes, while a binomial-coefficient Taylor expansion establishes joint fixed-rank limits. The macroscopic CDF, mean and endpoint moments are direct Gaussian-quadrant/probability-integral-transform consequences. A standard-library verifier checks crossed-face counts, covariance normalization, finite expected counts and large-dimensional coupled approximations. Simulations do not constitute a proof of convergence.

## Originality — PASS, with stated residual risk

The full inspected primary text of Schange (arXiv:2610.28084, first posted 2026-10-20) gives expected face numbers of random shifted sections, but no corresponding joint face-vector distribution or displacement-dependent dimension-asymptotic crossover. The full available published research notes on regular-simplex central sections give exact sign reductions and joint chi-square fluctuations, but their shift parameter is identically zero; the new results require resolving a moving random threshold and an additional independent Gaussian. The Kabluchko–Seidel full text covers angles and central face expectations; De Loera–Lopez-Campos–Torres treats deterministic section-vertex counts. The known central endpoint and finite expected count have been explicitly excluded from claims of independent novelty. Alternative historical formulations in empirical-threshold statistics or convex geometry cannot be ruled out completely.

## Mathematical value — PASS

The question is motivated by recent explicit formulas for shifted random sections: what happens to the full *distribution*, rather than just its mean, as the interior shift competes with dimension-dependent Gaussian normal fluctuations? The answer provides a complete natural transition across three geometric scales, exhibits a critical \(n^{-1/2}\) crossover, and identifies a macroscopic nonconcentration law (with a particularly simple universal endpoint distribution). The joint face-vector law exposes a single random factor governing every fixed face rank, rather than a one-off expectation or unmotivated parameter specialization.

## Scientific limitations and comparison

All statements are for Haar normals, a regular simplex and shifts on one vertex ray. Only fixed face dimensions are included in joint asymptotics; no error rate is claimed. The existing primary paper's mean result and the older central chi-square limit are not presented as newly discovered results. Earlier noncentral formulations in unindexed literature remain a residual historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
