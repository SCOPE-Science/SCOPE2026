# Review of the sharp Kirchhoff-star heat variation error

## Correctness (PASS)

The claim quantifies over each integer degree \(m\ge3\), with a degree-dependent nonempty short-time interval; it does not claim all-time optimality. The seminorm counts distributional arm variation and a median cost at the hub. The cut-measure identity gives the full operator norm exactly as a one-dimensional maximization, including singular and Cantor derivative measures. The orthogonal common/zero-sum decomposition of the Kirchhoff Laplacian proves the scalar Neumann–Neumann/Dirichlet–Neumann spectral formulas, including all coefficients and endpoint conditions. Direct Gaussian reflection gives the hub profile, bulk and leaf profiles. Their strict, rationally bounded gap, together with the derivative estimate near the hub, proves unique maximization at the hub for sufficiently small times. Injectivity modulo constants proves all equality cases. The same Gaussian identity gives the leading coefficient. The attached exact-fraction and spectral numerical checks passed; finite checks are not substituted for these analytical steps.

## Originality (PASS, with residual priority risk)

Kostrykin–Potthoff–Schrader, *Heat kernels on metric graphs and a trace formula* (arXiv:math-ph/0701009, sections 2–4), supplies graph heat kernels and scattering weights, not a sharp variation-to-error norm or jump-location optimization. Frank–Kovařík, *Heat kernels of metric trees and applications* (arXiv:1108.6145, main theorems), supply tree heat-kernel upper bounds and Schrödinger estimates, not this sharp residual operator norm. Marola–Miranda–Shanmugalingam, *Characterizations of sets of finite perimeter using heat kernels in metric spaces* (arXiv:1405.0186, Theorem 4.1, Proposition 5.2), studies perimeter and BV heat characterizations, not the exact norm and extremizer class. Mazón, *The Total Variation Flow in Metric Graphs* (arXiv:2112.13035, section 2.1), defines relevant vertex-aware variation and a different nonlinear flow, not the linear heat residual theorem. Related explicit heat estimates for degree-two circles/intervals and endpoint analyticity on infinite stars do not imply the strict hub/outer-leaf optimizer gap on compact branching stars. The search comparison does not constitute proof of historical uniqueness; an unindexed or otherwise inaccessible equivalent may exist.

## Value (PASS)

The object is a natural metric-graph Markov heat semigroup paired with the vertex-aware BV seminorm. The theorem solves its full infinite-dimensional sharp error problem on a nonempty interval of times for every branching degree, gives the exact convergent finite-time series, and classifies the equality functions. The non-obvious feature is a branch-induced optimizer localization: for three arms the whole-arm discontinuity has short-time coefficient above \(0.44\), strictly larger than every outer reflecting-leaf jump (below \(0.42\)); a degree-two folding cannot imply this. The coefficient quantifies a genuine degree law rather than a numerical improvement to a known generic bound.

## Limits

The time threshold is established existentially, not explicitly. Equal unit arms, ordinary arclength and the stated hub-penalized variation are essential assumptions. No independent validation of the mathematical result has been performed. Historical-priority risk remains despite source comparisons.

Self-review: passed. Independent audit: not yet performed.
