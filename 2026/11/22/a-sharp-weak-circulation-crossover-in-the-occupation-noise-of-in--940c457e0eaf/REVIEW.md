# Scientific assessment: weak-circulation occupation noise

## Correctness — PASS

The statement fixes the order of limits, the nonnegative interaction range and the exact logistic jump intensities. A globally dissipative mean-field quadratic functional proves concentration around the uniform state for all repulsive interactions, not just small perturbations. The stationary generator and fourth-moment bounds justify the stationary OU limit. Circular Fourier diagonalization yields the all-lag covariance and integrated variance; a summable Fourier bound and the standard hyperbolic-cotangent partial fraction identity prove the large-ring crossover. The independent matrix checker passed 1,554 numerical assertions, including finite-difference nonlinear drift tests. These computations corroborate but do not replace the analytic proof.

## Originality — PASS, qualified

The Gaussian stationary approximation, linearized Fokker–Planck equation, three-urn oscillatory eigenvalues, and four-urn static covariance are already established by Cheng and Lai (2021, 2024). This result does **not** claim those facts to be new. The specific finite-ring long-window occupation-noise coefficient, strict directional-bias suppression, and its \(M^{-1}\) hydrodynamic bias crossover have no covering statement in the inspected primary papers. Exact published versions of a general biased circulant Markov-chain Poisson theorem could imply some algebra; independent priority assessment remains important.

## Mathematical value — PASS

Time-averaged occupation estimates are a natural way to measure mixing and precision in the interacting urn/Potts model. The equality of all static Gaussian covariances across irreversible biases conceals a sharp and measurable change in integrated temporal noise. The explicit nontrivial hyperbolic-cotangent function identifies the dimension-dependent bias scale at which this change occurs, rather than an arbitrary parameter slice or a recomputation of a known covariance table.

## Literature and limits

Compared closely with Cheng and Lai, arXiv:2106.00915 (2021), Sections IV–V and Appendix A; arXiv:2401.02632 (2024), Sections 2–5; and arXiv:2403.15708 (2024), Sections III–V and especially IV on Gaussian fluctuations. The journal abstract of Phys. Rev. E 101, 012123 (2020) was also consulted as background only. The theorem covers \(g\ge0\) and sequential limits; it does not claim an exact finite-particle covariance, a general attractive-regime result or a simultaneous particle/time/urn limit.

Self-review: passed. Independent audit: not yet performed.
