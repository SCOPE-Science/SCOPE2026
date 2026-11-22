# Review of the spanning-tree exchange geometry theorem

## Correctness — PASS

The exact forcing rule is skew: a white or blue vertex with one white neighbor can force that neighbor. The proof rules out a zero-original starting set and a white subdivision cycle, and constructively forces any remaining edge forest by leaf elimination. Connectedness then forces all original vertices. The minimum cardinality and rooted-tree parametrization follow from the sharp forest edge bound. The exact exchange product and all-pairs distance follow from fundamental-cycle tree exchanges. For complete graphs, tree path-length counting proves the Wiener degree identity, while Cayley's tree counting across edge cuts yields the exact edge sum. Edge-disjoint spanning trees witness the diameter bound. The proof handles the boundary orders two and three separately. Both included standard-library programs successfully reproduced independent exhaustive and Prüfer-enumerative finite checks; their finite range is not an infinite proof.

## Originality — PASS, with explicit coverage boundaries

The 2023 work of Jacob defines the skew forcing polynomial, and the 2024 Curtis–Flagg–Hogben study treats skew-forcing reconfiguration by token addition/removal. Bonato et al., arXiv:2412.04389, Theorem 33, already establish the general incidence-graph/lazy-burning equivalence. In particular, the forest feasibility criterion here can be deduced from that broader reduction, and no independent priority for the mere feasibility predicate or minimum number is asserted. DeAlba's 2014 matroid theorem concerns bipartite graphs whose maximum matchings satisfy a restrictive uniqueness hypothesis. Bong et al.'s 2025 tree sliding theorem already covers the special case where the entire subdivided source is itself a tree. The published record on ordinary zero forcing of subdivided complete graphs uses a distinct forcing rule and yields different optimal configurations.

The contribution assessed is instead the precise minimum-configuration product for *every* connected source graph, its exact distance metric and absolute sliding rigidity on cycles as well as trees, together with the complete-graph Wiener-index degree law, closed exchange-edge census and sharp diameter. These conclusions are not stated by the inspected general incidence decomposition, tree theorem, or indexed ordinary-forcing record. The closest published indexed record was available by title and summary but not complete body; historical priority beyond the inspected sources cannot be guaranteed.

## Value — PASS

This result transports optimum-monitoring relocation on a large graph family to explicit spanning-tree geometry. It simultaneously gives a constructive fastest possible relocation path, a no-slide obstruction despite jump connectivity, a full Tutte-polynomial count of feasible starting sets, and an exact parameterized exchange-network edge count. The Wiener index supplies a nontrivial degree statistic that distinguishes choices of spanning trees. The scope is any connected finite source graph, rather than a one-off enumerated graph. The theorem does not imply anything about disconnected or higher-subdivision hosts or relaxation of minimum size.

Self-review: passed. Independent audit: not yet performed.
