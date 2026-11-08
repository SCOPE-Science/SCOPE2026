# Self-review

**Single claim:** A sharp even-order Taylor positivity window for sparse-core clique joins. For all even Taylor orders on unweighted joins satisfying the explicit degree-density condition, the exact entrywise positivity interval is \(0\le h\le\beta_p/n\). No assertion about other graph classes or stage positivity is included.

## Correctness — PASS
The proof gives the exact three-block join polynomial, an explicit positive rank-one correction from convexity, and a nonnegative residual shifted-adjacency expansion under \(h(k+\Delta)\le1\). Since all clique-to-core entries are \((1-F_p(nh))/n\), necessity and failure beyond the threshold are exact. The scalar root exists uniquely, with the endpoints treated explicitly. The standalone exact rational checker passed 222 graph/order configurations and 231,840 entry comparisons. This is supplemental evidence, not a replacement for the infinite proof.

## Originality — PASS on examined sources, with priority risks
Gottlieb--Shu--Tadmor (2001) provides general SSP theory; Horváth (2005) provides broad RK positivity conditions; Horváth--Song--Terlaky (2014) provides polynomial coefficient tests, but not the exact arbitrary-residual-graph clique-join criterion. Known complete-multipartite and disjoint-clique-core special cases are acknowledged and not presented as the contribution. The new implication handles residual paths, cycles and nonsymmetric bounded-degree graphs with a multi-vertex dominating clique, using a separate residual-block shift. Indexed published positivity records for Padé and Crank--Nicolson have different time maps. Full-text priority confirmation for every specialist source remains impossible, so this PASS is conditional on the inspected evidence.

## Mathematical value — PASS
This is an exact, size-independent-in-form threshold for a motivated class of network heat semidiscretizations with dominating vertices. It replaces a full matrix-polynomial sign problem by one scalar root, supplies a general all-even-order law on arbitrary sparse residual graphs, improves the direct generic coefficient bound, and proves a strict residual positivity phenomenon. The degree constraint is a sufficient structural regime, not claimed to be necessary.

## Limitations and closest literature
The source papers and prior restricted-family classifications do not imply the displayed iff statement on all qualifying clique joins. No independent audit or exhaustive literature search is claimed. Weighted edges, odd orders, intermediate stages, and joins outside the degree regime remain unclassified here. The available public indexed results do not prove uniqueness; inaccessible/unindexed stronger coverage remains the main originality risk.

Self-review: passed. Independent audit: not yet performed.
