# Clique–simplicial-neighborhood formula for independent domination of central graphs

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph with at least one vertex. Its **central graph** \(\mathtt C(G)\) has the original vertices \(V\) and one new vertex \(w_e\) for each edge \(e\in E\); each \(w_{uv}\) is adjacent only to \(u,v\), while two distinct original vertices are adjacent in \(\mathtt C(G)\) exactly when they are nonadjacent in \(G\). Let \(D_i(H;z)\) be the cardinality polynomial of independent dominating sets of a graph \(H\). Define the family \(\mathcal K(G)\) of all vertex subsets inducing complete subgraphs, including \(\varnothing\), and put
\[
\mathcal S(G)=\{N_G(v):v\in V,\ G[N_G(v)]\text{ is complete}\},\qquad e_G(X)=|E(G[V\setminus X])|.
\]
Here \(\mathcal S(G)\) is a **set of distinct vertex subsets**: vertices having the same open neighborhood contribute just once.

**Theorem (all independent dominating sets).** Independent dominating sets of \(\mathtt C(G)\) are in canonical bijection with \(\mathcal K(G)\setminus\mathcal S(G)\). The bijection sends an eligible clique \(X\) to
\[
I_X=X\cup\{w_{uv}:uv\in E(G[V\setminus X])\}.
\]
Thus the complete polynomial, including every coefficient, is
\[
\boxed{\displaystyle D_i(\mathtt C(G);z)=\sum_{X\in\mathcal K(G)}z^{|X|+e_G(X)}-\sum_{X\in\mathcal S(G)}z^{|X|+e_G(X)}.}
\]
In particular,
\[
\boxed{\displaystyle D_i(\mathtt C(G);1)=|\mathcal K(G)|-|\mathcal S(G)|.}
\]
The correction counts distinct open neighborhoods of simplicial vertices, not individual simplicial vertices.

**Triangle-free corollary.** If \(G\) is triangle-free with minimum degree at least two, order \(n\), and size \(m\), then \(\mathcal S(G)=\varnothing\) and every clique has at most two vertices. Hence
\[
\boxed{\displaystyle D_i(\mathtt C(G);z)=z^m+\sum_{v\in V}z^{m+1-d_G(v)}+\sum_{uv\in E}z^{m+3-d_G(u)-d_G(v)},\qquad D_i(\mathtt C(G);1)=1+n+m.}
\]
For a triangle-free \(d\)-regular graph with \(d\ge2\), this becomes \(z^m+n z^{m+1-d}+m z^{m+3-2d}\). Thus all connected triangle-free cubic graphs of the same order have the same independent-domination polynomial after centralization, despite possibly having different graph structures.

**Complete multipartite corollary.** For \(G=K_{a_1,\ldots,a_r}\), \(r\ge2\), all \(a_i\ge1\), write \(\mathbf1_{i\in T}\) for the selection indicator and let \(c(\mathbf a)\) equal zero if at least two parts have size greater than one, one if exactly one part does, and \(r\) if none does. Then
\[
\boxed{\displaystyle D_i(\mathtt C(G);z)=\sum_{T\subseteq[r]}\!\left(\prod_{i\in T}a_i\right)z^{|T|+\sum_{i<j}(a_i-\mathbf1_{i\in T})(a_j-\mathbf1_{j\in T})}-c(\mathbf a)z^{r-1}.}
\]
Consequently \(D_i(\mathtt C(G);1)=\prod_i(1+a_i)-c(\mathbf a)\).

## Assumptions and scope

Graphs are finite, loopless, undirected and without multiple edges. Connectivity is not required, and isolated vertices are allowed. The open neighborhood \(N_G(v)\) is the set of neighbors of \(v\) in the base graph. An independent dominating set is a pairwise nonadjacent vertex set that dominates all other vertices. A simplicial vertex is one whose open neighborhood induces a complete graph; the empty neighborhood is permitted. A clique is any complete vertex subset, including the empty set. \(\mathcal S(G)\) is explicitly a set, so equal neighborhoods cannot lead to double subtraction. All vertex subsets are labelled, and the polynomial counts sets, not automorphism orbits.

## Proof

Fix an independent dominating set \(I\subseteq V(\mathtt C(G))\), and let \(X=I\cap V\). Two original vertices are adjacent in \(\mathtt C(G)\) if and only if they are not adjacent in \(G\); independence of \(I\) therefore forces \(X\in\mathcal K(G)\).

Every subdivision vertex \(w_{uv}\) has exactly its two original endpoints as neighbors in \(\mathtt C(G)\). If an endpoint lies in \(X\), then independence forbids \(w_{uv}\in I\), and that subdivision vertex is dominated by the selected endpoint. If neither endpoint lies in \(X\), then \(w_{uv}\) has no selected neighbor (subdivision vertices have no edges between them); domination forces \(w_{uv}\in I\). Thus \(I=I_X\), so there is at most one independent dominating set with a given original-vertex intersection \(X\).

