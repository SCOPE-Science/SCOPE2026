# Forest defects in multipartite clique-avoidance: a shape-invariant sphere-wedge law and an integral persistence transition

## Finding
Let \(r\ge3\), and partition the vertices of a finite graph into \(r\) nonempty independent sets \(A_1,\ldots,A_r\). Start with the complete multipartite graph \(K_{|A_1|,\ldots,|A_r|}\), and remove a bipartite forest \(F\) consisting solely of cross-edges between \(A_1\) and \(A_2\). Write \(c\) for the number of connected components of \(F\) that contain at least one edge; ignore isolated vertices of \(F\). The complex \(\mathsf{CF}_r(G_F)\) contains precisely the vertex subsets inducing no clique of order \(r\). Its geometric realization satisfies
\[
|\mathsf{CF}_r(G_F)|\simeq
\begin{cases}
S^{r-2},&c=0,\\
\mathrm{pt},&c=1,\\
\bigvee^{c-1}S^{r-1},&c\ge2.
\end{cases}
\]
This is an integral homotopy classification: it determines the fundamental group, every higher homotopy group up to homotopy equivalence, and all integral homology. Its dependence on the deleted forest is *only* through the number of its edge-bearing connected components, independently of their branching, lengths, and the sizes of the remaining graph parts.

There is also an exact natural persistence statement. For \(1\le m\le\min(|A_1|,|A_2|)\), choose \(m\) disjoint cross-edges and let \(F_t\) contain the first \(t\) of them, for \(0\le t\le m\). Put \(X_t=\mathsf{CF}_r(G_{F_t})\). Graph-edge deletion enlarges the clique-avoidance complex, so \(X_0\subseteq X_1\subseteq\cdots\subseteq X_m\). Extend the filtration constantly after \(m\). Its complete reduced barcode over every field has exactly one interval \([0,1)\) in degree \(r-2\), together with one infinite interval \([t,\infty)\) in degree \(r-1\) for each \(2\le t\le m\). At the integral level, all such modules have free groups and split injection/surjection structure determined by the same sequence. For \(m=1\), the higher-degree interval family is empty.

The acyclicity hypothesis on \(F\) matters: when \(|A_1|=|A_2|=3\) and the removed edges form the bipartite six-cycle, the result is \(S^r\), not the forest formula. The remaining classes \(A_3,\ldots,A_r\) may have arbitrary positive sizes.

## Assumptions and scope
All graphs are finite, simple, and undirected; \(r\ge3\). A complete multipartite graph has every cross-edge and no edge within a part. A *forest defect* is the graph \(F\) on \(A_1\sqcup A_2\), whose edge set comprises the deleted cross-edges; it may contain isolated vertices. The term *component* in \(c(F)\) excludes isolated vertices. Denote by \(\Delta_W\) the complete simplex on a nonempty vertex set \(W\), by \(*\) simplicial join, by \(\operatorname{Ind}(H)\) the complex of independent sets of a graph \(H\), and by \(\Sigma\) unreduced suspension. Every homotopy type concerns geometric realization. The term \([t,\infty)\) in the finite filtration means the class survives the final stage, which is subsequently held constant.

## Proof
**1. A natural suspension reduction.** For any deleted-edge pattern \(E\subseteq A_1\times A_2\), write \(H_2=K_{A_1,A_2}\setminus E\), and let \(H_j\) be the induced graph on the first \(j\) independent classes, with all other cross-edges present. Set \(Y_j=\mathsf{CF}_j(H_j)\), for \(2\le j\le r\). The base case is \(Y_2=\operatorname{Ind}(H_2)\). Since \(H_{j-1}\) has no clique of order \(j\), and every vertex in \(A_j\) is adjacent to every vertex of \(H_{j-1}\), the following is an exact equality of simplicial complexes, not just a homotopy equivalence:
\[
Y_j=\Delta_{A_1\cup\cdots\cup A_{j-1}}\ \cup\ (Y_{j-1}*\Delta_{A_j}),\qquad
\Delta_{A_1\cup\cdots\cup A_{j-1}}\cap(Y_{j-1}*\Delta_{A_j})=Y_{j-1}.
\]
Each piece is contractible, with a simplicial cofibration as intersection. Their homotopy pushout is the unreduced suspension of their intersection. Iterating yields
\[
|\mathsf{CF}_r(G_E)|\simeq\Sigma^{r-2}|\operatorname{Ind}(K_{A_1,A_2}\setminus E)|.
\]
The Mayer–Vietoris connecting maps provide natural isomorphisms of reduced integral homology under inclusions of deleted-edge patterns, shifting degree by \(r-2\). We do not assert that an arbitrarily chosen wedge splitting is natural.

