# Scientific review

## Correctness — PASS

For each of the two specified stationary Gaussian-process kernels, the conditional variance of the origin derivative after two noisy symmetric observations equals \(1-2g(h)^2/[1+\eta-k(2h)]\). The two exact reductions become \(E_G(z)\) with \(z=h^2\) and \(E_M(z)\) with \(z=h\). Both derivatives have the identical sign of \((1+\eta)(1-z)e^{2z}-(1+z)\). The critical function \(F(z)=(1+z)e^{-2z}/(1-z)\) increases strictly from \(1\) to infinity on \((0,1)\), while both gains decrease beyond \(1\). Their unique global maximizers give the duality and optimal risks. Checked algebraically through five exact SymPy identities and numerically through 96 independent covariance/radius tests; infinite-domain claims are proved analytically.

## Originality — PASS, provisional

The fully inspected 2019 noisy gradient-estimation paper studies estimator guarantees under smooth-objective models, not exact two-prior Gaussian-process derivative posterior designs. The fully inspected 2020 Gaussian-process differential-equation paper uses conditional derivative regression but does not derive the shared stationarity equation or squared-radius identity. The closest accessible mathematical-results entries concerned noisy two-site kernel quadrature and deterministic finite-difference noise rather than the two-kernel posterior derivative optimization. A relevant further covariance paper was not accessible in full text, and historical priority requires independent review. The generic Gaussian conditional-variance formula is acknowledged as known; the new assessed claim is its two-kernel global optimizer coincidence, strict risk ordering, and asymptotic design exponents.

## Value — PASS

This identifies an exact, noise-adaptive sensor spacing rule for derivative inference, a natural and practically motivated two-query design problem, across two classical smoothness assumptions. The squared-radius relationship and the change from a one-third to a one-sixth small-noise spacing exponent show that smoothness profoundly changes the optimal geometric resolution even though the two scalar optimization equations unexpectedly coincide. The theorem is not an arbitrary numeric optimum: it holds for every positive noise level, includes strict global uniqueness, and supplies exact risks. It does not purport to optimize unrestricted asymmetric designs.

## Closest literature and limits

Berahas, Cao, Choromanski, and Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization* (arXiv:1905.01332v1, 2019), treats noisy gradient sampling radii. Zhou and Wang, *Inferring the unknown parameters in Differential Equation by Gaussian Process Regression with Constraint* (arXiv:2011.10971v1, 2020), supplies conditional Gaussian-process derivative methodology. Neither inspected article states the two-kernel global equivalence or its risks. A complete literature priority guarantee is not given.

Self-review: passed. Independent audit: not yet performed.
