# Review of the stationary stormwater export covariance theorem

## Correctness
**PASS.** The two-sided affine series converges in \(L^2\) because \(\mathbb E(1-F)^2<1\), providing existence and coupling uniqueness. The stationary second-moment equation and independent calculation of consecutive exported-load covariance agree algebraically. Conditional expectation supplies the geometric dependence at all lags. Both correlation-bound factorizations have nonnegative numerators on the full stated parameter domain. The accompanying code was executed from its actual location and its rational and finite-simulation diagnostics passed. Simulations are not used as infinite proofs. A zero exported-load variance is excluded from correlation statements.

## Originality
**PASS relative to inspected evidence, with remaining risk.** The closest inspected hydrological texts are Chen and Adams (2006), which treats distributions and mean loads; Botter (2010), which treats autocorrelation of continuous streamflow under stochastic recession rates; and Al Ali, Bonhomme and Chebbo (2016), which treats event-to-event residual pollutant stock and model calibration. The published stochastic wash-off study by Daly, Bach and Deletic (2014) was located but only its abstract was accessible; its uninspected full text is a residual priority risk. No accessible inspected primary text or published result in the searched scientific database was found to cover the explicit all-lag event-export sign transition and its two sharp universal bounds. Generic random-coefficient storage methods underlie the proof and must not be represented as new.

## Value
**PASS.** The distinction between the sign of autocorrelation in a retained pollutant stock and that in actual event exports is a motivated interpretive issue for stormwater monitoring. The theorem gives an exact distribution-free moment threshold, shows that the sign does not depend on event lag, and provides sharp lower and upper correlation envelopes. In the periodic-input case the negative envelope becomes independent of removal-fraction variance, giving a concrete structural diagnostic. No claimed field applicability exceeds the independent, linear, stationary model.

## Scope and limits
Independence of removals from accumulated mass and dry-weather addition, stationarity, a finite second moment, and the event-count sampling scale are essential. Contaminant loss between events, nonlinear saturation, correlated rain depth and wash-off, or nonstationary forcing can invalidate the equations. The closest inaccessible primary text is named, not inferred to be noncovering. The outcome is a self-review, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
