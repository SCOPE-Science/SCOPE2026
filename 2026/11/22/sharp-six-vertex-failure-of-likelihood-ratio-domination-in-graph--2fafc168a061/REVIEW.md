# Self-review

## Correctness — PASS

The objects, maximal-set condition, and common positive support are explicit. For every finite graph, the sequential first-vertex decomposition computes exact probabilities and the independent-set-plus-dominating-set test identifies each static terminal set. The `checker.py` certificate enumerates every one of the 1,099 labeled graph inputs on at most five vertices with no isomorphism heuristics, verifies 772 exact cross-product comparisons, and independently enumerates all vertex-priority permutations on each graph. The computations were replayed from the actual included `checker.py`. For the infinite connected family \(K_1\vee(K_2\sqcup K_{1,m})\), \(m\ge2\), the three-atom laws are proved symbolically from the universal vertex, edge and star decomposition. The inequalities for first-order dominance and the nonmonotone likelihood ratios follow by direct exact algebra; no finite test is used to infer an infinite result.

## Originality — PASS against the checked sources

The 2026 finite-graph parking paper proves first-order dominance for paths and cycles and compares an *auxiliary* law to the uniform-static law by likelihood ratio; this does not cover the comparison of sequential and static cardinality laws. The 2019/2023 greedy independent-set article studies limiting densities and local convergence, not this cross-law sharp failure. The published cycle obstruction concerns *individual terminal maximal independent sets*, not size-likelihood ratios; the published subcubic finite census confirms this likelihood-ratio comparison only for graphs of maximum degree at most three, whereas the six-vertex witness has degree five. The published pendant-extension result compares two sequential laws on different graphs, rather than sequential versus static on one graph. No equivalent or stronger covering statement was found in the checked published-finding corpus queries or recoverable local claims. Residual risk: unindexed earlier stochastic-order treatments may contain an implicit equivalent; priority has not been independently certified.

## Value — PASS

Likelihood-ratio domination is a strictly stronger, useful comparison than first-order stochastic domination. The motivating path proof explicitly obtains the stronger property only for an intermediate auxiliary law, making extension to the actual sequential output a natural substantive question. The present finding proves the sharp universal size boundary over **all** simple graphs and supplies a connected infinite family showing that first-order domination persists even when likelihood-ratio domination fails. Thus it identifies the exact limit of a natural proof-strengthening idea, rather than adding a routine finite graph example. The finite exhaustive step and the infinite analytic mechanism are both essential.

## Closest literature and remaining risks

Higuita-Diaz–López–Roldán-Correa (arXiv:2611.14718v1, 2026-11-10) is the direct motivating source; the complete 21-page PDF and its most relevant Sections 2–6 were inspected. Krivelevich–Mészáros–Michaeli–Shikhelman (arXiv:1907.07216v6) is foundational to the priority-greedy process. The full texts of two relevant publicly indexed mathematical findings on cycles and pendant-extension stochastic comparisons were inspected. Historical priority beyond these sources remains open for independent assessment. Finite checker tests do not prove other graphs behave similarly.

Self-review: passed. Independent audit: not yet performed.
