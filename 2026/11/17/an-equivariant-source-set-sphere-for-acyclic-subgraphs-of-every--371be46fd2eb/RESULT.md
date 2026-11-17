# An equivariant source-set sphere for acyclic subgraphs of every strongly connected digraph

## Finding
Let \(G=(V,E)\) be a finite loopless simple strongly connected digraph with \(n=|V|\ge2\). Let \(\mathcal A(G)\) be the abstract simplicial complex of all arc subsets with no directed cycle, and let \(\Gamma=\operatorname{Aut}(G)\) act by vertex and arc permutations. Write
\[
W_V=\{(x_v)_{v\in V}\in\mathbb R^V:\sum_{v\in V}x_v=0\},
\qquad S(W_V)=\{x\in W_V:\|x\|=1\}.
\]
There is an explicit \(\Gamma\)-equivariant homotopy equivalence
\[
\boxed{|\mathcal A(G)|\simeq_{\Gamma} S(W_V).}
\]
For **each** subgroup \(H\le\Gamma\), let \(o_V(H)\) be the number of vertex orbits. Then
\[
|\mathcal A(G)|^H\simeq
\begin{cases}
\varnothing,&o_V(H)=1,\\
S^{o_V(H)-2},&o_V(H)\ge2.
\end{cases}
\]
Moreover \(|\mathcal A(G)|/H\simeq S(W_V)/H\). The only nonzero reduced integral homology of \(\mathcal A(G)\) is \(\widetilde H_{n-2}\cong\mathbb Z\), on which each automorphism acts by the sign of its permutation of \(V\). Hence
\[
\widetilde H_i(|\mathcal A(G)|/H;\mathbb Q)\cong
\begin{cases}
\mathbb Q,&i=n-2\text{ and every element of }H\text{ is even on }V,\\
0,&\text{otherwise}.
\end{cases}
\]

## Assumptions and scope
A directed cycle may have length two (two mutually opposite arcs); no loops or parallel arcs are used. A face of \(\mathcal A(G)\) is an arc set \(F\subseteq E\) for which \((V,F)\) is directed acyclic. The empty face is present but is excluded from the face poset used below. Geometric fixed points are fixed points of the actual realization, not merely of vertices. The orbit and quotient statements concern **all** subgroups of \(\Gamma\), not only cyclic subgroups. When \(o_V(H)=1\), the fixed-point space is genuinely empty; no negative-dimensional sphere is asserted as a nonempty space.

## Proof
Let \(P\) be the poset of nonempty acyclic arc sets, ordered by inclusion, and \(Q\) the poset of nonempty proper subsets of \(V\), also ordered by inclusion. For \(F\in P\) put
\[
\phi(F)=\{v\in V:\text{some arc of }F\text{ has head }v\}.
\]
The set \(\phi(F)\) is nonempty because \(F\ne\varnothing\), and is proper because every finite directed acyclic graph has a source. Inclusion of arc sets preserves inclusion of head supports, so \(\phi:P\to Q\) is an order-preserving \(\Gamma\)-equivariant map.

Fix any subgroup \(H\le\Gamma\). Its fixed-posets \(P^H\) and \(Q^H\) consist of the \(H\)-invariant arc sets and vertex subsets, respectively. Fix \(T\in Q^H\), and let \(S=V\setminus T\). Strong connectivity gives a nonempty set
\[
B_T=\{(s,t)\in E:s\in S,\ t\in T\}.
\]
Indeed, otherwise no directed path from \(S\) could reach \(T\). This arc set is invariant under \(H\), consists only of arcs exiting \(S\), and is acyclic. The lower fiber \(\phi_H^{-1}((Q^H)_{\le T})\) is precisely the poset of nonempty invariant acyclic \(F\) with all heads in \(T\). Such \(F\) has **no** arc entering \(S\), so adjoining every arc in \(B_T\) cannot create a directed cycle: any cycle containing a new arc would have to return to \(S\). The poset maps
\[
F\longmapsto F\cup B_T,\qquad B_T\longmapsto F\cup B_T
\]
are therefore well defined. In more detail, \(F\subseteq F\cup B_T\supseteq B_T\); these two natural transformations contract the fiber order complex to the vertex \(B_T\). This argument works for each \(H\), including the trivial subgroup.

