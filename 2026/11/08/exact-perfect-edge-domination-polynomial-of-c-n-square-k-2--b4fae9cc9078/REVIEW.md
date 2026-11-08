# Scientific review: perfect edge domination on circular ladders

## Correctness — PASS

The original adjacency count for each omitted edge is converted to three explicit Boolean local constraints on consecutive columns. The 64-state directed transfer graph represents every admissible cyclic edge set without quotienting. Its complete positive-return graph is an isolated loop and a directed six-cycle, established by checking all 512 possible local triples and reachability on all 64 states. The finite calculation is a fixed nonstandard lemma, not an estimate based on testing a finite list of cycle orders. Each closed walk gives exactly one labelled edge selection; the six-cycle contributes six periodic selections when its length divides the cycle order. The standalone verifier separately tests graph-endpoint incidence for all edge subsets through seven columns. No other graph families or boundary values are claimed.

## Originality — PASS, with residual priority risk

The July 2026 work of Grippo, Lin, Moyano and Vera (arXiv:2607.03894) motivates exact enumeration of perfect edge dominating sets, but its inspected available text and stated contributions concern extremal trees, forests, chordal graphs, and counting algorithms for generalized series-parallel or chordal graphs, not the explicit polynomial for circular ladders. Prior 2025 work by Grippo, Lin and Vera (arXiv:2509.04598) treats algorithmic complexity, including \(P_6\)-free graphs, and does not directly imply this infinite cycle-prism formula. The 2024 work of Mahmoodi et al. rules out dominating induced matchings on prisms, which is not a covering assertion because the six additional sets here are not matchings. Targeted searches and comparisons of historical mathematical records returned no equivalent complete enumeration. Risk: the remainder of the July 2026 full text was inaccessible during the review, and historical priority cannot be guaranteed by searches.

## Mathematical value — PASS

The recent literature identifies counting perfect edge dominating sets as difficult in broad graph families. This exact polynomial resolves all sizes and all edge subsets of the standard circular ladder, rather than producing a scalar minimum or an algorithm-only answer. The sharply discontinuous period-six phenomenon and the constant multiplicity of six across unbounded graph orders are structurally informative. The result also exhibits a natural family with no dominating induced matching but, for infinitely many orders, six smaller perfect edge dominating sets. This is a motivated, complete infinite-family classification, not an arbitrary finite census.

## Limits and source availability

The result does not enumerate equivalence classes under dihedral or row-swap symmetries, and it does not address arbitrary prism products. The critical reachability lemma is backed by an explicit reproducible finite enumerator; independent human verification is outstanding. The originating paper was inspected through accessible HTML introductory/preliminary material, but attempts to retrieve the remaining full text were unsuccessful. This residual source-access limitation was included in the originality assessment rather than silently treated as negative evidence.

Self-review: passed. Independent audit: not yet performed.
