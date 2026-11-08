# Self-review

## Correctness — PASS
The one-step midpoint transition has exact conditional Gaussian variance \(1-r(u)^2\), so the invariant Gaussian and both Hermite eigenrelations follow without approximation. The contraction argument establishes uniqueness. The exact convex envelope uses the verified factorization \(f(u)-\ell_B(u)=(B-u)(Bu-B-2)^2/((B+1)^3(1+u)^2)\), and the contact and strict-convexity conditions establish uniqueness at all boundaries. The source code checks symbolic equalities and 9,952 finite rational two-atom comparisons; the proof, not the finite checks, establishes all-law optimization.

## Originality — PASS, qualified
The closest primary random-step source is Abdulle and Garegnani, arXiv:1801.01340: pathwise numerical integration with random time steps but no OU stationary quadratic autocorrelation optimization. He et al., arXiv:2011.03176, study a distinct randomized-midpoint Langevin algorithm, and Lie et al., arXiv:2103.16506, study additive randomization for deterministic equations. A related scalar midpoint-damping result optimizes the scale of a prescribed binary log-symmetric distribution, not an arbitrary bounded law at fixed mean and not the conflicting Gaussian-observable risks. Published mathematical records and targeted searches found no precise claim or stronger encompassing formula, though a specialized predecessor or elementary convex-analysis interpretation remains a residual risk. Novelty is not inferred merely from nonmatching titles.

## Value — PASS
Fixed arithmetic mean and cap are natural controls for random-time-step integrators. The first two Hermite observables of the Gaussian target are canonical, not arbitrary tests. The exact law demonstrates a sharp point-mass/two-point transition while exposing an unavoidable improvement-versus-deterioration conflict across observable classes. This gives a precise benchmark for constrained random-step sampler design. It makes no claim that broad randomization improves real-time trajectory accuracy or all-observable efficiency.

## Scope and review status
All-new scientific claims are supported by the analytic proof and the attached symbolic checker. Bibliographic coverage is a self-review, not an independent certification; specialist constrained-mixing literature remains a risk.

Self-review: passed. Independent audit: not yet performed.
