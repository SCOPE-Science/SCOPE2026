# Independent mathematical audit

## correctness

PASS

Independently replayed the complete 177147-state domain using memoized paths and first-repeat dictionaries, not either frozen implementation. Each successor uses the displayed adjacency and the old configuration, with unconditional GHM 1->2->0 and contact-only CCA advances. On first repetition within a path the suffix beginning at the previous occurrence has the least period and zero entry depth; a reverse pass assigns the prefix, or assigns the entire path from a previously classified tail. Every input is covered. There are zero pointwise period mismatches and the common populations at periods 1,3,4 are 17397,23346,136404. Recurrent-state totals are CCA (3,3060,4752) and GHM (1,3060,1200); the replay checked recurrent containment, identical period-three sets and matching successors on every GHM recurrent state. The orbit counts follow by division by least period. Every one of the 21 CCA and 27 GHM depth-period histogram cells matches both frozen tables. The only deepest cells are CCA (8,3) with 108 starts and GHM (10,3) with 36. The displayed graph was also checked independently to be simple, 3-connected planar, non-Hamiltonian and of size (11,18), identifying it as Herschel by the uniqueness for those parameters.

## originality

PASS

The distinct content is the exact finite Herschel classification: the period support, pointwise basins and their sizes, refined recurrent populations and all first-entry clocks, especially the nonuniversal period-four census. Synchronization and period divisibility are credited; generic recurrent transition agreement and period-three coincidence are not independent graph-specific discoveries. No inspected stronger statement or table gives the numerical or pointwise Herschel classification.

## value

PASS

Herschel is a natural extremal irregular polyhedral graph for comparing two closely related excitable automata. The exact equality of period selection, alongside four-cycle population disparity and different maximal clocks, separates identical eventual periodicity from equality of the recurrent sets and transients. The census is a useful exact benchmark beside biclique agreement and period halving on other sparse graphs, not a claim that non-Hamiltonicity enforces equality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
