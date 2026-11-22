# Scientific review

## Correctness (C): PASS

The continuum heat normalization, both boundary conditions and the initial interior state are explicit. The sine-series solution and Brownian exit identity identify the exact reference, with no confusion between a continuum scaling length and a discrete number of sites. A direct differentiable subsolution gives the strict all-time inequality. The uniform error bound follows from the half-line hitting probability and is *sharp in the sense of the spatial supremum* by a two-boundary reflection/strong-Markov estimate. The separate fixed-interior late-time error follows from the error-function expansion and the exponentially decaying Fourier series. The exact finite integrated deficit is obtained from a Dirichlet Poisson equation; the shortcut's is infinite because of a positive \(1/t\) term. An independent image-series implementation, finite-difference residual and time quadrature pass 401 scalar checks. Risk: numerical checks are finite and do not substitute for the maximum principle or probabilistic argument.

## Originality (O): PASS, qualified

Henkel (2026), arXiv:2606.16848v1, is the primary source for the exact finite semi-open correlation and proposed approximation. Its relevant continuum equations, approximation discussion, and mathematical appendix were inspected. The paper discusses the distinction between the theta solution and the approximation but no strict universal sign, sharp spatial-supremum bound, or integrated relaxation identity was identified there. Henkel (2025), arXiv:2501.05912, treats periodic rather than semi-open geometry. The closest accessible published Glauber comparison claims concern Pareto/global resetting and not the semi-open finite-interval shortcut. Searches included the shortcut's formula, Brownian first-passage equivalents, boundary heat kernels, spectral-gap versus algebraic error and related exact models. Residual risk: the bound uses classical heat comparison and could be implicit in an unindexed Brownian-exit inequality; absence of a search match is not evidence of mathematical uniqueness.

## Mathematical value (V): PASS

The practical question is whether a widely used explicit substitute for a theta-function correlation has a controlled **finite-size uniform approximation window**, independent of location, and where that window fails. The theorem gives a rigorously certified 0.47-percentage-point absolute-error ceiling for every spatial separation at \(t\le N^2/8\), and proves the exponential scale of that ceiling is best possible. The paired finite-versus-infinite integrated relaxation result identifies a qualitative error that would arise if the compact shortcut were reused in late-time response calculations, while carefully acknowledging that such extrapolation is outside its recommended range. These quantitative and domain-of-validity results are more than a pointwise Taylor exercise; they supply a checkable finite-size error budget. Risk: no wider many-body theorem beyond this continuum boundary problem is claimed.

## Closest literature and limitations

Primary: M. Henkel (2026), arXiv:2606.16848v1, sections treating semi-open correlation and approximation, and its appendix; antecedent: M. Henkel (2025), arXiv:2501.05912, periodic geometry. Related published Glauber resetting records have distinct dynamics. The original paper's exact formulas and approximation are not asserted to be new here. Unindexed equivalent probabilistic inequalities remain a priority risk. No independent review is represented.

Self-review: passed. Independent audit: not yet performed.
