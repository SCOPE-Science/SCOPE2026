# Scientific review

## Correctness — PASS
The claim specifies fixed finite sample size, standard-Cauchy reduction, interior ranks, limits and normalizations. An ordered-density one-extreme asymptotic establishes the joint boundary density; a two-variable product-tail calculation separates the logarithmic adjacent-rank case from the linear separated-rank case. The four-observation right endpoint is a two-doublet boundary simplex integral with uniform integrable domination. `check.py` confirms key integrals and independent numerical approximations; it is not the proof. The result does not imply any large-sample or uniform threshold approximation.

## Originality — PASS (best-knowledge priority)
Pekgör (2023, DOI 10.1155/2023/9200213) is the closest primary source: its four-quantile Cauchy statistic is studied via fixed-quantile asymptotic normality and simulation, not a fixed-\(n\) vanishing-threshold rank-gap transition. Rublík (2001) analyzes a distinct quadratic extreme-order-statistic test; Ghosh and Jammalamadaka (1998) work with transformed uniform additive spacing tests. The large-sample local-spacing theorem of Nagaraja, Bharath and Zhang (2015) does not cover this limit order. Exact claim/alias/stronger-result searches did not reveal decisive coverage, but older spacing literature or uninspected supplementary materials are residual priority risks.

## Value — PASS
The exact small-tail exponents and constants explain how an extreme-range denominator changes the rare-significance calibration of the rank version of a four-quantile Cauchy test. The logarithmic critical case is adjacent ranks; when an interior rank is skipped, a single remote Cauchy observation instead drives a linear null tail. Even at fixed small sample size this matters for extreme critical values and is not predicted by the paper's large-sample Gaussian approximation. No general power or optimality claim is made.

## Scientific boundaries
The theorem covers only Cauchy location-scale samples, fixed \(n\), raw empirical inverse-CDF rank quantiles and tails approaching the support endpoints. It does not evaluate software-specific interpolated quantiles, broad numerical calibration accuracy or the test's inferential performance outside those assumptions. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
