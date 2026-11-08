# Review: two-sided Gumbel edge layers in a switching harmonic gas

## Correctness

**PASS.** The conclusion applies to the exactly stated stationary two-state harmonic model with strictly ordered positive stiffnesses and fixed positive switching rates and diffusion. The known positive, normalized beta-weighted Gaussian-variance mixture is reproduced with the source's normalization; conditioning gives an exact finite-population CDF. A corrected Gaussian maximum centering and two local variance-coordinate changes produce the two endpoint fractional-Gumbel integrals. Normal Mills estimates supply integrable domination off the endpoint windows. The rare-event posterior statements follow by testing the same integrals against bounded continuous functions. A separate logarithmic threshold sandwich gives the lower unshifted endpoint, while Mills' rare-tail approximation and a gamma integral give the upper unshifted endpoint. The factor of \((\log N)^{-1/2}\) and the \(\log\log N\) enhancement are separately justified. The included numerical script passed 66 assertions but is not treated as proof of an infinite limit.

## Originality

**PASS, with residual literature risk.** The exact conditional Gaussian mixture and compact leading support are established in Biroli et al. (arXiv:2312.02570); they are not claimed here. The 2023 general conditional-i.i.d. paper (arXiv:2307.15351), especially Section III.2.1, gives the leading Gumbel-class concentration but not the boundary-layer fractional integrals, their posterior environmental laws or the asymmetric unshifted-edge exponents. The 2025 experimental follow-up (arXiv:2508.07199) provides exact finite-sample order-statistic representations, not the stated singular endpoint limits. A 2026 article on simultaneous *instantaneous* resetting (arXiv:2606.31634) discusses slow harmonic extreme-edge resolution in a different process; the full text was not accessible in this review, and general upper-edge overlap remains possible. Semantic literature and record searches returned no equivalent or stronger statement for the two-stiffness model. Absence of a match is not a proof of global priority.

## Mathematical value

**PASS.** The source's large-population maximum law gives a finite interval of support despite unbounded individual Gaussian positions. Its finite-size violation is therefore a motivated physical question, not an arbitrary parameter slice. The two edges have genuinely different asymptotic mechanisms and constants, and the posterior localization formulas identify which hidden trap-variance configurations generate rare observed extremes. These conclusions are not numerical recitations of a finite-\(N\) integral and provide testable asymptotic predictions in principle. They do not establish practical detection at experimentally available small populations.

## Limits and closest literature

The analysis is confined to one-dimensional stationary signed-position maxima under common positive two-state stiffness switching, with independent Brownian particle noises. It assumes fixed parameters and exact probabilistic measurements, and does not establish convergence-rate inequalities, parameter-coalescence limits, hydrodynamic robustness, or independent verification. Closest accessible full text: arXiv:2312.02570, arXiv:2307.15351, arXiv:2508.07199. Relevant but not fully inspected: arXiv:2606.31634.

Self-review: passed. Independent audit: not yet performed.
