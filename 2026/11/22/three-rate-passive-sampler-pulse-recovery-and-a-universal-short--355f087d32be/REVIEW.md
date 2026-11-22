# Review: Three-rate passive-sampler pulse recovery and a universal short-pulse sensitivity law

## Correctness: PASS

The proof derives the exact normalized sampler convolution, reconstructs the two exponential endpoints using the two power ratios, and supplies a necessary-and-sufficient strict physical feasibility criterion. A continuous two-channel alias, the factorized full Jacobian, and the exact relative derivative establish the minimum measurement count and the sharp short-duration coefficient \(6\). The exact rational example and 47,013 supplementary checker assertions pass. These checks are not a substitute for the analytic universal proof.

## Originality: PASS on inspected evidence

Becker et al. (2024) provides the time-dependent passive-sampler forward model and a concrete motivating difficulty from unknown pulse timing. Hawker (2009) reconstructs pulse profiles from temporal response curves rather than one synchronized retrieval at three harmonic elimination rates. Plonka and Tasche (2014) establishes broad Prony reconstruction concepts and collision issues; those are acknowledged as prior. The targeted three-rate, physically feasible inverse and exact duration-only sensitivity were not found in inspected materials. A general-Prony full-text comparison could not be completed, so historical priority remains provisional; this does not claim an exhaustive literature survey.

## Value: PASS

The finding quantifies a specific monitoring gap: exact three-channel identifiability with an asymptotically severe, universal local sensitivity as the pulse becomes short. This separates what is theoretically recoverable from what may be stable enough to estimate, and identifies why a third readout can be both necessary and fragile. It does not yield a field-calibrated instrument recommendation or statistical variance bound.

## Closest literature and limits

- Becker et al. (2024), https://doi.org/10.1007/s11356-024-34460-x: relevant single-compartment time-integrative response and episodic exposure uncertainty.
- Hawker (2009), https://doi.org/10.1002/etc.69: prior pulse response and repeated-time retrieval logic.
- Plonka and Tasche (2014), https://doi.org/10.1002/gamm.201410011: general Prony inverse methodology; full text unavailable for this comparison.

Strictly interior rectangular pulses, known coefficients and exactly harmonic elimination rates are required. Noise, nonrectangular environmental exposures, arbitrary kinetics and independent external validation are beyond scope.

Self-review: passed. Independent audit: not yet performed.
