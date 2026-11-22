# Scientific review: dimer-covering spatial covariance

## Correctness — PASS

The accepted-edge criterion follows from the first Poisson arrival at each edge: it is successful if and only if at least one neighboring edge has not already arrived. This yields a local four-clock representation for each site multiplicity. Exact conditioning/integration gives the accepted-edge covariances at separations zero, one and two, from which the displayed site covariances and sharp three-step dependence follow. The strict signs and strictly positive asymptotic variance are certified by positive Bernstein coefficients. A bounded stationary three-dependent central limit theorem establishes the Gaussian law. The independent, exhaustive rational checker in `verify.py` confirmed the polynomial coefficients and terminal values.

## Originality — PASS, with residual priority risk

Krapivsky (2022, arXiv:2209.03992, Sections II–III and VI A) contains the deposition model, total deposited-count statistics and one-site dimer probabilities, but not the all-time pair-multiplicity covariance table. Viot and Krapivsky (2024, arXiv:2410.12373, Sections 2 and 7) focus on selected joint states sufficient for one-site occupation densities and explicitly identify pair correlations as future work. A separate published 2026 trimer result gives *terminal triple-coverage indicators*, not the all-time dimer multiplicity counts, so neither its quantified laws nor its Gaussian variance dominate the present claim. The generic first-arrival localization and finite-dependence CLT are older tools and are not represented as new. Relevant sources were inspected and exact semantic overlap compared; unindexed literature may still contain the result.

## Mathematical value — PASS

The source literature identifies spatial correlations as a natural missing observable. Here a complete time-uniform positive–negative–positive correlation profile and sharp dependence range give information absent from single-site coverage probabilities. The exact covariance sum determines macroscopic fluctuation noise at any fixed deposition time, rather than only the final mean. The spatial sign pattern is non-obvious and physically distinguishes shared-edge positive coupling from intermediate-range anticorrelation; the fact remains informative even without an extension to longer rods.

## Limitations

The result is about a single observation time and multiplicity counts under homogeneous independent Poisson proposals on the infinite integer line. It is not a general result about all deposition geometries or binary covered/uncovered events. Saturated total-count fluctuations were studied previously, and priority against all unindexed research remains unverified. The checker certifies finite algebraic identities; the infinite-volume and Gaussian arguments are proved mathematically, not by sampling.

Self-review: passed. Independent audit: not yet performed.
