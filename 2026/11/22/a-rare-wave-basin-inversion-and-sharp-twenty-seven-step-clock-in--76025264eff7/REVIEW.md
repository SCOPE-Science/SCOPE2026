# Scientific review

## Correctness — PASS
The two C++17 programs enumerate the exact same set of \(4^{12}\) possible initial states under equivalent independently constructed Frucht-graph labels; graph equivalence is checked by an explicit edge permutation. One classifies the full functional graph by indegree peeling; the other traces paths until first repeats. Both produce identical period/entry populations, sorted individual orbit basins and the sharp extremal layer. Their counting algorithms are complete for a finite map, not random samples. In particular, the per-orbit comparison is strict even at the worst endpoints \(385193>373631\). The separate initial-state witness reaches a four-cycle first at update \(27\), while the full census proves no deeper transient.

## Originality — PASS, subject to historical-priority risk
The 1991 Fisch–Gravner–Griffeath framework defines general multicolor excitation and studies planar lattice waves, not an exhaustive finite Frucht-graph basin census. Gravner–Lyu–Sivakoff analyze **three-color** arbitrary-graph excitation; their theorems do not transfer four-state orbit counts. Readable public exact finite-graph records give (a) the *three-state* Frucht spectrum and (b) *four-state* Chvátal dynamics. Neither contains or implies this same-graph, four-state, individual-basin inversion. Semantic and exact-parameter searches found no dominating prior statement, but search is not a proof of first discovery and nonindexed sources remain possible.

## Value — PASS
The Frucht graph is the canonical smallest asymmetric cubic graph, removing all nontrivial geometric-symmetry explanations of orbit-basin populations. Its four-state excitation has a natural and complete finite orbit classification, with an unexpected ordering: each of only ten five-cycle basins is larger than every one of 1,024 four-cycle basins. The distinction is essential for interpreting random initial conditions—most likely eventual period and most common attractor period are different—and its 27-update sharp transient contrasts with established related graph/color cases. This is a meaningful whole-object classification and strict basin separation, not a merely arbitrary subset or numerical improvement.

## Closest prior statements and limitations
Publicly inspected 3-state Frucht census: different color count and 21-update maximum; publicly inspected 4-state Chvátal census: different graph and 12-update maximum; general 1991/1993 and 2016 references: no exact Frucht orbit/basin table. The result is a reproducible finite exhaustive proof, not an all-graphs theorem; historical precedence and independent external assessment remain open.

Self-review: passed. Independent audit: not yet performed.