The Quillen fiber lemma applied to \(\phi_H\) gives a homotopy equivalence \(|\Delta(P^H)|\simeq|\Delta(Q^H)|\). Barycentric subdivisions remove all inversions, so their geometric fixed-point spaces are precisely these order complexes. Thus the simplicial map \(|\Delta(P)|\to|\Delta(Q)|\) induced by \(\phi\) is a homotopy equivalence on the fixed-point spaces of **every** subgroup. The equivariant Whitehead theorem for finite \(\Gamma\)-CW complexes makes it a \(\Gamma\)-homotopy equivalence.

The complex \(\Delta(Q)\) is the barycentric subdivision of the boundary of the simplex with vertex set \(V\). Radial projection from its barycenter identifies that boundary \(\Gamma\)-equivariantly with \(S(W_V)\). If \(H\) has \(t=o_V(H)\) vertex orbits, the invariant subspace \(W_V^H\) has real dimension \(t-1\), so its unit sphere is empty for \(t=1\), and \(S^{t-2}\) otherwise. Equivariant homotopy equivalences descend to quotient homotopy equivalences, establishing the other assertion.

The reduced integral homology of \(S(W_V)\) is \(\mathbb Z\) in degree \(n-2\), and zero otherwise. The action on that orientation line is \(\det(\sigma|_{W_V})=\operatorname{sgn}(\sigma|_V)\), since the complementary constant line is fixed. Finally, for any finite group acting simplicially without inversions (as after subdivision), the rational chains of the orbit CW complex calculate invariant rational homology. Taking invariants of this orientation line yields the stated exact rational quotient formula.

## Verification
Run \(\texttt{python3 verify.py}\) with a standard Python 3 installation. The program enumerates invariant acyclic arc subsets and calculates mod-two homology of all fixed-orbit complexes in fifty-five explicitly stated tests involving directed cycles, bidirected cycles, complete bidirected graphs, and their rotation, reflection, and permutation subgroups. It also checks the strong-connectivity hypothesis and the nonempty invariant cone \(B_T\) and its acyclicity-preserving union operation for every invariant proper nonempty head-support \(T\) in those examples. The included output must end in \(\texttt{ACYCLIC_DIGRAPH_EQUIVARIANT_HEAD_MAP_CHECKS_PASS}\). These finite checks corroborate, but do not prove, the universal theorem; the argument above supplies the proof.

## Relationship to prior work
Björner and Welker (1999) proved the ordinary sphere homotopy type of the acyclic-subgraph complex of the complete directed graph. Hultman (2004, Theorem 3.3) proved the nonequivariant sphere-or-contractible classification for any finite directed graph, and its Section 3 was inspected in full. These established sphere results are not claimed as new. The additional theorem here is the **specific equivariant head-support equivalence** for every strongly connected digraph, determining all subgroup fixed spaces and the integral automorphism orientation character. The path-free complexes of Grinberg, Katthän, and Lewis forbid paths between distinguished endpoints rather than all directed cycles, so their sphere statements have different hypotheses and spaces. A potentially relevant early full text was not available for comparison; see Limitations.

## Limitations
The result does not claim a homeomorphism from the original acyclic arc complex to the sphere, nor classify integral homology torsion of all quotients, nor address digraphs that are not strongly connected. The complete 1999 paper of Björner and Welker was inaccessible beyond its publisher abstract and references, despite searches for accessible full text; it remains a literature-priority risk for its complete-digraph special case. The new general result is not inferred from a failed literature search. Independent mathematical validation has not been performed.

## References
1. A. Hultman, “Directed subgraph complexes,” *Electronic Journal of Combinatorics* **11** (2004), R75. DOI: 10.37236/1828. First verified public publication: 2004-10-26. Full seven-page article inspected.
2. A. Björner and V. Welker, “Complexes of directed graphs,” *SIAM Journal on Discrete Mathematics* **12** (1999), 413–424. DOI: 10.1137/S0895480198338724. Publisher abstract and references accessible; complete text inaccessible.
3. D. Grinberg, L. Katthän, J. B. Lewis, “The path-missing and path-free complexes of a directed graph,” arXiv:2102.07894, initially submitted 2021-02-15; HTML introduction and definitions inspected.
4. D. Quillen, “Homotopy properties of the poset of nontrivial \(p\)-subgroups of a group,” *Advances in Mathematics* **28** (1978), 101–128 (fiber lemma).
5. J. Thévenaz and P. Webb, “Homotopy equivalence of posets with a group action,” *Journal of Combinatorial Theory, Series A* **56** (1991), 173–181 (equivariant-poset framework).
