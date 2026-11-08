# Scientific review

## Correctness — PASS

The statement fixes the direction of Gaussian KL, the normalization, the integer dimension, the covariance condition-number bound, and the equality cases. Deriving the spectral KL identity reduces the problem to a compact eigenvalue cube. The nonstandard endpoint lemma is proved by the explicit coordinate derivative identity, Cauchy--Schwarz, and positivity of the second coordinate derivative at every interior stationary point. This proves that all maximizing eigenvalues lie at the two endpoints, without relying on finite enumeration. The subsequent mesh maximization, peak uniqueness, and limiting coefficients follow by direct algebra and Taylor expansions. Standard-library `verify.py` passed 8770 supplementary checks.

## Originality — PASS, qualified

Fifen, Karambal and Hennig (2026, arXiv:2609.10080, Section 4.3, Theorem 13) already study the trace-matched isotropic Gaussian covariance block and provide a condition-number upper bound. The present claim replaces that bound with an attained, dimension-specific exact supremum, identifies all maximizing spectra, and gives a sharp linear large-condition-number law. The standard Kantorovich inequality and Liao--Wu (2015) AM-HM operator inequalities were explicitly compared and do not by themselves give this joint KL functional's exact optimum. Formula, alias and stronger-coverage searches found no equivalent published result; a differently indexed classical extremal inequality remains a priority risk.

## Value — PASS

The exact extremal risk is a useful reliability benchmark for isotropic uncertainty representations of unresolved matrix-inverse components. It isolates when covariance spectral spread causes maximal KL miscalibration and makes a dimension-dependent, asymptotically sharp guarantee available; it does not claim a new matrix algorithm.

## Limitations

The result concerns centered finite-dimensional Gaussian covariance blocks, not full block-coupled approximations or random trace-estimation error. Finite numerical checks do not certify the universal inequality and do not establish historical novelty. An independent assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
