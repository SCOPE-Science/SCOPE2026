# Review of exact one-bit Brownian occupation sampling

## Correctness — PASS
The target, likelihood, measurement alphabet and loss are explicit. The Gaussian two-sign formula gives the complete conditional mean because a fair sign has only two outcomes. The occupation variance is obtained from a convergent double integral and equals \(1/8\). Two elementary integrations produce the scalar information score \(F\); its strict negative second derivative and positive/negative first-derivative boundary signs prove a unique maximizer globally, including the endpoint exclusion. At the optimizer the nontrivial radical terms cancel, giving the exact risk. The limiting expansions follow from the Taylor expansion of the explicitly defined auxiliary function. The standalone checker reproduced the split integral and the stated constants; random comparisons do not substitute for the analytic proof.

## Originality — PASS, with residual risk
The nearest explicitly inspected primary literature concerns continuous-valued observations on high-frequency meshes (Altmeyer 2017; Ivanovs–Podolskij 2020; Altmeyer–Le Guével 2021) or one-bit channel estimation of Gaussian targets (Fesl–Koller–Utschick 2022). Neither inspected statement supplies the complete time- and signal-to-noise-dependent design for the *nonlinear positive occupation integral* from one sign bit. Classical Gaussian orthant formulas and the arcsine occupation variance are acknowledged prior results and are not claimed as contributions. No identical theorem was identified in targeted literature/index comparisons, but that does not prove unique historical priority; an earlier equivalent under different terminology is a residual risk.

## Value — PASS
The precise choice of one-bit sensing time is a natural finite-information analogue of stochastic occupation quadrature. The theorem answers every finite relative-noise level and provides an exactly quantified information floor: in the noiseless case, just one bit explains more than \(66\%\) of the variance; under vanishing signal-to-noise ratio the favored time converges to \(9/16\), rather than the noiseless \(16/(16+\pi^2)\). The ratio and noise model specify the domain in which this is mathematically and practically meaningful. The result is not a general theorem for all quantizers or noise models.

## Closest literature and limitations
- Altmeyer (2017), https://arxiv.org/abs/1706.03418 : occupation-integral approximation from preselected full observations and asymptotic rates, not one-bit time optimization.
- Ivanovs and Podolskij (2020), https://arxiv.org/abs/2001.02517 : conditional-mean estimators from full high-frequency Lévy data.
- Altmeyer and Le Guével (2021), https://arxiv.org/abs/2108.11632 : high-frequency conditional risk for stable-process occupation and local times.
- Fesl, Koller and Utschick (2022), https://arxiv.org/abs/2212.04470 : one-bit Gaussian channel estimators, not this nonlinear path-functional/time-design problem.

Fixed zero comparator, independent Gaussian prequantization noise with variance proportional to measurement-time variance, exactly one predetermined bit, and an unconditional Bayesian risk are substantive restrictions. Publication-priority searches are not exhaustive. No independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
