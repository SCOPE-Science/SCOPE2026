# Scientific review: weighted-cycle Kemeny coordinate trap

## Correctness — PASS

The conclusion is restricted to the zero-target Kemeny constant of the positive-conductance, loopless **discrete-time** random walk. The proof uses the standard commute-time/resistance identity, the exact cycle parallel-resistance formula, and a closed all-length single-defect sum. The resulting numerator factors into a strictly positive multiple of \((t-1)^2\), so no endpoint or parameter region is omitted. The five-cycle descent is an exact rational identity valid for every \(0<|\epsilon|<1\) at constant cost. A spectral convexity proof covers the triangle, while bipartite spectral pairing and a two-by-two determinant give the complete four-cycle equality class. The standalone exact-rational verifier passed 631 comparisons, including independent hitting-time solves; those finite comparisons are supplementary and not treated as an infinite proof.

## Originality — PASS on inspected evidence, qualified

The established resistance identity, Kemeny's eigenvalue formula, and global network-topology minimization are credited as prior work, not new. The focal 2012 article by Zhang, Sheng, Hu and Chen studies unweighted complete graphs and sparse fractal network families; inspecting its full accessible manuscript reveals no independently variable edge-conductance optimization on a fixed five-cycle. Kirkland and Zeng (2016) study Kemeny--Braess changes from adding graph edges to trees, not an all-positive, fixed-topology reallocation; only their first pages and abstract were accessible here, leaving a genuine coverage risk.

The closest inspected published research records respectively analyze adding a chord to a cycle, last-coverage probabilities on weighted cycles, continuous-time **spectral-gap** optimization on a priced five-cycle, and edge-resampled walks on complete bipartite graphs. None of those statements entails the simultaneous combination of (i) all-length strict single-edge optimality, (ii) a strict five-cycle Kemeny descent at constant total conductance, and (iii) sharp C3/C4 exclusion. The novelty claim remains relative to available indexed and primary literature; equivalent unindexed classical calculations are a residual priority risk.

## Value — PASS

Kemeny's constant measures expected travel to a stationary-random target, while conductances are an actionable fixed-topology network-design variable. The theorem supplies a **minimal** and explicit failure mode for one-coordinate optimization: every isolated conductance scan reports an optimum although a feasible coordinated perturbation immediately improves the objective. It is a structural warning about a natural design landscape, not a purely arbitrary numerical instance. The complete three-/four-vertex boundary and the all-length coordinate identity locate the obstruction precisely. Its quantitative advantage near uniformity is only quadratic and may be small; no global five-cycle optimum or practical performance guarantee is claimed.

## Closest sources and integrity limits

- Zhang et al., arXiv:1211.4295, full accessible HTML manuscript inspected (network-topology Kemeny optimization).
- Kirkland and Zeng, DOI 10.13001/1081-3810.3222, abstract and opening pages only (tree edge addition, broader forest framework).
- *A single antipodal shortcut optimally reduces Kemeny transport on cycles*, complete accessible result inspected (added chord, not fixed-topology conductance allocation).
- *Hidden one-dimensional fairness in reversible weighted cycle cover tours*, complete accessible result inspected (last-visited-vertex distribution, not Kemeny's constant).
- *Exact active-edge allocation on a five-cycle with one priced link*, complete accessible result inspected (continuous-time spectral gap, different objective).

Residual risks: unindexed historical weighted-cycle Kemeny formulas or an implicit corollary in unavailable specialist texts. The proof uses exact analytic identities; no independent mathematical audit is represented.

Self-review: passed. Independent audit: not yet performed.
