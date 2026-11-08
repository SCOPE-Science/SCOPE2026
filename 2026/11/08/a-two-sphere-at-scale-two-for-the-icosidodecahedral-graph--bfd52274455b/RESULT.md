# A two-sphere at scale two for the icosidodecahedral graph

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph, and let \(I=L(D)\) be its line graph, the graph of the icosidodecahedron. Give \(I\) its shortest-path metric and use inclusive graph-metric Vietoris–Rips complexes. Then

\[
\operatorname{VR}_{\le 1}(I)\simeq \bigvee^{11}S^1,
\qquad
\operatorname{VR}_{\le 2}(I)\simeq S^2.
\]

More strongly, the scale-two complex admits **468 elementary simplicial collapses** onto a connected triangulated closed surface with \(16\) vertices, \(42\) edges and \(28\) triangles. That surface is a two-sphere. Thus the inclusion from scale one to scale two kills all eleven independent integral first-homology classes, and one integral second-homology generator appears. In particular, the stage-two complex has no reduced integral homology outside degree two, where it is \(\mathbb Z\).

## Assumptions and scope

The dodecahedral graph has vertices \(0,\ldots,19\), with arithmetic on the indices \(i\in\mathbb Z/10\mathbb Z\). Its \(30\) edges are

\[
\{i,i+1\},\qquad
\{10+i,10+(i+2)\},\qquad
\{i,10+i\},\qquad i\in\mathbb Z/10\mathbb Z,
\]

where all indices on the inner row are reduced modulo ten before adding ten. The graph \(I\) has one vertex for each of these unordered edges, and two of its vertices are adjacent precisely when the corresponding edges of \(D\) meet. This gives \(30\) vertices, \(60\) edges, and graph diameter \(5\).

For \(r=1,2\), a finite subset \(\sigma\subseteq V(I)\) is a simplex of \(\operatorname{VR}_{\le r}(I)\) exactly when every two distinct vertices of \(\sigma\) have shortest-path distance at most \(r\). This is the flag complex of the graph obtained by adjoining pairs at distance at most \(r\). No Euclidean ambient metric or Čech convention is being used.

## Proof

**Scale one.** The graph \(D\) is connected, trivalent and triangle-free. Every triangle of its line graph is therefore the set of three incident edges of \(D\) at one vertex. There are \(20\) such triangles, and each of the \(60\) edges of \(I\) belongs to exactly one triangle. Removing one free edge with each triangle gives \(20\) elementary collapses from the flag complex of \(I\) to a connected graph with \(30\) vertices and \(40\) edges. Its cycle rank is \(40-30+1=11\), proving the first homotopy equivalence.

**Exhaustive scale-two complex.** The complete graph-metric construction in the accompanying dependency-free verifier enumerates the cliques of the square of \(I\). The resulting numbers of simplices in dimensions \(0,1,2,3,4\) are, respectively,

\[
(30,180,380,330,102).
\]

There are exactly \(1022\) nonempty simplices. A machine-readable certificate, `collapse_certificate.json`, specifies \(468\) pairs of simplices, each lower simplex being a codimension-one face of its upper simplex. The verifier starts with the **entire** enumerated face set and, for each pair in order, verifies that the lower simplex has exactly one remaining proper coface, namely the designated upper simplex. It deletes that pair and proceeds. These are genuine elementary simplicial collapses, not merely a homology calculation or an unverified discrete-Morse matching. The certificate is reproducible from a deterministic free-face selection rule given in the verifier.

**Identify the remaining surface.** After the \(468\) pairs, the remaining simplicial complex \(K\) has the face vector

\[
(f_0,f_1,f_2)=(16,42,28).
\]

The verifier checks every remaining edge lies in exactly two triangles; moreover, the link of each of its sixteen vertices is a **single cycle**, not a disjoint union of cycles. It also checks the one-skeleton is connected. Hence \(|K|\) is a connected closed triangulated surface. Its Euler characteristic is \(16-42+28=2\). By the classification of closed connected surfaces, \(|K|\) is homeomorphic to \(S^2\). Elementary collapses preserve homotopy type, proving the second equivalence over the integers.

