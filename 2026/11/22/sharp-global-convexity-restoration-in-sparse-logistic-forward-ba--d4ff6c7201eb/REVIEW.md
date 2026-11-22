# Scientific review

## Correctness

**PASS.** The scalar Moreau envelope is the exact Huber formula. Differentiation yields the active and inactive curvature formulas, and the negative-active curvature obstruction has the exact completed-square form \(D_r(p)=(1-r+r^2)/3-3(p-(1+r)/3)^2\). The maximizer \(p_0=(1+r)/3\) is shown to lie in the required active region, making the threshold necessary. All other branches have nonnegative curvature below the stated cutoff. The \(\gamma>4\) case is treated separately. The gradient-mapping identity proves the unique stationary minimizer when \(\gamma<4\). Exact symbolic and rational checks passed; finite grids are only spot checks.

## Originality

**PASS, with historical-priority risk.** The 2026 source analyzes general envelope smoothness and sufficient convexity, but not the sharp globally necessary-and-sufficient \(\ell_1\) threshold. The 2014 FBE paper supplies the definition and sparse-logistic application, not the derived penalty-sensitive phase transition. An unregularized scalar logistic boundary is a known covered limit, explicitly separated from the new positive-penalty theorem. Indexed searches of regularized/logistic/FBE/Moreau aliases returned no statement of the threshold; this does not establish exhaustive novelty. The closest source comparisons and residual risks are recorded in the accompanying audit.

## Value

**PASS.** Sparse logistic fitting is a standard composite optimization model; a fully explicit sharp convexity boundary for its smooth merit function is relevant to methods that optimize or precondition that merit function. The penalty-induced convexity-restoration window and the identity linking the optimizer's effective shrinkage to the exact curvature frontier are nontrivial, parameter-stable structural facts, not a change of notation or a single arbitrary numerical example. The result makes no claim about coupled-feature regression or universal algorithmic acceleration.

## Limitations

The theorem concerns the scalar and coordinate-separable cases, not general correlated design matrices. The original source gives general sufficient bounds, while the present result gives a sharp special-model classification. Independent literature-priority checks and an independent proof audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
