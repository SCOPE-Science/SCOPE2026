# Self-review

## Correctness — PASS

The geodesic obstruction is exactly a fully selected 2-by-2 rectangle: a diagonal selected pair has exactly the two other corners as length-two intermediates. Therefore any two distinct column supports intersect in at most one row. Partition by triple columns versus no triples, then enumerate distinct pair supports. For maximality, empty columns and at most one pair can be extended; with two distinct pairs all other singleton rows must equal their intersection, and with all three pairs every remaining singleton is arbitrary. These arguments prove necessity, sufficiency, uniqueness and all three counts, including \(n=2\). Direct literal graph tests on 299,584 vertex subsets (\(n=2\) through \(6\)) confirm all coefficients and maximal types; finite tests do not prove the infinite range.

## Originality — PASS (provisional priority)

The known general \(C_4\)-free representation of rook mutual visibility (Cicerone–Di Stefano–Klavžar) and known lower scalar bound (Brešar–Yero) are explicitly excluded from the novelty claim. The complete labelled visibility polynomial and the complete labelled maximal-set/facet classification are strictly more detailed than those statements. Inspected primary texts of the two papers, plus accessible related visibility-polynomial papers, did not state a matching formula. The closely related Bryant–Fu 2002 paper studies the possible saturated edge counts; only an abstract was accessible, and full-text overlap cannot be ruled out. Searches under \(C_4\)-saturated bipartite matrices, rook graphs, visibility polynomials, and maximal mutual-visibility sets found no directly covering statement. This is best-knowledge novelty, not a priority certificate.

## Value — PASS

The lower mutual-visibility parameter asks how a maximal-set construction can terminate. Counting every maximal configuration and its possible sizes gives a natural exact refinement: for every \(n\ge3\), the mutual-visibility simplicial complex has two different facet sizes, with sharply different labelled multiplicities, whereas the earlier lower-number result gives only their smallest size. The complete generating polynomial also enumerates all feasible configurations at each weight, not merely the extremizers. The 3-row scope is natural because exactly three pair-support types occur, leading to a finite structural partition.

## Limits and nearest literature

The graphs are labelled \(K_3\square K_n\), \(n\ge2\); this is **ordinary**, not total, mutual visibility. Scalar lower bound \(n+2\) was already known. The strongest unresolved overlap risk is the inaccessible complete paper by Bryant and Fu (2002), DOI 10.1016/S0012-365X(02)00371-0; its abstract speaks of existence of saturated graphs with prescribed edge numbers, not the counting formulas. A separate priority search may reveal an equivalent enumerator under matrix or saturation terminology. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
