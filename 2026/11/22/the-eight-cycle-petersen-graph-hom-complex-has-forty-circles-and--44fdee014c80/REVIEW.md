# Independent mathematical audit

## correctness

PASS

The repaired claim identifies the cell complexes themselves. For an oriented simple hexagon (v_j), put a variable spur color in N(v_j) at source site i+1, fix i and i+2 to v_j, and traverse the hexagon on the remaining six steps. These are all single-spur maps and their containing triangles. At any vertex of a triangle the only potential second variable site is i or i+2, and the two cases require distinct spur colors v_(j−1) and v_(j+1). Those vertices glue to the triangles indexed by (i−1,j−1) and (i+1,j+1). Pairs of distinct vertices of the target have at most one common neighbor, so no other site can be recolored. No adjacent sites can both vary in a cell: it would contain a complete bipartite subgraph on two plus two distinct vertices in the square-free target. The incident cells are therefore exactly triangle faces. Translation by (1,1) on Z/8 × Z/6 has two orbits of order 24; it gives two entire connected components with the stated incidence and a private vertex per triangle. Each triangle and one private-vertex edge can be collapsed, and then the private vertex and remaining incident edge, leaving the embedded 24-cycle. Exact rooted walks give 120 hexagon parametrizations, hence 20 orientations modulo rotation and 40 components. The original numerical census also checks out: independent direct enumeration of compatible target masks gives (1)×240, (48,72,24)×40 and the one large component with Euler characteristic −10. The square-free-target wedge-of-circles theorem then gives the large component rank eleven, the same homotopy type as the connected bipartite double cover. The smaller even cases also have exactly one rank-eleven component and no circle components. The repair is for overlap, not numerical error.

## originality

PASS

The frozen headline homotopy census fails as a distinct contribution against available stronger coverage: the documented all-length Petersen primitive-period result supplies the point and circle multiplicities and the even double-cover component. In the eight-step case the only nontrivial shorter cyclically reduced cores are simple hexagons, giving two components for each of twenty oriented even-period necklaces. Rigid maps are the fifteen octagons with sixteen rooted directed maps each. This is coverage, not an assertion of publication order on the shared date. The repair instead proves the filled-triangle incidence model and explicit embedded-cycle collapse, not just the number, homotopy type, or 2-dimensional profile. The available stronger statement about reduced-walk necklaces does not supply these cell-level gluings.

## value

PASS

What survives is a cell-level normal form for the first nontrivially flexible even-source components, with every gluing specified and a canonical subcomplex cycle after collapse. A homotopy circle or a matching face vector alone does not give this geometry. The proof explains how backtrack position and core position govern attachment, useful when comparing polyhedral representatives or studying source reindexing, without claiming those further results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
