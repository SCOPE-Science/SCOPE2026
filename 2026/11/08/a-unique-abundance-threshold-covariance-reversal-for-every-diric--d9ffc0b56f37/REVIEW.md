# Scientific review

## Correctness
PASS. Dirichlet parameter shifting gives the normalized mixed beta-tail identity, independent of asymptotic arguments. Conditional power sums give a strictly convex function with two level crossings; the upper-tail integral has exactly one zero. The quadratic beta-integration formula and large-power shifted-beta limits prove both specializations. The standalone `verify.py` passed 860 rational and numerical checks. No finite check is claimed as a proof of the universal quantifiers.

## Originality
PASS on the accessible claim-implication comparison, with residual priority uncertainty. Cerquetti (2012, arXiv:1203.1666) gives Simpson moments and a finite symmetric Dirichlet species model; Cerquetti (2014, arXiv:1404.3441) gives generalized power-diversity moments. Neither inspected result includes abundance threshold indicators, their mixed covariance, a unique sign-switch classification or the high-power expected-one-exceedance limit. Existing general moment formulas do not themselves provide the thresholded mixed moment without an additional beta-tail argument. Closest searchable published-finding corpus records concern iid observed richness versus diversity and occupancy richness versus frequency counts rather than a latent finite Dirichlet abundance vector. Negative-search evidence does not establish exhaustive priority. Classical Dirichlet moment methods are acknowledged.

## Value
PASS. A threshold count is a natural operational definition of how many species are abundant, while the power sum governs the Simpson/Tsallis concentration continuum. For every power greater than one the theorem gives a complete sign phase diagram, a closed-form critical abundance for Simpson concentration, and a high-order limit with a distinct operational interpretation (expected one exceedance). This resolves dependence that marginal power-moment formulas do not answer, and avoids an arbitrary chosen threshold.

## Residual limits
The result is restricted to a fixed finite number of symmetric Dirichlet proportions and to power orders greater than one. No claim is made for heterogeneous parameters or for monotonicity of the transition in the power order. Some general or later works might encode an equivalent mixed covariance implicitly, and independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
