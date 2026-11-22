# Review of the diagonal-quadratic simplex sensitivity theorem

## Correctness

**PASS.** The KKT multiplier gives a unique threshold and a piecewise affine prediction map. On active set \(T\), the Jacobian is \(\operatorname{diag}(a_T)-a_Ta_T^\mathsf T/A_T\); this is a weighted-variance positive-semidefinite matrix. Positive-semidefinite sign duality identifies its \(\ell_\infty\)-to-\(\ell_1\) norm, and the variational formula for weighted variance proves full-support dominance across active sets. The full-support maximizing sign vector produces a *finite* exact norm-attaining input pair. The PARTITION reduction is by exact equality with the total weight; subset-sum dynamic programming proves pseudo-polynomial tractability. The self-contained checker passed 1080 exact-rational test cases. Numerical experiments alone are not used as a proof of any universal statement.

## Originality

**PASS, with priority risk.** Martins–Astudillo (2016) states the unweighted sparsemax Jacobian, so that uniform-weight subcase is prior work and is not the claimed contribution. Blondel–Martins–Niculae (2019 preprint / 2020 full paper) establishes the encompassing regularized prediction framework and generic smoothness, without the weighted sharp induced norm or its subset-sum complexity. Perez–Ament–Gomes–Barlaud (2020 preprint) treats weighted-simplex threshold computation, not its globally sharp input-output cross-norm coefficient. Published graph Lipschitz-variance findings with partition discrepancies do not address the same operator, perturbation geometry, or consequence. The substantive new statement is the arbitrary-weight sharp formula, full-support dominance/attainment and exact hardness classification. An equivalent historical formula under weighted variance or sensitivity of quadratic knapsack projection could still exist; the source comparison is not exhaustive.

## Value

**PASS.** Heterogeneous classwise quadratic penalties are a natural specialization of convex regularized prediction; the precise worst-case score-to-probability sensitivity controls total-variation robustness of sparse predictions and gradients of their associated convex losses. The theorem turns its exact stability constant into a meaningful balanced-partition invariant, proves finite attainment and a complete fixed-total range, and distinguishes easy pointwise map evaluation from weakly NP-complete exact worst-case sensitivity. These properties are not merely renaming the familiar uniform sparsemax Jacobian. The complexity classification is a natural endpoint for the precise quantity and has a pseudo-polynomial constructive counterpart.

## Evidence and limitations

Primary sources examined include Martins–Astudillo (2016), *From Softmax to Sparsemax*, especially §2.5; Blondel–Martins–Niculae (2020), *Learning with Fenchel–Young Losses*, especially §§2–3 and §8; and Perez et al. (2020), *Efficient Projection Algorithms onto the Weighted \(\ell_1\) Ball*, especially §2 and the conclusion. A narrowly similar computational invariant appears in graph-Lipschitz variance literature, but the metric-graph theorem does not furnish a diagonal-simplex prediction theorem. No claim is made for general quadratic Hessians, stochastic stability, approximation hardness, or noninteger input complexity. Earlier unpublished or unindexed equivalents cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
