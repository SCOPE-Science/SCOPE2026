# Review of finite-contact threshold optimization

## Correctness

PASS. The reflected boundary-local-time normalization is explicit, and the hitting-time/first-contact decomposition gives the stopping-time Laplace transform. Differentiation at the Laplace origin yields dimensionally consistent first and second cumulants. For every positive contact threshold, the strictly decreasing stationary-point map from \((1,z_0)\) to \((0,\infty)\) proves global uniqueness; at its root the variance-minus-squared-mean expression cancels to an exact strictly negative square. A convexity argument proves a strict optimal-rate gap relative to full renewal. A standalone standard-library checker passes 549 diagnostic assertions, including high-precision transform derivatives. Finite checks are corroboration, not proof of universal assertions.

## Originality

PASS with priority qualification. Bressloff (2022, arXiv:2203.04868), section 3, already gives the retained-local-time *mean* in equation (3.17); a later public result, *A sharp two-site cusp for boundary-reaction throughput under position-only resetting*, gives the entire inverse-local-time transform and includes this one-reset-site case. Those ingredients are explicitly credited and are not submitted as new. Reuveni (arXiv:1512.01600) gives coefficient of variation one under complete renewal at mean-optimal Poisson restarting. The present exact strictly negative variance deficit at the **nonrenewal finite-contact mean optimum**, its strictly monotone finite-threshold optimizer, and its second-order separation from the full-reset optimum were not stated in the inspected prior material. General transform and subordinator theory may imply portions indirectly; independent publication-priority review remains advisable.

## Mathematical value

PASS. Whether surface-reaction progress survives a reset is a central modeling distinction. The exact optimal-dispersion identity quantifies a complete and surprising difference from a standard universal renewal-first-passage fluctuation law, while the sharp optimizer inequalities identify the tunable rate for all positive thresholds. It is not just a numerical point, a change of symbols, or an unsupported physical extrapolation; the result isolates the precise nonrenewal source of reduced optimal dispersion. The model scope is deliberately limited.

## Closest literature and limits

- P. C. Bressloff, *Threshold surface reactions and local time resetting*, arXiv:2203.04868 (first public 2022-03-09), especially sections 2.3 and 3.
- *A sharp two-site cusp for boundary-reaction throughput under position-only resetting*, public 2026 result, full `RESULT.md` inspected. It supplies the entire transform but studies a different optimization objective (large-contact throughput and two reset sites).
- *Power-law survival versus exponential rescue for retained and refreshed surface-reaction thresholds*, public 2026 result, full `RESULT.md` inspected. It treats heavy-tailed random thresholds and survival, not fixed-threshold optimal variance.
- S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal*, arXiv:1512.01600: accessible abstract establishes the complete-renewal fluctuation benchmark.

No finite-sample estimation or experimental verification is claimed. Existing full-transform theorems are not described as discoveries. Literature novelty is assessed against the compared mathematical claims and remains subject to independent checking.

Self-review: passed. Independent audit: not yet performed.
