# The minimum-maximal-matching exchange graph of the Möbius–Kantor graph

## Finding

Let \(G\) denote the Möbius–Kantor graph \(GP(8,3)\). A *minimum maximal matching* is an inclusion-maximal set of pairwise vertex-disjoint edges of smallest possible size. The minimum size is \(6\), and there are exactly \(176\) such matchings. Across all maximal matchings the size distribution is \((6,176),(7,336),(8,33)\); there are no other sizes.

Form a simple exchange graph \(\mathcal E(G)\) whose vertices are the \(176\) minimum maximal matchings, with an edge joining distinct states precisely when their matching-edge sets differ by removing one edge and inserting one edge, leaving another minimum maximal matching. Then
\[
\mathcal E(G)\cong 6C_{16}\sqcup80K_1.
\]
Thus \(\mathcal E(G)\) has \(96\) edges; its six nontrivial components each have radius and diameter \(8\); its other \(80\) vertices are isolated. Every legal exchange is an edge pivot: the removed and inserted graph edges share a vertex.

## Assumptions and scope

The simple undirected graph \(G=GP(8,3)\) has vertex labels \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\), with the \(24\) distinct edges
\[
\{u_i,u_{i+1}\},\qquad \{u_i,v_i\},\qquad \{v_i,v_{i+3}\}
\quad (i\in\mathbb Z/8\mathbb Z).
\]
Here a matching is *maximal* by inclusion, not necessarily maximum by size. Both the minimum matching size and state set refer to the full graph \(G\). An exchange changes exactly one whole edge, not one vertex of a matching; distinct matchings are unlabeled edge subsets. The graph \(\mathcal E(G)\) is simple, with one undirected adjacency per pair regardless of the number of descriptions of a move.

## Proof

**Maximality criterion.** For any matching \(M\), write \(U(M)\) for the vertices not incident to an edge of \(M\). The matching \(M\) is maximal if and only if \(U(M)\) is independent: otherwise an edge with both ends unmatched can be appended, and conversely the existence of any appendable edge has both endpoints in \(U(M)\).

**Exhaustive matching classification.** Enumerate the \(24\) edges in increasing lexicographic order on endpoint pairs, with \(u_i=i\) and \(v_i=8+i\). The finite recursion starts with the empty matching and processes each edge once, choosing to omit it, or to include it only if both endpoints are still unmatched. It thereby visits every graph matching exactly once. At each terminal state, retain the matching precisely when every graph edge has an endpoint already incident to a selected edge, by the preceding criterion. The complete integer tally, reproduced by `verify_gp_matching.py`, is
\[
N_6=176,\qquad N_7=336,\qquad N_8=33,
\]
with all other \(N_j=0\). In particular this excludes *every* matching of size at most five from being maximal, not merely some sample, and proves the claimed optimum.

**Exchange classification.** For each of the \(176\) optimum matching masks \(M\), and for each \(e\in M\) and \(f\notin M\), test whether \((M\setminus\{e\})\cup\{f\}\) is in the completed table of optimum matchings. This is an exhaustive necessary-and-sufficient test for the declared adjacency. The resulting symmetric adjacency set has \(96\) unordered pairs. Its breadth-first component enumeration has exactly eighty singleton components and six components of sixteen vertices each; every vertex of a nonsingleton component has degree exactly two. Every finite connected simple \(2\)-regular graph is a cycle, hence these six components are \(C_{16}\). Their eccentricities are all \(8\), as follows also directly from cycle distance.

**Pivot lemma.** In any graph, if two maximal matchings differ by one removed edge \(e\) and one inserted edge \(f\), then \(e\) and \(f\) share a vertex. Otherwise \(e\) is disjoint from the entire new matching, and could be appended to it, contradicting maximality. Thus edge pivots give the entire legal exchange graph in this setting, independently of the finite enumeration.

**Independent completion-first reconstruction.** An alternative finite proof enumerates all independent sets \(U\) of the graph and all perfect matchings of the complement \(G-U\). Each such perfect matching has exactly \(U\) as its unmatched vertices and is maximal by the criterion; this gives a bijection, so neither duplicates nor omissions arise. Applied to the independent LCF representation \([5,-5]^8\), it reproduces the size distribution and assembles adjacency via shared five-edge cores, again obtaining \(6C_{16}\sqcup80K_1\). An explicit bijection of the two graph labelings is asserted and checked in the second verifier.

## Verification

Run the standard-library Python programs `python3 verify_gp_matching.py` and `python3 verify_lcf_complement.py`. Their recorded outputs are `verify_gp_matching.out` and `verify_lcf_complement.out` respectively. Both terminate with `VERIFY_OK`; both independently report \(176\) optimum matchings, \(96\) exchanges, and components of sizes \(16\) (six times) and \(1\) (eighty times). The first program additionally checks all \(96\) nonisolated states have eccentricity \(8\) and that each exchange necessarily pivots about an endpoint. The second program checks a fixed explicit graph isomorphism from \(GP(8,3)\) to the LCF graph before enumerating independent complements.

These are exhaustive finite algorithms with explicit loop domains and no random samples. They do not establish anything about an infinite family of graphs or external computational models.

## Relationship to prior work

Demange and Ekim (2008) studied the minimum maximal matching problem and proved its NP-hardness for fixed-degree regular bipartite graphs; their inspected article discusses reductions and gadgets, not this exact fixed-graph optimum-state exchange graph. The 2014 extension with Tanasescu addresses complexity and approximation, not the displayed reconfiguration classification in its accessible abstract; its full text was not inspected.

The publicly available study *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge* calculates the homotopy type and ordinary matching-complex face vector for this same host graph. Those results are distinct: a face count by dimension, or a homotopy type, does not specify which faces are inclusion-maximal, nor the adjacency among its minimum-cardinality facets. Its fully inspected `RESULT.md` has no stated \(176\)-state optimal exchange classification. MathWorld supplies the graph identity \(GP(8,3)\cong\operatorname{LCF}([5,-5]^8)\), not the minimum maximal matching exchange invariant.

## Limitations

This is a complete finite computation about one named graph. The general pivot lemma does not by itself determine any component count. Historical-priority review was limited to the named and searched sources; unindexed edge-domination tables or computations could subsume the claimed finite data. The full 2014 complexity/approximation paper was inaccessible, and its accessible abstract alone does not rule out a relevant appendix. Independent scholarly audit has not been performed.

## References

1. M. Demange and T. Ekim, *Minimum Maximal Matching Is NP-Hard in Regular Bipartite Graphs*, TAMC 2008, LNCS 4978, pp. 364–374, DOI: 10.1007/978-3-540-79228-4_32; full paper publicly accessible at https://www.researchgate.net/profile/Tinaz-Ekim/publication/220908394_Minimum_Maximal_Matching_Is_NP-Hard_in_Regular_Bipartite_Graphs/links/02e7e51b606c2aa5c7000000/Minimum-Maximal-Matching-Is-NP-Hard-in-Regular-Bipartite-Graphs.pdf. Proceedings softcover first published April 8, 2008.
2. M. Demange, T. Ekim, and C. Tanasescu, *Hardness and approximation of minimum maximal matchings*, International Journal of Computer Mathematics 91 (2014), 1635–1654, DOI: 10.1080/00207160.2013.853052.
3. E. W. Weisstein, *Möbius–Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html.
4. *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge*, publicly available RESULT.md at https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-m-bius-kantor-matching-complex-is-a-mixed-dimensional-sphere--4bfded76792e/RESULT.md.
