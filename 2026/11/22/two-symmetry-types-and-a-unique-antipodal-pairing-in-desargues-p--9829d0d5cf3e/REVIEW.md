# Scientific review: Desargues optimum-sensor relocation

## Correctness

PASS. Both canonical constructions of the Desargues graph are used in standalone deterministic programs. The first directly checks all 20 one-vertex, 190 two-vertex and 1140 three-vertex candidates and then computes every legal configuration transition and every shortest-path distance. A separate GP(10,3) bitset implementation repeats the enumeration and uses Floyd–Warshall rather than breadth-first search for the configuration distances. Both give exactly 240 minima of two distance signatures, 480 slide edges, eccentricities 7/8 by signature and 60 distance-eight pairs. The explicit antipodal matching is asserted for all its 120 endpoints. These are exhaustive finite checks with bounded loops and exact integer operations; no infinite claim is inferred from the computation.

## Originality

PASS under the inspected-source, best-knowledge comparison, with historical-priority uncertainty. The 2022 full-text power-domination reconfiguration paper discusses general move models, not the optimum Desargues metric. The 2020 generalized-Petersen power-domination paper supplies bounds and special families, but does not provide the two-orbit classification and slide-distance metric on GP(10,3). The closest indexed studies of Desargues graph configurations concern zero forcing and independent domination, whose different predicates do not entail the present claim. Several combinations of alternative names and distance-signature parameters were searched; failed searches alone are not proof of uniqueness. The 2011 generalized-Petersen power-domination article was compared through its abstract and secondary description, not fully inspected.

## Value

PASS. This classifies every minimum monitoring placement and every allowed relocation in a canonical cubic, distance-transitive, bipartite network. The new structural distinction is not a tiny numerical improvement: two equally large symmetry types have the same local slide degree but different global eccentricities, and one has an explicit involutive perfect matching of unique farthest configurations. This makes the result an exact reference case for migration of minimum power-monitoring sets while uninterrupted observability is required.

## Closest literature and limits

Primary references: Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798 (2022); Zhao, Shan and Kang, *Power domination in the generalized Petersen graphs* (2020); Xu and Kang, *On the power domination number of the generalized Petersen graphs* (2011). The 2011 complete article and potentially unindexed equivalent classifications remain historical-priority risks. No general-family theorem or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
