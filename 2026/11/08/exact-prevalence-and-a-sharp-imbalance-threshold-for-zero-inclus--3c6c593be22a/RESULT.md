# Exact prevalence and a sharp imbalance threshold for zero-inclusive EFX orientations on bicliques

## Finding

For every pair of integers \(a,b\ge 1\), consider the simple complete bipartite graph \(K_{a,b}\). Its \(ab\) edges are indivisible goods, its vertices are labeled agents, and each edge must be allocated to one of its endpoints. Agent \(v\) assigns additive value one to each edge incident to \(v\) and zero to each other edge. An allocation is **zero-inclusive EFX**, or **EFX0**, when for all ordered pairs of distinct agents \(u,v\) and *every* edge \(e\) in agent \(v\)'s bundle,

\[
U_u(X_u)\ge U_u(X_v\setminus\{e\}).
\]

In particular, a virtually removed edge may have value zero to \(u\). Orient each edge towards its recipient. Then the number of EFX0 orientations on the labeled graph is

\[
F(a,b)=(2^b-1)^a+(2^a-1)^b-2^{ab}+a+b.
\]

More precisely, the EFX0 orientations are exactly (i) those with positive indegree at every vertex, together with (ii) the \(a+b\) orientations having a single source, in which all neighbors of the source have indegree one. In the latter case, the entire orientation is uniquely determined by its source.

If every edge is oriented independently with probability \(1/2\) in either direction, its EFX0 probability is

\[
P(a,b)=(1-2^{-b})^a+(1-2^{-a})^b-1+(a+b)2^{-ab}.
\]

For \(1\le a\le b\) with \(a\to\infty\) this yields the sharp imbalance transition

\[
\frac{b}{2^a}\longrightarrow\lambda\in[0,\infty]
\quad\Longrightarrow\quad
P(a,b)\longrightarrow e^{-\lambda},
\]

where \(e^{-\infty}=0\). In the balanced case, as \(n\to\infty\),

\[
P(n,n)=1-2n2^{-n}+O(n^2 4^{-n}).
\]

For a one-vertex part, \(F(1,b)=b+1\). The first nontrivial examples are \(F(2,2)=6\), \(F(3,4)=1687\), and \(F(4,4)=35722\).

## Assumptions and scope

The graph is a finite *simple* complete bipartite graph with labeled parts of positive sizes. There are no parallel edges, ties in the positive value of edges are intentional, and all agents use the specified binary additive incidence valuation. An orientation assigns every good to exactly one of its two endpoints. No goods are left unallocated and no goods are assigned to uninterested agents. An indegree counts received edges rather than supplied edges. EFX0 demands comparisons after removal of **every** good in the other bundle, not merely goods having positive value to the comparing agent. The formula counts orientations with distinct labeled edge endpoints; it does not quotient graph automorphisms.

The asymptotic statement concerns sequences of positive integers with \(a\le b\) and \(a\to\infty\); when \(b/2^a\) diverges, the limiting probability is zero. A fixed \(a\) and growing \(b\) also produces probability tending to zero, but is not needed for the stated threshold.

## Proof

**Step 1: a source criterion on any simple graph.** For arbitrary distinct vertices \(u,v\), the bundle of \(v\) contains at most one good that \(u\) values positively: the edge \(uv\), if present and allocated to \(v\). If \(u\) has positive indegree, its own utility is at least one, whereas the value it assigns to any other bundle, even without a deletion, is at most one. Thus a nonsource cannot violate EFX0.

If \(u\) is a source (indegree zero), all its incident edges point away from it. For each neighbor \(v\), its edge \(uv\) belongs to \(v\). If \(v\) has at least two received edges, remove from \(v\)'s bundle an edge different from \(uv\). The removed edge has value zero to \(u\), and \(u\) still values the remaining bundle at one while its own value is zero. This violates EFX0. Conversely, if every neighbor of every source has indegree one, removing any good from a source-neighbor's singleton bundle leaves value zero to the source, and bundles of nonneighbors have value zero to it. Hence an orientation is EFX0 **if and only if every source has only indegree-one neighbors**.

**Step 2: classify EFX0 orientations with sources.** If a source lies in the size-\(a\) part, all \(b\) incident edges point into the opposite part. By the source criterion, each opposite-side vertex must have indegree exactly one. Therefore every remaining edge must point into the size-\(a\) part. There is exactly one orientation per specified source in this part. The symmetric argument gives exactly one orientation for each of the \(b\) vertices in the other part. Such an orientation has no second source, and no orientation can have a source in both parts, since the edge between them must enter one of them. Thus there are exactly \(a+b\) valid orientations having a source, including the cases in which a part has size one.

