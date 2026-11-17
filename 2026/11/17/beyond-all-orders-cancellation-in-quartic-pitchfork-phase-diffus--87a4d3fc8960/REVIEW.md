# Scientific review: quartic pitchfork phase diffusion

## Correctness — PASS

The stationary quartic Langevin diffusion is reversible and confining. Its odd-observable Poisson equation has the explicitly differentiated solution stated in `RESULT.md`; the stationary martingale decomposition yields the variance rate. The identity for the complementary error function is derived by the substitution \(u=y^2\). With \(\lambda>0\), the well partition function and saddle numerator have identical complete Gaussian coefficient sequences \(a_k=(4k)!/(16^k(2k)!k!)\). Uniform tail controls suppress every off-saddle contribution faster than a fixed algebraic power. Therefore the ratio has no inverse-power corrections at any order. Finite rational checks and direct quadrature in the included script corroborate, but do not substitute for, the analytic argument.

## Originality — PASS within inspected evidence

The 2007 Kalmykov–Coffey–Titov paper already provides the full integral relaxation-time formula for the same quartic potential and its first high-barrier correction; this general formula is explicitly credited. The 2022 Weis et al. paper provides the critical variance constant and telegraph description; the 2023 Shmakov–Littlewood paper provides the phase-coupling model and scaling. The narrowly claimed novelty is the all-orders vanishing of the *unnormalized phase-variance-rate* algebraic corrections, a cancellation not located in the primary presentations or targeted literature and semantic database searches. Because a prior exact integral expression implies the new asymptotic after further nontrivial manipulation, this is a real priority caveat, not proof of uniqueness. See `AUDIT.json` for precise implication comparisons.

## Mathematical value — PASS

A phase-diffusion observable central to noisy limit-cycle coalescence has a much sharper large-barrier scaling law than the usual leading Kramers estimate, because two individually nonzero infinite sequences of corrections cancel. The cancellation is structurally specific to the quartic odd-observable problem and provides a stringent analytical benchmark for rare-switching models. It is not a generic textbook inference from a leading-order escape rate. Neither an optimal exponential remainder nor a broader potential class is asserted.

Self-review: passed. Independent audit: not yet performed.
