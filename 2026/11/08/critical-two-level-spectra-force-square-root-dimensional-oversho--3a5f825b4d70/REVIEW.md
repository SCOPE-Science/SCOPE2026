# Scientific review of the critical two-level overshoot theorem

## Correctness — PASS

The scalar error transformation is obtained directly by diagonalizing the matrix update. Expanding the quartic objective yields strictly negative linear and strictly positive cubic and quartic coefficients. The derivative cubic has exactly one sign change and therefore exactly one positive root; since its endpoint signs differ, this root is the unique global minimizer on the nonnegative half-line. For critical two-level inputs, the objective divided by dimension converges locally uniformly under the \(n^{1/4}\) coefficient scaling to an explicit quadratic in the squared scaled coefficient. The exceptional-coordinate loss bounds all global minimizers on that scale; uniqueness of the limiting minimizer gives convergence. Direct eigenvalue evaluation proves the spectral, Frobenius and sign-error asymptotics. The standard norm comparison supplies the universal order bound. The standalone verifier reports exact-rational quartic checks and supplementary numerical diagnostics. Limitations: asymptotic rather than finite-dimensional equality, exact arithmetic, unsafeguarded one-step variant only.

## Originality — PASS, with residual risks

The primary paper [Yang et al., arXiv:2601.22137, Section 4.1] itself warns of possible spectral-residual increases if its fitting coefficient is unrestricted. This *qualitative warning is not claimed as new*. Its statement does not quantify the largest possible dimension dependence, identify the two-level critical scale or give the derived precise coefficients and matrix-sign error. [Amsel et al., arXiv:2505.16932] solve interval-minimax spectral approximation; [Grishina et al., arXiv:2506.10935] likewise design Chebyshev polynomial routines; [Topollai--Choromanska, arXiv:2609.33047] select predesigned routines using spectral moments. Their optimization domains and conclusions do not cover the specific unrestricted Frobenius one-parameter minimizer's asymptotic outlier. Published mathematical-record semantic searches and accessible prior-claim comparisons yielded no stronger directly covering result. Risks: generic least-squares outlier constructions may have an unindexed equivalent; source authors may possess undocumented examples. The universal \(\sqrt n\) upper bound alone is standard, not a novelty assertion.

## Mathematical value — PASS

The precise finite-rank mechanism resolves how badly a physically natural but unsafeguarded instance-adaptive Frobenius fitting rule can mistreat one singular mode while improving its own exact objective. Its sharp scale, tunable critical-family constant, unique optimality and actual matrix-function error quantify why coefficient bounds are mathematically important. It does not assert behavior of the protected implementation or multi-step iteration.

Self-review: passed. Independent audit: not yet performed.
