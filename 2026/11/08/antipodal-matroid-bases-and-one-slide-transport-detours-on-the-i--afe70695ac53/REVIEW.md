# Mathematical review

## Correctness — PASS

The claim is a complete finite result for the icosahedral graph on twelve vertices. The explicit neighborhood list removes ambiguity about graph labeling. The decisive nonstandard fact—that every pair's equal-distance witnesses form at most two antipodal blocks—is checked for all \(66\) pairs. The pair-signature obstruction for every two-landmark set proves minimality, and the equidistance classification proves exactly which triples resolve. This yields the partition-matroid basis description without assuming a matroid axiom.

Two standalone, exact-integer implementations independently enumerate the \(220\) candidate triples and all \(160\) accepted bases. They independently construct slide and jump edges, run complete all-source shortest-path computations, and test every one of \(12720\) distinct basis pairs against all six transportation matchings. Agreement establishes the \(9\)-regular graph, the \(720\) edges, radius \(4\), diameter \(6\), and the precise \(610\) transport detours. The separate unrestricted \(220\)-state token-graph comparison verifies that the transport baseline is achievable when the metric-basis condition is lifted. These are complete finite checks, not extrapolation. Residual correctness risk: ordinary implementation or shared-graph-input mistakes; fully explicit source permits independent recalculation.

## Originality — PASS, qualified

The prior icosahedral metric dimension \(3\), antipodal Taylor-graph method, resolving-set exchange-property framework, and general token graph construction are **not** claimed as new. Relevant primary full texts were inspected, especially Bailey's table for the icosahedron and his Taylor-graph theorem, Boutin's resolving-set exchange framework, and Fabila-Monroy and coauthors' general \(k\)-token graph. The specific all-bases partition-matroid classification and the adjacency-restricted \(160\)-state graph with its exact eccentricities and one-step transport-defect count were not found there.

The unrestricted \(220\)-state three-token graph is a supergraph, not a stronger theorem implying the geodesic metric of its \(160\)-state basis-induced subgraph. A general matroid basis-exchange graph describes token jumps, not original-graph-edge-constrained slides. Published-record searches for metric bases, resolvability, icosahedral antipodes, induced token graphs and exact transportation detours, along with semantic searches for matching recorded claims, did not yield a covering theorem. Source-access uncertainty for unindexed or unpublished enumerations remains; failure of search is not proof of historical novelty.

## Value — PASS

Metric bases are optimally small landmark sets whose move-by-move reconfiguration is a natural sensor-relocation problem. The state space is not an arbitrary slice: *all* minimum metric bases on a canonical symmetric graph are classified, with a structurally meaningful partition-matroid description. This supports an exact comparison of unconstrained basis exchange, physically local token sliding, and graph-metric transportation. The finding that \(610\) pairs require exactly one additional move, no pair requires two, and the radius and diameter differ from the jump model is a motivated complete metric classification, not merely an uncontextualized sequence of counts.

## Closest literature and limits

Boutin (2008, arxiv:0808.1427) is the archive-date anchor and develops exchange for resolving sets. Fabila-Monroy et al. (2009, arxiv:0910.4774) introduces the *unconstrained-state* token graph. Bailey (2013, arxiv:1312.4971 and arxiv:1312.4973) treats antipodal Taylor graphs and records the known icosahedral metric dimension. These do not explicitly classify the constrained slide graph or its detours in the material inspected. A university faculty page also lists a 2026 master's thesis entitled *Reconfigurations of Metric Bases*. Its full text could not be located; the available project description discusses other graph families, so no conclusion of noncoverage is inferred for that thesis. The exact numbers refer only to the ordinary \(12\)-vertex icosahedron. Independent scholarly validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
