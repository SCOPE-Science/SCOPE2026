# Scientific review

## Correctness — PASS

The complete density of the conditional typical facet comes directly from Bonnet–O'Reilly's exact equation (6.3) and is explicitly normalized, including signed negative offsets. The scaled-density potential has a direct, globally verified curvature lower bound \(\kappa_d=1-2/d-1/d^2\). The compact-uniform \(C^2\) expansion of the sphere-coordinate CDF and the strict inverse-Mills saddle calculation establish the Gaussian law at its correct moving center; global curvature supplies integrable tails, justifying total variation and fixed moment convergence. The Gaussian-plane offset density is derived from independence of the Gaussian sample mean and centered affine residuals. The small-parameter implicit-function expansion gives the exact \(d^{3/4}\) crossover. The numerical checker separately tests integral normalizations, curvature, direct geometric facets, TV approximation, and the crossover coefficient. The limits apply only for bounded ratios and an annealed candidate-facet conditioning.

## Originality — PASS, with historical risk

Bonnet–O'Reilly [3] prove first-order height results at finite ratios and a CLT under the narrower \((n-d)/\sqrt d\) scaling; their high-sample gamma result concerns a different regime. Kabluchko–Temesvari–Thäle [1] and Böröczky–Lugosi–Reitzner [2] focus on expected facet counts/intrinsic volumes, not the normalized conditional height distribution at the moving saddle. The present claim is specifically the finite-ratio TV Gaussian fluctuation theorem and explicit variance, the exact nonlinear centering crossover, finite-dimensional subGaussian inequality, and sphere–Gaussian TV equivalence. Accessible primary texts and semantic searches yielded no dominating same-observable claim. Historical risk remains that an independently discovered saddlepoint theorem could imply the CLT under another name; none is assumed away.

## Mathematical value — PASS

The typical supporting-plane offset is a natural metric statistic of high-dimensional random convex hulls. Earlier work locates the typical height at leading order but leaves its exact order-one fluctuations and finite-dimensional concentration unresolved in the full proportional regime. The variance parameter quantifies their dependence on sample density, and the \(d^{3/4}\) transition identifies the precise breakdown of a natural linear extrapolation from the known near-simplex Gaussian theorem. Total-variation equivalence connects two classical random-polytope sampling models at the metric-fluctuation scale. These conclusions are neither arbitrary parameter slices nor numerical recomputations of earlier tables.

## Sources and residual limits

[1] https://arxiv.org/abs/1707.02253; [2] https://arxiv.org/abs/1808.01431; [3] https://arxiv.org/abs/1908.04033 and open-access full text https://doi.org/10.1002/mana.202000314. Primary comparisons concern exact observable and implication, not just titles. The global concentration proof uses the classical one-dimensional strong-log-concavity log-Sobolev inequality. Computer experiments support, but do not prove, the limiting results. The priority judgment remains provisional, and there is no independent validation.

Self-review: passed. Independent audit: not yet performed.
