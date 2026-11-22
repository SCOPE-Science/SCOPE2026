# Scientific review: mean-centered clipping in path variation

## Correctness
**PASS.** The map is a continuous piecewise-affine translation-equivariant clipping transformation. The exact variation norm of each affine mask is bounded by summing left/internal, right/internal and crossing edges for the single-step basis, giving \(2j(n-j)/n\). The complete upper bound follows from step decomposition and integration along input segments, including clipping boundaries. Alternating masks with both bridging sites active realize equality; the written explicit zero-mean constructions establish strict feasibility for odd/even clipped counts, including the one-clipped-site edge case. Exact-rational code independently checks finite masks, explicit witnesses, and randomized rational pairs. The analytical proof, not the finite checker, bears the unbounded-dimension claim.

## Originality
**PASS, qualified by remaining historical-priority risk.** Kitić et al. (2013, arXiv:1303.1023), Section 3, equation (4) and Sections 4–7, study uncentered clipping and inverse sparse declipping; their map is not translation equivariant and the paper does not furnish the centered map's BV perturbation norm. Chen–Selesnick (2013, arXiv:1304.0035), Sections 1–2 and 4, study overlapping group shrinkage in other metrics and do not imply this exact scalar-mask result. Indexed comparisons included Euclidean-ball clipping sensitivity, capped-simplex projections, and recent variation-stability estimates for medians/morphology; these use different operators, metrics, or constraints. A related centered *radial* shrinkage coefficient in accessible prior research uses a different nonlinear derivative and is not implication-equivalent. No exact duplicate or stronger covering theorem was found in the accessed material. Full text of certain indexed publications was unavailable, and search noncoverage is not proof of priority.

## Value
**PASS.** Both amplitude centering and clipping are standard signal preprocessing operations, and each individual signal's variation decreases. The exact two-input factor instead grows linearly with sequence length, quantifying a substantial and previously non-obvious fragility in perturbation comparisons. The formula is sharp and attained at every size and clip level, includes the first expansive dimension \(n=3\), and has constructive data pairs useful for stability testing. The mathematical contribution is the exact natural quotient-seminorm invariant and the feasible alternating-mask mechanism, rather than merely a restatement of scalar clipping nonexpansivity.

## Limits
Finite unweighted paths and uniform clip level only; no statement about nonuniform reference averages, multiple passes or higher-dimensional grids. Independent mathematical and historical-priority audits have not been conducted.

Self-review: passed. Independent audit: not yet performed.