For \(v\in V\setminus X\), adjacency to some selected original vertex holds precisely if \(v\) has a nonneighbor in \(X\) in the base graph. Adjacency to a selected subdivision vertex holds precisely if \(v\) has a neighbor in \(V\setminus X\). Hence \(v\) is undominated precisely when neither condition holds, that is, when \(N_G(v)=X\). Therefore \(I_X\) is independent and dominating if and only if no vertex outside \(X\) has open neighborhood exactly \(X\). Because \(v\notin N_G(v)\) for loopless graphs, the excluded candidate cliques are exactly the distinct clique neighborhoods \(\mathcal S(G)\). This proves the bijection and the weighted subtraction formula, including all boundary cases with isolated vertices.

For triangle-free \(G\) with minimum degree at least two, every vertex has at least two mutually nonadjacent neighbors, so no vertex is simplicial and \(\mathcal S(G)=\varnothing\). Its cliques are precisely the empty set, singleton vertices and adjacent pairs. The retained edges number \(m\), \(m-d_G(v)\), and \(m-d_G(u)-d_G(v)+1\), respectively, proving the triangle-free formula. The coefficient sum at \(z=1\) is \(1+n+m\).

For the multipartite corollary, every clique chooses at most one vertex from each part. Choosing parts \(T\) gives \(\prod_{i\in T}a_i\) distinct cliques and leaves \(a_i-\mathbf1_{i\in T}\) vertices in part \(i\), yielding the stated exponent. A vertex in part \(i\) is simplicial exactly when every other part is a singleton; if there are at least two nonsingleton parts there are no such vertices. If there is exactly one nonsingleton part, all its vertices share the same clique neighborhood, comprising every singleton part. If all parts are singletons, the graph is complete and its \(r\) simplicial vertices have distinct neighborhoods. Each forbidden clique leaves no original edge, and has \(r-1\) vertices. Thus the correction is exactly \(c(\mathbf a)z^{r-1}\). All claims follow.

## Verification

The standalone `verify.py` uses only the Python standard library. Running `python verify.py` builds the central graph from each tested base graph, enumerates independent dominating sets using the original adjacency definition, independently enumerates eligible cliques, and checks all polynomial coefficients. It covers all 75 labelled graphs on one through four vertices, 20 seeded connected random graphs of orders five and six, all 112 tested multipartite size profiles and direct examples, and all 560 tested triangle-free labelled graphs with minimum degree at least two through six vertices. The asserted `VERIFY_OK` output was observed on the actual standalone source. The mathematical proof above, rather than these finite tests, establishes the unrestricted statements.

## Relationship to prior work

Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz, *Independent domination in central graphs* (arXiv:2609.16357v1, first submitted 14 September 2026), give an optimization formula for the **minimum size** of an independent dominating set of a central graph (Theorem 2.1) and further minimum-size results. Their minimization uses cliques and a test for vertices whose neighborhood equals a candidate clique. The present claim upgrades this to a bijection for **every** independent dominating set and a complete cardinality polynomial, with distinct-neighborhood correction and the broad triangle-free counting law. Their work is a close conceptual antecedent, so the extension should not be described as independent of that insight.

Dod, *The Independent Domination Polynomial* (arXiv:1602.08250v1), and Jahari and Alikhani, *On the independent domination polynomial of a graph* (arXiv:1808.07369v3), study the general counting polynomial, with universal identities and formulas for other graph constructions. Their generic polynomial identities can in principle be evaluated on a central graph but do not directly identify its original-graph clique correspondence, simplicial-neighborhood correction, or universal triangle-free coefficients. A public finding on higher iterated central graphs gives independent-domination **numbers** for later iterates, not these first-iterate cardinality distributions. A separate public finding concerns **total domination**, a different predicate.

## Limitations

The exact clique sum may be exponentially large and is not a polynomial-time algorithm for arbitrary graphs. The value of this result is the all-set structural reduction and consequences, not a claimed complexity breakthrough. The article arXiv:2609.16357 was accessible in HTML through most of its results, including the principal minimization theorem, but later text could not be reopened; a residual priority risk remains that an equivalent all-set statement is present in material not retrieved. No claim of an independent audit or of established publication priority is made. Finite experiments support but do not replace the proof.

## References

1. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, A. Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357v1 (14 September 2026). https://arxiv.org/abs/2609.16357
2. M. Dod, *The Independent Domination Polynomial*, arXiv:1602.08250v1 (26 February 2016). https://arxiv.org/abs/1602.08250
3. S. Jahari, S. Alikhani, *On the independent domination polynomial of a graph*, arXiv:1808.07369v3 (2018). https://arxiv.org/abs/1808.07369
4. *Independent domination of higher iterated central graphs*, publicly accessible mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-iterated-central-graph-independent-domination--7dc2104ad847
5. *Exact vertex-cover formula for total domination of central graphs*, publicly accessible mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-exact-total-domination-formula-central-graphs--f6679e0fe594
