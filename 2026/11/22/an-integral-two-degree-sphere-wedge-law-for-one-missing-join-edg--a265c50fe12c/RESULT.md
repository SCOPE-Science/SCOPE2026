# An integral two-degree sphere-wedge law for one missing join edge

## Finding
For integers \(m\ge 2\) and \(b\ge 2\), take \(m\) disjoint edges \(a_{2i}a_{2i+1}\) on \(A=\{a_0,\ldots,a_{2m-1}\}\) and an independent set \(B=\{z_0,\ldots,z_{b-1}\}\). Add every edge between \(A\) and \(B\), then remove exactly \(a_0z_0\); denote the resulting simple graph by \(G_{m,b}^{-}\). Let \(\mathcal F(G)\) be the simplicial complex of vertex subsets whose induced subgraph in \(G\) is a forest. There is an **integral homotopy equivalence**, for every indicated pair of integers,
\[
\mathcal F(G_{m,b}^{-})\simeq
\left(\bigvee^{b-1} S^2\right)\vee
\left(\bigvee^{b-1} S^m\right).
\]
For \(m=2\), the two collections occupy the same degree, giving \(\bigvee^{2(b-1)}S^2\). For \(m\ge3\), the only nonzero reduced integral homology groups are free of rank \(b-1\) in degrees \(2\) and \(m\). In particular, there is no integral torsion. The intact join has the known type
\[
\mathcal F((mK_2)*\overline K_b)\simeq
\left(\bigvee^{(2m-1)(b-1)} S^2\right)\vee
\left(\bigvee^b S^m\right),
\]
where \(\overline K_b\) is the edgeless graph. That intact formula is background, not part of the new claim.

## Assumptions and scope
All graphs are finite simple undirected graphs, \(m,b\) are integers in the specified ranges, and all complexes are ordinary **vertex-induced forest** complexes, not graphic-matroid edge-forest complexes, degree-bounded forest complexes, or independence complexes. The wedge symbol means the ordinary based topological wedge after geometric realization; a zero-fold wedge, where relevant, means a point. No statement about natural inclusion maps or equivariant actions is asserted.

