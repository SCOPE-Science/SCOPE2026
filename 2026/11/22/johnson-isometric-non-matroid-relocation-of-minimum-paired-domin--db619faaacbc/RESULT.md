# Johnson-isometric, non-matroid relocation of minimum paired domination on the Franklin graph

## Finding
Let \(F\) be the twelve-vertex Franklin graph with LCF presentation \([5,-5]^6\), and let \(\mathcal P\) be the family of its minimum paired dominating vertex sets. Thus a set is admissible if it dominates every vertex and its induced graph has a perfect matching. Let \(R\) have vertex set \(\mathcal P\), with an edge whenever one selected vertex can be replaced by one unselected vertex and the new set remains admissible.

The family consists of exactly \(184\) six-vertex sets. For **every** \(S,T\in\mathcal P\), including coincident sets,
\[
d_R(S,T)=6-|S\cap T|.
\]
In particular, \(R\) is an **isometric induced subgraph** of the Johnson graph \(J(12,6)\), and every distinct ordered pair of optima admits an exchange that strictly increases the overlap with its specified target. Nevertheless, \(\mathcal P\) is **not** a matroid-basis family: it fails the basis-exchange axiom at an explicit pair of optima.

The exchange graph has \(984\) edges, degree distribution \(120\) of degree \(10\) and \(64\) of degree \(12\), radius \(4\), and diameter \(6\). Its eccentricity distribution is \(24\) at \(4\), \(96\) at \(5\), and \(64\) at \(6\). Its unordered-pair distance counts at distances \(1,2,3,4,5,6\) are respectively
\[
984,\quad3900,\quad6640,\quad4512,\quad768,\quad32.
\]
Under the full graph automorphism group (of order \(48\)), the minimum sets form eight orbits of sizes \(8,8,12,12,24,24,48,48\).

## Assumptions and scope
All graphs here are finite, simple, and undirected. The graph \(F\) has vertices \(\mathbb Z/12\mathbb Z\), all twelve cyclic edges \(\{i,i+1\}\), and the six chords \(\{2j,2j+5\}\) for \(0\le j<6\), with indices reduced modulo \(12\). This graph is cubic, bipartite, and is the standard Franklin graph. An admissible set \(S\subseteq V(F)\) is *paired dominating* when \(N[S]=V(F)\) and \(F[S]\) has a perfect matching. The minimum size is \(\gamma_{\mathrm{pr}}(F)\). Token jumping (one-for-one replacement) is the rule defining \(R\); the graph's own edges do **not** restrict where the replacement vertex may lie.

A shortest-path distance is finite if and only if its endpoints lie in the same component. The claimed formula proves connectedness in this particular finite instance. There is no claim about every bipartite or cubic graph, or about all sizes of a graph family.

## Proof
**1. Exact feasible-set predicate and minimum size.** Construct a twelve-entry adjacency bitmask from the above edges. For any subset mask \(s\), determine domination exactly by taking the bitwise union of the closed neighborhoods of its selected vertices. Determine existence of a perfect matching recursively: take the least selected vertex and pair it with each selected neighbor, recursively testing the remaining induced set, with the empty set as the successful base case. This recursion is necessary and sufficient because every perfect matching pairs the least vertex with one of its neighbors, and conversely any successful submatching extends to a perfect matching.

Any set whose induced graph has a perfect matching has even cardinality. Exhausting all \(\binom{12}{2}=66\) two-vertex and \(\binom{12}{4}=495\) four-vertex sets yields no paired dominating sets. Exhausting the \(\binom{12}{6}=924\) six-vertex sets yields exactly \(184\) satisfying both exact predicates. Hence \(\gamma_{\mathrm{pr}}(F)=6\) and \(|\mathcal P|=184\). An independent enumeration uses the bipartite adjacency matrix specified below: each six-vertex paired set must choose exactly three vertices on each side; among the \(\binom63^2=400\) candidate balanced sets, exactly \(184\) dominate and have a perfect matching.

**2. Exact one-replacement graph.** Number the \(184\) masks in deterministic lexicographic order and connect two if their symmetric difference has exactly two elements. Looping over the selected and unselected vertices produces \(984\) undirected edges and the degree distribution stated above. Every edge is valid by construction, and every legal one-for-one exchange is tested, so the adjacency list is exact.

**3. The target-improving property and isometry.** For each of the \(184\cdot183=33{,}672\) ordered pairs \((S,T)\) of distinct minimum sets, enumerate all \(u\in S\setminus T\) and \(v\in T\setminus S\), and test the exact lookup of \((S\setminus\{u\})\cup\{v\}\) in \(\mathcal P\). In **every** ordered pair at least one such exchange exists. The number of valid target-improving exchanges, over these ordered pairs, has histogram
\[
\begin{array}{c|rrrrrrrrrr}
\text{count}&1&2&3&4&5&6&7&8&9&12\\
\text{ordered pairs}&2352&7992&9984&7008&2784&1184&1536&384&384&64.
\end{array}
\]
Thus we can improve the overlap with \(T\) by one at each step. By induction on \(|S\setminus T|\), this gives a legal route of length \(|S\setminus T|=6-|S\cap T|\). Every one-for-one replacement increases overlap with \(T\) by at most one, proving the reverse inequality. The two bounds yield the asserted exact shortest-path formula. An independent all-sources breadth-first search reproduces this formula for all \(\binom{184}{2}=16{,}836\) unordered pairs and yields the distance and eccentricity distributions.

