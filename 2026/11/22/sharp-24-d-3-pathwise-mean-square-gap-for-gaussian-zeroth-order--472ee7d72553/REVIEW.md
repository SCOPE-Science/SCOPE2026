# Scientific self-review

## Correctness — PASS
The scope fixes the exact central-difference quadratic identity and dimension-order quantifiers. Conditional rotational invariance proves the radial multipliers are i.i.d.; chi-square expectations give the exact mean-square factor. The critical second-moment polynomial identity is reconstructed from raw moments and checked in `verify.py`. Uniform high-moment and chi-square logarithmic-tail estimates justify Taylor expansion of the expected logarithm, giving coefficient \(2a-48\). Strict Jensen handles the exact mean-square edge. The sign criterion is the strong law, not an inference from finite simulation. The coefficient at equality and any global boundary uniqueness are explicitly unproved.

## Originality — PASS, qualified
The motivating 2026 source establishes the Gaussian mean-square stability operator, **not** the critical logarithmic exponent. The directly relevant published scalar probe-averaging result addresses growing probe count \(n\) in dimension one, so its \(8/n\) formula does not imply the ambient-dimension single-probe \(24/d^3\) law. The norm-normalized high-probability source studies a different update. Broader stochastic-subspace literature was searched and abstract compared; no dominating exact coefficient was located. These checks establish best-knowledge differentiation, not exhaustive priority.

## Value — PASS
At the very stability edge used to tune zeroth-order optimizers, this theorem measures precisely how mean-square diagnostics can misclassify an almost-surely contracting algorithm. The sharp \(d^{-3}\) window is a natural, dimension-dependent reliability invariant for a canonical strongly convex test problem; unlike a mere Jensen inequality it identifies the exact first nonzero constant and an actual opposite-sign regime. The narrowness is an outcome of the mathematics, not an arbitrarily selected parameter slice.

## Closest sources and residual limits
Song et al., *Zeroth-Order Optimization at the Edge of Stability* (2026), §4, Theorem 1, Appendix B.3; Ye (2026), §2–5; *Probe averaging can reverse almost-sure stability in Gaussian zeroth-order descent* (2026), main theorem and proof; Kozak et al. (2020/2021), abstract and search records. An unlocated general product-of-random-matrices theorem could imply the coefficient; no global novelty certification is asserted. Independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
