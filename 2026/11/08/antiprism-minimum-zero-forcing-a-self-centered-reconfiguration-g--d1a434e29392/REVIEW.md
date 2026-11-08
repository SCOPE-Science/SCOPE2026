# Self-review

## Correctness — PASS

The all-order proof in `RESULT.md` does not rely on extrapolating finite tests. A first force in the four-regular antiprism requires the initial blue set to be four vertices of a closed five-vertex neighborhood; exhaustively deleting each of four possible neighbors gives the three cyclic families. Explicit parallel forcing fronts give their propagation times. Pairwise four-set intersections give every reconfiguration adjacency. A cyclic center-coordinate map bounds distances below by the half-circumference, and three-consecutive-index anchor sets bound all distances above by the same value. Independently written C++17 and Python verifiers corroborate the graph counts, degree split, eccentricities and full forcing sets for the tested orders. Remaining scientific limit: the proof addresses the specified infinite family but not the octahedral boundary or larger starting sets.

## Originality — PASS (historical priority qualified)

The earliest qualifying foundation is Hogben et al., arXiv:1410.4191v1 (2014-10-15), developing propagation-time invariants; it does not provide this antiprism classification in the inspected text. Boyer et al., arXiv:1801.08910v1, give zero-forcing polynomial theory and exact ordinary-cycle results, but not this cycle-square minimum-set distribution. Geneson, Haas and Hogben, arXiv:2009.00220v1, introduce the relevant token-jumping reconfiguration graph; their exact cycle result does not imply the square-cycle graph. Searches using antiprism/circulant/cycle-square aliases, the \(6n\)/\(18n\) counts and the reconfiguration-diameter statement found no equivalent direct result. The possibility of unindexed prior computation remains; no claim of independently certified novelty is made.

## Value — PASS

The result addresses the natural, labelled square-cycle antiprism family and simultaneously classifies optimum controlling placements, their two propagation speeds, and shortest one-token transformations among them. In particular, it gives a non-vertex-transitive, nonregular, connected and self-centered family of minimum zero-forcing reconfiguration graphs with uniformly bounded degrees yet unbounded diameter. This combination is a concrete structural example, not simply a re-evaluation of a known scalar forcing number or an arbitrary finite slice.

## Limits and relevant literature

The claim concerns ordinary zero forcing and token jumping, not positive-semidefinite forcing, token sliding, or the entire zero-forcing polynomial. Closest relevant sources: Hogben et al. (2014, arXiv:1410.4191), Boyer et al. (2018, arXiv:1801.08910), and Geneson–Haas–Hogben (2020, arXiv:2009.00220). The source comparisons are recorded with queries, inspected material and residual priority risks in `AUDIT.json`. The proof and two checkers support the mathematical statement; they do not replace external independent assessment.

Self-review: passed. Independent audit: not yet performed.
