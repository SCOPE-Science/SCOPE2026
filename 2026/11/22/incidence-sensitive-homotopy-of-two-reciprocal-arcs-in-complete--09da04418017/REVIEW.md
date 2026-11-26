# Independent mathematical audit

## correctness

PASS

Forward arcs alone form the chessboard graph with edge p_j q_k iff j differs from k. A single reverse arc forbids only its reciprocal forward vertex: degrees are compatible with a forward matching and any cycle using only one reverse would be a 2-cycle. With incident reverse arcs at most one can be used; the two cones cover because their excluded forward vertices never co-occur. Their cofibrant intersection gives the unreduced suspension. In the shared-source case its graph is a crown on n-1 vertices per shore. At n=2 or 3 it has two tree components, and for n>=4 every pair on the same shore has a common neighbor. With a shared target, the remaining p_j (j>=3) all see q_1 and q_2; the other q_j see a remaining p_k when n>=4. At n=2 there are two isolated q vertices and at n=3 a tree and an isolated q. The common cycle rank for n>=4 is (n-1)(n-2)-(2n-2)+1, hence the indicated integral suspension type. For disjoint reverse arcs, a face containing p_j for j>=3 lacks both p_1 and p_2, so inserting r_1 cannot complete either its reciprocal cycle or the only possible 4-cycle; the analogous q_j rule gives insertion of r_2. Each extra vertex can be deleted by pairing its faces missing the apex with those containing it, in decreasing face size; every such pair is then a free-face elementary collapse and the apex remains for other deletions. This gives the relative statement for each natural inclusion. The disjoint base has four triangles on p_2,q_1,r_1,r_2 forming a tetrahedral boundary, plus the path r_1,q_2,p_1,r_2 attached only at its endpoints, hence S^1 wedge S^2. The exact all-n argument, not mod-two evidence, determines the homotopy types.

## originality

PASS

The combination of cone intersection and column collapses applies to adding reciprocal arcs without deleting forward arcs. The strongest indexed replacement theorems specialize to S^2 in the disjoint K_{2,n} case, not S^1 wedge S^2, and have no shared-endpoint theorem. Credit their exact coverage of the closely related replacement model and do not infer date precedence.

## value

PASS

This gives a complete integral classification for the first two-arc placements in a basic multipath family. The same number of new arcs yields materially different topology depending on their incidence, and the disjoint case gives explicit elementary collapse stability under the actual inclusions, not just coincident Betti numbers or an Euler-characteristic computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