**4. Non-matroid witness.** In the above cyclic labels, consider the two admissible sets
\[
A=\{0,2,3,9,10,11\},\qquad B=\{0,1,6,9,10,11\}.
\]
The element \(2\in A\setminus B\) has **no** valid basis-exchange partner in \(B\setminus A=\{1,6\}\): neither \(A-\{2\}+\{1\}\) nor \(A-\{2\}+\{6\}\) is paired dominating. This violates the basis-exchange axiom even though another target-improving exchange exists for \((A,B)\). The finite verifier independently checks membership of \(A,B\) and non-membership of both replacements.

**5. Exact symmetry, degrees, and distances.** To enumerate automorphisms, map the six even vertices injectively to either bipartition shore; their images uniquely determine the images of odd vertices through neighbor signatures. Check all \(6!\) proposed even-shore permutations in each orientation, retaining exactly \(48\) automorphisms. Acting on the \(184\) sets gives the eight orbit sizes displayed. Applying exhaustive BFS to the exact exchange graph establishes the eccentricity and distance counts stated in the Finding. These calculations terminate on finite explicit sets, not on a heuristic sample.

## Verification
Run `python3 verify_lcf.py` and `python3 verify_bipartite.py` using Python 3 with no third-party packages. Both should print one JSON object with `"status": "ALL CHECKS PASSED"` and exit successfully. The corresponding exact output files are `verification_lcf_output.json` and `verification_bipartite_output.json`.

The first program uses the Hamiltonian LCF construction, twelve-bit exact domination predicates, recursive perfect-matching decisions, exhaustive target-improving exchanges, all-pairs BFS, and a complete automorphism enumeration. The second constructs the graph independently from the six-by-six bipartite neighborhood matrix
\[
(013),\ (023),\ (124),\ (045),\ (125),\ (345),
\]
where each parenthesized triple lists the neighboring \(Y\)-indices of \(x_0,\ldots,x_5\). It uses explicit permutations of selected vertices in the other shore to decide perfect matchings, counts balanced candidates directly, and independently reproduces all distances. An explicit labelled isomorphism between representations is checked within the second program.

## Relationship to prior work
Tripathi, Kloks, Pandey, Paul, and Wang (2021) study algorithms and complexity for paired domination and supply the underlying paired-dominating-set predicate. Křišťan and Svoboda (2023) study shortest reconfiguration under token *sliding* for ordinary dominating sets, especially on trees and interval graphs; neither the paired-matching feasibility constraint nor the Franklin optimum exchange graph is covered by their theorems. Lu and Wu (2026) prove a sharp general bound for paired domination in cubic bipartite graphs, but the bound does not determine the exact set of minimizers or their exchange distances.

A separately published twelve-vertex cubic bipartite census identifies Franklin as the unique order-twelve class of paired domination number six. That statement supplies the optimum *size*, not the present \(184\)-configuration enumeration, target-improving exchange criterion, isometric metric, or failure of matroid exchange. Published results for paired domination on icosahedral graphs, triangular graphs, and Kneser graphs concern different graphs and neither imply nor subsume this Franklin-specific claim.

## Limitations
This is an exact finite theorem about a fixed graph, not an infinite graph-family characterization. The key isometry property is proved by the transparent complete finite enumeration; no shorter conceptual characterization of all \(184\) solutions is claimed. Ordinary token sliding in the original bipartite graph admits no move between paired dominating sets, because each set must have equally many vertices on either shore and a slide changes this balance. That elementary fact is **not** claimed as a novel contribution. Completeness of bibliographic searching is not provable; unindexed earlier work could contain an equivalent exchange description. Independent mathematical review of this finding has not been performed.

## References
1. V. Tripathi, T. Kloks, A. Pandey, K. Paul, and H.-L. Wang, *Complexity of Paired Domination in AT-free and Planar Graphs*, arXiv:2112.05486v1, first public 2021-12-10. https://arxiv.org/html/2112.05486v1
2. J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv:2307.10847v1, first public 2023-07-20. https://arxiv.org/abs/2307.10847
3. C. Lu and Q. Wu, *Paired Domination in Cubic Bipartite Graphs*, arXiv:2609.30152v1, first public 2026-09-24. https://arxiv.org/abs/2609.30152
4. *The Franklin graph is the unique twelve-vertex cubic bipartite equality graph for paired domination*, published 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-franklin-graph-is-the-unique-twelve-vertex-cubic-bipartite-e--f490f3f3f842
5. E. W. Weisstein, *LCF Notation*, MathWorld, includes the Franklin graph entry \([5,-5]^6\). https://mathworld.wolfram.com/LCFNotation.html
