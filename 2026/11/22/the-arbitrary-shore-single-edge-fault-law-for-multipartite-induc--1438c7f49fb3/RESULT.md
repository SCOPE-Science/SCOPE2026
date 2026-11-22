# The arbitrary-shore single-edge fault law for multipartite induced-forest complexes

## Finding
Let \(r\ge3\), with finite, nonempty independent vertex shores \(A_1,\ldots,A_r\) of sizes \(n_1,\ldots,n_r\ge1\). Let \(G=K_{n_1,\ldots,n_r}\), choose \(x\in A_1\), \(y\in A_2\), and set \(G'=G-xy\). For a graph \(H\), let \(\mathcal F(H)\) be the simplicial complex of subsets of \(V(H)\) inducing an acyclic subgraph. Define
\[
U=\sum_{1\le i<j\le r}(n_i-1)(n_j-1),\qquad p=(n_1-1)(n_2-1),\qquad s=\sum_{k=3}^r(n_k-1).
\]
Then the **complete integral homotopy type** is
\[
\boxed{\mathcal F(G')\simeq\bigvee^{\binom{r-2}{2}}S^1\vee\bigvee^{U-p+s}S^2.}
\]
The convention is that a wedge of zero spheres contributes a point. The previously established intact case is
\[
\mathcal F(G)\simeq\bigvee^{\binom{r-1}{2}}S^1\vee\bigvee^U S^2.
\]
The inclusion \(j:\mathcal F(G)\hookrightarrow\mathcal F(G')\) induces a **split-surjective integral map** on first homology with primitive kernel \(\mathbb Z^{r-2}\); on second homology it has primitive kernel \(\mathbb Z^p\) and free cokernel \(\mathbb Z^s\). All other positive-degree integral homology vanishes, and neither space has integral torsion. No uniformity assumption on the shore sizes is imposed.

## Assumptions and scope
Graphs are finite, simple, loopless, and undirected. The same full vertex set is retained upon removing the edge, and all homotopy and homology refer to geometric realizations and integer coefficients. A singleton shore is permitted. \(S^i\) denotes the standard \(i\)-sphere. The forest complex is *unrestricted* (there is no bound on maximum degree). The first two shores are the ones containing the deleted edge; the other shores are unaffected. The asserted natural maps are induced by the simplicial inclusion, not by a chosen noncanonical wedge decomposition.

## Proof
**1. Pair pieces for the intact complex.** For each \(1\le i<j\le r\) define \(Q_{ij}=\mathcal F(K_{n_i,n_j})\) on \(A_i\sqcup A_j\). An induced forest in a complete multipartite graph uses at most two shores: three occupied shores make an induced triangle. Consequently \(\mathcal F(G)=\bigcup_{i<j}Q_{ij}\). Two different pair pieces have intersection equal to the full simplex \(\Delta_{A_i}\) when they share precisely the shore \(A_i\); pieces with disjoint shore labels are disjoint. All \(\Delta_{A_i}\) are contractible. By the standard homotopy-pushout gluing lemma for cofibration diagrams over the incidence graph of shores and pairs, this union has the homotopy type of the graph \(K_r\) together with the independent reduced homotopy summands of the pair pieces. More concretely, collapse each shore simplex to a separate point and replace each simply connected pair piece by an interval between those points wedged with its based reduced homotopy type. Contractible intersections ensure that this replacement is compatible with all pairs. For the bipartite piece,
\[
Q_{ij}\simeq\bigvee^{(n_i-1)(n_j-1)}S^2.
\]
Indeed \(Q_{ij}=(\Delta_{A_i}*A_{j,\mathrm{disc}})\cup(\Delta_{A_j}*A_{i,\mathrm{disc}})\), a union of contractible complexes whose intersection is the simplicial complete-bipartite graph. Mayer–Vietoris and the homotopy pushout identify its type with the suspension of that graph. The original incidence graph has cycle rank \(\binom{r-1}{2}\); summing the pair contributions gives the intact formula. This pair decomposition is also natural for the inclusion maps below, at the level of the associated graph and integral homology direct summands.

**2. Exactly which faces change under the edge fault.** A face newly admitted by removing \(xy\) must contain both \(x\) and \(y\). If a third shore is occupied, the only possible newly admitted faces are the triangles \(\{x,y,z}\), where \(z\in A_k\), \(k\ge3\). Any fourth vertex in another shore creates an undeleted triangle; a second vertex in any occupied shore gives an undeleted triangle or four-cycle. Within only \(A_1\sqcup A_2\), the only new faces are the tetrahedra \(\{x,y,a,b}\), where \(a\in A_1\setminus\{x}\) and \(b\in A_2\setminus\{y}\): the unique four-cycle in their induced graph loses an edge. Adding any additional vertex produces an undeleted four-cycle. All proper subfaces of these triangles or tetrahedra already lie in \(\mathcal F(G)\). There are exactly \(\sum_{k=3}^r n_k\) new triangles and \(p\) new tetrahedra, and no other new faces.

**3. Contractible replacement for the exceptional pair.** Let \(Q'_{12}=\mathcal F(K_{n_1,n_2}-xy)\). The \(p\) new tetrahedra attach solely within the original \(Q_{12}\). If both shore sizes exceed one, the boundaries map, under the bipartite Mayer–Vietoris isomorphism, to the four-cycles \(x-b-a-y-x\), indexed by all \(a\ne x\), \(b\ne y\). These form an *integral basis* of the cycle lattice of the simplicial graph \(K_{n_1,n_2}\): take as spanning tree all edges \(xb\), \(b\in A_2\), together with all \(ay\), \(a\in A_1\setminus\{x}\). Thus these added three-cells kill the complete pairwise second homology by a unimodular attaching matrix. There are no higher new faces. The simply connected complex \(Q'_{12}\) is acyclic and hence contractible by Hurewicz–Whitehead. If either shore is a singleton, \(p=0\) and \(Q_{12}\) was already contractible (its complete-bipartite factor is a tree). Therefore the conclusion holds for all sizes.

**4. How the new triangles attach.** First replace \(Q_{12}\) by \(Q'_{12}\), leaving the other pair pieces unchanged. Step 1's incidence-graph argument still applies, except the pair \(12\) now contributes no two-sphere summands. Call the resulting complex \(Z\). Its homotopy model is a graph \(K_r\) wedged with \(\bigvee^{U-p}S^2\). Each new triangle \(xyz\), with \(z\in A_k\), attaches along three pair-piece edges \(xy\), \(xz\), \(yz\), and in the graph model its boundary is homotopic to the triangular graph loop on shore vertices \(1,2,k\). The boundary class is independent of the specific choice of \(z\in A_k\), since the simplices \(\{x,z,z'}\) and \(\{y,z,z'}\) in the existing pair pieces give explicit homotopies between the corresponding edge paths. The pair pieces are simply connected, so these path identifications introduce no unrecorded fundamental-group generators.

Use the star of shore \(1\) as spanning tree of the graph \(K_r\). The non-tree edges \(\{2,k}\), \(k=3,\ldots,r\), have fundamental cycles exactly \(1-2-k-1\), so the first added triangle from each of the \(r-2\) other shores kills a *free basis element* of the graph fundamental group. The remaining \(n_k-1\) triangles from that shore attach along nullhomotopic loops and create independent two-sphere wedge summands. The other \(\binom{r-2}{2}\) non-tree edges, joining shores at least three, retain the free circle generators. The two-sphere summands from \(Q_{ij}\), \(ij\ne12\), are untouched because each triangular attaching map lies in the graph one-skeleton after the described homotopies. Hence
\[
\mathcal F(G')\simeq\bigvee^{\binom{r-2}{2}}S^1\vee\bigvee^{U-p+\sum_{k=3}^r(n_k-1)}S^2.
\]
This derives an actual homotopy equivalence, rather than inferring it merely from Betti numbers.

**5. Primitive integral inclusion maps.** The same graph-of-spaces model tracks the original inclusion. On first homology it is the map from the free cycle lattice of \(K_r\) to the quotient killing the independent primitive triangle cycles \(1-2-k-1\), so its kernel has rank \(r-2\) and is a direct summand. On second homology all pair summands \(ij\ne12\) inject as direct summands, the entire \(12\)-pair lattice of rank \(p\) dies by Step 3, and the new independent triangle spheres provide a free cokernel of rank \(s\). Thus all asserted maps are integral, primitive, and split, including boundary cases with zero ranks.

## Verification
The bundled standard-library program `check_multipartite.py` constructs all graph-edge relations and tests acyclicity for **every** vertex subset using union–find, independently enumerates all forest faces before and after the fault, and calculates all reduced mod-two Betti numbers from simplicial boundary matrices. It asserts the intact and faulted predicted ranks as well as the exact new face-count law on fifteen parameter vectors, covering three, four, and five shores with singleton and nonuniform sizes. Run `python3 check_multipartite.py`. The finite results corroborate the formulas; the all-size integral homotopy and primitive inclusion maps are established by Steps 1–5, not by mod-two experiments. The graph-of-spaces proof and the unit fundamental cycle matrix supply the required integer-lattice information.

## Relationship to prior work
Carnero Bravo's forest-filtration theorem supplies the induced-forest framework and the **intact** complete-multipartite sphere-wedge classification; the intact formula above is not claimed as new. The established one-edge bipartite theorem supplies the contractibility of the exceptional two-shore piece; its proof is recapitulated in Step 3 for self-containment. A previously published equal-two-shore instance describes the fault in \(K_{2,\ldots,2}\), but does **not** imply the arbitrary nonuniform-size formula or the additional \(\sum_{k\ge3}(n_k-1)\) degree-two classes in that generality. Work on missing edges in multipartite *clique-avoidance* complexes addresses a different vertex-subset condition; a subset may have no large clique and still contain an induced cycle. The new contribution here is the all-size, all-shore integral homotopy and inclusion-map theorem, including singleton shores.

## Limitations
Exactly one cross-edge is deleted. Multiple deletions may create induced forests on more than two shores or additional higher-dimensional faces, so this proof does not classify them. Noncanonical sphere-wedge splittings are used only as homotopy models; the inclusion-induced homology kernels and cokernels are canonical subquotients. No equivariant action or persistence past the one-edge transition is asserted. An equivalent unindexed result may exist, and independent mathematical review remains outstanding.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first publicly posted July 25, 2023. https://arxiv.org/abs/2307.13271 . See the complete-bipartite and complete-multipartite homotopy theorems.
2. *A one-edge homotopy transition for induced-forest complexes of bipartite graphs*, published November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-one-edge-homotopy-transition-for-induced-forest-complexes-of-b--e5b294bc3a20 .
