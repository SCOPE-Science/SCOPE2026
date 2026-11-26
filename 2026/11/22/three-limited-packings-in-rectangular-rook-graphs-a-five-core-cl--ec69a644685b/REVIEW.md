# Independent mathematical audit

## correctness

PASS

For the selected-edge graph in K_(m,n), the closed-neighborhood load at any cell ij is d_i+e_j−1_{ij selected}, including at missing cells. At maximum shore degrees r,c the load condition forces r+c≤4, and when equality holds precisely all intersections of maximum-degree vertices must be selected. Up to transposition the cases r+c≤3 give a matching or disjoint two-stars with centers on one shore, including the empty set separately. In the (3,1) case all used columns must meet the degree-three row, so only that star exists. In the (2,2) case the maximum-degree vertices induce a selected K_(a,b) with a,b in {1,2}. Filling their remaining incidences with degree-one endpoints gives P₄, either orientation of P₅, or C₄; the remaining edges are a matching on unused vertices. These conditions are sufficient as well. Choosing p double and q single centers and assigning disjoint opposite endpoints gives the R summand, with two orientations intersecting exactly in the matchings. The P₄ and C₄ counts are 4 and 1 per 2-by-2 block; a row-centered P₅ uses a center row, an unordered column pair and an ordered pair of other rows, then a matching on unused roots. Together with the isolated-star count these give the exact polynomial. The forest on the smaller shore attains min(2s,ℓ), and the C₄ family attains s+2 while the other exceptions do not exceed it. At ℓ≥2s, s≥3 makes 2s strictly better than s+2: every optimum is a double star centered at every smaller-shore vertex with all leaves distinct, counted by ℓ!/[2^s(ℓ−2s)!]. Read the finding's 'rows' as the smaller shore, after the transposition explicit in the proof.

## originality

PASS

The strongest same-host matches count induced three-independence or pack edges of the rook graph; the closest closed limited-packing product theorems are at capacity two. The related same-day triangular finding does not give this bipartite-root classification. Credit applies to the closed-three exact all-set census, rectangle maximum and long-board optimizers, not to the common degree formula.

## value

PASS

Rook graphs are a natural two-parameter family in which unselected intersections couple the row and column loads. The exact census exposes which small cores can coexist with a matching and predicts a sharp aspect-ratio change: the C₄ construction wins on short rectangles and doubled occupancy on the smaller shore wins on long ones. All coefficients and the long-rectangle extremizer count convey information beyond a generic product bound or an existence example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
