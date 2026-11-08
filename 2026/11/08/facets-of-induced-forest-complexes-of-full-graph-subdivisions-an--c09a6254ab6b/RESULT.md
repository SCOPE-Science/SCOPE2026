# Facets of induced-forest complexes of full graph subdivisions and an exact Cayley spectrum

## Finding
Let \(G\) be any finite, simple, undirected graph with at least one vertex. Write \(S(G)\) for its **full one-subdivision**, in which every edge \(e=uv\) is replaced by the path \(u-s_e-v\). An **induced-forest facet** is a vertex subset maximal under inclusion subject to inducing an acyclic graph. Its complement is an inclusion-minimal feedback vertex set.

**Theorem (subdivision facet criterion).** The complete set of induced-forest facets of \(S(G)\) is in bijection with the pairs \((A,F)\) satisfying the following conditions:

1. \(A\subseteq V(G)\), and \(F\subseteq E(G[A])\) restricts to a spanning tree in every connected component of \(G[A]\) (including isolated one-vertex components, with empty tree edge set).
2. For every \(x\in V(G)\setminus A\), at least two distinct neighbors of \(x\) are in the same connected component of \(G[A]\).

The corresponding facet is precisely
\[
U(A,F)= A\ \cup\ \{s_e:e\notin E(G[A])\}\ \cup\ \{s_e:e\in F\}.
\]

**Corollary (complete graphs).** For every integer \(n\ge3\), put \(N=\binom n2\). The polynomial enumerating all inclusion-maximal induced forests of \(S(K_n)\), weighted by selected-vertex cardinality, equals
\[
Q_n(z)=\sum_{a=2}^{n}\binom na a^{a-2}z^{N+2a-1-\binom a2}.
\]
The polynomial counting all inclusion-minimal feedback vertex sets of \(S(K_n)\), weighted by cardinality, is
\[
R_n(z)=z^{n+N}Q_n(1/z)
=\sum_{a=2}^{n}\binom na a^{a-2}z^{n-2a+1+\binom a2}.
\]
The minimum and maximum cardinalities in \(R_n\) are, respectively, \(n-2\) and \(\binom{n-1}{2}\). The number of minimum-size feedback vertex sets is \(\binom n2+3\binom n3\); for \(n\ge4\), the number of inclusion-minimal feedback vertex sets of the largest size is \(n^{n-2}\). The induced-forest complex of \(S(K_n)\) is pure exactly when \(n=3\) in the stated domain, and the gaps between successive possible facet sizes are unbounded as \(n\) grows.

## Assumptions and scope
All graphs are finite, simple and undirected. A subdivision vertex \(s_e\) is distinct for each original edge. The empty tree on an isolated selected original vertex is allowed. A feedback vertex set is *minimal* in the inclusion sense; it need not have minimum cardinality. The general characterization allows disconnected graphs and isolated vertices, while the closed Cayley polynomial assumes \(n\ge3\).

## Proof
**1. Forest test.** For an arbitrary vertex set \(U\subseteq V(S(G))\), put \(A=U\cap V(G)\), and let \(F\) consist of those original edges \(e\in E(G[A])\) whose subdivision vertices lie in \(U\). A selected subdivision vertex incident with at most one selected original vertex is isolated or a leaf in the induced subgraph and cannot participate in any cycle. Every remaining selected subdivision vertex has two original endpoints in \(A\). Suppressing these degree-two subdivision vertices identifies the cycles of \(S(G)[U]\) exactly with the cycles of \((A,F)\). Thus \(U\) is a forest if and only if \((A,F)\) is acyclic.

**2. Subdivision vertices forced by maximality.** If \(e\notin E(G[A])\), adding \(s_e\) to a forest adds an isolated vertex or leaf, so every facet must contain it. Among internal edges, an omitted \(s_e\) can be added without creating a cycle precisely when its endpoints lie in distinct components of the selected forest \((A,F)\). Consequently the selected internal edges are inclusion-maximal acyclic within \(E(G[A])\), hence form a spanning tree in each connected component of \(G[A]\). Conversely, with these choices, adding any omitted internal subdivision vertex creates a cycle.

**3. Original vertices forced by maximality.** Let \(x\notin A\). All subdivision vertices on edges incident with \(x\) are already selected by Step 2. After adding \(x\), a cycle appears precisely when two of its neighbors in \(A\) are joined by a selected path through \((A,F)\). Because \((A,F)\) spans each component of \(G[A]\), this is equivalent to two distinct neighbors of \(x\) lying in one connected component of \(G[A]\). Every omitted original vertex must satisfy this condition, proving necessity and sufficiency of the theorem.

