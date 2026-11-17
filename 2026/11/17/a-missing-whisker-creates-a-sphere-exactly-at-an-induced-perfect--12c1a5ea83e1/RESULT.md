# A missing whisker creates a sphere exactly at an induced perfect matching

## Finding
Let \(G\) be any finite simple connected graph with \(n\ge3\) vertices, and choose a vertex \(z\) of core degree at least two. Attach a new leaf \(\ell_v\) adjacent only to each \(v\in V(G)\setminus\{z\}\), leaving \(z\) unwhiskered, and call the resulting graph \(H(G,z)\). Let \(\operatorname{Ind}_2(H)\) consist of those vertex subsets for which the induced graph has all connected components of size at most two. Then

\[
|\operatorname{Ind}_2(H(G,z))|\simeq
\begin{cases}
S^{n-2},&G-z\text{ is a disjoint union of edges covering all }n-1\text{ vertices},\\
\{\mathrm{point}\},&\text{otherwise}.
\end{cases}
\]

In particular, the exceptional condition is **that the entire induced graph** \(G-z\) be one-regular; merely containing a perfect matching is insufficient. When the sphere occurs, \(n\) is necessarily odd and the only nonzero reduced integral homology is \(\widetilde H_{n-2}\cong\mathbb Z\). There is a perfect acyclic simplicial matching yielding one critical vertex and, in the exceptional case, one critical \((n-2)\)-simplex.

The change from complete whiskering is sharp. For the friendship or windmill core \(G=K_1\vee\big(\bigsqcup_{j=1}^{m}K_2\big)\), rooted at its common vertex, \(m\ge1\), the partially whiskered complex is \(S^{2m-1}\); the fully whiskered complex is contractible by the previously known complete-whiskering theorem.

## Assumptions and scope
Graphs are finite, undirected, simple, and connected; \(n\ge3\), and \(\deg_G(z)\ge2\). The notation \(G-z\) denotes the **induced** subgraph on \(V(G)\setminus\{z\}\). A one-regular graph has every vertex degree exactly one, hence is an edge-disjoint union of copies of \(K_2\). The two-independence complex is the ordinary simplicial complex of induced maximum-degree-at-most-one vertex sets, equivalently the three-vertex-path-free complex. All homotopy equivalences and homology statements are integral and nonequivariant. The new leaves are mutually distinct and only adjacent to their designated original vertices.

## Proof
Write \(V=V(G)\) and \(L=\{\ell_v:v\in V\setminus\{z\}\}\). A face \(F\) of \(\operatorname{Ind}_2(H)\) determines a *core* \(S=F\cap V\). The induced graph \(G[S]\) necessarily has maximum degree at most one. Conversely, fixing any such \(S\), define the eligible leaf indices

\[
E(S)=\{v\in V\setminus\{z\}: v\notin S\text{ or }\deg_{G[S]}(v)=0\}.
\]

Precisely the faces with core \(S\) are
\[
F=S\cup\{\ell_v:v\in T\}\qquad(T\subseteq E(S)).
\]
This is an exact description: including \(\ell_v\) is forbidden only when \(v\) already has a neighbor in \(G[S]\), which would give the selected vertex \(v\) induced degree two. Two distinct leaves do not interact.

Fix an arbitrary total ordering of \(V\setminus\{z\}\). For each allowable core \(S\) with \(E(S)\ne\varnothing\), set \(w(S)=\min E(S)\) and match each face in its Boolean leaf fiber that omits \(\ell_{w(S)}\) to that face with \(\ell_{w(S)}\) added. This is a complete matching in every such fiber. It is acyclic: within one fiber, the matching on a single cube coordinate has no directed alternating cycle. More explicitly, along directed unmatched cover edges every other leaf coordinate can only be deleted, and the distinguished leaf coordinate is never deleted; therefore a directed cycle is impossible.

