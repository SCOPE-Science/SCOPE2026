# Review of the Gaussian cyclic Gabor hard-edge law

## Correctness
PASS. The exact Fourier orthogonality calculation decomposes the original operator into cyclically neighboring two-by-two Gaussian Gram matrices, retaining the nontrivial boundary coordinate swap. The square complex Wishart density gives a single-block exponential survival law with exact rate four. A conditional Gaussian argument bounds adjacent simultaneous small eigenvalues by \(O(\varepsilon^2[1+|\log\varepsilon|])\). Arratia--Goldstein--Gordon dependency-graph approximation then yields the Poisson law and fixed-threshold error; an independent matching gives uniform exponential tails and all positive moments. Direct complete-matrix checks and statistical diagnostics reproduced the expected structure and scale. Finite tests do not substitute for the proof.

## Originality
PASS relative to the specified comparison set, with publication-priority uncertainty. The 2026 primary source proves block equivalence but no Gaussian hard-edge law; the 2019 and 2025 random-Gabor sources give frame-bound estimates in different settings, not the rate-four Poisson limit for one-dependent cyclic blocks. Classical complex Wishart results determine an individual two-by-two block but not the cyclic minimum. A previous computation of the same model's logarithmic determinant does not imply the extreme lower frame bound. Scientific comparisons cover exact formulations, stronger possible consequences, table-level matches and source inspections in `AUDIT.json`. Residual risk: a differently indexed sliding-window Gaussian extreme-value paper could cover the result.

## Value
PASS. The smallest frame-operator eigenvalue directly governs noise amplification by canonical-dual reconstruction, unlike volume-only summaries. Its dimension-dependent scaling, explicit exponential law, quantitative rare-event count, and complete positive-moment limit identify a sharp stability regime in a natural critically sampled Gaussian Gabor design. The shared window creates real short-range dependence that must be handled, not a purely independent-block exercise. The result is limited to the stated model; no universality or global condition-number theorem is inferred.

Self-review: passed. Independent audit: not yet performed.
