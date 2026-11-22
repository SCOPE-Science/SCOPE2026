# Scientific review

## Correctness — PASS
The observation model and Gaussian conditioning yield exact risk reduction \(J/(V+\eta)\), with two cross-covariance kernels independently integrated in `verification.py`. For the displacement mode, the derivative numerator factors through a strictly decreasing positive polynomial and a strictly increasing sign-changing polynomial, proving a unique optimal time and the exact terminal threshold \(11/336\). For velocity sensing, the two competing derivative factors define a strictly increasing time-to-noise map on a short interior interval, proving uniqueness for every positive variance. The optimized-gain logarithmic ratio strictly decreases because the maximum displacement observation variance is \(1/12\) whereas every velocity-optimal observation variance exceeds \(6/25\). Exact endpoint comparisons bracket the unique modality switch; exact rational Bernstein coefficients isolate the algebraic root. Numerical quadrature is supplementary, not a substitute for the infinite-parameter proof.

## Originality — PASS on inspected evidence, with residual risk
The first focal source, Lachal (2011; arXiv:1108.2132v1), explicitly covers integrated Brownian bridges, their covariance and conditional prediction but does not state a choice between noisy displacement and velocity measurements or the all-noise unique threshold. Ji and Müller (2016; arXiv:1604.05375v1) give the general posterior-risk design objective, not the explicit competition or strict single-crossing theorem. Mukherjee's dissertation abstract addresses product-covariance design, including Brownian bridge itself, but does not settle this non-product integrated-bridge, dual-mode comparison; only the abstract was accessible. Related derivative-only timing is not claimed as new. The distinct cross-modality comparison is not implied by the earlier time-only classification without the new envelope-variance ordering and exact endpoint comparison.

Residual originality risks include equivalent results under another description of integrated Brownian-bridge mixed-mode sensing and unexamined full dissertation content. A literature search is not a proof of absolute novelty.

## Value — PASS
The two-sensor-type choice is a natural resource-limited sensing question for a differentiable random trajectory: a device can measure displacement or its instantaneous velocity, with calibrated additive noise. A complete design rule identifies a continuous approach to terminal placement followed by a genuinely discontinuous switch in observation type and time. The one-way switching law is derived from a structural variance separation, rather than numerical parameter sweeping, and the exact polynomial/crossover make the result reusable as a benchmark. The result is scoped to common calibrated noise; it does not assert hardware-independent preferences under arbitrary unit conversions.

## Verification and independence
`verification.py` passed exact symbolic, rational interval, quadrature and numerical stress checks. Remaining questions concern publication priority, applicability beyond the model, and external proof review.

Self-review: passed. Independent audit: not yet performed.
