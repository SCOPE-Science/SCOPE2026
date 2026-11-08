# Tree-leaf joins and sphere-wedge total mutual-visibility complexes of rook prisms

## Finding

Let \(T\) be any finite tree with at least three vertices, let \(L(T)\) be its leaf set, and let \(H\) be any finite connected graph of order at least two. Define \(\mathcal V_{\mathrm t}(G)\) to be the abstract simplicial complex whose faces are the vertex subsets \(S\subseteq V(G)\) for which every pair of vertices of \(G\) has a shortest path with no internal vertex in \(S\). With the natural labeled vertex identifications,
\[
\boxed{\mathcal V_{\mathrm t}(T\square H)=\mathop{*}_{v\in L(T)}\mathcal V_{\mathrm t}(H)^{(v)}.}
\]
The equality is literal as face families: every feasible set is supported on leaf layers and its restrictions to those layers are independently feasible in \(H\). In particular, if \(F_G(z)=\sum_{S\in\mathcal V_{\mathrm t}(G)}z^{|S|}\) and \(M_G(z)\) counts inclusion-maximal faces, then
\[
F_{T\square H}(z)=F_H(z)^{|L(T)|},\qquad M_{T\square H}(z)=M_H(z)^{|L(T)|}.
\]

For any integer \(n\ge2\), put \(R_n=K_n\square K_2\), and write \(\ell=|L(T)|\). Then the entire face family, both cardinality polynomials, and the integral homotopy type are explicit:
\[
\boxed{F_{T\square R_n}(z)=\bigl(2(1+z)^n-1+nz^2\bigr)^\ell,}
\]
\[
\boxed{M_{T\square R_n}(z)=\bigl(2z^n+nz^2\bigr)^\ell,}
\]
\[
\boxed{\mathcal V_{\mathrm t}(T\square R_n)\simeq\bigvee^{(n-1)^\ell}S^{2\ell-1}.}
\]
More precisely, every maximal face chooses, independently in each leaf layer, either the complete \(n\)-vertex row (two choices) or the complete two-vertex column (\(n\) choices). For \(n\ge3\), the possible maximal-face sizes are exactly \(2\ell+j(n-2)\), for all integers \(0\le j\le\ell\), with multiplicity \(\binom\ell j 2^j n^{\ell-j}\). For \(n=2\), every maximal face has size \(2\ell\), with \(4^\ell\) such faces. Hence this complex is pure exactly when \(n=2\).

## Assumptions and scope

Graphs are finite, simple, undirected, connected, and equipped with ordinary unweighted shortest-path distance. The tree has at least three vertices, so distinct leaves are not adjacent. The Cartesian product uses coordinates \((t,h)\); its distance is \(d_{T\square H}((t,h),(t',h'))=d_T(t,t')+d_H(h,h')\). Each face may be empty. A facet means an inclusion-maximal face; no assertion about merely maximum-cardinality faces is substituted for facet maximality. The wedge statement concerns the geometric realization and integral homotopy type, not only mod-two homology.

## Proof

**1. All selected vertices lie in leaf layers.** Suppose \(t\) has at least two distinct tree neighbors \(t_1,t_2\), and fix \(h\in V(H)\). The only length-two path in \(T\square H\) between \((t_1,h)\) and \((t_2,h)\) runs through \((t,h)\): a shortest path between these endpoints must spend both steps changing the tree coordinate, and the path in a tree is unique. If \((t,h)\) were selected, this pair would not be visible. Thus every feasible set avoids all nonleaf tree layers.

**2. Restriction to a leaf layer is feasible in the second factor.** Fix any leaf \(v\). A shortest path between \((v,h)\) and \((v,h')\) never changes its tree coordinate because its length is exactly \(d_H(h,h')\). Hence any feasible set in \(T\square H\) intersects the \(v\)-layer in a total mutual-visibility set of \(H\).