**4. Complete graph classification.** Suppose \(G=K_n\) with \(n\ge3\). If \(|A|\le1\), any omitted old vertex has fewer than two neighbors in \(A\), so the facet condition fails. For every \(a=|A|\ge2\), the graph \(G[A]\) is connected and every outside old vertex has at least two neighbors in it, so the condition holds automatically. Thus facets are specified by choosing \(A\) of size \(a\) and a labelled spanning tree of \(K_a\). Cayley's formula gives exactly \(a^{a-2}\) trees, hence \(\binom na a^{a-2}\) facets of that type.

Every such facet contains \(a\) old vertices, \(N-\binom a2\) subdivisions of noninternal edges, and \(a-1\) subdivisions of tree edges. Its cardinality is \(N+2a-1-\binom a2\), proving \(Q_n\). Taking complements inside the \(n+N\) vertices proves \(R_n\).

**5. Extremes and nonpurity.** Write \(f_n(a)=N+2a-1-\binom a2\) for \(2\le a\le n\). Then \(f_n(2)=f_n(3)=N+2\) and, whenever \(a\ge3\),
\[
f_n(a+1)-f_n(a)=2-a.
\]
Thus the largest facet size is \(N+2\), attained at \(a=2,3\), and the smallest is \(f_n(n)=2n-1\). The complementary minimum and largest *minimal* feedback vertex set sizes are \(n-2\) and \(N-n+1=\binom{n-1}{2}\). At \(n=3\) all facets have size \(5\), and for every \(n\ge4\) the \(a=4\) facets are smaller than the \(a=2,3\) facets, proving nonpurity. As \(a\) grows, the differences between successive facet sizes increase without bound. Summing the tree multiplicities for \(a=2,3\) yields \(\binom n2+3\binom n3\). For \(n\ge4\), only \(a=n\) gives the smallest facet, with \(n^{n-2}\) possibilities. This completes the proof.

## Verification
A standalone verifier (`verify.py`) independently enumerates all original graphs on at most four labelled vertices, constructs each full subdivision directly, detects cycles of every selected induced subgraph, and compares every inclusion-maximal induced forest with the proposed structural rule. It additionally exhausts all vertex subsets of \(S(K_5)\), comparing each facet with its closed Cayley polynomial. The successful execution reported:

```text
VERIFY_OK labeled_base_graphs_and_cliques=76 full_subsets=44662 maximal_induced_forests=555 predicted_facets=PASS cycle_detection=PASS Cayley_cardinality=PASS size_extremes_n3to12=PASS
```

The exhaustive range is finite. The all-graph and all-\(n\) statements are proved in the preceding paragraphs, not by this computation.

## Relationship to prior work
The 2022 work of Gaikwad and collaborators and the 2023 work of Lampis, Melissinos and Vasilakis study the maximum-cardinality *minimal* feedback vertex set problem and its parameterized complexity, including the standard private-cycle characterization. The 2023 work of Gunderson, Meagher, Morris and Pantangi studies maximum induced forests of several distance-regular families. None of the inspected material states the facet characterization of graph one-subdivisions or its complete Cayley-weighted cardinality distribution. General feedback-vertex-set algorithms and the classical Cayley tree count are acknowledged as prerequisites, not claimed as new.

## Limitations
The originality assessment is based on consulted literature and accessible prior research records and does not establish publication priority. An equivalent characterization under incidence graphs, subdivision graphs, graphic matroids or minimal cycle transversals could exist elsewhere. The special-case enumeration derives from the classical Cayley formula; its proposed contribution is the explicit graph-complex classification and its exact feedback-vertex-set spectrum. Independent mathematical review is not represented by this report. No topological homotopy type or algorithmic running-time improvement is claimed.

## References
1. A. Gaikwad, H. Kumar, S. Maity, S. Saurabh and S. K. Tripathi, *Maximum Minimal Feedback Vertex Set: A Parameterized Perspective*, arXiv:2208.01953v1, first posted 2022-08-03. https://arxiv.org/abs/2208.01953
2. K. Gunderson, K. Meagher, J. Morris and V. R. T. Pantangi, *Induced forests in some distance-regular graphs*, arXiv:2301.05207v1, first posted 2023-01-12. https://arxiv.org/abs/2301.05207
3. M. Lampis, N. Melissinos and M. Vasilakis, *Parameterized Max Min Feedback Vertex Set*, MFCS 2023, DOI:10.4230/LIPIcs.MFCS.2023.62, published 2023-08-21. https://doi.org/10.4230/LIPIcs.MFCS.2023.62
4. A. Cayley, classical labelled-tree enumeration \(a^{a-2}\), used without a novelty claim.
