# Independent mathematical audit

## correctness

PASS

For n>=9 the signed shifts from -4 to 4 are distinct modulo n; the positive shift intersections of Q_0 with Q_d have sizes 2,1,2,1 for d=1,2,3,4, and larger cyclic shifts give zero. Thus triangles have unique supporting neighborhoods. Difference-two edges {i-1,i+1} are supported only in their own Q_i; after its U_i collapse their only coface is V_i. The surviving A_i,B_i form a connected closed orientable triangulated surface: the edges of differences 1,3,4 have degree two, the six-cycle links have distinct vertices, and the listed orientations cancel on each edge. Its Euler characteristic is zero, giving the intact torus. A length-one fault reduces Q_0,Q_1 to A_0,B_1; the same collapses elsewhere remove exactly the open faces B_0,A_1 from the torus, with disjoint vertex sets and all boundary edges retained. A length-two fault reduces Q_0,Q_2 to U_0,V_2, which collapse on their own difference-two edges. The residual complex lacks the two pairs A_0,B_0 and A_2,B_2 and just their two internal diagonals; it is connected via difference-one edges and has Euler characteristic -2. Its two missing disks touch at one boundary vertex, so the manifold-with-boundary argument for length one should not be used verbatim. Instead, closed-surface dual connectivity gives each remaining triangle component an edge to a deleted triangle. That edge survived since it has a remaining coface. Peeling a rooted spanning tree outward uses a parent edge still present and free at each step, leaving a connected graph of rank three. Rotations and reflections cover all edges.

## originality

PASS

The intact homotopy torus is already known. The supported contribution is the all-order edge-fault wedge classification for both edge orbits, with different puncture geometry but the same homotopy type. No inspected matching theorem handles these nonregular open neighborhood complexes after an edge fault.

## value

PASS

This is a complete, uniform stability test of a familiar intact torus model under the simplest graph fault. Neither graph edge orbit preserves the fundamental class, and both create an extra independent loop. Contrasting separate holes with disks touching at a vertex yields a concrete reason not to predict the new topology from the intact type or from a manifold heuristic alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
