# A primitive four-sphere edge-fault splitting for the Petersen dominance complex

## Finding
For the Petersen graph \(P=\mathrm{KG}(5,2)\) and each one of its fifteen edges \(e\), the natural simplicial inclusion
\[
\mathcal D(P-e)\hookrightarrow\mathcal D(P)
\]
has the homotopy type of the standard inclusion of \(\bigvee^7 S^4\) into \(\bigvee^{11}S^4\) as a wedge summand. Thus
\[
|\mathcal D(P-e)|\simeq\bigvee^7S^4,\qquad |\mathcal D(P)|\simeq\bigvee^{11}S^4,
\]
and the inclusion induces a split injection \(\widetilde H_4(\mathcal D(P-e);\mathbb Z)\simeq\mathbb Z^7\hookrightarrow\mathbb Z^{11}\simeq\widetilde H_4(\mathcal D(P);\mathbb Z)\) with primitive image and cokernel \(\mathbb Z^4\). Its homotopy cofiber is \(\bigvee^4S^4\). The statement is uniform over all edges and asserts the natural inclusion maps, not merely individual Betti numbers.

## Assumptions and scope
The vertices of \(P\) are the ten two-element subsets of \(\{0,1,2,3,4\}\), ordered lexicographically, with two adjacent exactly when disjoint. For a finite simple graph \(G\), write \(N_G[v]\) for its closed neighborhood and define
\[
\mathcal D(G)=\{S\subseteq V(G):N_G[v]\nsubseteq S\text{ for every }v\in V(G)\}.
\]
Equivalently, the complement of every face is a dominating set. We consider the geometric realization of this abstract simplicial complex; the graph edge \(e\) is removed while keeping all ten graph vertices. Edge deletion decreases closed neighborhoods, so \(\mathcal D(P-e)\) is a subcomplex of \(\mathcal D(P)\).

## Proof
We provide an exact finite, reproducible discrete-Morse proof, applicable to every edge by symmetry. Lexicographically enumerate the two-subsets as \(v_0,\ldots,v_9\); the fifteen edges are pairs of disjoint labels. Take \(e=\{v_0,v_7\}\), the first enumerated graph edge. Every other edge is carried to this one by a permutation of the underlying five symbols, a fact checked by enumerating all \(5!\) permutations.

Write \(X=\mathcal D(P)\), \(Y=\mathcal D(P-e)\), and \(R=X\setminus Y\). The exact membership predicate above, applied independently by directly checking that the complementary set dominates all vertices, gives the following nonempty face counts, ordered by dimensions zero through six:
\[
f(X)=(10,45,120,200,192,75,10),\qquad
f(Y)=(10,45,118,188,166,59,6).
\]
Thus \(R\) has exactly two two-simplices, twelve three-simplices, twenty-six four-simplices, sixteen five-simplices, and four six-simplices, and no other faces. All counts are complete: ten vertices admit exactly \(2^{10}\) subsets, each tested.

For an exact matching certificate, initialize the set of augmented face bitmasks, including the empty face, and process vertices in the deterministic order \((2,5,1,3,7,8,6,0,9,4)\). At each vertex, pair every still-unmatched face not containing the vertex with its still-unmatched extension by that vertex, in increasing numerical bitmask order, then discard both. Perform this separately on \(Y\) and on the relative face set \(R\). For \(Y\) the procedure pairs 293 faces-pairs and leaves exactly seven critical four-simplices, with the empty face paired. For \(R\), it pairs 28 face-pairs and leaves exactly four critical four-simplices. For \(X\) directly, 321 pairs leave exactly eleven critical four-simplices. The composite matching from \(Y\) and \(R\) is also acyclic on the entire augmented face poset of \(X\), contains 321 pairs, and has precisely the seven plus four critical cells.

Acyclicity is certified by forming the directed Hasse graph of every facet relation, orienting unmatched covers downward and matched covers upward, and topologically sorting all vertices. The standalone verifier checks that every vertex is removed by this sort: there are 2,432 directed arrows for \(Y\), 128 internal relative arrows for \(R\), and 2,740 arrows for \(X\), including the composite matching. It also checks every matched pair is a genuine codimension-one face relation and that no face appears twice. These finite checks reconstruct a complete acyclic matching, not a sample of gradients.

The standard acyclic-matching collapse theorem gives \(|Y|\) a CW homotopy model with a basepoint and seven four-cells, and \(|X|\) one with a basepoint and eleven four-cells. With no cells in positive dimensions below four, the attaching maps of those four-cells are null; hence each model is the asserted sphere wedge. More importantly, the composite acyclic matching respects the subcomplex \(Y\). Its relative discrete-Morse CW pair is obtained from the CW model of \(Y\) by attaching exactly four additional four-cells and no cells of any other positive dimension. Because \(Y\) is \(3\)-connected, their attaching maps \(S^3\to Y\) are nullhomotopic. Therefore \(X\simeq Y\vee\bigvee^4 S^4\) **as a map under \(Y\)**. The claimed integral split injection and cofiber follow. The graph's full symmetric-group action on its five underlying symbols makes the result identical for all fifteen edges.

## Verification
Run `python3 verify_petersen_dominance.py` using only the Python standard library. The verifier enumerates all \(2^{10}=1024\) masks under two independent predicates, checks exact face counts, constructs all three acyclic matchings, verifies the composite acyclic matching on \(X\), and separately reduces the mod-two boundary matrices for the three complexes (with the relative boundary on \(X\setminus Y\)). It obtains reduced Betti counts eleven in degree four for \(X\), seven for \(Y\), and four for the relative pair, zero in all other nonnegative degrees. These binary ranks corroborate the integral Morse proof but do not themselves establish the integral conclusion. The script also enumerates all fifteen edge choices and the full edge orbit induced by five-symbol permutations.

## Relationship to prior work
Matsushita (2020) introduced the closed-neighborhood hypergraph viewpoint and general connectivity bounds for \(\mathcal D(G)\); Matsushita and Wakatsuki (2023) identify \(\mathcal D(G)\) with the Alexander dual of \(\mathcal N(\overline G)\). Since \(\overline P=T_5=L(K_5)\), an existing exact **mod-two** computation of \(\mathcal N(T_5)\) already implies the intact complex's mod-two rank eleven by combinatorial Alexander duality. That baseline rank is not claimed as new. The new content is the integral homotopy pair under every graph-edge deletion, in particular its primitive natural inclusion and four-cell splitting. In the inspected primary articles and closest mathematical-record result, no statement determines the edge-faulted dominance complex or the integral relative pair.

## Limitations
The theorem is specific to the ten-vertex Petersen graph and to deleting exactly one graph edge; it makes no assertion about larger Kneser graphs, multiple edge faults, arbitrary graph perturbations, or canonical equivariant splittings. The proof is a finite, fully enumerated Morse certificate and a standard relative discrete-Morse theorem, not a closed-form combinatorial reduction for general graphs. Search noncoverage is not proof of absolute novelty; an unindexed equivalent calculation could exist. The homotopy equivalences are not asserted to respect all graph symmetries.

## References
1. T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145, first public 2020-09-09, https://arxiv.org/abs/2009.04145.
2. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first public 2023-12-05, https://arxiv.org/abs/2312.02639.
3. *Mixed-dimensional mod-two neighborhood homology first appears at* \(T_7\), published mathematical-record result, https://api.github.com/repos/published-finding corpus/2026/git/blobs/3a6211cf2abc3943237c2cc77dec6af0af51e792 (the \(T_5\) baseline computation).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic discrete-Morse matching method).
