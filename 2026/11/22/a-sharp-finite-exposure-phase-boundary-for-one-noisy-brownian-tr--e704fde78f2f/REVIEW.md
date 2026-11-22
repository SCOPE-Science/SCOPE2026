# Mathematical review

## Correctness — PASS

The model explicitly fixes one boxcar-averaged Brownian observation, independent Gaussian noise of positive variance, the admissible exposure starts, and integrated posterior variance. The three-piece covariance integral yields the claimed cubic \(N_h\). Maximizing \(N_h(t)/(t+h/3+\eta)\), its derivative numerator \(P=N_h'(t)(t+h/3+\eta)-N_h(t)\) satisfies \(P'=2(1-h-2t)(t+h/3+\eta)\). This derivative has a single turning point, and its strictly positive start and explicit endpoint value prove both uniqueness and the sharp interior-to-terminal transition for every admissible \(h,\eta\), including equality at threshold. The noise monotonicity and the zero-width limit are proved, not inferred from finite sampling. Symbolic identities, rational root isolation and independent numerical quadrature were replayed. Remaining correctness risk is limited to the exact stated Brownian/constant-noise normalization; other sensing models are not claimed.

## Originality — PASS on inspected evidence, qualified

The relevant primary texts were read for claims in the same or a covering formulation: Nguyen and Peraire (2014) provide linear-functional Gaussian-process conditioning; Ji and Müller (2016) optimize noisy point-location trajectory recovery; Longi and coauthors (2020) optimize sensor geometry for integral observations of spatial Gaussian processes. The exact scalar Brownian finite-exposure global optimizer and the phase threshold are absent from the inspected results and not an immediate stated corollary of the general formulas. Database searches included moving averages, boxcar windows, Gaussian linear functionals, integral sensors, and noisy trajectory reconstruction. Indexed neighboring findings involve Brownian point observations, random point quadrature or different Gaussian-process models, not this single fixed-width observation theorem. The non-appearance of an exact match does not prove absolute originality: an unindexed or alternative-name treatment may exist, especially in integral-observation optimal design.

## Value — PASS

Fixed-duration averaged measurements model instruments with nonzero exposure time. Exact design can choose between a window away from the endpoint and one touching it; a narrow, parameter-dependent transition cannot be resolved by the usual informal prescription to sample as late as possible. The algebraic width frontier, explicit noise threshold, strictly increasing interior solution and singular point-sampling limit provide precise calibration and regression tests in Gaussian trajectory monitoring. This is a natural full-classification result for a motivated two-parameter family, not an arbitrary finite numerical table. It does not claim to solve variable-duration or multiple-sensor design.

## Limits of literature and reproducibility checks

No independent scientific audit or originality certification has been performed. General linear-functional formulas alone do not supply this theorem's root analysis. The included checker depends on SymPy and SciPy, and its finite numerical samples are corroboration only; exact symbolic identities and the displayed analytic proof carry the unlimited-parameter claim. Other noise-normalization conventions may change the threshold.

Self-review: passed. Independent audit: not yet performed.
