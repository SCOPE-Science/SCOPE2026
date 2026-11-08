# Mathematical review

## Correctness

PASS. The assertion is for the literal twenty-five-column generator in the original paper. Unique reduced row echelon bases enumerate each of the 2663 nonzero subcodes exactly once, and all 243 codewords are enumerated separately. The dual supports are checked by exhausting all 2300 triples and 12650 quadruples with normalized nonzero ternary coefficients. A direct matrix-rank calculation verifies projectivity and the LCD property. The executable checker recomputes the complete numerical statement from the embedded generator, with no floating-point approximations.

## Originality

PASS against checked sources, subject to historical-priority uncertainty. An et al. provide the generator and its minimum distance but do not report the exhaustive support distribution, higher weights, low-weight dual spectrum, or coordinate localities in Proposition 4.1 and Table 1. Wei gives the general definition and consequences of generalized weights, not these numeric values. Related work on a different \([23,5,12]\) LCD construction does not imply the invariants of this nonidentical twenty-five-coordinate matrix. No matching indexed claim was found under exact-code, support hierarchy and locality formulations. Residual risk: an unindexed table or preexisting computation may contain the same spectrum.

## Value

PASS. The code is a recent minimum-distance-improving construction whose full support hierarchy, previously unspecified in the inspected source, determines more detailed erasure and wiretap-II properties than its advertised \([25,5,14]\) parameters. The novel, nonuniform coordinate-locality profile is operationally meaningful for local repair: four specified symbols require one extra helper, and the dual check enumeration establishes exactly why. The finite result is a natural structural fingerprint of a named coding construction rather than an arbitrary parameter slice.

## Limits

The result does not characterize all equivalent or optimal codes with these parameters, and does not establish a new universal code bound. A self-review is not independent certification. The relevant 2026 source and classical generalized-weight literature are inspected; unindexed historical priority remains a risk.

Self-review: passed. Independent audit: not yet performed.
