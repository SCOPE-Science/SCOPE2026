# Independent mathematical audit

## correctness

PASS

Three perfect matchings contain a total of |E| edge slots, so a cover partitions the edges. Labelling the three nonempty colour classes gives a free six-element action. On a replacement triangle the internal edges must use all three colours, forcing the external colours to be distinct and determining each internal edge by the opposite external one. On a two-terminal unit each colour is a matching, so its number of external incidences has the parity of the unit's (even) order; the two terminal links must have the same colour. A 2-cycle then has the two orders of the other colours, and in a diamond the two orders of the side colours at one terminal each force all remaining edges. The channel rules multiply independently; in a ring the common link colour gives an extra factor of three. Both exceptional graphs have six labelled colourings. Zhou–Wang's Lemma 2.1 matches the stated connected multigraph scope and (1) gives |V(G)|=3|V(H)|+4ℓ+2r, with totals ℓ,r. The small-core fact can be checked without relying on the book census: in a minimum non-3-edge-colourable bridgeless loopless cubic multigraph a triangle contracts or a double edge smooths to a smaller bridgeless cubic graph with equivalent colourability (the triple edge is already colourable, and coincident external endpoints of a double edge would force a bridge). A perfect matching exists by Petersen's theorem. Its complementary 2-factor must contain an even positive number of odd cycles, of lengths at least five after the reductions. Thus no smaller obstruction exists and any obstruction of order ten consists of two chordless 5-cycles with a matching between them. An adjacent pair matched to an adjacent pair gives a Hamilton cycle, hence a 3-edge-colouring. Otherwise the matching identifies one cycle with the complement of the other, giving Petersen. In Petersen a perfect matching uses 1, 3 or 5 spokes: three is impossible because the two unmatched indices cannot be adjacent on both cycles, while one and five each leave odd cycles. This proves the required uniqueness, and equality at 30 forces no channel units. The frozen verify.py was inspected, not executed; its finite examples do not yield the global taxonomy or the census.

## originality

FAIL

The exact multiplicities, not just existence, are covered by the previously published small-cut factorization of the flow polynomial after evaluation at four. Dong, arXiv:1808.00175, Lemma 3, equation (2.5), records the general formula credited to Jackson. Its contractions and normalization give the claimed factors on exactly the Zhou–Wang decomposition. The stated order cutoff is then the known minimum-core fact and the prior order identity. No inspection established that the entire frozen piecewise statement was printed verbatim elsewhere; failure concerns implication by stronger existing results, not correctness or an inaccessible source.

## value

FAIL

Three-cover counts are a natural baseline for the four- and five-cover problems, and the decomposition gives a convenient presentation. But the exact invariant here is obtained by evaluating an existing stronger flow formula at four and substituting two elementary gadget values. The cutoff is likewise a direct order substitution and adds no new core classification. The record neither computes the hard core count in general nor establishes any independent consequence beyond these deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
