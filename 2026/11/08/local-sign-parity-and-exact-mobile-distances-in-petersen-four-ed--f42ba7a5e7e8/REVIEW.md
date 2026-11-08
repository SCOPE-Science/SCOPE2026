# Scientific review

## Correctness — PASS

The exact graph is defined without quotienting the named colours or Petersen vertices. A legal edge change exists precisely if both endpoints have the same missing colour; both corresponding local permutation signs reverse, proving sign conservation. A complete lexicographic edge-assignment search covers all 49,920 legal configurations and tests every alternative colour on every edge. Full adjacency and component BFS establish 109,440 undirected edges, 960 isolated configurations, and two connected 24,480-state sectors of opposite sign. The locally invariant sign is therefore a **complete** distinguishing invariant among mobile states. The finite enumeration of all 42 actual \(A_5\times S_4\)-orbits and 40 full component BFSs proves exact eccentricities, hence radius 24 and diameter 25. A second exact-cover method independently reconstructs the complete state space and component data. The frozen missing-colour structural classification is also verified. No infinite extrapolation is used.

## Originality — PASS (qualified)

OEIS A159233, authored 2009-04-06, already provides the underlying count 49,920, which is explicitly excluded from the novelty claim. Ito–Kamiński–Demaine (2009) studies the same type of single-edge move in the general list-edge setting, but its relevant statements are complexity bounds for broader classes and constructive results for trees, not the exact Petersen sector geometry. McDonald–Mohar–Scheide (2010) proves connectivity under Kempe-chain interchanges, strictly broader than one-edge moves: a connected graph for the stronger moves may have disconnected finer single-edge reconfiguration. The prior known Petersen four-edge Kempe classification also concerns the stronger move. The parity obstruction, its complete mobile-sector characterization, 960 frozen states, exact degree counts and component metrics are not implied by these cited results. Full-text comparisons and semantic record searches did not identify an earlier complete matching classification. Priority beyond inspected sources is qualified, not certified.

## Value — PASS

Four is the **minimum** proper edge palette for the Petersen snark. The theorem resolves global reachability at that natural threshold, rather than an arbitrary colour/graph slice. It demonstrates sharp topological fragmentation (962 components) despite full Kempe-chain interchange connectivity, supplies a simple structurally motivated obstruction, and gives reproducible finite component geometry and sharp conversion distances useful in studying low-palette graph recolouring algorithms. The degree and metric data distinguish mathematically different kinds of states and are not merely known counts recomputed.

## Closest literature and remaining risks

OEIS A159233 supplies only colouring counts, not reconfiguration transitions. Ito–Kamiński–Demaine, *Reconfiguration of List Edge-Colorings in a Graph* (2009), DOI 10.1007/978-3-642-03367-4_33, defines and studies the same allowed local move but does not supply this special classification. McDonald–Mohar–Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs* (2010), arXiv:1005.2248, concerns a stronger move and is logically consistent with local disconnection. Exhaustive historical priority cannot be certified: older unpublished computational tables or equivalent line-graph recolouring descriptions may exist. The radius/diameter depends on the supplied fully exhaustive executable certificate, and has not been independently audited externally.

Self-review: passed. Independent audit: not yet performed.
