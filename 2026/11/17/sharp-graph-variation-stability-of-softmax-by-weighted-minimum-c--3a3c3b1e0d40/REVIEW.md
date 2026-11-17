# Scientific review: weighted graph-variation stability of softmax

## Correctness: PASS

The claim is an exact two-input supremum, not an assertion of finite-pair equality. The central covariance optimization is proved by eliminating discordant support pairs and applying variance bounds to the remaining concordant support. This yields a sharp norm formula for every quotient norm; weighted graph coarea turns its factors into weighted degrees and reciprocal minimum cuts. The unit-graph envelope and equality characterization follow from the minimum-cut size distinction. All boundaries include \(n=2\), arbitrary strictly positive edge weights and \(\beta>0\). Exact-rational diagnostics independently check finite cases; the analytical proof, not the enumeration, covers all orders.

## Originality: PASS (qualified)

The softmax Jacobian in Martins--Astudillo (2016) does not yield the graph norm without nontrivial covariance optimization and minimum-cut duality. The sharp standard-\(\ell_p\) bounds in Nair (2025) are not the weighted graph-variation bound and cannot yield its graph-specific equality classification. Sandryhaila--Moura (2013) studies a different graph-variation definition based on a normalized shift, and Liu--Yin (2021/2023) defines a different variation-regularized optimization map. Semantic and formula-level searches did not identify the claimed formula, but an unindexed equivalent covariance or graph-Lipschitz result is a residual bibliographic risk. The earlier papers' distinct norms and maps are not taken as novelty proof by title alone.

## Mathematical value: PASS

Graph-edge variation is a natural norm for smoothness of graph signals, while softmax is a canonical probability-normalization operator. The exact min-cut/weighted-degree formula is an efficiently computable graph invariant for stability under arbitrary perturbations, not merely a numerical special case. It yields an exact nonexpansivity criterion, the full unit-graph sharp envelope and extremizers, a complete tree stability classification, and a biclique threshold. The contrast with standard \(\ell_p\)-norm contractivity explains why a bound on a probability map in ordinary coordinates does not control edgewise variation on irregular graphs.

## Scope and residual risks

The proof does not address infinite, directed or disconnected graphs, nor alternative normalization maps. Boundary softmax profiles are approached in a limit; finite-pair attainment is not claimed. Independent examination of possible older equivalent formulations, especially in abstract covariance optimization, remains useful.

Self-review: passed. Independent audit: not yet performed.
