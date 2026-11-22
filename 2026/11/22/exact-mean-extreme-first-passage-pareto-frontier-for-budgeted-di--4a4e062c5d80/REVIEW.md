# Scientific review: exact mean–extreme first-passage Pareto frontier

## Correctness — PASS

The continuous claim is established analytically. The backward absorbing–reflecting boundary equation gives \(M[D]=\int_0^1(1-x)/D(x)\,dx\); the intrinsic metric \(F[D]=\int_0^1D(x)^{-1/2}\,dx\) supplies the established many-searcher first-arrival coefficient \(F[D]^2/4\) at fixed regular \(D\). Strict convexity of the weighted integral yields a unique scalarized minimizer for each positive tradeoff weight. The explicit quartic inverse \(u^4-u=(r^4-r)(1-x)\), exact budget normalization and primitive integrals prove both frontier formulas. Strict multiplier ordering and a same-mean dominance argument prove completeness rather than only necessary optimality.

The singular boundary design \(D_\infty(x)=\tfrac32\sqrt{1-x}\) is analyzed separately: under the transformation \(u=(1-x)^{3/2}\), it becomes an absorbed squared-Bessel-type process. Its exact Laplace transform gives the leading small-time decay exponent \(8/27\), validating the endpoint collective coefficient. A standalone standard-library checker replayed 177 finite deterministic checks from the packaged code. Such checks corroborate, but do not establish, the continuum theorem.

## Originality — PASS, with publication-priority qualification

The closest primary source is Luiz Menon's November 12, 2026 paper, arXiv:2611.17470v1, which derives the fixed-budget *mean-only* optimizer. Sean D. Lawley's arXiv:1909.09883 gives the *fixed-profile* extreme-first-passage asymptotic. The new theorem explicitly credits both and does not repackage their endpoints as novelty; the assessed contribution is every intermediate Pareto-efficient diffusivity and its exact quartic/logarithmic cost pair, including uniqueness and a complete dominance theorem.

Additional comparisons included dos Santos–Menon Jr.–Anteneodo (arXiv:2206.14229), published-finding corpus records for static diffusivity mixtures, clustered searchers, and unrelated mean–variance frontiers, and the accessible same-topic historical claims. No directly covering theorem was identified, but a previously implicit equivalent in broad variational optimization literature remains a real risk; an abstract-access-only related paper cannot be conclusively excluded from its entire contents.

## Value — PASS

The exact inverse tradeoff matters because redistributing a fixed diffusivity budget to reduce mean lone-particle escape time can worsen the leading time for a large search team. The sharp cost factor \(32/27\) and complete profile classification answer a physical design question with all equality cases, rather than reporting just a known endpoint or a finite experimental trend.

## Scope and limitations

The mathematical classification holds for positive almost-everywhere measurable unit-budget diffusivities with finite objectives. The stochastic interpretation is for fixed sufficiently regular strictly positive profiles and the separately verified singular endpoint, never a uniform-in-profile claim. It does not assert optimality at finite population size, stability under experimental noise, multidimensional applicability, alternative stochastic conventions, or independent publication-priority certification.

Self-review: passed. Independent audit: not yet performed.
