# Scientific review

## Correctness — PASS

The scalar AB2 coefficients follow by linear interpolation of the two derivative values. Multiplication of the two exact companion matrices gives the trace and determinant, and the three factored real Schur criteria yield the strict boundary \(a+b<2\), including the unit-root equality case. In the stable domain, the periodic covariance solves an ordinary discrete Lyapunov equation. The singular small-step law follows by scaling that equation by \(a^2\), taking the proven stable matrix limit, and explicitly solving the limiting Lyapunov equation. The positive coefficient proves sharp divergence. The standalone symbolic verifier checks symbolic identities, rational covariance equations and the particular \(b=1\) formula; finite checks do not replace the general proof.

## Originality — PASS, with precedence risk

The closest directly inspected literature gives variable-step Adams implementations, step-ratio coefficients, high-order conservative multirate formulas, and adaptive AB3 in PDE computations. No inspected primary source establishes the specific joint period-two real-decay spectral criterion and the stationary additive-noise variance singularity with its exact coefficient. General Lyapunov theory provides a framework but does not supply the AB2 step-ratio cancellation or the scaled singular covariance coefficient without additional analysis. Earlier Nordsieck stability work is important prior art for the stability component; its directly available material was only metadata and abstract, leaving an explicitly documented specialist precedence risk. No claim of novelty is inferred merely from search absence.

## Value — PASS

For a standard variable-step integrator the spectrum can give a reassuring ratio-insensitive decay interval while independent local perturbations experience unbounded stationary amplification. The sharp \(a^{-2}\) divergence and coefficient quantify that diagnostic failure for every fixed nondegenerate long step. This is a motivated boundary for interpreting adaptive-step stability tests, not an arbitrary numerical slice. The result does not equate the idealized additive forcing with actual hardware floating point.

## Closest literature and limitations

Throwe–Teukolsky (arXiv:1811.02499) supply the motivating variable-step Adams framework. López–Romay (DOI 10.1155/2010/765620) study preassigned step ratios and implementation costs. Tavakkol–Son–Lynett (arXiv:1909.04153) study adaptive AB3 for PDEs. Skeel–Jackson (DOI 10.1137/0720056) and Calvo–Lisbona–Montijano (DOI 10.1137/0726052) address variable-step Nordsieck stability, but their full text was not obtained and remains a precedence risk. Model scope and its non-Gaussian finite-variance noise assumption are stated in the result.

Self-review: passed. Independent audit: not yet performed.
