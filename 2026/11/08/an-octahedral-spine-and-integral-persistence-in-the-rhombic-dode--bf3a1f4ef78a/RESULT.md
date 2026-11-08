# An octahedral spine and integral persistence in the rhombic-dodecahedral graph Čech nerve

## Finding
Let \(R\) be the graph of the rhombic dodecahedron, realized by the incidence graph between the eight vertices and six square faces of a cube. Give each edge length one and let \(\mathcal N(R,r)\) be the nerve of closed radius-\(r/2\) balls centered at the graph's fourteen vertices in its full intrinsic unit-edge metric realization.

Write \(O\) for the subcomplex on the six degree-four vertices of \(R\) whose eight facets choose exactly one vertex from each of the three naturally opposite pairs of cube faces. Then \(O\) is the simplicial boundary of an octahedron, and **there is a sequence of 626 elementary simplicial collapses, fixing \(O\),**
\[
\mathcal N(R,3)\searrow O\cong S^2.
\]
At the preceding scale, \(\mathcal N(R,2)\simeq\bigvee^{13}S^2\). Because \(O\subseteq\mathcal N(R,2)\subseteq\mathcal N(R,3)\), the integral inclusion homomorphism is a split surjection:
\[
0\longrightarrow\mathbb Z^{12}\longrightarrow
\widetilde H_2(\mathcal N(R,2);\mathbb Z)
\longrightarrow\widetilde H_2(\mathcal N(R,3);\mathbb Z)
\longrightarrow0,
\qquad
\widetilde H_2(\mathcal N(R,3);\mathbb Z)\cong\mathbb Z.
\]
The surviving generator is the fundamental class of the canonical octahedral subcomplex. The full graph automorphism group has order \(48\), and its action on the surviving integral homology class is the orientation character of signed permutations of three coordinates:
\[g\cdot z=\det(g)z.\]
All statements at integer scales \(2\) and \(3\) remain valid throughout the respective real intervals \(2\le r<3\) and \(3\le r<4\).

## Assumptions and scope
Label the cube's corners by integers \(i=0,\dots,7\), with bit \(b_j(i)=(i\mathbin{\mathrm{div}}2^j)\bmod2\) for \(j=0,1,2\). Label the six face centers by \(8+2j+s\), where \(s=0,1\). The edges of \(R\) are exactly
\[\{i,8+2j+b_j(i)\},\quad 0\le i<8,\quad 0\le j<3.\]
This is a connected bipartite graph with eight degree-three vertices, six degree-four vertices, 24 edges and diameter four. Distances are measured along the **metric graph**, not in Euclidean three-space, and balls are closed. All homotopy and homology assertions are integral and nonequivariant unless an ordinary homology group action is expressly mentioned. The collapse sequence is not asserted to be equivariant.

For a finite graph \(G\), let \(N_G[v]\) denote the closed radius-one vertex neighborhood. For any edge \(ab\) of \(G\), put \(F_{ab}=N_G[a]\cup N_G[b]\). The exact graph Čech formula of Adams--Shukla--Singh, Lemma 2.2, identifies the facets at scale three with maximal sets among \(F_{ab}\). At scale two the generating sets are the \(N_G[v]\).

## Proof
**1. The generating simplices and the octahedral sphere.** Construct all edges from the displayed incidence rule. At scale two there are fourteen generating closed neighborhoods. At scale three the 24 sets \(F_{ab}\) are distinct and maximal. Enumerating all their subsets gives exactly 211 simplicial faces at scale two and 1,279 at scale three, both counts including the empty face. The nonempty face vectors, ordered from dimension zero, are
\[
\begin{aligned}
f(\mathcal N(R,2))&=(14,60,92,38,6),\\
f(\mathcal N(R,3))&=(14,84,260,410,342,144,24).
\end{aligned}
\]
For every choice of signs \((s_0,s_1,s_2)\in\{0,1\}^3\), the three face centers \(8+2j+s_j\) are all adjacent in \(R\) to the cube corner with these bits, so their triple is a simplex already at scale two. The eight such triples and their subsets form \(O\), the boundary of the octahedron whose antipodal pairs are the two centers of the opposite cube faces. Hence \(O\subseteq\mathcal N(R,2)\subseteq\mathcal N(R,3)\).