**3. Arbitrary independent leaf-layer choices are sufficient.** Conversely select any feasible subset \(S_v\subseteq V(H)\) for each leaf \(v\), and let \(S\) be their union in the corresponding layers. Consider endpoints \((t,h)\) and \((t',h')\). If \(t=t'\) is a leaf, the prescribed feasible set \(S_t\) gives an avoiding shortest path entirely inside that layer. If \(t=t'\) is nonleaf, every shortest path in its layer avoids \(S\) internally. If \(t\ne t'\), the unique tree path between \(t\) and \(t'\) has at least one nonleaf vertex \(w\): a path consisting entirely of two leaf endpoints joined by one edge cannot occur in a tree of order at least three. Move from \((t,h)\) to \((w,h)\) along that tree path, traverse any shortest \(H\)-path from \(h\) to \(h'\) in the unselected \(w\)-layer, then finish along the tree path from \((w,h')\) to \((t',h')\). This path has length \(d_T(t,t')+d_H(h,h')\), so it is shortest. All its internal tree coordinates are nonleaf; any selected endpoints are not internal. The path therefore avoids \(S\) internally. Steps 1–3 establish equality of labeled complexes. Face and facet polynomials multiply for simplicial joins on disjoint vertex sets; facets in a join are exactly unions of factor facets.

**4. The rook-prism factor.** Label \(R_n\) by \((i,b)\) for \(i\in\{1,\dots,n\}\) and \(b\in\{0,1\}\). Its graph diameter is two. Each pair at distance two, \((i,0),(j,1)\) with \(i\ne j\), has precisely two common neighbors \((i,1),(j,0)\). Therefore a vertex subset is total mutual-visible exactly when it does not contain both elements of any pair \(\{(i,0),(j,1)\}\) with \(i\ne j\): if it did, the opposite distance-two pair would have all common neighbors selected; if it does not, every distance-two pair has a common neighbor outside the set and hence an avoiding geodesic. A feasible set with vertices in both binary rows must therefore consist of the two vertices in one column. All remaining feasible sets lie within one binary row. These are exactly the faces of two disjoint \((n-1)\)-simplices, together with the \(n\) vertical matching edges joining corresponding vertices. Counting all row subsets once each, subtracting the doubly counted empty set, and adding the vertical two-element faces gives \(2(1+z)^n-1+nz^2\). The facets are precisely the two full rows and the \(n\) vertical edges, giving \(2z^n+nz^2\). The \(n=2\) case is valid as well: all four facets are edges.

**5. Integral homotopy.** Collapse each row simplex simplicially onto a spanning star on its \(n\) vertices, leaving the \(n\) vertical edges fixed. For example, choose one apex in each row and successively pair every face of cardinality at least two not containing that apex with its cone face, retaining apex-to-vertex edges; this is an acyclic elementary collapse inside the simplex. The result is a connected graph on \(2n\) vertices with \(2(n-1)+n=3n-2\) edges and cycle rank \((3n-2)-(2n)+1=n-1\). It is homotopy equivalent to a wedge of \(n-1\) circles. Since joins preserve homotopy equivalence of nonempty CW complexes and \(X*Y\simeq\Sigma(X\wedge Y)\) for based connected CW complexes, joining \(\ell\) copies of a wedge of \(n-1\) circles gives a wedge of \((n-1)^\ell\) spheres of dimension \(2\ell-1\). This proves the integral homotopy statement, including the case \(n=2\).

**6. Maximal-face spectrum.** In each of the \(\ell\) factors a facet has one of \(2\) choices of size \(n\), or one of \(n\) choices of size two. Choosing \(j\) large facets and \(\ell-j\) small facets gives \(\binom\ell j2^j n^{\ell-j}\) facets of size \(2\ell+j(n-2)\). For \(n=2\), all four choices have the same size. All statements follow.

## Verification

