# Scientific review

## Correctness — PASS

For every sampled step strictly inside \((0,2)\), the numerical update is elliptic, determinant-one and preserves the explicit positive form \(G_h\). The symmetric covariance transfer is positive; its nonzero cone Perron eigenmatrices and dual eigenmatrices must be positive definite because an elliptic matrix has no real invariant line. Strict Jensen equality for \(\log\det\) forces a shared quadratic invariant if the spectral radius is one, and distinct steps cannot share such an invariant. A dual eigenform then gives uniform two-sided exponential energy bounds for every nonzero initialization. For binary jitter, exact symbolic matrix computation verifies the transfer, characteristic determinant and first nonvanishing perturbation coefficient. The packaged verifier's 75 checks passed. The proof's domain, quantifiers, and the distinction between mean-square and pathwise growth are explicit.

## Originality — PASS (with stated residual risk)

Abdulle–Garegnani [1], inspected in the actual preprint including its randomized-step definition and energy theorem, proves finite-time mean-energy accuracy under variance scaling but not the fixed-jitter infinite-horizon Perron factor. Richardson–Finn [2], inspected in original full text, treats deterministic time-varying steps and resonance conditions, not iid step laws. The closely related continuous-time parametric-noise literature [4] is broader in physical phenomenon but does not state this explicit discrete symplectic-Euler calculation in the accessible abstract; its full text was not available for comparison. Thus the assessed claim is the **exact discrete all-nondegenerate-laws second-moment instability with sharp Bernoulli-jitter coefficient**, not the generic observation that random or varying parameters can destabilize oscillators. Published neighboring stochastic geometric integrators and accessible related finding records were compared by their operators and implications rather than names. An unindexed equivalent random-product calculation remains a risk.

## Value — PASS

Random step selection is a natural device in probabilistic/geometric numerical integration. Symplecticity of every individual map does not bound its ensemble-averaged energy: the result gives the exact failure mode, proves that no nontrivial bounded iid jitter escapes it, and supplies a sharp quantitative weak-jitter coefficient that becomes sensitive near the deterministic stability boundary. The closed-form transfer and reproducible two-point example provide a useful benchmark when designing energy-control mechanisms. The claim is bounded to a canonical oscillator and is not presented as a general integrator error theorem.

## Boundaries and literature

The analytical theorem does not assert an almost-sure positive Lyapunov exponent, does not cover correlated or state-adapted steps, and does not quantify energy accuracy uniformly in the small-base-step limit. Accessible sources: [1] https://arxiv.org/abs/1801.01340; [2] https://arxiv.org/abs/1108.0322; [3] https://strathprints.strath.ac.uk/164/ (abstract); [4] https://doi.org/10.1137/S003613999529589X (abstract).

Self-review: passed. Independent audit: not yet performed.
