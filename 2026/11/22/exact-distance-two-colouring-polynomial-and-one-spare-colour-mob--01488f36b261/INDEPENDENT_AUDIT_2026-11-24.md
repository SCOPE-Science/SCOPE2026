# Independent mathematical audit

## correctness

PASS

Each shore is a 7-clique in the square; a point and line form a cross-shore conflict exactly at incidence. Thus shared names are a matching in the 4-regular bipartite nonincidence graph. Assigning the point names, then a matching, then distinct new names to the unmatched lines is bijective, proving the falling-factorial polynomial. The subset recurrence counts a matching once by its skipped lines and the point chosen at each remaining line. A separate run reproduced (1,28,294,1456,3514,3864,1596,144), hence chi=7, P(7)=725760 and P(8)=70156800. Seven colours freeze both cliques. In the eight-name palette, seven-used states can move only to the globally spare name, at each of 14 vertices. Eight-used states can move only to the name missing on the moved vertex's shore; exactly four vertices on each shore are nonincident with the opposite singleton and can do so. Only the two singleton moves can drop a name, and both are legal precisely for an extendible six-matching. Each perfect matching gives seven distinct extendible six-matchings, each with a unique extension, yielding 1008 and leaving 588 unextendible. The action of the 8! colour permutations is free, including when one name is unused, so these numbers and the degrees give all the claimed named counts and edge counts by double counting. The independent program checked moves with multiplicity at 1740 normalized states, not all named states. Merkel's Theorem 2 proves named connectivity directly. For the supplementary lift, the normalized paths lift by colour equivariance; at a seven-used state the two vertices of one shared name can be recoloured in turn to the name that was initially unused (now legal on its opposite shore), swapping that name with the spare. These operations generate all name permutations.

## originality

PASS

The supported distinct contribution is the exact square chromatic polynomial and named seven/eight-colour degree and transition census, not the matching method or the connectivity conclusion. Merkel covers the connectivity and also an upper diameter bound. The inspected matching and colouring records use different graphs or different colouring rules and do not give the exact census. The target itself appearing in Resultary is not independent coverage.

## value

PASS

The square of the smallest projective-plane incidence graph gives a natural example at the optimal-colour threshold. The exact polynomial fixes the optimal palette count, while the transition census distinguishes the frozen optimum, mobility with one extra name, and precisely which states can return to seven used names in one move. These are quantitatively useful benchmarks for distance-colouring or reconfiguration work even though the connectedness with a spare colour is already known. The value is the full motivated finite invariant, not just repeating a mixing theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
