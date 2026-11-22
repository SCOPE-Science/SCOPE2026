# Matching-fault simple-homotopy invariance of the Heawood dominance complex

## Finding
Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane. For a finite graph \(G\), let \(\mathcal D(G)\) be its **dominance complex**: its faces are the vertex subsets whose complements dominate \(G\). Let \(M\subseteq E(H)\) be an arbitrary graph-edge matching, including the empty matching or a matching that does not extend to a perfect matching.

**Theorem.** For every such \(M\), and every \(e\in M\), there is an explicit finite sequence of elementary simplicial collapses
\[
\mathcal D\bigl(H-(M\setminus\{e\})\bigr)\searrow\mathcal D(H-M).
\]
Consequently, for any nested matchings \(M\subseteq M'\), the canonical inclusion
\[
\mathcal D(H-M')\hookrightarrow\mathcal D(H-M)
\]
is a simple-homotopy equivalence (indeed a sequence of inverse elementary collapses). All of these complexes have the integral homotopy type \(S^6\), and the displayed inclusions induce isomorphisms on **all integral homology groups**. In particular, their unique reduced homology group is \(\widetilde H_6\cong\mathbb Z\), with all its classes persisting under any order of independent edge deletions from a matching.

The graph has \(21\) edges and \(3{,}462\) matchings, of which \(1{,}260\) cannot be extended to any perfect matching. At most \(7\) graph edges can be deleted this way, exactly one third of the original edges. The theorem includes all \(24\) perfect matchings, all \(336\) six-edge matchings, and all smaller matchings; it is not limited to a prescribed edge order.

## Assumptions and scope
Let the point vertices be \(P_0,\ldots,P_6\) and the line vertices be \(L_0,\ldots,L_6\), with indices modulo \(7\) and adjacency
\[
P_i L_j\in E(H)\quad\Longleftrightarrow\quad (j-i)\bmod7\in\{0,1,3\}.
\]
Vertices are indexed as integers \(0,\ldots,13\) in point-first order. The graph is undirected and loopless. A matching is a set of pairwise vertex-disjoint edges. The graph \(H-M\) retains all \(14\) vertices and omits precisely the edges of \(M\). For every graph \(G\) on this vertex set, the face test is
\[
S\in\mathcal D(G)\quad\Longleftrightarrow\quad
N_G[v]\not\subseteq S\ \text{for every vertex }v.
\]
Equivalently, each vertex \(v\in S\) has at least one neighbor outside \(S\). With more edges deleted, the dominance complex **shrinks**; the inclusions above have the stated direction. Elementary collapse means removing a simplex and its unique codimension-one free face, producing a deformation retraction and a simple-homotopy equivalence.

## Proof
**1. Exact matching universe.** Build a bit-mask list of the \(21\) edges in lexicographic order. Start with the empty matching. Process each edge exactly once, either not selecting it or adjoining it to any previously constructed matching disjoint from its endpoints. Induction on the processed edge prefix proves every matching is reached, and each is a matching. The complete histogram by matching cardinality \(0,1,\ldots,7\) is
\[
(1,21,168,644,1218,1050,336,24),
\]
which sums to \(3{,}462\). Comparing each matching with the \(24\) seven-edge matchings identifies exactly \(1{,}260\) nonextendible matchings. These figures are exhaustively checked by the supplied standalone verifier.

**2. Exhaustive symmetry reduction, with no unverified orbit assumption.** The seven line triples are the translates of the Fano difference set \(\{0,1,3\}\). Enumerating all \(7!=5040\) point permutations and keeping exactly those mapping every line triple to a line triple gives \(168\) distinct point–line collineations, each uniquely extended to the incidence graph. Composing these with the explicit point–line polarity
\[
P_i\longleftrightarrow L_{-i}
\]
yields \(336\) distinct permutations of the graph vertices, and each sends every edge to an edge; the verifier reconstructs and checks the edge permutations. Since the graph is connected bipartite with uniquely determined shores, any automorphism either preserves or swaps the shores. A shore-preserving automorphism must be a Fano collineation, so these \(336\) permutations are the full graph automorphism group.

Acting on edge-bit masks with these \(336\) permutations partitions all \(3{,}462\) matchings into precisely \(30\) disjoint orbits, with \(1,1,2,6,8,7,4,1\) orbits at matching sizes \(0,1,\ldots,7\). The verifier checks that each computed orbit lies inside the full matching set, that different orbits are disjoint, and that their union is the full matching set. Thus checking every edge of every nonempty orbit representative will cover every possible one-edge matching-deletion transition, since graph automorphisms transport both dominance complexes and elementary simplicial collapses.

**3. Every representative transition is an actual elementary collapse.** For a missing-edge bit mask \(m\), reconstruct the adjacency array after deleting exactly those graph edges and enumerate **every** one of the \(2^{14}\) possible vertex masks \(s\). Keep \(s\) if every chosen vertex has a neighbor outside \(s\). This tests the defining domination condition exactly, rather than estimating homology. Write \(B=\mathcal D(H-(M\setminus\{e\}))\) and \(A=\mathcal D(H-M)\), so \(A\subseteq B\).

Consider the set \(R=B\setminus A\) of simplices outside the target. Because \(A\) is a subcomplex, every coface in \(B\) of a simplex in \(R\) also lies in \(R\). Initialize an explicit list of the immediate cofaces of every simplex in \(R\). Whenever an active simplex \(s\) has exactly one active immediate coface \(t\), remove the pair \(s,t\). This is a genuine elementary simplicial collapse: if a larger coface of \(s\) existed, adjoining one vertex of that larger coface distinct from the vertex in \(t\) would give another immediate coface. Moreover, none of its cofaces can have been hidden inside \(A\). Maintain the coface data exactly after each removal until no such pair remains. A complete disappearance of \(R\) is therefore an explicit certificate that \(B\searrow A\).

For the \(30\) representative matchings, testing every one of their matching edges gives \(121\) distinct representative transitions, distributed by size \(1,\ldots,7\) as \((1,4,18,32,35,24,7)\). The free-face algorithm removes **all** relative simplices in all \(121\) cases, using \(28{,}910\) elementary pairs in total across these cases. In every case the face difference contains exactly twice the number of removed pairs and the residual set is empty. No rank test, numerical approximation or inference from a failed algorithm is used. By the exact symmetry coverage from Step 2, this proves the first theorem statement for every matching and every edge of that matching. Composing the elementary collapses proves the nested-matching assertion.

**4. Anchor homotopy and integral persistence.** For completeness, the verifier also reconstructs the intact complex \(\mathcal D(H)\) from the same adjacency definition. It contains \(8{,}851\) faces including the empty face. Perform the standard vertex-toggle matching successively at each of the fourteen vertices: pair an unmatched face not containing the current vertex with its one-vertex extension if both are still unmatched. After discarding the empty-face/point-vertex pair, the ordinary nonempty face poset has \(4{,}424\) matched pairs, one critical vertex and one critical six-simplex. Direct every unmatched Hasse relation downward and each matched relation upward. An exhaustive topological sort checks all \(52{,}304\) relations among all \(8{,}850\) nonempty faces and visits every node, so the matching is acyclic. Forman's discrete-Morse theorem therefore gives a CW model with one zero-cell and one six-cell, homotopy equivalent to \(S^6\). Every inclusion in the theorem is an elementary-collapse equivalence and therefore induces an integral homology isomorphism, proving the homotopy and persistence conclusions.

## Verification
The accompanying `verify_heawood_matching_collapse.py` is a standard-library-only Python 3 verifier. Run it with `python3 verify_heawood_matching_collapse.py`. It constructs the graph, the full face poset and its acyclic Morse matching, enumerates all matchings, enumerates all graph automorphisms and orbit representatives, and **reconstructs every relative face-poset collapse rather than trusting a precomputed log**. The recorded output `verification_output.txt` documents one successful execution, but the complete executable check is the actual finite certificate. As a boundary test, the same implementation independently verifies that deleting a single edge of the seven-cycle changes the Euler characteristic of its dominance complex from \(0\) to \(2\); such edge-fault invariance is not universal for graphs.

## Relationship to prior work
Matsushita and Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals* (arXiv:2312.02639, first posted 2023-12-05), define the dominance complex and identify its combinatorial Alexander dual with the open-neighborhood complex of the complement graph. That general duality is not a claim of this result; their published calculations concern cycles, chordal examples, and graph products and do not establish collapse maps for Heawood matching faults. Their transformation to a different independence complex would require a new computation for each deleted matching to imply this theorem.

Two separately available Heawood-specific computations, *The Heawood dominance complex is a six-sphere with orientation-preserving full symmetry* and *The Heawood dominance complex is a six-sphere with trivial full symmetry action*, already prove the intact sphere type and its symmetry behavior. Those pre-existing results are fully credited and are **not claimed as new**. Knowing only \(\mathcal D(H)\simeq S^6\), even with a primitive cycle or a full character, does not imply that any strict subcomplex \(\mathcal D(H-M)\) is homotopy equivalent or that its inclusion is an elementary collapse. The new result is precisely the universal matching-fault **relative** collapse and consequent natural integral persistence statement, backed by all matching orbits.

Related matching-deletion results for bipartite *dissociation complexes* and matching complexes describe different face conditions, so their individual homotopy classifications do not cover this dominance-complex inclusion theorem. Neither an exact alternate formulation nor a stronger covering statement was located in targeted searches; this is a best-knowledge bibliographic assessment rather than a claim that all literature has been exhausted.

## Limitations
The theorem concerns only the Fano-plane incidence graph, and only edge sets forming matchings. It makes no assertion about arbitrary sets of deleted edges, arbitrary cubic bipartite graphs, or higher-order projective planes. It does not claim an **equivariant** choice of each collapse: group automorphisms are used to transport non-equivariant exact certificates. The barcode has one essential reduced degree-six class for any monotone choice of matching-deletion stages, but this does not classify metric, clique or other graph filtrations. Although the finite certificate is exhaustive and replayable, it has not been independently mathematically audited. An inaccessible or unindexed equivalence in the literature is a residual originality risk.

## References
1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first publicly posted 2023-12-05, https://arxiv.org/abs/2312.02639 and full text https://arxiv.org/html/2312.02639v2.
2. *The Heawood dominance complex is a six-sphere with orientation-preserving full symmetry*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-heawood-dominance-complex-is-a-six-sphere-with-orientation-p--12927407d989.
3. *The Heawood dominance complex is a six-sphere with trivial full symmetry action*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-heawood-dominance-complex-is-a-six-sphere-with-trivial-full--9a17eecfb344.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
