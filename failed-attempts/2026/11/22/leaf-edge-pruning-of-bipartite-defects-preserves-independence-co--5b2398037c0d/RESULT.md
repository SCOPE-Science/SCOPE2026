# Leaf-edge pruning of bipartite defects preserves independence-complex simple homotopy

## Finding
Let \(A,B\) be disjoint nonempty finite vertex sets, let \(F\) be any simple bipartite graph on \(A\sqcup B\) with edges only between the shores, and set \(H_F=K_{A,B}\setminus E(F)\). Write \(X_F=\operatorname{Ind}(H_F)\) for the ordinary independence complex. Suppose \(v\) is a degree-one vertex of \(F\), with unique neighbor \(w\), and \(d=\deg_F(w)\ge2\). Then the inclusion \(X_{F-vw}\hookrightarrow X_F\) is an explicit elementary simplicial collapse equivalence:
\[
X_F\searrow X_{F-vw}
\]
using exactly \(2^{d-2}\) free-face pairs. There is no hypothesis that \(F\) is acyclic or connected.

Consequently, let \(F\) be any bipartite forest on the same two nonempty shores, and let \(c\) denote the number of connected components of \(F\) containing an edge (isolated vertices do not count). Then
\[
X_F\simeq
\begin{cases}
S^0,&c=0,\\
\bigvee^{c-1}S^1,&c\ge1,
\end{cases}
\]
where the wedge with zero circles means a point. In particular, there is no integral torsion. Pruning any nontrivial pendant tree attached to a cyclic core also preserves simple-homotopy type.

## Assumptions and scope
All graphs are finite and simple. The shore sets \(A,B\) are nonempty but need not have equal cardinality. The edge set \(E(F)\) consists of *deleted* edges of the complete bipartite graph; thus the mixed pair \(\{a,b\}\), with \(a\in A,b\in B\), is a face of \(X_F\) exactly when \(ab\in E(F)\). Every pure-shore subset is a face. An elementary simplicial collapse removes a free face together with its unique containing facet. A forest may have isolated vertices and disconnected components. In the first assertion the degree \(d\) is taken in the defect graph \(F\), not in \(H_F\).

## Proof
Write \(e=vw\), and let \(U=N_F(w)\setminus\{v\}\). Because \(\deg_F(v)=1\), every face of \(X_F\) containing the pair \(\{v,w\}\) must consist of \(v,w\) and some subset of \(U\). Indeed, any other vertex on the shore of \(w\) would have to be a second neighbor of \(v\) in \(F\), which is impossible; vertices on the shore of \(v\) are unrestricted relative to \(v\) but must be adjacent to \(w\) in \(F\). Conversely, all such sets are faces. This characterization holds independently of all other edges and cycles of \(F\).

Choose \(x\in U\), which exists because \(d\ge2\), and put \(Y=U\setminus\{x\}\), so \(|Y|=d-2\). For each subset \(T\subseteq Y\), define
\[
L_T=\{v,w\}\cup T,\qquad U_T=L_T\cup\{x\}.
\]
Remove pairs \((L_T,U_T)\), in decreasing order of \(|T|\), breaking ties arbitrarily. At the moment of each removal, the only remaining proper coface of \(L_T\) is \(U_T\): any larger coface not containing \(x\) has the form \(L_{T'}\) with \(T'\supsetneq T\) and has already been removed; any larger coface containing \(x\) is \(U_{T'}\) for such a \(T'\) and has also been removed. Hence \(L_T\) is free with unique facet \(U_T\). The pairs partition *all* faces containing \(\{v,w\}\), so the complex remaining after the \(2^{|Y|}=2^{d-2}\) removals is exactly \(X_{F-e}\). This proves the explicit simple-homotopy statement and the equivalence induced by the inclusion.

If \(F\) is a forest and a component has at least two edges, choose a leaf \(v\) in that component. Its neighbor has degree at least two, so the collapse applies. Deleting its incident edge isolates \(v\) but leaves the other edges of that component connected; therefore the number \(c\) of edge-containing components is unchanged. Iteration leaves exactly one edge in each of the \(c\) edge-containing components, namely a matching \(M\), together with isolated vertices. It follows that \(X_F\searrow X_M\).

For \(c=0\), \(X_M\) is the disjoint union of the two full shore simplices and hence is homotopy equivalent to \(S^0\). For \(c\ge1\), \(X_M\) consists of the two disjoint full shore simplices \(\Delta_A\) and \(\Delta_B\), connected by precisely \(c\) mixed edges, and there are no mixed faces of dimension at least two. Contracting the two simplices (contractible CW subcomplexes) gives a connected one-dimensional CW complex with two vertices and \(c\) parallel edges, homotopy equivalent to \(\bigvee^{c-1}S^1\). This determines the complete integral homotopy type.

For any defect graph, the first assertion may be iterated until no degree-one vertex is adjacent to a vertex of degree at least two. The surviving nontrivial components are 2-cores or isolated edges, showing that pendant branching is invisible to the simple-homotopy type of \(X_F\). The degree condition is sharp as an operation: for a defect graph consisting of one edge, \(X_F\) is contractible, whereas removing that sole edge produces \(S^0\).

## Verification
The accompanying self-contained script `verify_leaf_pruning.py` enumerates every defect subset of \(K_{2,2}\), \(K_{2,3}\), and \(K_{3,3}\), plus 48 deterministically sampled defect graphs on two shores of four vertices. It verifies each indicated free-face pair in the *current* complex and verifies that the final face set is exactly that for the smaller defect graph. It separately computes reduced mod-two simplicial homology for every forest case. The recorded output gives 592 exhaustive graph instances, 48 additional instances, 440 forest homology cross-checks, and 1,399 valid elementary-collapse pairs. These finite checks corroborate but do not replace the unrestricted integral proof.

## Relationship to prior work
General suspension results for independence complexes of bipartite graphs are due to Jonsson, Nagel–Reiner, and Barmak. Berghoff develops general homology methods for independence complexes (arXiv:2008.06267), while Abdelmalek and collaborators study higher-independence complexes of chordal graphs (arXiv:2106.10863). Bakshi and collaborators analyze circle-graph independence complexes (arXiv:2412.01125), including a complementary-graph construction and restrictions on circle-wedge ranks. Those results do not, by their stated conclusions, supply the present explicit \(2^{d-2}\)-pair collapse for arbitrary bipartite defect graphs or the whole-forest classification through a simple-homotopy map. The latter statement concerns deletion of cross edges, not ordinary vertex deletion or the independence complex of \(F\) itself.

## Limitations
The theorem is specific to ordinary (first) independence complexes and to deleting cross edges from a complete bipartite graph with fixed shores. It does not classify a general defect graph with a nontrivial cyclic 2-core, nor does it assert shellability, a canonical collapse order, or any higher-independence analogue. The homotopy classification for forests does not assert an equivariant equivalence. The comparison with published literature cannot rule out an unindexed equivalent argument. No independent scientific audit has been performed.

## References
1. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, first posted 14 August 2020; Combinatorial Theory 2 (2022).
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418 (2010), Advances in Mathematics 241 (2013), 33–57.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (2021).
4. R. P. Bakshi et al., *Independence complexes of circle graphs*, arXiv:2412.01125, first posted 2 December 2024.
