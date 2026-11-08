# Scientific review: curvature-dependent parabolic Fourier Smith invariants

## Correctness — PASS

The claimed matrix is exactly the dot-product Fourier kernel between the parametrized curves. The nonzero-coordinate multiplicative-character change of basis is integral and invertible because its inverse requires only division by \(p-1\), a local unit. The transformed matrix comprises a two-dimensional origin/constant block and a permutation-diagonal block. Every coefficient below the proposed leading cyclotomic order is divisible by \(p\), and the identified leading coefficient is nonzero modulo \(p\); since \(v_\pi(p)=p-1\), no cancellation from earlier coefficients is possible. The flat case follows independently from a Newton-Vandermonde reduction. Exact truncated-ring elimination for 20 cases corroborates the symbolic proof. No numerical experiment is used as an infinite proof.

## Originality — PASS, bounded comparison

The closest inspected primary sources are Mockenhaupt–Tao (arXiv:math/0204234), Iosevich–Koh (arXiv:0804.4505), and Li (arXiv:2609.16030). The first two establish Fourier restriction estimates for quadratic varieties, not local Smith divisors of a square parabolic self-restriction. Li's parabolic sparse-zero theorem concerns the whole frequency plane and support sizes at most \(p-1\), not the exact full-support matrix and arithmetic invariant factors. The full mathematical record *Complete exponential spectra of the parabola over odd prime-power rings* classifies orthonormal exponential bases by character orthogonality, a different requirement from general invertibility and local Smith factorization. Related conic Fourier results use distinct multiplicative conics and do not imply the curved/flat parabolic dichotomy. The local binomial-jet technique itself is standard; the asserted claim is the complete arithmetic profile for this precise natural square sampling family. Residual priority risk: a broader unpublished or historically unlocated exponential-sum valuation theorem might imply it.

## Mathematical value — PASS

Simultaneously restricting spatial support and frequency samples to two natural quadratic graphs is a critically sampled Fourier interpolation problem. Beyond nonsingularity, the result determines all local invariant factors and the precise arithmetic reconstruction loss; the sharp change as either curvature vanishes gives an intrinsic geometric boundary. The prime-uniform classification is a natural exact invariant, rather than an arbitrary numerical example or a reparametrization of a known rank table. It does not yield numerical complex condition numbers or arbitrary-curve interpolation.

Self-review: passed. Independent audit: not yet performed.
