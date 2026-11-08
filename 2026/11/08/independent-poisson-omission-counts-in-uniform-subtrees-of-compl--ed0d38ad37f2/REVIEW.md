# Scientific review: Independent Poisson omission counts in uniform subtrees of complete split graphs

## Correctness — PASS

The theorem is explicitly scoped to the simultaneous proportional-growth regime with a fixed finite positive limit of the independent-set-to-clique ratio. The complete split spanning-tree formula follows from the exact Laplacian spectrum, with the clique-only boundary handled separately. Every subtree belongs to exactly one selected-vertex class and is counted by a spanning-tree count on that selected set. For a fixed pair of omitted-class counts, the exact ratio has the stated product-form limit. For all nonboundary counts, the factorial envelope bounds the entire double series; the clique-only boundary is superexponentially negligible and isolated independent singletons have negligible mass. These estimates justify normalization and total-variation convergence, not just pointwise convergence. The derivative computation proves strict monotonicity, and the endpoint expansions apply only to the limiting function. An independent finite-graph construction implemented in `check.py` reproduced the required exact counts, and coefficient ratios converged toward the stated parameters. Finite enumeration was not used in place of infinite proof.

## Originality — PASS, with historical-priority risk

Chin et al. (2018) introduce subtree statistics for general graphs, particularly complete and bipartite cases. Wagner (2021, 2019 preprint) addresses spanning probabilities and total missing-vertex counts in random dense graphs. Cambie et al. (2023 preprint, 2024 journal) examine the very same complete split graph but prove a mean-subtree-order comparison in the fixed-clique, disproportionately large independent-set regime. Wagner and Wang (2026) establish a general *scalar* Poisson limit for the total number of omitted vertices on dense graphs. That scalar limit cannot determine the two-class joint distribution: dependence and allocations with the same Poisson sum need not be independent. The new claim gives explicit distinct rates and their independent joint limit when both class sizes grow linearly. Closely matching source and parameter searches did not reveal the same statement. The complete 2018 paper was not inspected, so historical priority is qualified rather than certified.

## Value — PASS

The source papers make the probability that a random subtree is spanning a natural invariant. On a dense but nonregular graph, the total number of omitted vertices conceals whether omissions come from high-degree clique vertices or lower-degree independent-set vertices. The result resolves that exact natural two-type composition: the two class counts become asymptotically independent, with explicit nonidentical positive intensities. It also proves a strict decline of the limiting spanning probability as the independent-class fraction grows, and recovers the known complete-graph constant continuously at the boundary. This is a structural probabilistic refinement, not a restatement of the scalar Poisson theorem. The exact spanning-tree formula alone is standard and is not claimed as new.

## Closest literature and limits

- Chin et al., *Subtrees of graphs* (2018): foundational univariate subtree enumeration; abstract/metadata consulted, not the full body.
- Wagner, *On the probability that a random subtree is spanning* (2019 preprint; 2021 journal): full HTML article consulted, particularly the definition, dense-random model and probability bounds.
- Cambie et al., *Decreasing the mean subtree order by adding k edges* (2023/2024): preprint Sections 1 and 3 consulted; same graph, different asymptotic regime and a mean comparison.
- Wagner–Wang, *The Distribution Of Subtrees In Dense Graphs And The Roots Of The Subtree Polynomial* (2026): full HTML sections on general scalar Poisson law consulted; an important broader result, but it does not state a colored joint law.

The proof does not give a quantitative total-variation convergence rate, a variable-ratio theorem, or a generalization to arbitrary split graphs. Unindexed or inaccessible prior results might affect historical priority. No independent external audit is claimed.

Self-review: passed. Independent audit: not yet performed.