## Proof
Write \(a=2m\), \(B'=B\setminus\{z_0\}\), \(c=b-1\), \(I=\operatorname{Ind}(mK_2)\), and \(K=\mathcal F(G_{m,b}^{-})\). The independence complex \(I\) is a join of \(m\) copies of \(S^0\), so \(I\cong S^{m-1}\) is connected. Set \(X=K-z_0\) and \(L=\operatorname{lk}_K(z_0)\). The standard simplicial deletion-star decomposition gives the homotopy pushout \(K=X\cup_L (z_0*L)\), so \(K\) is the homotopy cofiber of \(L\hookrightarrow X\).

**Step 1: the deletion.** The graph obtained by deleting \(z_0\) is the intact join \((mK_2)*\overline K_c\). Within \(X\), define
\[
Q=\Delta(A)\cup\bigcup_{z\in B'}(z*I),\qquad
Z=A_{\mathrm{disc}}*\Delta(B').
\]
Here \(\Delta(S)\) means the full simplex on \(S\), and \(A_{\mathrm{disc}}\) the zero-dimensional complex on \(A\). Every allowed face is either wholly in \(A\), uses one vertex of \(B'\) with an independent subset of \(A\), or uses at least two vertices of \(B'\) with at most one vertex of \(A\). Thus \(X=Q\cup Z\) and \(Q\cap Z=J=A_{\mathrm{disc}}*B'_{\mathrm{disc}}\), the graph \(K_{a,c}\). The simplex \(\Delta(A)\) is contractible; each added cone \(z*I\) meets the existing union exactly in \(I\), whose inclusion is nullhomotopic inside \(\Delta(A)\). The successive homotopy pushouts give
\[Q\simeq\bigvee^c\Sigma I\simeq\bigvee^c S^m.\]
Since \(m\ge2\), \(Q\) is simply connected. Every map from the connected graph \(J\) to \(Q\) is therefore nullhomotopic. Also \(Z\) is contractible. The homotopy pushout yields
\[
X\simeq Q\vee\Sigma J
\simeq\left(\bigvee^c S^m\right)\vee
\left(\bigvee^{(a-1)(c-1)}S^2\right).
\]
More precisely, Mayer–Vietoris supplies a split exact sequence of free abelian groups
\[
0\longrightarrow H_2(Q;\mathbb Z)\longrightarrow H_2(X;\mathbb Z)
\overset{\partial}{\longrightarrow}H_1(J;\mathbb Z)\longrightarrow0.
\]
The surjection is canonical, independent of the choice of wedge splitting. For \(c=1\), \(J\) is a tree, and its first homology vanishes.

**Step 2: the link.** Put \(A''=A\setminus\{a_0,a_1\}\), \(I'=\operatorname{Ind}((m-1)K_2)\), and
\[P=\Delta(\{a_0,a_1\})*I'.\]
The faces of \(L\) using no vertex of \(B'\) are exactly \(P\): the edge \(a_0a_1\) is harmless, but choosing both ends of any other matching edge together with \(z_0\) makes a triangle. The faces using vertices of \(B'\) are those in \(Z\), together with the triangles \(\{a_0,x,z\}\) for \(x\in A''\), \(z\in B'\). Indeed any other two vertices of \(A\) combined with \(z_0,z\) form a four-cycle, while \(\{a_0,a_1,z\}\) forms a triangle. Hence, exactly,
\[
L=P\cup Z\cup\bigcup_{x\in A'',\ z\in B'}\Delta(\{a_0,x,z\}).
\]
Both \(P\) and \(Z\) are contractible, and their intersection is the discrete set of \(a\) vertices \(A\). Therefore \(P\cup Z\simeq\bigvee^{a-1}S^1\). The boundary of each new triangular two-cell \(\{a_0,x,z\}\) represents the same primitive loop indexed by \(x\), independent of \(z\): paths via distinct \(z\) lie in the contractible subcomplex \(Z\). The \(a-2\) loops for \(x\in A''\) are distinct members of the free circle basis based at \(a_0\); the one indexed by \(a_1\) is not killed. Attaching one triangle per \(x\) kills its loop, and the other \(c-1\) triangles for that \(x\) attach along nullhomotopic loops. Thus
\[
L\simeq S^1\vee\bigvee^{(a-2)(c-1)} S^2.
\]
This is an integral homotopy equivalence, not merely a Betti-number count.

**Step 3: the attaching map is primitive.** Fix \(z_1\in B'\). The graph \(J=K_{a,c}\) has a spanning tree consisting of all edges \(a_0z\) for \(z\in B'\) and all edges \(xz_1\) for \(x\ne a_0\). Its integral fundamental-cycle basis comprises the rectangles
\[a_0-z-x-z_1-a_0,\qquad x\in A\setminus\{a_0\},\ z\in B'\setminus\{z_1\}.\]
Choose for each \(x\in A''\) the two-sphere generators of the link from differences between the triangles for \(z\) and \(z_1\). Under \(L\hookrightarrow X=Q\cup_J Z\), the Mayer–Vietoris boundary \(\partial\) sends these generators, up to sign, to exactly the rectangular cycles above with \(x\in A''\). This follows by dividing each sphere cycle into its triangular pieces in \(Q\) and its connecting disks in \(P\subset Q\) and \(Z\), and taking the resulting signed intersection one-cycle in \(J\). Therefore the image is a direct summand of rank \((a-2)(c-1)\) in the free group \(H_1(J;\mathbb Z)\), with an explicitly complementary basis indexed by \(x=a_1\). The induced integral \(H_2(L)\to H_2(X)\) is consequently injective with primitive image. When \(c=1\), this is the empty-basis statement.

**Step 4: the homotopy cofiber.** The complex \(X\) is simply connected. The circle summand of \(L\) therefore attaches nullhomotopically and contributes one new \(S^2\). By the primitive-basis calculation, the map of the \((a-2)(c-1)\) two-sphere summands cancels the same number of the \((a-1)(c-1)\) two-spheres of \(X\). This is valid at the homotopy level: maps from \(S^2\) into a simply connected wedge of spheres of dimensions at least two are classified by integral second homology (Hurewicz), and every unimodular basis change on the two-sphere summands is realized by a homotopy self-equivalence. The \(c\) copies of \(S^m\) survive; for \(m=2\) all sphere generators simply lie in the same dimension and the primitive-basis argument still applies. In total, the cofiber contains \((a-1)(c-1)-(a-2)(c-1)+1=c\) two-spheres and \(c\) copies of \(S^m\). Substituting \(c=b-1\) proves the theorem.

## Verification
The independent Python 3 program `verify.py` enumerates every vertex subset, tests the induced graph for cycles using disjoint-set union, constructs signed-independent mod-two simplicial boundary ranks, and compares the predicted reduced Betti numbers for the intact, damaged, and vertex-link complexes. It covers 11 parameter pairs: \(2\le m\le4\), \(2\le b\le4\), plus \((m,b)=(5,2),(5,3)\). It checks inclusion of intact faces in damaged faces. Run `python3 verify.py` from the extracted directory. The exact output from the executed program is in `check_output.txt`. These finite field-two tests are corroboration; the all-parameter integral homotopy theorem rests on Steps 1–4, especially the primitive rectangular-basis calculation.

## Relationship to prior work
Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first publicly submitted 2023-07-25), Section 4.2.1, gives a homotopy splitting for **intact** graph joins. That result yields the intact baseline above but does not apply after one cross-edge is missing. Barton, Brown, and Pike, *Acyclic polynomials of graphs*, arXiv:2011.01735 (first submitted 2020-11-03), Section 1.3, gives face enumerators for graph joins; a face polynomial does not supply the new integral homotopy type, and the damaged graph is not an intact join. Published edge-deletion results on pure complete bipartite and complete multipartite graphs have different edge patterns: the present graph contains the internal matching triangles and is not a complete multipartite graph for \(m\ge2\). Searches found no published theorem whose conclusion implies the missing-cross-edge formula. These searches are not a uniqueness certificate.

## Limitations
The theorem applies to one removed cross-edge from a join of a nonempty matching with an independent graph. It does not classify arbitrary forests inside \(A\), multiple missing cross-edges, degree-bounded induced-forest complexes, persistent inclusion maps, or automorphism representations. An unindexed equivalent mathematical treatment remains possible. Finite computations alone would not prove the integral or infinite claims.

## References
- Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, https://arxiv.org/html/2307.13271v3 (first submitted 2023-07-25; Section 4.2.1).
- Caroline Barton, Jason I. Brown, David A. Pike, *Acyclic polynomials of graphs*, arXiv:2011.01735, https://arxiv.org/abs/2011.01735 (first submitted 2020-11-03; Section 1.3).
