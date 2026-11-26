# Independent mathematical audit

## correctness

PASS

The open-neighborhood simplex at e=uv is on the two disjoint truncated stars A_e and B_e. The unmixed faces are exactly the union of the star boundaries. For a mixed pair uw,vz, the endpoints are distinct by triangle-freeness; the only possible alternative connectors to uv are uz, vw or wz, which would give a triangle or quadrilateral. Thus all cofaces of a mixed pair stay in one block. In each block, first match every mixed face containing an A_e vertex other than a_e by toggling a_e, then match the remaining mixed faces with some B_e vertex other than b_e by toggling b_e. In either stage, a coface other than the chosen upper partner belongs to a pair with a larger lower face, so reverse-size order gives actual elementary collapses with no external cofaces. The only retained mixed face is the chosen cross edge. The target is a connected union of boundary spheres glued at point intersections according to H, with no triple intersection and one added interval per edge. One may insert a connecting interval for each point identification (contracting that interval recovers the identification), move attachment points within each connected sphere by homotopy of the attaching maps, then contract an incidence spanning tree. This yields m−n+1 incidence loops and the separate sphere summands; the added intervals contribute m more loops. The degree-three spheres supply n_3 further circles. For the order-three plane incidence graph (26 vertices, 52 edges, degree four) the counts are 79 circles and 26 two-spheres. Integral homotopy and torsion-freeness are proved by this reduction, not by mod-two numerics. Replay: RESULT.md lines 24–52; verify.py and verification_output.txt inspected, not executed. The examples do not certify graphs with triangles, squares, or smaller degrees.

## originality

FAIL

A distinct same-day indexed finding states the identically scoped wedge theorem, including the projective-plane case, and already gives the same block decomposition and relative intersection facts. The explicit elementary collapse is a genuine strengthening of the type of equivalence, not asserted in the matched passage, but it follows by a routine vertex-toggle collapse on exactly the two-block simplex already isolated by that finding. Relative priority within the day is not resolved or presumed.

## value

FAIL

The exact wedge classification is a worthwhile invariant, but it is already covered for the identical domain. The narrower relative-collapse list is constructive, yet after the known two-block intersections it is just the generic matching that toggles a vertex on each side; no further application, obstruction, or nonroutine invariant of the prescribed target is established here. This does not support salvaging the frozen classification by presenting that routine refinement as a distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
