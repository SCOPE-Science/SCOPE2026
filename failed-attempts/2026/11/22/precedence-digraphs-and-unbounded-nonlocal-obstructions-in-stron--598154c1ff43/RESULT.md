# Precedence digraphs and unbounded nonlocal obstructions in strong Morse matching complexes

## Finding
Let \(G=(V,E)\) be any finite simple graph with at least one edge, regarded **strictly as a one-dimensional simplicial complex** (even when its graph contains triangles). Let \(\mathcal{SM}(G)\) be the strong discrete-Morse matching complex obtained from vertex filtrations, in the sense of Knudson and Owens-White [1]. Its vertices are indexed by incidences \((v,u)\) with \(\{u,v\}\in E\), representing the matching pair between the vertex \(v\) and the one-simplex \(\{u,v\}\). Write a set of distinct incidences as \(S\).

Define the *precedence digraph* \(D_G(S)\) on \(V\) by inserting, for every \((v,u)\in S\), the arc \(u\to v\) and all arcs \(v\to w\) for \(w\in N_G(v)\setminus\{u\}\). Then the following statements hold.

**(A) Exact face oracle.** Every nonempty \(S\) is a face of \(\mathcal{SM}(G)\) if and only if \(D_G(S)\) is acyclic. Thus membership can be decided by topological sorting, without enumerating vertex filtrations.

**(B) Explicit flag model for forests.** If \(G\) is a forest, \(\mathcal{SM}(G)\) is the independence complex of a graph \(F(G)\) whose vertices are the incidences \((v,u)\). Distinct incidences \((v,u)\) and \((w,z)\) are adjacent in \(F(G)\) precisely when either \(v=w\), or \(\{v,w\}\in E\) and both choose each other (\(u=w,z=v\)) or neither chooses the other (\(u\ne w,z\ne v\)). Consequently \(\mathcal{SM}(G)\) is flag, and the number of edges in its incompatibility graph is exactly
\[
|E(F(G))|=\sum_{v\in V}\binom{\deg(v)}{2}+\sum_{\{v,w\}\in E}\bigl(1+(\deg(v)-1)(\deg(w)-1)\bigr).
\]
The equality of complexes uses the usual augmented empty-face convention; the original definition [1] excludes the empty matching, which does not affect the nonempty faces or geometric realization.

**(C) Arbitrarily large minimal nonfaces on cycles.** For every \(n\ge5\), the strong matching complex of the *unfilled* cycle \(C_n\) has an inclusion-minimal nonface containing exactly \(\lceil n/2\rceil\) incidence vertices, even though all its two-element subsets are faces. Hence no fixed bound on the size of forbidden faces describes these complexes. The short cycles \(C_3,C_4\) have flag strong matching complexes, so five is the sharp cycle-length onset for this obstruction.

## Assumptions and scope
The graph is finite, undirected, simple and has at least one edge. The simplicial complex is its one-dimensional realization, not its flag or clique filling. In particular the descending link of a vertex in an induced vertex filtration is a discrete set consisting of its previously inserted neighbors. It is a simplicial cone exactly when this set has one element. Thus a vertex \(v\) is paired with \(\{u,v\}\) precisely when \(u\) is its **unique** earlier neighbor. The full complex \(\mathcal{SM}(G)\) is the downward closure of all complete strong matchings arising from total orders, rather than the set of complete matchings alone.

## Proof
**Step 1: precedence equivalence.** Let \(S\) be any incidence set. If a vertex order generates a strong matching containing \(S\), each \((v,u)\in S\) must have \(u\) before \(v\) and all other neighbors of \(v\) after \(v\). Therefore that total order extends every arc in \(D_G(S)\); this digraph has no directed cycle. Conversely, if \(D_G(S)\) is acyclic, choose a topological ordering of its vertices. Every chosen \((v,u)\) has exactly one earlier neighbor, namely \(u\), so its vertex-edge pair occurs in the strong matching obtained from this ordering. This remains true if other unchosen incidences also occur. Since the complex is downward closed, \(S\) is a face. No graph planarity, connectivity or acyclicity hypothesis is used in this step.

