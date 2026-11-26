# Independent mathematical audit

## correctness

PASS

Each admissible cyclic word is a balanced de Bruijn traversal using at most one edge per nonpalindromic reversal orbit. The frozen conservation-difference and quotient-degree conditions are necessary, so its integer program is a valid relaxation for the upper bound. Independently of solver tolerances, the signed orbit graph has 12 unit-imbalance vertices and 4 odd-degree constant vertices. Pairing compatible discarded half-edges leaves eight edge-disjoint trails between these 16 defects. For a trail with c constant endpoints, length is at least 2+c unless it uses an aabb orbit with a≠b, in which case it is at least 1+c. The short-trail cases follow by reading consecutive directed four-grams with opposite-sign joins; they are also exhaustively verified in the independent checker. The six aabb orbits can discount at most six trails, so at least 2·8+4−6=14 of the 120 orbits must be discarded. The literal frozen word has 106 distinct cyclic reversal classes and no palindromic windows.

## originality

PASS

Credit the published graph equivalence, the prior upper bound of 112 and the independently indexed 106-symbol construction. The supported distinct result is that 107 through 112 are impossible, establishing the exact maximum, not discovering the word or graph representation.

## value

PASS

This closes the documented first small quaternary order-four capacity gap for direction-distinguishing cyclic codes. The exact number is useful to anyone deciding whether one can encode more than 106 locations under those constraints. It rules out every larger admissible cycle, rather than contributing another construction at an already known length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