To see that the global union is acyclic, project each face to its core \(S\). Under any directed edge in the matched Hasse diagram, the core is unchanged for a leaf toggle, and strictly decreases under a core-vertex deletion. The projection therefore cannot increase along a directed path, so a directed cycle would have to lie entirely within one Boolean fiber. This is excluded above.

The only possible unmatched core fibers have \(E(S)=\varnothing\). Then every \(v\ne z\) belongs to \(S\), because an omitted \(v\ne z\) would make its leaf eligible. Moreover each such \(v\) must have exactly one neighbor in \(G[S]\), since zero neighbors would again make its leaf eligible and two neighbors would make \(S\) inadmissible. There are just two candidate cores: \(S=V\setminus\{z\}\) and \(S=V\). The second cannot be a face because a connected graph on at least three vertices has some vertex of degree at least two. The first is admissible and has no eligible leaf exactly when \(G-z\) is one-regular. Thus the matching leaves either no unmatched faces or exactly one nonempty unmatched face \(V\setminus\{z\}\), of dimension \(n-2\), when the exceptional condition holds.

For ordinary (rather than augmented) discrete Morse theory, the empty face is paired with the first available leaf, which is a vertex of the complex. Remove this one pair from the matching and omit the empty face. The chosen leaf becomes the single critical zero-cell; the only possible other critical cell is the exceptional \((n-2)\)-simplex. Acyclicity is retained on the nonempty face poset. Consequently, Forman's finite acyclic-matching theorem produces a CW homotopy model with either one zero-cell or one zero-cell and one \((n-2)\)-cell. As \(n-2\ge1\), in the latter case the cell attaches to the unique zero-cell and the CW model is \(S^{n-2}\). This proves both cases integrally, with no rank-only or field-only inference.

For the friendship graph with common vertex \(z\) and \(m\) disjoint core edges away from \(z\), the graph \(G-z\) is one-regular on \(2m\) vertices, giving the asserted sphere \(S^{2m-1}\).

## Verification
Run `python3 verify_one_missing_whisker_morse.py` using only the Python standard library. The checker enumerates every connected labelled core graph of orders three through five, every root (including some roots outside the stated degree restriction), and the corresponding two-independence simplices. It performs 3,804 exact binary boundary-matrix Betti computations, including 144 noncontractible predictions, and verifies the claimed Betti profiles. It separately builds and checks the global acyclic-matching digraph for 59 connected rooted samples, including friendship cores with one, two, and three triangles. The expected output is embedded in `VERIFIER_OUTPUT.txt`. These finite checks corroborate, but do not replace, the all-graph proof above.

## Relationship to prior work
Deshpande and Singh's 2020 Theorems 3.8 and 3.10 determine homotopy types for fully whiskered graphs and more general graphs whose every non-leaf vertex has at least one adjacent leaf. Our graph deliberately has an unwhiskered **non-leaf** vertex \(z\), so their hypotheses do not cover the new dichotomy. Their leaf-matching method is a clear methodological antecedent, not claimed as new here. Sawant (first posted 24 May 2026) establishes vertex decomposability of higher-independence complexes of all trees; this does not determine the present sphere/contractible dichotomy for arbitrary connected cores, including graphs with cycles. Ghosh and Selvaraja study shellability of several graph families but do not state the one-missing-whisker homotopy criterion. The result concerns the *whole graph after one removed leaf* rather than other invariants of fully whiskered graphs.

## Limitations
This theorem concerns the second independence complex only; arbitrary higher thresholds, multiple missing leaves, and equivariant homotopy remain unclassified. It does not imply a corresponding classification of shellability, nor does it assert the sphere condition merely from the existence of a perfect matching in \(G-z\). The proof is complete as written, but independent mathematical review and comprehensive priority assessment have not been performed; unindexed equivalent results cannot be excluded.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 15 January 2020, especially Theorems 3.8 and 3.10. https://arxiv.org/abs/2001.05448
2. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, first posted 10 May 2025. https://arxiv.org/html/2505.06614v3
3. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first posted 24 May 2026. https://arxiv.org/html/2605.25150v1
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, the discrete Morse matching theorem.