**Step 2: forest flagness and conflict graph.** For a forest, the underlying undirected graph of \(D_G(S)\) is a subgraph of \(G\). Any directed cycle must therefore be a two-cycle on an original edge. The two opposed arcs cannot arise from a single selected incidence: one selected incidence directs each of its incident graph edges in exactly one direction. Consequently every obstruction already involves a pair of selected incidences. Two different incidences with the same child \(v\) force opposing directions along an edge to one of the chosen parents. For distinct children \(v,w\), opposing constraints can occur only when \(v,w\) are adjacent: along their common edge the choices conflict exactly if both choose each other or neither chooses the other. This gives the stated graph \(F(G)\) and proves the exact independence-complex description. Summing same-child conflicts \(\binom{\deg(v)}2\) and, independently, cross-child conflicts \(1+(\deg(v)-1)(\deg(w)-1)\) over each original edge counts every edge of \(F(G)\) exactly once.

**Step 3: cycle minimal nonfaces.** Number the vertices of \(C_n\) cyclically \(0,\ldots,n-1\), and let \(U=\{0,2,4,\ldots\}\) (all even labels less than \(n\)). This is a *minimum-cardinality*, hence inclusion-minimal, vertex cover of the cycle, with \(|U|=\lceil n/2\rceil\). Choose
\[
S_n=\{(v,v-1\bmod n):v\in U\}.
\]
Each selected incidence imposes the forward cycle arcs \(v-1\to v\to v+1\) (modulo \(n\)). Because \(U\) meets every original edge, \(D_{C_n}(S_n)\) contains the complete forward directed cycle and cannot be acyclic. If any one selected incidence is deleted, minimality of \(U\) leaves at least one original edge with neither endpoint selected, so no precedence arc crosses that edge; all remaining arcs point consistently forward along a proper subgraph of the cycle. The result is acyclic. Thus every proper subset of \(S_n\) is a face, establishing an inclusion-minimal nonface of cardinal \(\lceil n/2\rceil\). When \(n\ge5\), this cardinality is at least three, hence \(S_n\) is a clique in the one-skeleton but not a simplex, proving nonflagness. For \(n=3\), the strong complex consists of six isolated vertices; for \(n=4\), its twelve maximal one-simplices form a triangle-free graph on eight incidence vertices. These last two finite statements follow either by the 6 and 24 vertex orders, respectively, or by the exact checker below.

## Verification
The accompanying standalone `checker.py` implements the definitions independently through both vertex-order enumeration and precedence-digraph topological sorting. Its replay checks 38,280 complete face-membership comparisons on 90 finite graphs, including all nonempty labeled graphs through four vertices and representative five-/six-vertex graphs; 35 forest instances additionally check the local incompatibility rule and edge-count formula. It also checks the cycle minimal-nonface certificates for every \(5\le n\le12\) and flagness of \(C_3,C_4\). The written proofs, not these bounded experiments, establish the universal claims. Reproduce by running `python3 checker.py` with Python 3 and no external packages.

## Relationship to prior work
Knudson and Owens-White [1] introduce this particular strong matching complex, distinguish it from the ordinary Morse complex, and work out paths, stars, simplexes and cycle homotopy calculations. Their vertex-filtration definition is the starting point here; the general precedence-digraph face characterization, forest conflict graph and cycle minimal-nonface sizes are the additions claimed. Donovan and Scoville [2] prove that the **ordinary** discrete Morse matching complex of a graph is flag exactly for a tree. This does **not** settle the strong complex, a generally proper subcomplex of the ordinary one; in fact the small strong cycle complexes \(C_3,C_4\) are flag. A related publicly indexed tree classification [3] concerns purity and diameter rather than a face oracle or flagness; a publicly indexed cycle theorem [4] concerns fundamental groups rather than minimal forbidden faces. These comparisons limit, but do not eliminate, the possibility of an equivalent earlier result.

## Limitations
The local two-incidence incompatibility graph in (B) is asserted only for forests. For graphs containing cycles the general exact criterion (A) still holds, but global precedence cycles may create higher-cardinality minimal nonfaces. The theorem does not compute all Betti numbers or homotopy types of strong matching complexes of arbitrary forests or cycles; flagness alone does not determine them. All results concern the explicitly defined unfilled one-dimensional graph complex, and an independently checked literature-priority claim is not made.

## References
[1] K. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844, first public 2026-09-06, https://arxiv.org/abs/2609.06844.

[2] C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780 (2022 preprint); journal version, *New York Journal of Mathematics* 29 (2023), 1393–1412, https://arxiv.org/abs/2207.13780.

[3] *A diameter-three characterization of pure strong Morse matching complexes of trees*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-diameter-three-characterization-of-pure-strong-morse-matching--9f25582f2bc2.

[4] *Sharp simple-connectivity threshold for strong Morse matching complexes of cycles*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-simple-connectivity-threshold-for-strong-morse-matching-co--1c57a9270d74.
