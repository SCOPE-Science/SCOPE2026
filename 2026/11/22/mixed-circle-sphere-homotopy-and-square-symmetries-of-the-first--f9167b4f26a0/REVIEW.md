# Independent mathematical audit

## correctness

PASS

Coordinatewise betweenness in the Manhattan grid is equivalent to shortest-path betweenness. The independent subset generator gives 9 vertices, 36 edges, 16 triangles and just the tetrahedron (1,3,5,7); its next face level is empty. There is a direct independent topological check: collapse the tetrahedron with its free triangle (3,5,7), then collapse the free edge (3,5) with (1,3,5). The union of the remaining triangles has 9 vertices, 21 edges and 14 triangles. It is connected, each edge is in two triangles, and each vertex link is a connected cycle. Thus it is a closed connected triangulated surface of Euler characteristic 2, hence S². The fourteen remaining edges attach only at points of that sphere; homotope their attaching maps to a common point to obtain fourteen free circles. This also independently establishes the homotopy conclusion of the frozen CW elimination. Orienting the collapsed sphere by propagation across its edges produces an integral generator, which is also a cycle of the original complex. Applying the signed permutations of its triangles, the difference from its determinant-signed copy is an integral multiple of the tetrahedral boundary for all eight symmetries. The signed fixed-face alternating traces are −12 at the identity, 2 at either quarter turn, 4 at the half turn, −2 at either axial reflection, and 0 at either diagonal reflection. Alternating homology traces then give the listed H_1 character. As an independent quotient check, face-chains in the barycentric subdivision have 16,32,18,3 simplex orbits by dimension, with boundary ranks 15,15,3 over Q. Every stabilizer fixes its chain pointwise, so the orbit chain complex computes the quotient, giving ordinary Betti numbers (1,2,0,0). This confirms the rational quotient only.

## originality

PASS

The face vector and maximal face size are prior coverage. The supported distinct claim is the homotopy type, the integral action on H_2 and rational H_1 character, and the resulting rational quotient homology. The inspected older work and distinct same-day records do not give that claim for this grid.

## value

PASS

This grid is the smallest square path grid with a four-point general-position set. Its exact topology is a natural base case for comparing geodesic-set complexes of larger rectangles, and the dihedral action supplies orbit-space data not recoverable from known face counts or ordinary Betti ranks. The independent surface reduction makes the primitive sphere and its orientation character directly usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
