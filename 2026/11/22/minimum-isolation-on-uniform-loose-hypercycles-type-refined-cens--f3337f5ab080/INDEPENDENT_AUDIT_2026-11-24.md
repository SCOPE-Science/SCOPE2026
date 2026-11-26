# Independent mathematical audit

## correctness

PASS

A private vertex and the junction with the same start hit cyclic intervals of length 3 and 4, respectively. Coverage by four per vertex gives the lower bound; junctions with positive gaps at most four attain it. Nested arcs at a repeated start would make one vertex redundant. In the periodic lift of distinct starts for m>=5, right endpoints are nondecreasing (lengths differ by at most one), so each gap must be covered by its own start. The boundary cases m=3,4 also give that condition directly. Deficits 4-d sum to delta<=3; at a positive deficit the gap admits one junction or r-2 private labels, and at zero it admits only the junction. Marking one start double counts with factor m/k and yields the polynomial and the at-most-delta private bound. For exchange, promote each private vertex to its same-start junction. Advancing a junction by one transfers one deficit from its outgoing gap to the previous gap; a positive donor implies the receiving gap has deficit at most two, so the move is legal and collision-free. Such transfers gather and redistribute all deficits, and a full circuit of one unit advances all marked junctions by one, giving every labelled translation. Zero deficit gives four disjoint periodic minima, hence isolated for k>=2; m=4 is K4 and m=3 has all singletons. A separate direct subset and exchange check confirmed every coefficient and component size for m=3..12, r=3..5.

## originality

PASS

Pass for the rank>=3 census by private-vertex type. The ordinary cycle minimum size, unmarked junction-only count and four-periodic connectivity threshold have direct prior coverage. The private-vertex count and its extension of the exchange statement require identifying a different local coverage rule and its legal decorations; the inspected cycle result alone does not state or imply those counts without that additional analysis. The exchange obstruction is inherited, not independently new.

## value

PASS

The complete type distribution answers how many optimal configurations use each kind of vertex when the uniform rank varies, a question not answered by the ordinary-cycle number or phase transition. It distinguishes ranks and shows that the non-junction contribution is confined to at most three vertices even at arbitrarily large order. This gives an exact benchmark for minimum isolation and for the effect of adding alternative vertices to an exchange system, with modest rather than standalone novelty for connectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
