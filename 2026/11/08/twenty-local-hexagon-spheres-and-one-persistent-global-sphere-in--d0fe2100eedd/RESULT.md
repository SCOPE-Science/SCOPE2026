# Twenty local hexagon spheres and one persistent global sphere in the truncated-icosahedral Rips filtration

## Finding

Let \(G\) be the truncated-icosahedral graph (the 60-vertex buckyball graph), with shortest-path distance \(d_G\). For \(r\geq0\), let \(K_r=\operatorname{VR}_{\leq r}(V(G),d_G)\), the clique complex of the graph joining pairs at distance at most \(r\). Then

\[
K_2\simeq\bigvee^{21}S^2,\qquad K_3\simeq S^2.
\]

The inclusion \(K_2\hookrightarrow K_3\) induces a split surjection on integral second homology, with kernel \(\mathbb Z^{20}\). More precisely, the 20 oriented octahedral two-cycles contributed by the six-vertex hexagonal faces of the buckyball, together with an explicitly triangulated global polyhedral two-sphere, form an **integral basis** of \(H_2(K_2;\mathbb Z)\). The local 20 cycles die in \(H_2(K_3;\mathbb Z)\), while the global cycle maps to a primitive generator of \(H_2(K_3;\mathbb Z)\). Thus exactly 20 degree-two intervals die between inclusive graph-distance thresholds 2 and 3, and one class survives through scale 3. No claims are made about later thresholds.

## Assumptions and scope

The metric is intrinsic graph distance, **not** Euclidean distance between the polyhedron's embedded vertices. Distances and thresholds are integer-valued and inclusive. The graph is canonically constructed by truncating the icosahedral graph: its 60 vertices are the ordered ends \((u,v)\) of the 30 original edges. Reversing each original edge gives 30 new edges, and consecutive original neighbors at each original vertex give 60 additional edges. A five-neighbor cyclic rotation table, uniquely specifying the construction, is included in `verify_buckyball_rips.py`. It produces a connected cubic graph with 60 vertices, 90 edges, 12 pentagonal and 20 hexagonal faces, and graph diameter 9.

All homotopy equivalences and homology groups below are integral and nonequivariant. No homotopy equivalence is asserted to be compatible with graph automorphisms or filtration inclusions. The only inclusion statement is the specified integral degree-two homology map.

## Proof

**Exact enumeration and collapses.** All nonempty cliques of the distance-power graphs are enumerated by a deterministic increasing-vertex recursion (not by sampling). At threshold 2 there are 802 nonempty faces, with an exhaustive sequence of 145 elementary free-face collapses reducing to a connected two-dimensional simplicial complex with 60 vertices, 245 edges, and 207 triangles. At threshold 3 there are 6,462 nonempty faces; 3,120 elementary collapses leave 60 vertices, 110 edges, and 52 triangles. Every collapse removes a codimension-one face of a unique maximal coface. These are actual simplicial deformation retractions, with the full sequence recomputed and locally checked by the attached verifier.