**2. The exact collapse at scale three.** Encode any simplex by the fourteen-bit integer whose selected vertices have bit value one. The independent certificate `collapse_pairs.tsv` contains 626 pairs of nonempty face masks \((\sigma,\tau)\). For each pair in its listed order, \(\sigma\) is outside \(O\), \(\tau\) is obtained by adjoining one vertex, and \(\tau\) is the **unique remaining immediate coface** of \(\sigma\). A face with a unique immediate coface has no larger proper coface, so \(\sigma\) is a free face of the facet \(\tau\); removing the pair is an elementary simplicial collapse. The accompanying verifier reconstructs every face and checks all 626 free-face tests and, at the end, equality of the remaining face set with the 27 faces of \(O\), including the empty face. Because \(1,279-27=2(626)\), the displayed sequence accounts for every face outside the octahedral sphere. Thus the **actual inclusion** \(O\hookrightarrow\mathcal N(R,3)\) is a simple-homotopy equivalence.

**3. Scale two.** A separate exact discrete-Morse matching on the 210 nonempty faces of \(\mathcal N(R,2)\) sweeps the fourteen vertices in increasing order and matches any still-unmatched face lacking the current vertex to its coface obtained by adding it. The verifier checks the complete directed Hasse graph (578 covering incidences), proving acyclicity, and records 98 matched pairs. The only unmatched faces are one vertex and thirteen triangles. A second matching with the reverse vertex order has exactly the same critical-cell counts and passes the same acyclicity test. Forman's discrete-Morse theorem yields a CW model with one zero-cell and thirteen two-cells and no one-cells; all two-cell attaching maps are constant. Therefore \(\mathcal N(R,2)\simeq\bigvee^{13}S^2\). Independent mod-two simplicial boundary ranks in degrees one through four are \((13,47,32,6)\), consistent with the integral classification.

**4. Integral persistence.** The composite inclusion \(O\hookrightarrow\mathcal N(R,2)\hookrightarrow\mathcal N(R,3)\) induces an isomorphism in degree-two integral homology by Step 2. Hence the second inclusion induces a surjection onto \(\mathbb Z\) and the first embeds a primitive rank-one summand of \(\mathbb Z^{13}\). The short exact sequence splits since its quotient is free, and its kernel is free of rank twelve. This is stronger than merely knowing the two Betti numbers: exactly one integral class from scale two survives through scale three, represented by the octahedral fundamental cycle.

**5. Symmetry.** Any graph automorphism preserves the degree-four face-center vertices. Two of these centers have disjoint sets of cube-corner neighbors precisely when they correspond to opposite faces; hence an automorphism permutes three opposite pairs, possibly swapping each pair. Each cube corner is uniquely specified by its three incident face centers. Thus the automorphism group has order at most \(2^3\,3!=48\), and all 48 signed coordinate permutations act, so the bound is exact. Their action on \(O\) is the standard octahedral action on the vertices \(\{\pm e_1,\pm e_2,\pm e_3\}\), which acts on the oriented fundamental two-cycle by the determinant. Since the inclusion \(O\hookrightarrow\mathcal N(R,3)\) is equivariant and an ordinary homology isomorphism, the same orientation character describes the integral second-homology action of the full graph automorphism group. The verifier checks all 48 actions on both graph edges and the signed octahedral fundamental cycle.

## Verification
Run `python3 verify_rhombic_cech.py collapse_pairs.tsv` in the directory containing these two files. No dependencies beyond Python 3's standard library are required. The script independently reconstructs graph distances by breadth-first search, generating facets at both scales from the metric rule, every simplicial face, and the octahedral target. It verifies the complete explicit elementary-collapse certificate, recomputes two independent acyclic Morse matchings at scale two, checks all Hasse incidences by directed topological sorting, independently calculates mod-two boundary ranks, and checks the action of all 48 signed coordinate permutations and their determinant signs. An actual successful execution is supplied in `verification.log`, ending in `VERIFICATION_OK`.

