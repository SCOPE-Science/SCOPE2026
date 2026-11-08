# Scientific review: two spectral scales for wheel excitation

## Correctness — PASS

The theorem is decomposed into disjoint initial-state classes. In the nontricolored case, the explicit three hub-state case analysis proves that all sites rest by time four. In the tricolored case, a triangle rotates indefinitely, fixing a three-periodic external hub drive. The finite-speed lemma reduces the all-order identity to exactly 43,046,721 length-15 ternary local configurations, exhaustively checked with the included C program. An independent graph-based Python implementation checks all 265,680 labelled initial states on eight small wheels, independently matches extinction counts and the primitive-orbit-state census, and verifies both characteristic polynomials. The transfer counting and period-three argument yield both exact formulas for all rim lengths. Limit: the computational portion of the all-order claim depends on the transparent, complete finite light-cone reduction and reproducible C enumeration, rather than a handwritten symbolic simplification of its 43 million cases.

## Originality — PASS with residual priority risk

Gravner, Lyu, and Sivakoff's 2016/2018 general graph theorem characterizes synchronization through conservative initial 1-forms and gives the diameter bound. Thus the qualitative tricolored-triangle criterion is established prior coverage by implication, and the four-update upper bound is a close consequence of that theorem. The claimed distinctive result is instead the exact wheel-specific primitive three-orbit trace count, the extinction trace count and their comparison as two different exponential rates. These enumerations and the two-scale asymptotic are not statements supplied by the inspected general theorem. The earlier Durrett–Griffeath 1993 paper is relevant background, but its full manuscript could not be inspected; its accessible abstract concerns lattice waves and phase thresholds. Results recorded for wheel majority and wheel chip-firing apply different update rules and do not imply this Greenberg–Hastings census. No wheel-specific exact excitation census was identified in the conducted literature and research-database searches. An equivalent unindexed treatment remains possible.

## Mathematical value — PASS

The two exact enumerations describe complementary natural invariants: the full attraction basin of the unique resting fixed point and the number of distinct primitive sustained-activity orbits. Their growth rates are not equal: the extinct basin grows like \((1+\sqrt2)^n\), but the set of initially recurrent states grows like \(\rho^n\), for \(\rho<1+\sqrt2\). Thus a typical initial state is destined for a period-three attractor within four steps even though periodic initial states are exponentially exceptional. The temporal and orbit-count statements together give a concrete finite-network excitable-media classification not reduced to the prior qualitative circulation criterion.

## Sources and remaining limitations

Primary text inspected: Gravner–Lyu–Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, DOI:10.1214/17-AAP1350, specifically model definitions, Theorem 3, and proof. Original preprint: arXiv:1610.07320, submitted October 24, 2016. Earlier context: Durrett–Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, submitted March 22, 1993; only the abstract was available. The result is restricted to deterministic synchronous threshold-one three-state excitation and wheel graphs. An unindexed equivalent enumeration or more comprehensive historical treatment is a remaining possibility; independent audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.
