# Review of sharp phase-count and order-cost barriers

## Correctness — PASS

The polynomial-cutoff witnesses satisfy global boundedness, real-on-real values, and holomorphy near the evaluation point. The roots-of-unity identity gives the two exact random variables before any asymptotics. Gaussian tails make the cutoff negligible for fixed polynomial order. Hermite orthogonality eliminates the lower-order mean, and the standard Hermite product formula gives the exact positive coefficient. The source's already-proved sufficiency for adequate phases completes the uniform if-and-only-if claim. For the sample-cost part, Gaussian integration by parts, the Hermite product identity, binomial–Legendre identity, and a one-endpoint Laplace expansion establish the claimed coefficient and exponential base. The extracted exact-arithmetic checker passes 1721 tests. Finite checks do not substitute for the all-order arguments.

## Originality — PASS, with remaining risks

The primary preprint [1] already proves the adequate-phase sufficiency and gives a general leading variance expression, and it explicitly presents root-of-unity aliasing. These facts are *not* counted as original. The comparison concerns the sharper **necessary** phase count under the paper's full bounded local-analytic assumption, its exact undersampling blowup coefficient, and the sharp asymptotic exponential sampling barrier for derivative order on a normalized and admissible witness. Theorem 5 of [1] is at fixed order and does not assert this necessary side or its evaluated derivative-order cost. Deterministic circular coefficient extraction [2] controls roundoff, not independent Gaussian probe variance; stochastic Taylor-mode differentiation [3] uses a different estimator. No matching joint theorem was located in the checked sources, but an unindexed equivalent derivation or general Gaussian-polynomial moment calculation may exist. The associated identities are classical and not claimed as new.

## Value — PASS

The phase-budget threshold makes a published sufficient condition sharp within its exact admissible class, and the explicit large-order base distinguishes variance stability as smoothing tends to zero from the statistical cost of raising derivative order. The latter is practically relevant when deciding whether increasing phase count can substitute for more independent probes: in this witness it cannot. The result is not a lower bound for every estimator and makes no general claim about trained PDE solvers.

## Closest literature and limitations

[1] S. Fang, X. Wang, H. Zeng, T. Zhou, *Variance Stable Gaussian Smoothing Estimator for Arbitrary High-order Derivatives*, arXiv:2611.19909v1, https://arxiv.org/html/2611.19909v1 (full original paper examined, especially §3.2, Theorem 5 and proof).

[2] F. Bornemann, *Accuracy and Stability of Computing High-Order Derivatives of Analytic Functions by Cauchy Integrals*, arXiv:0910.1841, https://arxiv.org/abs/0910.1841 (introduction and deterministic stability framework examined).

[3] X. Shi et al., *Stochastic Taylor Derivative Estimator*, arXiv:2412.00088, https://arxiv.org/abs/2412.00088 (abstract-level comparison only; full text not obtained in this review).

Self-review: passed. Independent audit: not yet performed.
