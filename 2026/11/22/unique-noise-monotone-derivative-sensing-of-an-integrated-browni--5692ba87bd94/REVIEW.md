# Scientific assessment

## Correctness — PASS

Exact piecewise covariance integration recovers \(F(t)=t^2(1-t)^2(8-4t-t^2)/60\), with denominator \(\eta+t(1-t)>0\). Differentiating this rational function produces the claimed polynomial one-crossing equation. The root brackets for \(\beta\), exact formula for \(\alpha\), and sign analysis of \(A\), \(B_*\), and their derivatives establish global uniqueness for every positive noise level, including endpoints. Implicit differentiation gives strictly positive time sensitivity to noise. The endpoint objective is a strictly increasing function of \(t(1-t)\), so its midpoint optimum is unique. The independent quadrature and symbolic checker passed 87 assertions. Numerical trials are not the proof.

## Originality — PASS on inspected evidence, with residual risk

Lachal (arXiv:1108.2132v1), sections 1, 4.4 and 5, characterizes integrated Wiener bridges via terminal derivative conditioning and gives a predictor decomposition; it does not give the present single noisy, movable interior-derivative sensor theorem. Šimák (2002), section 4.1 and chapter 5, provides the integrated mean-square derivative-observation criterion for primarily stationary kernels but not this particular nonstationary bridge optimization. Ji and Müller (arXiv:1604.05375v1), sections 1–3, use noisy **same-process** point observations, not observed derivatives of an integrated bridge. Schober et al. (arXiv:1406.2582v1), introduction and derivative-data construction, addresses ODE solvers, not global sensor placement. Close indexed results on bridge quadrature and noisy bridge trajectory recovery concern different observation operators and targets. General covariance-conditioning principles alone do not state the all-noise unique root or strict separation from optimal terminal-area sensing. Mukherjee's relevant historical path-design dissertation is available only through an abstract in this inspection; this unresolved priority risk is explicitly retained.

## Value — PASS

This is a natural, fully classified one-budget sensor design: a derivative sensor records the bridge level while the quantity of interest is the cumulative trajectory. Path recovery and terminal-area recovery genuinely demand **different** sampling times at every positive noise level, even though both are posterior variances built from the same prior and datum. The proof characterizes the precise allowed interval and monotone transition, rather than a single parameter substitution or isolated calculation. The practical gain relative to a midpoint sensor is modest, so usefulness is a qualitative design diagnostic, not a claimed large performance improvement.

## Limitations

One sensor, fixed homogeneous Gaussian noise and standard unit-bridge prior; no claim for broader designs. Publication priority cannot exclude uninspected historical text or unindexed equivalent findings. Verification is self-review, not external certification.

Self-review: passed. Independent audit: not yet performed.