**Inclusion and integral consequences.** Both complexes are connected. The first has the homotopy type of eleven circles and hence has \(H_1\cong\mathbb Z^{11}\) and \(H_2=0\); the second has the homotopy type of a sphere and hence has \(H_1=0\) and \(H_2\cong\mathbb Z\). Therefore the inclusion induces the zero homomorphism on first homology, whose kernel is all of \(\mathbb Z^{11}\), and the nonzero second-homology class is newly present at scale two. These statements concern the two indicated scales only.

## Verification

Run `python3 verify_icosidodecahedron.py collapse_certificate.json` in the directory containing both embedded files, using only the Python standard library. The program reconstructs the explicitly indexed dodecahedral graph; builds the line graph and exact shortest-path distances; enumerates **all** scale-one and scale-two cliques; verifies the 468 recorded free-face collapses against the entire current complex; independently regenerates the deterministic collapse sequence; and checks all edge incidences, all vertex links, connectivity, and Euler characteristic of the target triangulated surface. The accompanying `verification_output.txt` records the successful replay, with sentinel `ICOSIDODECAHEDRAL_RIPS2_SPHERE_OK`.

The finite certificate is exhaustive **for this specified graph and these two scales**. The surface-classification step is standard topology; neither a larger-graph extrapolation nor an unproved recognition heuristic is required.

## Relationship to prior work

Adams, Adetowubo, Barriga-Acosta, Feng and Sterling [1] study graph-metric Rips complexes on periodic torus grids. Their February 2025 investigation motivates examining exact homotopy transitions on other symmetric finite graph metrics; their stated classifications are for torus grids, not line graphs of polyhedral graphs.

Saleh, Titz Mite and Witzel [2] classify Rips complexes of the five **Platonic** solid vertex graphs, including the dodecahedral graph. The icosidodecahedral graph here is the **line graph** of the dodecahedron and has 30 rather than 20 vertices. The theorem in [2] does not contain a conclusion about this 30-vertex graph.

Goyal, Shukla and Singh [3] compute clique-complex homotopy types for line graphs, including the scale-one flag complex treated above. Their ordinary line-graph clique construction is not the scale-two flag complex of the square of that line graph.

The published line-graph Čech collapse result [4] gives the **intrinsic Čech** scale-two complex of the line graph of a sufficiently high-girth graph as homotopy equivalent to the base graph. This has a different simplex membership rule from the **Vietoris–Rips** scale-two complex here. For the dodecahedral base graph, [4] gives a wedge of eleven circles at its Čech stage, contrasting with the two-sphere at the present Rips stage. Related results for the rhombicuboctahedron concern a different polyhedral graph and do not imply this concrete collapse.

## Limitations

This is a complete **finite-graph** result for the named 30-vertex graph at inclusive graph-metric scales one and two. It is not a classification of all Archimedean polyhedra, line graphs of cubic graphs, or higher scales. It does not determine an automorphism representation or a full persistence barcode. The collapse certificate proves the stated simplicial homotopy equivalence and integral homology, not an assertion that the original scale-two complex is itself a two-dimensional manifold. An undiscovered equivalent classification under different terminology remains a literature-overlap risk.

## References

[1] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, *Vietoris-Rips complexes of torus grids*, arXiv:2502.07134, version 1 publicly posted 2025-02-10. https://arxiv.org/abs/2502.07134

[2] N. Saleh, T. Titz Mite and S. Witzel, *Vietoris-Rips complexes of Platonic solids*, arXiv:2302.14388 (2023). https://arxiv.org/abs/2302.14388

[3] S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (2020). https://arxiv.org/abs/2009.12130

[4] *A scale-two Čech collapse theorem for line graphs of girth at least five*, public mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-scale-two-ech-collapse-theorem-for-line-graphs-of-girth-at-lea--69ae03a7604c
