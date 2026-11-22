# Review of the stationary-plurality theorem

## Correctness — PASS
The graph, colors and synchronous open-neighbor update are completely specified. The peripheral fixed condition has a two-neighbor logical form, yielding exactly five page types for agreeing hubs and six for distinct hubs. The coefficient formulas retain every page label. The hub predicate explicitly accommodates any tied maximum, even a tie that excludes the current opinion. A separate large-deviation proof identifies the leading failure events, bounds competing unique-winner events by \(\beta^m\) and the two-hub intersection by \(\mu^m\), both with bases strictly smaller than \(\rho\), and obtains the precise positive prefactor using a lattice local central limit theorem. The agreeing-hub sector has at most \(5^m\) states. The scripts reproduce exact counts via independent dynamic-programming and graph enumeration algorithms and check the moment-generating-function constants. The asymptotic is analytic; the numerical tests are only corroboration.

## Originality — PASS, qualified
The closest literature is the 2012 information-aggregation work of Mossel–Neeman–Tamuz, the 2015 graph-coordination game paper of Apt and collaborators, and a 2025 study of deterministic three-opinion dynamics by Di Ianni. Their inspected theorem statements and model definitions do not give the exact quadrilateral-book fixed-state polynomial or its nontrivial large-deviation correction. In particular, Nash-equilibrium counting under best-response and fixation under arbitrary incumbent retention are different problems: a vertex may remain fixed on a maximal tie even though its present opinion is not tied for the maximum. Public research records on quadrilateral books concern Greenberg–Hastings excitation, chip firing or leader placement, not this map. No result that logically implies the stated formula was found in the searched records. Priority remains provisional because one 2010 tie-resolution conference article was available only in abstract, and unidentified older equivalents could exist.

## Value — PASS
The quadrilateral book is a canonical arbitrarily long, bounded-treewidth graph with a two-vertex hub edge. Counting its stationary configurations is a natural exact observable of a deterministic local social-influence system. The result proves that a uniform fixed state overwhelmingly has *different* hub opinions even though the rule is locally conformist; it quantifies this separation and its exponential rarity with a strict entropy gap. More strongly, it determines the first missing-mass correction to the total fixed-state count with a nontrivial algebraic rate \(1+2\sqrt6\) and a precise \(m^{-1/2}\) prefactor. The critical distinction between incumbent tie retention and best response is scientifically material. This is not a generic enumeration at a selected finite size, and no unsupported convergence-of-trajectories statement is made.

## Closest literature and remaining limitations
- Mossel, Neeman, Tamuz, arXiv:1207.0893v1 (2012): information aggregation and unanimity; no book fixed-state census.
- Apt et al., arXiv:1501.07388 (2015): Nash/coalitional equilibria for graph coordination, not this tie-retaining stationary map.
- Di Ianni, DOI 10.3390/appliedmath5040147 (2025): three-opinion deterministic dynamics and complexity, with different local update rules.
- Yang and Pan, DOI 10.1109/WMSVM.2010.30 (2010): tie-resolution study of group opinion updates, abstract only inspected.

The theorem concerns stationary states rather than basins of attraction, has three named opinions, and assumes unweighted synchronous updating. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
