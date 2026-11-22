# Scientific assessment — survival-conditioned entrance localization

## Correctness
**PASS, self-review.** The proof begins from the exact killed Bessel kernel, not an assumed conditional entrance distribution. The two-index Fourier representation yields uniform microscopic and diffusive Gaussian estimates and exponential off-diagonal control. Those inputs justify three separately normalized summation regimes, the terminal tightness needed for joint independence, and the counting-measure dominated convergence for the finite-state limit. The `checker.py` program passed 3,622 exact-rational and numerical assertions; an independent numerical comparison using `numerical_check.py` showed the predicted movement toward the three limit laws. Finite computations do not replace the infinite-limit proof.

## Originality
**PASS against inspected evidence; historical-priority risks remain.** Pollett's full 2026 paper establishes the killed chain's quasi-stationary attraction and its endpoint/survival asymptotics, while the new claim determines the *initial state of a successful long survivor* and its joint independence from the terminal state. The classical birth–death QSD work of van Doorn includes fixed/finite initial support; an available same-model marginal result likewise does not establish a conditional entrance law. Literature searches of similar claims and equivalent formulations did not find a statement covering all three entrance phases. The full texts of related drifted-Brownian and general birth–death sources were not accessible; their abstracts cannot establish noncoverage. A broad ratio-limit theorem may supply an alternative route and represents a genuine residual priority risk.

## Value
**PASS.** The phase boundary is mathematically natural: a survivor-size-biased initial distribution becomes nonnormalizable exactly at the exponent two. The new theorem explains *where a long-surviving trajectory typically began*, not merely how long it survived or where it ends. Its critical logarithmic-uniform entrance spans every polynomial scale, a qualitatively different behavior invisible to marginal quasi-stationary limits.

## Scope and limitations
Rates and the polynomial tail exponent are fixed, and the starting distribution is exactly critical-geometric with a power correction. No extension to general slowly varying corrections, time-dependent parameters, path-space limits, uniform error rates, independent verification or exhaustive historical priority is asserted. The optional numerical checks are corroborating only.

Self-review: passed. Independent audit: not yet performed.