The accompanying dependency-free Python program `verify_tree_rook.py` constructs Cartesian product graphs directly, computes shortest distances by breadth-first search, enumerates shortest-path directed acyclic graphs, checks the original visibility condition against the leaf-layer characterization, and checks the coefficients and facets by exhaustive vertex-subset testing in five parameter cases. It checks every forbidden internal-layer singleton separately, and computes boundary ranks over \(\mathbb F_2\) for three small topology cases. In total the tested leaf-support masks number \(12800\). Its successful terminal line is:

```text
VERIFY_OK cases=5 boundary_masks=12800 all_shortest_paths=PASS face_polynomials=PASS forbidden_interior_singletons=PASS mod2_homology=PASS
```

This finite computation corroborates but does not prove the all-parameter statement. The proof above establishes unrestricted validity and integral, rather than only mod-two, homotopy type.

## Relationship to prior work

Tian and Klavžar's 2022 preprint established the scalar identity \(\mu_{\mathrm t}(T\square H)=\mu_{\mathrm t}(T)\mu_{\mathrm t}(H)\), showing that a maximizing total mutual-visibility set lies in the leaf layers, and determined the scalar value for products of two complete graphs. Those facts and their supporting leaf-layer obstruction are prior results. The present claim classifies **every** feasible set by independent leaf choices, not just a largest one, and determines the entire labeled simplicial join. It then computes all face coefficients, all facet coefficients, and the integral homotopy of the particular rook-prism tree products. These stronger all-size and topological conclusions are not stated in their Theorem 4.5 or Proposition 4.3.

Kuziak and Rodríguez-Velázquez studied scalar total mutual-visibility bounds and product formulas in 2023, while Bujtás, Klavžar, and Tian studied Hamming products in 2023. The latter does not encompass a tree factor of order at least three; its \(K_2\)-factor boundary is explicitly excluded here. Bujtás, Klavžar, and Tian's later work introduced visibility polynomials and established a general distance-two characterization of feasible total mutual-visibility sets; that general criterion is acknowledged as background and may be used to rederive the rook-prism obstruction, but does not by itself state or enumerate this tree-leaf join or its integral homotopy type. Related lower-total-visibility results concern minimum sizes of maximal configurations, not these full polynomials. Existing indexed records on related product-visibility and graph-complex questions did not yield a directly covering theorem. An unindexed equivalent characterization remains possible.

## Limitations

The labeled-complex identity is asserted only for a tree with at least three vertices and a nontrivial connected second factor; it should not be applied to a two-vertex tree without a separate argument. The integral homotopy formula applies specifically to \(K_n\square K_2\) as the second factor; the general tree-leaf join holds for any connected \(H\), but no homotopy classification of arbitrary \(H\) is claimed. The finite verifier does not certify all parameters or provide an independent audit. Search results do not prove novelty or publication priority; a more general unindexed result might subsume the claim.

## References

1. Jing Tian and Sandi Klavžar, *Graphs with total mutual-visibility number zero and total mutual-visibility in Cartesian products*, arXiv:2212.07193, first public 2022-12-14, especially Proposition 4.3 and Theorem 4.5. https://arxiv.org/abs/2212.07193
2. Dorota Kuziak and Juan A. Rodríguez-Velázquez, *Total mutual-visibility in graphs with emphasis on lexicographic and Cartesian products*, arXiv:2306.15818, 2023. https://arxiv.org/abs/2306.15818
3. Csilla Bujtás, Sandi Klavžar, and Jing Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168, 2023. https://arxiv.org/abs/2307.05168
4. Csilla Bujtás, Sandi Klavžar, and Jing Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, 2024; *Aequationes mathematicae* 99 (2025), 1883–1901, especially Theorem 5.2. https://link.springer.com/article/10.1007/s00010-025-01197-y
5. Boštjan Brešar and Ismael G. Yero, *Lower (total) mutual-visibility number in graphs*, arXiv:2307.02951, 2023. https://arxiv.org/abs/2307.02951
