# Scientific review: Rule 73 temporal-one and temporal-two census

## Correctness

**PASS.** The update is fixed by the eight-entry truth table (ones on `000`, `011`, `110`). A fixed temporal-one word yields a closed walk in the four-state de Bruijn graph whose edges enforce the central output. A fixed temporal-two word yields a closed walk in a sixteen-state de Bruijn graph whose five-symbol windows enforce the second update. This equivalence remains valid when the ring is shorter than a local window, because cyclic overlap identifies repeated positions. Both graph determinants are computed exactly by complete disjoint-directed-cycle expansions, rather than inferred from finitely many word counts. Their formal log derivatives therefore give the claimed zeta functions for *every* ring length. Aperiodic strongly connected components and rigorously isolated positive Perron roots establish the distinct exponential rates. Exact bitwise programs were independently replayed over all 524,286 indexed configurations on rings of lengths 1–18; the graph/determinant program also checked the complete exact finite certificate. The finite tests are cross-checks, not substitutes for the transfer proof.

## Originality

**PASS, qualified.** The all-length Rule 73 one-step image formula counts distinct output words; that statistic does not determine temporally fixed or twice-fixed words. A known Rule 18 temporal-two zeta uses a similar graph method but its rule, characteristic determinant, and growth root differ, and it cannot imply this result. The inspected full text of Stricker (2023) concerns maximal temporal cycle lengths on bounded rings rather than all-length numbers of configurations having temporal periods one and two. Kang (2013) treats spaced-neighborhood dynamics, not the nearest-neighbor rule used here. Wolfram (2002) describes localized structures and period-three oscillations but does not compute these two exact zeta functions. Record, alias (Rule 109), literature, and exact formula searches did not locate an equivalent or dominating result. Unindexed earlier literature remains a meaningful residual priority risk.

## Mathematical value

**PASS.** Rule 73's documented walls and localized temporal structures make short temporal orbits a natural invariant. Unlike a single finite-ring calculation, two exact all-length rational zeta functions enumerate *every* equilibrium and primitive temporal two-cycle, establish a robust exponential abundance gap, and exhibit a ring of length five with six oscillations and no equilibria. This distinguishes coherent oscillatory states from equilibria without asserting general attractor behavior. The exact denominator factors and isolated Perron eigenvalues make the invariant reproducible and useful for comparisons to other elementary rules.

## Closest literature and limitations

Wolfram, *A New Kind of Science* (2002); Kang, *Investigation of Rule 73 as Case Study of Class 4 Long-Distance Cellular Automata* (2013); Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k* (2023); *Exact cyclic one-step image series of elementary cellular automaton Rule 73* (2026); *Exact temporal-two orbit census and spatial zeta for elementary cellular automaton 18* (2026). The theorem does not count transients, maximal periods, or all temporal attractors. The symbolic graph calculation has been checked in the stated mathematical and computational ways, but not independently audited.

Self-review: passed. Independent audit: not yet performed.
