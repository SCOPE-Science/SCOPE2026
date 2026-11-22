# Scientific review

## Correctness — PASS

The exact domain is two simple 20-vertex graphs GP(10,2) and GP(10,3), with 1,048,576 binary initial configurations each. The analytical proof establishes \(F^3=F\) on any finite undirected graph, so cycles have lengths only one or two and every trajectory is periodic after at most one update. The numerical conclusions are not inferred from samples: full indegree-peeling enumeration and a separately implemented vectorized preimage-and-orbit-key census agree on all fixed counts, two-cycle counts, attraction totals, fixed-point basin-size multiplicities and complete two-cycle basin-size multiplicities. Full-state graph validation matched the canonical named graphs. Boundary definitions of primitive cycle, basin and first-entry time are explicit.

## Originality — PASS, with residual priority uncertainty

The 2015 fixed-point/MIS theorem and general one-update NOR reduction are prior background rather than new contributions. The actual claim compares complete NOR attraction basins on two specific nonisomorphic Petersen covers. A 2020 general periodic-point article does not give the graph-pair counts. Indexed dodecahedral and Desargues majority analyses concern a different update rule, and indexed NOR leaf-corona/Kneser results concern different graph families. See AUDIT.json for the queries, primary material read, actual closest records, implication comparisons and inaccessible-source risks. No indexed equivalent numerical inversion was found, but inaccessible or unindexed equivalent computation cannot be ruled out.

## Value — PASS

The two graphs have the same number of vertices, degree, and a common ten-vertex covering quotient; the one-step dynamics isolates attraction-basin structure from long transient behavior. Dodecahedral NOR has 108 more equilibria yet 1,196 fewer initial configurations attracted to equilibria. On the bipartite Desargues cover, exactly two shore equilibria each attract 388 states, while every dodecahedral fixed-point basin has size at most 35. Thus this finite exact comparison answers the natural question of whether greater equilibrium multiplicity implies a greater chance of equilibrium selection, with a concrete sharp counterexample and full reproducible basin distributions. It does not claim a general theorem about arbitrary graph covers.

## Historical scope and limitations

The comparison is finite and complete only on the two named covers. Generic NOR periodicity and maximal-independent-set facts are known. Searches and primary-source inspection have limitations; full texts of some relevant indexed mathematical findings could not be reached, though their indexed rule/object descriptions differ decisively. Independent external validation has not been carried out.

Self-review: passed. Independent audit: not yet performed.
