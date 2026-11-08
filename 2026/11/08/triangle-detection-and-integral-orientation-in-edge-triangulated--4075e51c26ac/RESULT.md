# Triangle detection and integral orientation in edge-triangulated clique-free complexes

## Finding

Let \(F\) be any finite simple graph with \(n\ge2\) vertices, no isolated vertices and at least one edge. Form its **edge-triangulation** \(T(F)\) by retaining every edge \(uv\) of \(F\), and introducing one new vertex \(w_{uv}\) adjacent precisely to \(u\) and \(v\) for each edge. Let \(X(F)=\operatorname{CF}_3(T(F))\) be the simplicial complex of subsets spanning no triangle. Then

\[
X(F)\simeq_s
\begin{cases}
 S^{n-1},&F\text{ has no triangle},\\
 \{\mathrm{pt}\},&F\text{ contains a triangle}.
\end{cases}
\]

Here \(\simeq_s\) means **simple-homotopy equivalence**. The sphere assertion for triangle-free \(F\) is a direct application of Ehrenborg--Hetyei (2006), Proposition 4.3, and **is not claimed as a new standalone result**. The new classification aspect is the uniform triangle-triggered collapse with one explicit contractible edge, together with the following integral equivariant refinement.

The natural action of \(\operatorname{Aut}(F)\) on \(T(F)\) induces, when \(F\) is triangle-free, the **full top reduced integral homology representation**

\[
\widetilde H_{n-1}(X(F);\mathbb Z)\cong\mathbb Z_{\operatorname{sgn}_{V(F)}}.
\]

This means each automorphism \(g\) acts by the sign of its permutation of the **original** vertices of \(F\). Its action on the new edge vertices cancels from the final character, regardless of the number of edges and of connectivity. All other reduced integral homology groups vanish. When \(F\) contains a triangle, all reduced integral homology and all induced reduced homology representations vanish. Thus the ordinary homotopy type detects whether the base graph contains a triangle, while the residual sphere's orientation remembers precisely the parity of the original-vertex permutation.

## Assumptions and scope

Graphs are finite, undirected and simple. The base graph \(F\) has no isolated vertices. Distinct edges receive distinct new vertices; new vertices are adjacent only to their original endpoints, and not to one another. For an integer \(r\ge2\), the \(r\)-clique-free complex \(\operatorname{CF}_r(G)\) has as faces all vertex subsets inducing no complete subgraph \(K_r\); only \(r=3\) is addressed. Reduced homology uses integer coefficients. The indicated \(\operatorname{Aut}(F)\)-action preserves the original and new vertices and carries \(w_{uv}\) to \(w_{g(u)g(v)}\). Extra graph automorphisms that do not preserve this designated decomposition are not classified.

## Proof

**1. Complete list of minimal nonfaces.** Set \(V=V(F)\), \(E=E(F)\), \(m=|E|\), and \(W=V\sqcup\{w_e:e\in E\}\). The triangles of \(T(F)\) are exactly the \(m\) private-edge triangles \(C_e=e\cup\{w_e\}\) and the original triangles \(B\subseteq V\) of \(F\). Indeed a new vertex has exactly its two original edge endpoints as neighbors and no other new vertex as a neighbor. These triangles are exactly the minimal nonfaces of \(X(F)\). Each private vertex \(w_e\) occurs in exactly one minimal nonface. Every original vertex occurs in at least one \(C_e\), since there are no isolated vertices.

**2. Triangle-free branch (prior pointed-complex theorem).** If \(F\) is triangle-free, the \(C_e\) are the complete circuit family, each with its private pointed vertex \(w_e\). Their union is all \(W\). The pointed-complex sphere theorem of Ehrenborg--Hetyei, Proposition 4.3, applies on \(n+m\) vertices with \(m\) circuits. It yields a simple-homotopy sphere of dimension \((n+m)-m-1=n-1\). For \(F=K_2\), this is also directly the boundary of a two-simplex, hence \(S^1\).

**3. Triangle-containing branch, one edge contraction.** Suppose \(a,b,c\in V\) form a triangle. Write \(p=w_{ab}\), \(q=w_{ac}\). Both \(p,q\) occur in exactly one circuit, in \(C_{ab}=\{a,b,p\}\) and \(C_{ac}=\{a,c,q\}\), respectively, and no circuit contains both. By Ehrenborg--Hetyei, Lemma 3.1 and Theorem 2.4, the simplicial edge \(\{p,q\}\) is contractible and contracting it to a vertex \(z\) is a simple-homotopy equivalence. The explicit circuit-contraction formula, their Lemma 3.2, shows that the **only possible new forbidden block containing** \(z\) is \(\{a,b,c,z\}\): it comes from joining \(C_{ab}\) and \(C_{ac}\). But the old circuit \(\{a,b,c\}\) remains and makes this larger block redundant. Therefore \(z\) lies in **no minimal nonface** of the contracted complex; it is a cone apex. A cone collapses to one vertex. Consequently \(X(F)\) is simple-homotopy equivalent to a point. This argument works for arbitrary other triangles, chords, components and cycles in \(F\).

