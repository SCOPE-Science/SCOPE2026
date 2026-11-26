# Independent mathematical audit

## correctness

PASS

Yang–Wang Theorem 1 includes point contacts and fixes the central subdivision under the frozen 21-neighbor hypothesis. Tiles correspond to pairs (lattice edge, incident equilateral face). Within one face the bases of any two subtriangles share an endpoint; across different faces any contact must be on a common lattice edge or at a lattice vertex. In both cases of contact the bases have a shared endpoint, and conversely. This is L(T)[K_2], of degree 1+2(5+5)=21, and edge transitivity in T plus interchangeability of the twins gives vertex transitivity. For distinct lattice edges, line-graph distance is one plus the minimum distance between endpoints, by shortening an incident-edge chain to a vertex path and extending a shortest endpoint path to a chain. For r=k+1>0 the base-edge ball therefore comprises all edges incident to the union S_k of the two endpoint radius-k lattice balls. At fixed -k<=y<=k their triangular-metric x-intervals differ by a unit shift, hence have union of length 2k+2-|y| in lattice points. Summing gives (k+1)(3k+2), including k=0. The one-step exterior is S_{k+1} minus S_k, of size 6k+8. Its six corners have one inward neighbor each; for the noncorner points of the sides x=-k-1, y=-k-1 and x+y=-k-1 the inward step pairs are respectively {(1,0),(1,-1)}, {(0,1),(-1,1)} and {(1,0),(0,1)}; they stay in the other two strips. Central inversion (x,y)->(1-x,-y) supplies the opposite sides. Thus all noncorners have two inward neighbors, also for k=0. The lattice cut has 12k+10 edges, and six times |S_k| plus that cut is twice the number of incident base edges. Exactly this gives the tile ball size 18r^2+6r-2. At an exterior lattice vertex with a inward neighbors, a(6-a) distinct pairs of incident edges cross the line-graph cut. The six one-inward cases and 6k+2 two-inward cases give 48k+46, lifted fourfold to 192r-8; no fiber edge crosses when r>=1. The singleton cut has degree 21. Differences give spheres, and summing the quadratic after correcting its r=0 value gives the recorded series. The frozen script and its reported exact geometry and bounded counting/BFS checks were inspected, not rerun; the argument above checks all radii rather than extrapolating those counts.

## originality

PASS

No credit for the prior equality geometry or local neighbor count. A distinct same-day record has the equivalent doubled-line-graph model for periodic quotients, so the factorization is not treated as an independent originality claim. The supported contribution is the joint explicit all-radius point-contact ball and outgoing-edge profile of the plane tiling. Same-day publication does not establish priority in either direction.

## value

PASS

The extremal equality tiling is a canonical substrate. The outgoing contact-edge count measures a different aspect of its metric balls than degree or the population of the distance shells, and is not mechanically given by the local neighbor count or a coloring theorem. Its exact linear profile and the exact quadratic population together give useful benchmarks for propagation on this full contact graph. They make no claim of cut minimality for arbitrary vertex sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
