# Scientific review: universal optimal factor-two numerical-radius Pick guarantee

## Correctness
**PASS.** For arbitrary finite distinct disk nodes and matrix targets, the source's necessary circle test gives the lower bound \(P\le\Gamma\). Classical matrix-valued Nevanlinna--Pick interpolation gives \(\Gamma\le\|\mathcal S^{-1/2}D\mathcal S^{1/2}\|\le2P\), including zero data. Sharpness is analytic: the square-zero compressed matrix for the two-node nilpotent family has norm \(t/r\) and numerical radius \(t/(2r)\). Scalar Schwarz--Pick forces \(\Gamma/P\ge1+\sqrt{1-r^2}\), which tends to two. All budgets, normalizations, boundaries, and inequalities were reconstructed. The diagnostic verifies only finite matrix identities.

## Originality
**PASS, qualified.** The 2026 primary source proves necessity of the Pick-circle condition and exhibits an isolated failed interpolation instance; it does not establish a universal approximation factor, its **optimality** under actual holomorphic interpolation, the exact two-parameter test cost, or the explicit false-positive wedge. The universal upper factor follows by combining **standard credited** operator-valued Nevanlinna--Pick and \(\|T\|\le2\nu(T)\); the new essential issue is its sharpness for the interpolation problem. Published mathematical-record and literature comparisons found no covering formulation; unindexed publications remain a priority risk.

## Value
**PASS.** For a natural necessary but insufficient semidefinite feasibility relaxation, the theorem determines the smallest possible universal multiplicative budget inflation making it sufficient, rather than merely exhibiting a negative counterexample. An explicit collision family proves the factor optimal and quantitatively locates false-positive data. This sharp relaxation guarantee is useful for certified numerical-radius interpolation budgets independently of any exact pointwise interpolant formula.

## Limits and reproducibility
The true optimal finite-distance cost for the two-node witness is not claimed exactly. The source's full Theorem 2.4 and Example 2.5 were inspected, and the use of classical matrix Nevanlinna--Pick is explicit. The checker `check_exact.py` can be executed with standard Python but does not certify the analytic argument. Primary source: Ahmed, Bhowmik, Das and Sau, arXiv:2611.19189v1, submitted 2026-11-14, https://arxiv.org/html/2611.19189v1.

Self-review: passed. Independent audit: not yet performed.
