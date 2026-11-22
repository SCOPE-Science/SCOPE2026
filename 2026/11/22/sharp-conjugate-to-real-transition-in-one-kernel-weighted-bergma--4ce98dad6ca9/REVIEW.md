# Self-review

## Correctness — PASS
The assertion has a complete proof: normalized kernel projection converts the Hilbert optimization into \((1-|w|^2)^\lambda|1+a w-w^2|^2\); the exact angular quadratic has one vertex; the radial envelope has at most one interior maximum; the real branch has exactly one stationary point by a strictly increasing rational function. All weights \(\lambda>1\), coefficient endpoints, and merging boundary are explicitly covered. The critical radius derivative follows by implicit differentiation. The included checker passed 21,896 numerical assertions. The infinite/global statements depend on the displayed monotonicity proof, not numerical search.

## Originality — PASS, best-knowledge
The closest general sources are Qu–Qian–Deng (arXiv:2006.03290), Qu–Qian–Li–Zhu (Applied Mathematics and Computation 416, 2022), and Qian (arXiv:2201.07228). They establish existence and the general one-kernel objective, but the examined principal results do not give the optimizer locations, weight-dependent conjugate bifurcation, sharp threshold curve, or critical exponents for the family \(1+a z-z^2\). Relevant indexed results on **two-kernel** approximation of \(z^2\) and on **fourth moments** of Bergman quadratics have different objectives and do not imply this exact theorem. Full primary material was inspected where directly relevant. Searches cannot establish exhaustive historical uniqueness; a pre-existing exact optimization of the same three-term weighted polynomial remains a residual priority risk.

## Value — PASS
This is a natural, complete first nontrivial phase-sensitive case of the established best single-kernel approximation problem, not an arbitrary numerical slice. It reveals a sharp qualitative distinction between negative and nonnegative standard Bergman weights, a genuine conjugate-to-real optimizer merger, an exactly pinned radius before transition, and an explicit universal square-root angular response. Those exact global sites and the complete approximation error are useful for reproducing-kernel parameter selection and interpreting local optimization outputs. The proof requires a global angular-to-radial reduction with exact equality cases, not a finite experimental search.

## Limitations and closest literature
The statement is confined to one kernel and the specified real quadratic family. The general one-kernel reduction is inherited from published work; the newly claimed content is the global phase diagram. Independent mathematical audit and exhaustive historical priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
