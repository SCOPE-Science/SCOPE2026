# Self-review

## Correctness — PASS

The all-dimensional proof follows from the exact discrete Gaussian Lyapunov sum, the equivalence between stable symmetric drifts and symmetric roots of \(I-2hC^{-1}\), the spectral-projection parameterization, the minimax endpoint-step argument, and cancellation between two known step-size precision matrices. The finite-time statement follows from \((I-hA)^2=q^2I\) for two spectral bands at the minimax step. The supplied exact-rational program verifies 690 finite identities and exact recurrences, not the general theorem itself.

## Originality — PASS, qualified

Kirsten et al. (arXiv:2608.09743, August 10, 2026) derive the Euler covariance recurrence and analyze a first-order gradient interpretation. That recurrence is prior evidence, not claimed as new. Their first-order covariance learning-rate optimum is \(1/(a+b)\), whereas the present blindness point \(2/(a+b)\) optimizes the exact Euler transition; the different rate criteria are not conflated. Aifer et al. (arXiv:2308.05660) solve the continuous-time thermodynamic inverse. Singh et al. (Phys. Rev. E 98, 012136) use full time-series observations; van Seeventer and Salehkaleybar (arXiv:2603.08311) treat continuous-time causal edge signs with unknown diffusion. Targeted searches of mathematical findings identified nearby sign-splitting and harmonic-equilibrium bias results but no covering theorem for the stated fixed-step SPD Euler inverse fibers or fastest-step full snapshot collapse. Scalar AR(1) sign ambiguity is standard. Full texts of some possible ancestors were not inspected, and historical priority is not independently settled.

## Value — PASS

A fastest-relaxing Euler discretization of a two-eigenvalue SPD matrix produces exactly the same isotropic Gaussian marginals from zero for a continuum of matrices with different eigenspaces. This can erase the very anisotropy sought in covariance-based inversion despite stable and rapid relaxation. The full inverse-fiber classification and two-step-size formula give exact theoretical tests for this failure and its remedy; neither high-dimensionality nor an arbitrary parameter slice is required for the issue to occur.

## Scope and residual risks

The result concerns known isotropic diffusion, stable SPD Euler drifts and population covariances. It does not determine joint trajectory equivalence or empirical estimator conditioning. The derivation uses known Lyapunov and spectral facts and does not assert that those facts themselves are original. Partial access to prior full texts leaves qualified literature-priority risk.

Self-review: passed. Independent audit: not yet performed.