**2. The fold is an actual simplicial collapse.** In any graph \(Q\), if distinct vertices \(u,v\) satisfy \(N_Q(u)\subseteq N_Q(v)\) for open neighborhoods, then \(u,v\) are nonadjacent. In \(\operatorname{Ind}(Q)\), pair every independent face containing \(v\) but not \(u\) with that face augmented by \(u\). The larger face is independent because it avoids \(N_Q(v)\supseteq N_Q(u)\). Matching along this single pivot is acyclic (no reversed matching path can restore an already removed pivot). It removes exactly all simplices containing \(v\), yielding a simplicial collapse to \(\operatorname{Ind}(Q\setminus v)\). This proves the form of the standard independence-complex fold lemma used here without assuming a homological approximation.

**3. Prune a bipartite forest by legal folds.** Let \(Q=K_{A_1,A_2}\setminus F\). Suppose first that \(F\) has an edge. If \(x\in A_1\) has degree zero in \(F\), choose an active \(x'\in A_1\). Then \(N_Q(x')\subseteq N_Q(x)=A_2\), so the fold deletes \(x\). The same argument deletes all zero-degree vertices from either shore. Within a nontrivial tree component of \(F\), choose a leaf \(x\) whose unique neighbor \(y\) has degree at least two; such a leaf always exists when the tree has more than one edge. Choose another neighbor \(x'\ne x\) of \(y\). In the complement between the shores, \(N_Q(x')\subseteq N_Q(x)\), because the missing-neighbor set of \(x\) is the singleton \(\{y\}\), a subset of the missing-neighbor set of \(x'\). Delete \(x\) by the fold. Repeat until each component of \(F\) is one isolated edge. No component with an edge is lost or merged, and the process terminates after finitely many vertices. Therefore
\[
\operatorname{Ind}(Q)\simeq\operatorname{Ind}(K_{c,c}\setminus M_c)
\]
for \(c\ge1\), where \(M_c\) is a perfect matching. If \(F\) has no edges, instead \(\operatorname{Ind}(Q)=\Delta_{A_1}\sqcup\Delta_{A_2}\simeq S^0\).

**4. Evaluate the reduced matching complement.** Every independent set of \(K_{c,c}\setminus M_c\) lies entirely in one shore or is exactly a matched cross pair. Hence its independence complex consists of two disjoint full simplices, one on each shore, connected by \(c\) individual matching edges. Contract each shore simplex to a point: the result is a connected graph with two vertices and \(c\) parallel arcs, and hence has integral homotopy type \(\bigvee^{c-1}S^1\) when \(c\ge1\). For \(c=1\), this is contractible. Combining with Step 1 gives the stated cases, including the initial \(S^{r-2}\) when \(c=0\). Every integral homology group is free; homotopy equivalence (rather than Betti-number inference) establishes all claims.

**5. The complete matching-deletion persistence module.** Take \(E=M_t\) for nested matchings. Before reducing any vertices, the independence complex has the **exact** description
\[
\operatorname{Ind}(K_{A_1,A_2}\setminus M_t)
=\Delta_{A_1}\cup\Delta_{A_2}\cup\bigcup_{i=1}^{t}\Delta_{\{a_i,b_i\}}.
\]
The two shore simplices are fixed throughout the filtration and can be contracted simultaneously at all stages. The resulting filtration has two vertices and \(t\) arcs connecting them. For \(t=0\), the two vertices give one reduced integral degree-zero class; the first arc joins them and kills that class. From the second arc onward, each new arc creates one primitive independent degree-one cycle, and previously created cycles persist as direct summands. This yields degree-zero barcode \([0,1)\) and degree-one barcodes \([t,\infty)\) for \(2\le t\le m\). The natural Mayer–Vietoris suspension shift in Step 1 transfers these statements to degrees \(r-2\) and \(r-1\), with the claimed integral split maps and no additional bars.

**6. Sharp cyclic boundary.** If \(F=C_6\subseteq K_{3,3}\) is a six-cycle spanning the two shores, then \(K_{3,3}\setminus F\) is a three-edge perfect matching. Its independence complex is the simplicial join of three two-point discrete spaces, which is a triangulated \(S^2\). Step 1 suspends it \(r-2\) times, giving \(S^r\). Thus one cannot replace the forest restriction by an arbitrary connected bipartite deleted-edge graph.

## Verification
The standalone standard-library program `verify_forest_clique_free.py` independently constructs graph cliques and all forbidden-clique-free faces from graph edges, compares them with a separate set-theoretic face characterization, and reduces the resulting simplicial boundary matrices over \(\mathbb F_2\). It enumerates all \(2^9\) edge-defect subsets between three-by-three shores and checks every one of the 328 forest cases. Its legal-neighborhood-fold simulation performs 1,090 deletions, always reducing each forest to a matching of exactly \(c\) edges. It additionally checks 21 cases in four and five parts, three six-cycle boundary cases, and four matching-filtration homology ranks. Run `python3 verify_forest_clique_free.py`; the complete expected output is in `verification_output.txt` and ends with `FOREST_DEFECT_CLIQUE_FREE_CHECK_PASS`. The code verifies mod-two homology and the exact combinatorial face structure on finite instances; it does not replace the all-size integral simplicial-collapse and suspension proof or independently certify natural integral persistence maps.

## Relationship to prior work
Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (arXiv:2602.09623v1, first public 2026-02-10), define this forbidden-clique complex and prove shellability under structural graph hypotheses and clique-attachment operations. Their results are not the present homotopy classification for missing bipartite forests in complete multipartite graphs, nor do they give the matching-edge persistence maps. The classical fold lemma for independence complexes is a known tool and is not claimed as new; the needed special case is proved directly above.

A separately available result, *Triangle-free graph joins: a complete integral homotopy splitting for three-clique avoidance* (2026-10-25), covers the general suspension relationship in the special case of three-clique avoidance and the join of a triangle-free graph with an independent factor. That suspension special case is **not** an originality claim here. Its hypothesis and conclusion neither evaluate forest-edge defects nor provide the complete arbitrary-\(r\) component-count law or matching-deletion persistence.

Other previous classifications concern (i) matching deletions in two different cross-part pairs of a tripartite graph (a different defect configuration), and (ii) the two-independence complex of a matching-deficient complete bipartite graph (a different forbidden configuration). Neither implies the present forest law or clique-avoidance barcode. The initial undeleted multipartite sphere is standard and is credited as a base case, not a new observation. The novel claim is the joint **forest-shape invariant** and **natural integral persistence transition**, with the cyclic boundary demonstrating scope.

## Limitations
Deleted edges must all lie between one specified pair of shores, and their defect graph must be a forest for the closed sphere-wedge classification. The general suspension reduction itself allows arbitrary deleted edges but does not classify their independence complexes. The cyclic counterexample shows that component count alone fails beyond forests. No equivariant homotopy classification is asserted. Tests use finite mod-two boundary calculations, while the integral statements rest on the theoretical collapse and homotopy-pushout arguments. No independent mathematical audit has been performed; equivalent unindexed formulations remain possible.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first public 2026-02-10; https://arxiv.org/abs/2602.09623 .
2. H. Chandrakar and A. Singh, *Independence Complexes of Hexagonal Grid Graphs*, arXiv:2512.21318, first public 2025-12-24; https://arxiv.org/abs/2512.21318 . (A contemporary use of the standard fold lemma; not a source of the new forest classification.)
3. *Triangle-free graph joins: a complete integral homotopy splitting for three-clique avoidance* (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-triangle-free-graph-joins-a-complete-integral-homotopy-splitting--f6e42b155b01 . (The overlapping three-clique suspension case is credited.)
4. *Equivariant compression and subgroup-fixed sphere spectra of multipartite clique-free complexes* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-equivariant-compression-and-subgroup-fixed-sphere-spectra-of-mul--d3da91e84d0d . (Only the fully multipartite, no-defect case.)
