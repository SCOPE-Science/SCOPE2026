# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md Steps 1–5 over the integers. Degree constraints permit at most one incoming and one outgoing hub arc and a matching of at most two middle arcs. Any cycle uses the hub and is exactly a directed triangle, so the missing middle vertex in each cone base is exactly v_ij. The crown graph and each single-vertex deletion are connected (left-side pairs have a common neighbor, and every opposite vertex still has a neighbor). An induced cycle has at most three vertices per shore, since each left vertex has only one available nonneighbor; any induced hexagon uses three common labels and is tiled by three squares meeting at an extra left vertex off those labels. Chord splitting and these disks yield integral cycle generation and normal generation by squares. In each L_i every square is coned over an unused label on shore i, killing π₁. K₀ is the union of cones on a connected graph; attaching both u_i cones along connected bases keeps X simply connected. For H₂(K₀;ℤ), the boundary of the w_j-cone over z_j gives the separate ∂z_j constraints and the common sum constraint Σz_j=0. There are no 3-boundaries in either base. Generating by (e_j−e_k) times a square and routing a mixed-shore pair via an unused fifth label gives integral surjectivity from the sum of the two bases. Relative homology then gives H₂(X;ℤ)=0. Direct face counting gives reduced Euler characteristic −n³+6n²−8n+1; top homology is free as a subgroup of the dimension-three chains. Hurewicz in degrees two and three and the simply connected homological Whitehead theorem give the wedge. The recorded checker output was inspected without executing the uploaded code. Independent replay `python3 /workspace/branches/30dab567-ed4f-416a-a806-e53af33d78d6/independent_n4_boundary.py` checks all 2^14 arc subsets for n=4: f=(14,68,128,72), mod-two boundary ranks (13,55,71), and ordinary Betti vector (1,0,2,1). This proves the stated mod-two obstruction, not a smaller-n homotopy classification.

## originality

PASS

The inspected multipath literature studies the same functor, and the catalogue contains close cyclic tripartite and bipartite wedge results. None of these statements covers the integral homotopy type for cyclic shores (1,2,n), its rank formula, or the n=4 boundary. The exact blow-up comparison uses path homology instead and is not equivalent. This is a best-of-knowledge comparison, not a priority claim.

## value

PASS

This gives the integral homotopy type for a natural strongly cyclic infinite family under an established functor, and settles when the sphere-only pattern begins, rather than furnishing just ranks at several n. The fifth-label argument explains why the two independent cone attachments jointly kill the entire integral second homology and identifies a meaningful threshold. The mod-two boundary is a substantive contrast, not claimed to be a classification in its own right.

The dated certificate retains the supplied scientific assessment, sources and limitations.
