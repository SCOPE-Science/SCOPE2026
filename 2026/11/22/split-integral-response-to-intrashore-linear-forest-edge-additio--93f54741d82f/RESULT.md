# Split integral response to intrashore linear-forest edge additions

## Finding
Let \(A\) and \(B\) be disjoint labeled sets with \(a=|A|\ge4\) and \(b=|B|\ge2\). For each **linear forest** \(L\) on \(A\) (a disjoint union of paths, with isolated vertices permitted), let \(G_L\) have all edges between \(A\) and \(B\), all edges of \(L\), and no edges inside \(B\). Write \(X_L=\mathcal F_2(G_L)\), where \(\mathcal F_2\) consists of vertex subsets inducing forests of maximum degree at most two.

For **every** inclusion \(L\subseteq L'\) of linear forests on the same vertex set, the reverse graph-complex inclusion \(X_{L'}\hookrightarrow X_L\) is a split integral homology embedding. More strongly, the pair has a relative homotopy wedge splitting:
\[
X_L\simeq X_{L'}\vee\bigvee^{b(|E(L')|-|E(L)|)}S^2,
\]
where the equivalence can be chosen to restrict to the identity on \(X_{L'}\). Equivalently, \(X_L\) is obtained from \(X_{L'}\) by attaching exactly \(b(|E(L')|-|E(L)|)\) two-cells, **all along null-homotopic circles**. Every such inclusion induces a primitive split injection on \(H_2(-;\mathbb Z)\), whose free cokernel has exactly that rank; there is no other nonzero reduced homology.

The stagewise homotopy type, included for orientation but not claimed as independently new, is
\[
X_L\simeq\bigvee^{R(a,b)-b|E(L)|}S^2,\qquad
R(a,b)=(a-1)(b-1)+a\binom{b-1}{2}+b\binom{a-1}{2}.
\]
For example, on \(K_{5,4}\), adding the four edges of a spanning path inside the five-vertex shore removes exactly sixteen independent two-sphere summands, taking the rank from \(51\) to \(35\); every intermediate inclusion is primitive.

There is also a **natural integral equivariant relative module**. If a group \(\Gamma\le S_A\times S_B\) preserves both \(L\) and \(L'\), set \(D=E(L')\setminus E(L)\), and let \(\mathbb Z^{\mathrm{or}}[D]\) be the free abelian group on directed versions of the edges in \(D\), modulo \([v,u]=-[u,v]\). Then the inclusion gives a natural \(\Gamma\)-equivariant exact sequence
\[
0\longrightarrow\widetilde H_2(X_{L'};\mathbb Z)
\longrightarrow\widetilde H_2(X_L;\mathbb Z)
\longrightarrow\mathbb Z[B]\otimes\mathbb Z^{\mathrm{or}}[D]
\longrightarrow0.
\]
The displayed sequence splits as abelian groups, but no equivariant splitting is asserted. Thus the cofiber classes form an oriented-edge permutation lattice tensored with the permutation lattice of the opposite shore.

## Assumptions and scope
All graphs are simple and undirected; all vertex sets are finite and labeled. A linear forest is an acyclic graph of maximum degree at most two, with isolated vertices allowed. The inclusion \(L\subseteq L'\) means literal inclusion of edges on the same \(A\), not a graph minor. The induced-forest complex \(\mathcal F_2(G)\) contains the empty face and consists of all \(S\subseteq V(G)\) for which \(G[S]\) has no cycles and maximum degree at most two. Every topological assertion is about the geometric realization, and all homology coefficients are integral unless explicitly noted. A zero-fold wedge is a point. The group in the equivariant statement is restricted to side-preserving permutations that preserve both internal forests.

## Proof
**1. Exact face description.** For every linear forest \(L\), the full simplices \(\Delta(A)\) and \(\Delta(B)\) are contained in \(X_L\): every vertex-induced subgraph of \(L\) is still a linear forest, and \(B\) is independent. A mixed set with at least two vertices in each shore contains a four-cycle; a mixed set with three vertices from one shore has a vertex of degree at least three on the other shore. Consequently the *only* mixed faces are the \(ab\) cross-edges, the triangles \(\{u,v,w\}\) with \(u\in A\) and \(v,w\in B\) distinct, and the triangles \(\{u,v,w\}\) with \(u,v\in A\) distinct and \(w\in B\) such that \(uv\notin E(L)\). There are no mixed faces of cardinality four or greater. Hence, when \(L\subseteq L'\), the complete list of faces of \(X_L\) absent from \(X_{L'}\) consists of the \(b|D|\) maximal triangles \(\{u,v,w\}\) with \(uv\in D\), \(w\in B\). Their boundaries lie in \(X_{L'}\), and there are no higher cells to add.

**2. Connected-complement lemma.** Let \(Q\) be the complement of \(L'\) on \(A\). It is connected. Otherwise, across two different connected components of \(Q\), every edge belongs to \(L'\). Three or more components would create a triangle in \(L'\). With two components of sizes at least two, the cross-edges create a four-cycle in \(L'\). With one singleton component, its vertex has degree at least \(a-1\ge3\) in \(L'\). Every case contradicts that \(L'\) is a linear forest.

**3. Explicit null-attaching disks.** Fix an added internal edge \(uv\in D\) and a vertex \(w\in B\). Connectivity of \(Q\) supplies a simple path \(u=u_0,u_1,\ldots,u_s=v\) consisting entirely of nonedges of \(L'\). For each consecutive pair, \(\{u_{i-1},u_i,w\}\) is a triangle of \(X_{L'}\). Their fan has boundary consisting of the desired two cross-edges and the \(A\)-path from \(u\) to \(v\). That path, together with the internal edge \(uv\), bounds a disk in the full simplex \(\Delta(A)\subseteq X_{L'}\). Gluing the two disks gives a null-homotopy of the attaching loop \(\partial\{u,v,w\}\) entirely inside \(X_{L'}\). In signed simplicial chains, with ordered triples interpreted as oriented simplices, a filling is
\[
\sum_{i=1}^{s}[u_{i-1},u_i,w]
-\sum_{i=1}^{s-1}[u,u_i,u_{i+1}],
\]
whose boundary is exactly \(\partial[u,v,w]\). Every summand is a face of \(X_{L'}\).

**4. Relative homotopy splitting.** By step 1, \(X_L\) is obtained from \(X_{L'}\) by attaching one two-cell per pair \((w,uv)\in B\times D\); by step 3, each attaching circle is null-homotopic. The elementary CW attaching-map theorem and homotopy-extension property identify the result, relative to the unchanged subcomplex, with a wedge of \(b|D|\) two-spheres. This establishes the pairwise wedge splitting and a split injection on integral second homology with a free cokernel. The quotient \(X_L/X_{L'}\) is literally a wedge of these spheres, with one oriented relative two-cell per missing triangle. Side-preserving automorphisms act on its relative cellular basis by the permutation of \(w\in B\) and the induced sign on the oriented edge \([u,v]\), proving the stated equivariant short exact sequence. The corresponding connecting homomorphism to \(H_1(X_{L'})\) vanishes by the explicit disks. A splitting in the category of abelian groups follows because the quotient is free; it need not be equivariant.

**5. Stagewise homotopy and ranks.** For \(L=\varnothing\), the complex \(Y=X_{\varnothing}\) contains the complete two-skeleton on \(A\sqcup B\), so it is simply connected. Beyond the two full pure simplices \(\Delta(A)\), \(\Delta(B)\), its only cells are cross-edges and mixed triangles; thus the relative cellular chains modulo the two pure simplices vanish above degree two and \(\widetilde H_i(Y;\mathbb Z)=0\) for \(i>2\). Since \(H_2(Y;\mathbb Z)\) is a subgroup of a free simplicial chain group, it is free. The Euler characteristic is \(2-ab+a\binom b2+b\binom a2\), whence \(\widetilde\beta_2(Y)=1-ab+a\binom b2+b\binom a2=R(a,b)\). By Hurewicz and Whitehead, \(Y\simeq\bigvee^{R(a,b)}S^2\). Applying the relative splitting to \(L=\varnothing\subseteq L'\) yields the claimed rank for every linear forest \(L'\), and shows that there is no other reduced homology. All intermediate graph perturbations are covered by step 4, not just initial-to-final comparisons.

## Verification
The standalone `verify_linear_forest_response.py` enumerates vertex-induced subgraphs independently of the face formula. It tests all labeled linear forests on four internal vertices for two opposite-shore sizes, together with longer paths, matchings, and disconnected path forests on five to seven internal vertices. It checks the exact face description, constructs and verifies **signed integral triangular filling chains** for every missing triangle, and computes reduced homology ranks independently over \(\mathbb F_2\) and \(\mathbb F_3\). All 98 tested graph instances passed. The included `verification_output.txt` records the replay. Finite checks are corroboration, not the proof for all sizes or a substitute for the equivariant chain argument.

## Relationship to prior work
Carnero Bravo's *The Forest Filtration of a Graph* (first posted July 25, 2023), particularly Lemma 31 and Theorem 33 in the current PDF, already determines the **individual, nonequivariant homotopy types** of a broad class of joins and of complete bipartite forest stages. Its join formula can be specialized to the stagewise sphere counts above, which are not independently claimed as new. The new assertion is the **relative null-attaching-map theorem across changes in the internal graph**, yielding the actual primitive inclusion maps and natural signed-edge relative homology lattice. Those maps do not follow from a list of the individual homotopy types. Earlier work on devoid complexes provides general splitting techniques, but no inspected statement covering these graph-perturbation maps. A published calculation of equivariant persistence along the *degree* filtration of an intact complete bipartite graph concerns different maps: \(\mathcal F_d(K_{a,b})\to\mathcal F_{d+1}(K_{a,b})\), not the present fixed-degree maps induced by adding edges to one shore.

## Limitations
The internal graph is required to remain a linear forest and the internal shore must have at least four vertices. Connectivity of its complement is essential to the relative disk construction; when it fails, first homology can appear (for example, the three-vertex internal path). The theorem does not classify arbitrary internal graphs or higher degree-bound stages. It makes no claim of canonical equivariant splitting of the integral exact sequence or of a canonical choice of the relative null-homotopies. No independent mathematical audit has been performed, and equivalent unindexed results remain possible.

## References
1. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first posted July 25, 2023, especially Lemma 31 and Theorem 33 (current PDF), https://arxiv.org/abs/2307.13271.
2. Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754, January 27, 2015, especially Sections 2–3, https://arxiv.org/abs/1501.06754.
3. *Symmetry layers and surviving classes in complete-bipartite forest filtrations*, public research record dated October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-symmetry-layers-and-surviving-classes-in-complete-bipartite-fore--153a8787c0e9.
