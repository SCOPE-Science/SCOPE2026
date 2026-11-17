# Independent mathematical audit

## correctness

PASS

The exact Gaussian modal transition Y_j^+=cos(jT)Y_j+sin(jT)ξ_j gives Hermite-quadratic eigenvalues ρ_j=E cos²(jT), γ_ij=E cos(iT)cos(jT). Cauchy–Schwarz bounds every |γ_ij| by ρ*=max_jρ_j and hence maximizes IACT at ρ*. Nonnegative Fejér-square identity for N=K+1 forces max_j E cos(2jT)≥−1/K. Uniform nontrivial N-th roots with T=mπ/N attain the bound while satisfying E T=π/2; saturation forces all c_j=−1/K, grid support, symmetric weights 1/K by discrete Fourier inversion and the listed antisymmetric mean constraint. For K≤3 the constraint kills all antisymmetric degrees, while for K≥4 there are nonzero feasible small perturbations. Boundary K=1 yields IACT=1, and persistent modes are assigned infinity. The source verifier code and analytic argument were inspected; finite K=1..18 spectral diagnostics do not prove the universal bound.

## originality

PASS

An exact, practically motivated finite-dimensional trigonometric design classification for all centered quadratic probes, including a sharp uniqueness-to-degeneracy transition.

## value

PASS

Sharp cost-constrained design of randomized ideal HMC durations for a fixed arithmetic multimodal Gaussian target; exact global minimax value and all optimizing measures are natural structural data, beyond routine reproduction of Fejér inequality. Limited to exact integration, quadratic observables and fixed mean integration time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
