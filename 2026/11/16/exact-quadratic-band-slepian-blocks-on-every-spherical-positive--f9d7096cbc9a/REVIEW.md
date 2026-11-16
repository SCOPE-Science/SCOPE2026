# Self-review

## Correctness — PASS

The statement restricts to the full low-pass spherical harmonic band of degrees zero, one, and two, for all ambient dimensions at least four. The orthant gamma-moment identity determines every entry. The trivial, standard, and incidence-kernel spaces are orthogonal and exhaustive, with multiplicities summing to the correct full-band dimension. The displayed matrices have been checked independently against full absolute-sphere monomial Gram matrices in dimensions three through nine (224 comparisons/checks). Positivity follows from real analyticity. The asymptotic proof uses the delta-method variance \(1-3/\pi\), moment convergence, conditional quadratic orthogonalization, and a separate lower eigenvalue bound for the standard block. No finite experiment is treated as proof for all dimensions.

## Originality — PASS with residual historical risk

The closest direct preceding orthant theorem concerns the *pure* degree-two space, not the simultaneous low-pass degrees zero through two. Its two-by-two and scalar sectors cannot determine mixed-degree coefficients: in the present formulas both full-band invariant types have new nonzero off-diagonal entries, and the sharp restriction growth is quadratic in dimension, not linear. A separately available ambient-three-dimensional full-band octant computation supplies only the fixed-dimensional special case and not the general formula or its asymptotic. The published general Slepian method of Simons, Dahlen and Wieczorek supplies a kernel eigenvalue framework, not the evaluated all-dimensional orthant spectrum; Roddy and McEwen develop wavelets for incomplete data rather than this exact spectral result. Related work on hemispheres and quarter-wedges concerns different regions. A general algorithm to form a matrix is not an explicit closed block decomposition or asymptotic constant. The public full texts of the closest orthant theorem and the classical Slepian framework were materially read; the accessible PDF text of the motivating wavelet work was inspected, but screenshot rendering of its large PDF was unavailable. A previously undiscovered specialized table or equivalent formulation remains possible.

## Mathematical value — PASS

The exact orthant is a canonical region for incomplete spherical observation, not a chosen arbitrary slice. The complete low-pass spectrum in unbounded ambient dimension is structurally reduced to two fixed-size matrices, and the sharp \(2/[\pi(\pi-3)]\) dimension-squared condition-number asymptotic identifies a new cross-degree cancellation mechanism absent from pure quadratic analysis. The restriction stability benchmark directly quantifies reconstruction difficulty from an orthant even at fixed low harmonic cutoff; the information is not merely a numerical instance or a renaming of a general kernel formula.

## Limitations and closest literature

The analysis does not assert an exact all-dimensional ordering among every root of the two blocks, and it addresses continuous noiseless restriction rather than finite noisy sampling. Historical priority remains provisional and independent mathematical validation has not occurred. Relevant literature: Simons–Dahlen–Wieczorek (2004), Roddy–McEwen (2021), Michel–Plattner–Seibert (2021), and the published pure-quadratic orthant spectrum (2026).

Self-review: passed. Independent audit: not yet performed.
