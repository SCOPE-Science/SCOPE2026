# Independent mathematical audit

## correctness

PASS

An independent exact check (`python3 /workspace/checks/icosa.py`) builds the icosahedral graph from cyclic signed permutations of (0,1,phi), tests integer-pair squared distances in Z[phi], and computes graph distances by Floyd–Warshall. Applying the strict triangle inequalities to every triple in every subset yields f=(12,66,100,30) and 120 prohibited triples. The admissible triangle patterns are (1,1,1), (1,2,2), (2,2,2), with counts 20,60,20. The distance-two core is connected; its edges have two incident triangles and all links are five-cycles. Its Euler characteristic is 2, so it is a closed combinatorial sphere. Each adjacency edge has two candidate (1,2,2) triangles: choose one per edge. In the union of the core and these selected pairs each such edge is free in its own triangle, since that is its only adjacency edge; collapsing all pairs returns to the sphere. The six distance-three edges occur in no triangles. With them removed the remaining complex contains the simply connected enlarged core with the same one-skeleton, so cells of dimension >=2 cannot introduce fundamental-group generators. Each tetrahedron has two faces occurring in no other tetrahedron; choosing one each gives independent valid collapses and a simply connected two-complex of Euler characteristic 22. Its H2 is free of rank 21; Hurewicz and the simply connected homological Whitehead theorem give a wedge of 21 two-spheres. Reattaching the six bare edges adds one free circle per edge to this connected complex. The finite check establishes the combinatorial data only; the integral homotopy conclusion follows from these topological steps.

## originality

PASS

The distinct supported result is the homotopy type and census of the entire intrinsic icosahedral geodesic general-position complex. The distance-two sphere and six antipodal one-cells already occur in the earlier independence-complex calculation and are not new in themselves. The additional face strata and the analysis needed to reach 21 two-spheres are not obtained from that earlier complex or from the available GP membership or other homotopy results.

## value

PASS

For a natural Platonic graph, the full admissible-configuration topology distinguishes GP from independence and neighboring metric complexes. The exact 21 two-spheres, with six free antipodal one-cells, supply a useful structural benchmark not determined by the GP number or by face counts alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