The finite certificates are **exhaustive for this specified fourteen-vertex graph**, not experiments on a subset of faces. A simple-homotopy equivalence is established by the explicitly verified elementary collapses; the scale-two integral homotopy classification follows from a complete acyclic matching, not from field-homology calculations alone. The group action on homology is not a claim that the chosen collapse sequence is equivariant.

## Relationship to prior work
Adams--Shukla--Singh [1] define this finite vertex-centered intrinsic graph Čech nerve and prove the even/odd generating-face rule, but their homotopy classifications study hypercube graphs, whose vertices all have the same degree. The rhombic-dodecahedral graph is a **biregular fourteen-vertex cube incidence graph**, not a hypercube graph. Previte's 2014 work [2] treats the equivalent even-scale distance-neighborhood construction for several named graphs, including Platonic graph skeleta, but neither this incidence graph nor its scale-three odd-radius nerve or inclusion-to-an-octahedron collapse appears in the inspected example table and relevant chapters. Matsushita [3] relates even-scale closed-neighborhood complexes to independence complexes and graph fundamental groups, without computing this graph-specific collapse or its degree-two persistence.

Nearby published classifications concern the **cuboctahedral graph** \(L(Q_3)\), a different twelve-vertex graph [4], or vertex-truncation graphs \(L(S(H))\) [5]. The latter have triangles at every vertex of \(H\) of degree at least three; when all degrees are at most two, the resulting line graph has maximum degree at most two. Thus the triangle-free, degree-four rhombic-dodecahedral graph is **not** in that family. Other matching-complex results for the same named rhombic-dodecahedral graph concern a different simplicial complex. Searches covered its aliases Fruchard graph, cube vertex-face incidence/radial graph, and rhombic-dodecahedral graph, as well as odd-scale Čech nerves and closed-neighborhood complexes. None of the checked statements implies this precise octahedral collapse or its integral persistence map. Search absence is not a proof that no differently indexed statement exists.

## Limitations
The claim concerns one natural finite graph and exactly the two consecutive scales \(2\) and \(3\), not all radial graphs of polyhedra, arbitrary scales, or a persistent homology classification in every dimension. The full automorphism action is established on the surviving **integral homology**, not by an equivariant collapse or equivariant homotopy equivalence. The scale-two kernel is classified as an abelian group, not as an integral representation of the symmetry group. An equivalent result under an unindexed alternate name remains a bibliographic risk, and no independent external audit has been performed.

## References
1. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first posted 2022-12-12; in particular §2, Lemma 2.2 and §4–5. https://arxiv.org/abs/2212.05871
2. C. Previte, *The D-neighborhood complex of a graph*, Colorado State University PhD dissertation, 2014, especially Chapter 3 and Table 3.1. https://mountainscholar.org/items/027fa02f-8d43-43a0-972f-b8af65fc4a95
3. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first posted 2025-11-16, especially Theorems 1.2, 1.4 and 1.5. https://arxiv.org/abs/2511.12608
4. *Complete intrinsic Čech persistence of the cuboctahedral graph*, published research record `2026/10/11/SCOPE-complete-intrinsic-ech-persistence-of-the-cuboctahedral-graph--d51acb79fc64`, full scientific result inspected.
5. *Scale-three Čech persistence survives vertex truncation of triangle-free graphs*, published research record `2026/10/11/SCOPE-scale-three-ech-persistence-survives-vertex-truncation-of-triang--050621e1a6fe`, full scientific result inspected.
6. Rhombic Dodecahedral Graph, *Wolfram MathWorld*, graph names and basic combinatorial parameters. https://mathworld.wolfram.com/RhombicDodecahedralGraph.html
