# Scientific review: exact variance of complete-bipartite spanning-tree overlap

## Correctness — PASS

The event that an edge belongs to both sampled trees has probability equal to the square of its single-tree inclusion probability. The transfer-current projection on \(K_{a,b}\) is computed explicitly from its three nonzero Laplacian eigenspaces. Its two-edge determinants give all three incident/disjoint geometries, whose exact numbers are listed in the proof. Summing covariance terms gives the factored variance. The derivative and exact comparison between smaller parts of sizes two and three establish the all-size maximizer and strict uniqueness, including stars and small-order boundaries. There is no extrapolation from finite checks. The standalone checker independently enumerates spanning trees for \(1\le a,b\le4\) and tests 836 exact assertions.

## Originality — PASS, with historical-priority qualification

London and Pluhár (2023) develop the expectation of the intersection size, not its finite variance. Albin and collaborators (2021) study the variance of *edge usage probabilities* across graph edges, which differs from the random overlap variance. Dong and Ge (2021) provide the general prescribed-forest spanning-tree count used as underlying machinery: the new claim does not appropriate that counting formula and instead identifies the factored two-tree overlap variance and its complete fixed-order optimizer transition. Bóna, Burghart and Wagner (2025) study asymptotic distributions for complete multipartite graphs, including a dense Poisson limit and a thin bipartite approximate binomial law, but their accessible full June 2025 text does not contain the finite variance extremum. The September 2026 revision was only available at metadata/abstract level; it remains a specific residual priority risk. Searches against indexed mathematical records and recoverable neighboring statements did not produce the \(n=10\) extremal transition. These observations do not assert exhaustive priority.

## Value — PASS

The overlap statistic directly quantifies agreement between two independent random network skeletons. Its mean is determined by edge-use probabilities, but its fluctuations are sensitive to interactions between pairs of edges. A closed form for an entire graph family and the sharp change in the maximizing bipartition at ten vertices are natural, complete finite statements. The same formula captures a qualitative variance scaling distinction: fixed thin side yields linear growth, whereas balanced parts yield a bounded variance converging to four. This is more informative than a numerical table or a restatement of the expected overlap.

## Limits and risk

The result covers only uniform trees in complete bipartite graphs and only the first two overlap moments. Historical novelty might be affected by an uninspected later version of Bóna--Burghart--Wagner, or by an older derivation not found in available searches. The all-size correctness proof does not depend on historical novelty or on finite numerical testing.

Self-review: passed. Independent audit: not yet performed.