**4. Integral orientation character in the triangle-free branch.** Assume first \(m\ge2\) and no original triangle. Let \(N=n+m\). The combinatorial Alexander dual \(X(F)^\vee\) has the \(m\) facets \(\Delta(W\setminus C_e)\), indexed by edges of \(F\). Every proper subfamily has nonempty intersection because an omitted private vertex \(w_f\) lies in every retained facet; the intersection of all \(m\) facets is empty because \(\bigcup_e C_e=W\). Every nonempty intersection is a simplex. Thus the nerve is the boundary of the \((m-1)\)-simplex on the edge index set \(E\). The standard natural nerve comparison (equivalently the simplicial Mayer--Vietoris/Čech double complex) identifies its integral top homology character with the sign of the edge permutation: \(\operatorname{sgn}_E(g)\).

Combinatorial Alexander duality is natural **with an ambient orientation twist** under permutations of the \(N\) ambient vertices. The induced action on the corresponding rank-one homology of \(X(F)\) is therefore

\[
\operatorname{sgn}_{W}(g)\operatorname{sgn}_{E}(g)
=\big(\operatorname{sgn}_{V}(g)\operatorname{sgn}_{E}(g)\big)\operatorname{sgn}_{E}(g)
=\operatorname{sgn}_{V}(g).
\]

The first equality accounts for the permutation of original and private vertices; the second uses that the private-vertex permutation is exactly the edge permutation. This is an **integral** one-dimensional representation, not merely a rational trace identity. For \(m=1\), necessarily \(F=K_2\), and the direct triangular boundary model verifies the same sign action under the nontrivial automorphism. Steps 2--4 establish the claim for every permitted graph.

## Verification

A standalone Python checker `verify.py` enumerates all triangles of the expanded graph and all faces of the clique-free complex independently of the proof. It computes exact mod-two simplicial boundary ranks for ten base graphs (both disconnected and cyclic, both triangle-free and triangle-containing) and checks the predicted Betti numbers. It further enumerates signed fixed faces to calculate the reduced Lefschetz number for fourteen explicitly listed automorphisms, verifying \((-1)^{n-1}\operatorname{sgn}_V(g)\) in the sphere branch and zero in the contractible branch. These finite checks corroborate, but do not establish, the unrestricted theorem; the proof uses the complete circuit description and natural duality, with the contractible branch certified by the explicit edge contraction.

Run `python3 verify.py` using Python's standard library. The expected terminal record is supplied as `VERIFY_OUTPUT.txt` and ends in `ALL_VERIFY_OK`.

## Relationship to prior work

Ghosh--Selvaraja (2026, arXiv:2602.09623v1) investigate \(t\)-clique-free complexes and shellability under vertex-based clique attachment and clique vertex-partition whiskering. Their definitions motivate the present topological question; their Theorems 4.2 and 4.9 concern distinct attachments and do not state this edge-triangulation classification or its integral orientation character. Ehrenborg--Hetyei (2006) provide the pointed-complex sphere theorem, the edge-contraction formula and Alexander duality framework used here. **The triangle-free sphere type is subsumed by their Proposition 4.3**, and its numerical homology is not presented as original. Their general contraction lemma is explicitly credited for the triangle-triggered step; the present result identifies a graph-theoretic condition making that contraction decisive for every base graph and determines the natural integral symmetry character. Indexed records on cut complexes, robust clique complexes and unrelated graph automorphism characters address different complexes and do not yield this combined statement.

## Limitations

The construction adds exactly one degree-two vertex per retained base edge. Isolated base vertices are excluded: they would become cone apices and destroy the stated sphere branch. The theorem is for three-clique-free complexes, not arbitrary higher-clique-free or ordinary graph-independence complexes. The claim classifies the natural action of base-graph automorphisms, not possible additional automorphisms of the expanded graph. The proof does not assert the original contractible complex has a sequence of elementary collapses without first permitting an edge contraction, nor that its homotopy equivalence is an equivariant one. Independent review has not been conducted.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, first publicly posted 2026-02-10, arXiv:2602.09623v1, https://arxiv.org/html/2602.09623v1.
2. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906--923; first available online 2005-11-28; https://www.ms.uky.edu/~jrge/Papers/Independence.pdf, DOI 10.1016/j.ejc.2005.04.010. Relevant results: Theorem 2.4, Lemmas 3.1 and 3.2, Proposition 4.3, and Section 8.
3. Standard simplicial nerve comparison and integral combinatorial Alexander duality, in the orientation-natural formulation described in the proof.