**Simply connected cores.** Contract a spanning tree in each surviving one-skeleton and use the remaining edges as free-group generators, with the triangle boundaries as relators. The threshold-two core has 186 such generators and the threshold-three core has 51. Repeatedly deleting generators forced trivial by length-one relators, and substituting their trivial values in all other relators, eliminates all 186 and all 51 generators respectively; no residual relator remains. These are legitimate elementary Tietze simplifications, so both cores are simply connected. Their Euler characteristics are 22 and 2; consequently, their second integral homology groups are \(\mathbb Z^{21}\) and \(\mathbb Z\), with no other reduced homology. Because a simply connected finite two-dimensional CW complex is homotopy equivalent to a wedge of second-homology-rank many two-spheres (Hurewicz and the homology form of Whitehead's theorem), the claimed complete integral homotopy types follow.

**Geometric cycles.** Each oriented pentagon is triangulated into three triangles and each oriented hexagon into four triangles along graph-distance-two diagonals. The result is a 116-triangle integral two-cycle \(z\) of the polyhedral sphere, all coefficients \(\pm1\). For each of the 20 hexagons, its distance-two clique complex on the six facial vertices is the octahedral boundary: the antipodal pairs are the three pairs of vertices opposite in that six-cycle. The signed join of these three oriented zero-spheres is an explicit eight-triangle cycle \(h_i\). All 21 chains lie in \(K_2\).

An elementary collapse \((\sigma,\tau)\), where \(\dim\sigma=2\) and \(\dim\tau=3\), transports each two-cycle by subtracting the unique integer multiple of the oriented boundary of \(\tau\) that removes its coefficient on \(\sigma\). Applying those exact chain changes along the listed collapse sequences sends every cycle to the corresponding two-dimensional core. In the threshold-two core, the resulting 207-by-21 coordinate matrix of the 20 local cycles followed by \(z\) has a 21-by-21 minor of determinant \(\pm1\): each local cycle has an exclusive triangle coordinate with coefficient \(\pm1\), absent from the other 20 cycles, and \(z\) has another triangle coordinate with coefficient \(\pm1\). The program constructs and verifies this block-triangular unit minor directly, with integer arithmetic. Hence these 21 cycles span a primitive rank-21 sublattice of the 207-dimensional group of two-chains. Since their span is contained in the rank-21 homology lattice (no three-cells remain), and both are primitive sublattices of the same rank, they coincide: the cycles are an integral basis, not merely rationally independent.

Each local hexagonal cycle \(h_i\) bounds in \(K_3\), since the six vertices of its face have pairwise graph distance at most 3 and hence span a five-simplex. The transferred global cycle \(z\) has exactly 52 nonzero coefficients, each \(\pm1\), in the threshold-three two-dimensional core. That core has \(H_2\cong\mathbb Z\), with no three-chains, so any cycle with a unit coordinate is a primitive generator. Thus the image of \([z]\) generates \(H_2(K_3;\mathbb Z)\). The 20 local cycles are an integral basis for the kernel and the inclusion is split surjective, as asserted.

## Verification

Run `python3 verify_buckyball_rips.py` using Python 3.10 or later; only the standard library is required. The deterministic program constructs the graph from the explicit rotation table, computes all 60-by-60 shortest-path distances, enumerates all cliques at thresholds 2 and 3, verifies free-face collapses, checks fundamental-group presentation eliminations, constructs all geometric cycles, transports their integral chains through the collapses, and checks the required unit determinant minor and primitive image. Its recorded output is in `verification_output.txt`; the success marker is `ALL_CHECKS_PASS`. The verifier uses exact integer operations throughout.

A separate exploration using a planar embedding and independent finite boundary ranks found the same 802 and 6,462 face counts and reduced mod-two Betti numbers \(21\) and \(1\) in degree two. The finite calculations in the standalone checker are exhaustive for these exact graph sizes; they are not extrapolated to an infinite family.

## Relationship to prior work

Adamaszek and Adams, *The Vietoris–Rips complexes of a circle* (arXiv:1503.03669, first publicly submitted March 12, 2015), treats geometric circle metrics and cyclic graphs, not the shortest-path metric on a 60-vertex fullerene graph. It provides the historical motivation for studying homotopy changes and persistence across thresholds, but does not imply the stated polyhedral calculation.

Saleh, Titz Mite, and Witzel, *Vietoris–Rips complexes of Platonic solids* (arXiv:2302.14388, first publicly submitted February 28, 2023), considers the five Platonic solids. Its theorem excludes Archimedean truncated icosahedra; its introduction explicitly mentions Archimedean solids as a possible generalization. Its graph-distance/Euclidean-distance distinction is also respected here.

Nearby published computations for the truncated octahedron, truncated cube, and rhombicuboctahedron use different graphs and do not determine these 60-vertex homotopy groups or the hexagon-versus-global degree-two persistence map. Exact-name and equivalent-wording searches disclosed no covering work, but failed searches cannot establish priority; unindexed treatments of fullerenes or graph-power clique complexes remain possible.

## Limitations

Only scales 2 and 3 and their degree-two integral inclusion map are classified. The homotopy type of the complexes at other radii, complete persistence in other degrees, equivariant homotopy types, and homology of symmetry quotients are not established. The proof depends on reproducible exhaustive finite certificates; independent mathematical validation and definitive publication-priority checking have not been performed. The graph metric must not be replaced by Euclidean chord distance.

## References

1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (initial posting 2015-03-12), https://arxiv.org/abs/1503.03669 ; full-text https://arxiv.org/html/1503.03669v2 .
2. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (initial posting 2023-02-28), https://arxiv.org/abs/2302.14388 .
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (background on finite simplicial collapse and discrete Morse theory).
4. A. Hatcher, *Algebraic Topology* (2002), Chapters 1–4 (van Kampen, Hurewicz, and Whitehead theorems).