**Step 3: count orientations without sources.** Encode an orientation by an \(a\)-by-\(b\) binary matrix, with entry one when the relevant edge points to the size-\(a\) endpoint. A source in the size-\(a\) part is precisely a zero row. A source in the size-\(b\) part is precisely an all-one column. There are \(2^{ab}-(2^b-1)^a\) matrices with at least one zero row and \(2^{ab}-(2^a-1)^b\) matrices with at least one all-one column. Those events are disjoint: a zero row and an all-one column disagree at their intersection. Subtracting both excluded sets from \(2^{ab}\), the number of source-free orientations is

\[
(2^b-1)^a+(2^a-1)^b-2^{ab}.
\]

By Step 1 all source-free orientations satisfy EFX0, and Step 2 supplies precisely the remaining \(a+b\), proving the exact formula.

**Step 4: probability and sharp transition.** Divide the integer count by the \(2^{ab}\) equally likely orientations to obtain the probability expression. For \(1\le a\le b\), Bernoulli's inequality gives

\[
\left|P(a,b)-(1-2^{-a})^b\right|
\le a2^{-b}+(a+b)2^{-ab}.
\]

Both terms tend to zero as \(a\to\infty\) with \(b\ge a\). Standard exponential limits give \((1-2^{-a})^b\to e^{-\lambda}\) when \(b2^{-a}\to\lambda\), including zero for divergent \(\lambda\). Finally, substituting \(a=b=n\) into the exact formula and using the binomial expansion of \((1-2^{-n})^n\) gives the claimed balanced asymptotic. Every displayed estimate follows from the exact finite formula and does not rely on simulation.

## Verification

The standalone script `verify_biclique_efx.py` enumerates every binary edge assignment for all \(22\) tested pairs \(1\le a,b\le5\) with \(ab\le16\), a total of \(142602\) labeled orientations. It independently computes the EFX0 definition by deleting every owned good for every ordered pair of agents, computes the source-neighbor criterion, and compares both counts against the closed formula. It also checks basic integer symmetry and bounds for \(9801\) parameter pairs with \(1\le a,b\le99\). All checks passed. Run with `python3 verify_biclique_efx.py`. The exhaustive tests cover only the stated finite ranges; the preceding argument proves the universal theorem and asymptotic limits.

## Relationship to prior work

Christodoulou, Fiat, Koutsoupias and Sgouritsa introduce EFX in graph-based allocations and EFX orientations; their results establish the general existence of EFX allocations, together with hardness and nonexistence examples for EFX orientations under heterogeneous valuations [1,2]. Their strict definition compares after removing every item, including zero-valued ones, as used here. Our result is not an existence theorem for arbitrary valuations: it counts **all** qualifying orientations in the uniform unit-edge complete-bipartite model and establishes a random-orientation threshold.

Afshinmehr and coauthors investigate EFX allocations and orientation existence on bipartite multigraphs, with the emphasis on multiple edges, diameter, and heterogeneous monotone valuations [3]. Neoh and Teh study general EFX counting complexity and minimum multiplicities, not this exact uniform-graph orientation count [4]. Standard source counting by inclusion-exclusion is a component of Step 3; the additional fairness-source equivalence and the sharp imbalance probability law are the assertions made here. Literature overlap remains a priority question rather than a claim of absolute uniqueness.

## Limitations

The theorem does not extend its exact count to arbitrary graphs, weighted edges, general valuations, multigraphs or allocations sending goods to nonendpoints. The zero-excluding version of EFX differs crucially: because each other agent's bundle contains at most one item positively valued by any comparer on a simple graph, all orientations pass that weaker deletion criterion in this model. Publication-priority risk remains for unindexed statements equivalent to the same source criterion, exact count or probability law. The computations are finite corroboration, not independent certification of the infinite claim.

## References

[1] G. Christodoulou, A. Fiat, E. Koutsoupias and A. Sgouritsa, *Fair Allocation in Graphs*, Proceedings of EC 2023, pp. 473–488, published July 7, 2023. https://doi.org/10.1145/3580507.3597764

[2] G. Christodoulou et al., *EFX Allocations on Graphs*, freely accessible full manuscript dated March 15, 2025. https://www.cs.ox.ac.uk/people/elias.koutsoupias/Personal/Papers/fair-allocations-on-graphs.pdf

[3] M. Afshinmehr et al., *EFX Allocations and Orientations on Bipartite Multi-graphs: A Complete Picture*, arXiv:2410.17002, first posted October 22, 2024. https://arxiv.org/abs/2410.17002

[4] T. Y. Neoh and N. Teh, *Understanding EFX Allocations: Counting and Variants*, arXiv:2504.03951, posted April 4, 2025. https://arxiv.org/abs/2504.03951
