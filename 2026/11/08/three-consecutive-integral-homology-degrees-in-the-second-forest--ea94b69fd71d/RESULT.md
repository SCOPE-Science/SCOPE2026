# Three consecutive integral homology degrees in the second forest complex of \(K_2\times K_3\times K_3\)

## Finding
Let \(G=K_2\times K_3\times K_3\) be the categorical graph product and let \(\mathcal F_2(G)\) consist of vertex subsets inducing acyclic graphs of maximum degree at most two. Then
\[
\widetilde H_i(\mathcal F_2(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{17},&i=7,\\
\mathbb Z^{36},&i=8,\\
\mathbb Z^{6},&i=9,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, all reduced integral homology is torsion-free, and \(\mathcal F_2(G)\) is \(6\)-connected. The complex is nine-dimensional and is nonpure, with respectively \(108\), \(1202\), and \(252\) facets in dimensions \(7\), \(8\), and \(9\). No wedge-of-spheres homotopy decomposition is claimed.

## Assumptions and scope
The three factors are simple complete graphs on respectively two, three, and three vertices. Write their product vertices as \((a,b,c)\), with \(a\in\{0,1\}\) and \(b,c\in\{0,1,2\}\). Two distinct product vertices are adjacent exactly when all three coordinates differ. Thus \(G\) has \(18\) vertices and \(36\) edges. Since \(K_2\times K_3\cong C_6\), the same underlying graph can alternatively be denoted \(C_6\times K_3\); this equivalent nomenclature is included in the literature comparison. A simplex is a subset \(S\subseteq V(G)\) for which every connected component of the *induced* subgraph \(G[S]\) is a path or an isolated vertex. This is the degree-two stage of the forest filtration, not the two-matching complex of an edge set and not an ordinary independence complex. Homology is reduced, with integer coefficients, and the empty simplex is included for chain calculations.

## Proof
**Step 1: exhaustive determination of the complex.** Index the \(18\) product vertices lexicographically, and encode subsets by \(18\)-bit integers. Two independent decision procedures inspect all \(2^{18}=262144\) subsets. One constructs valid sets incrementally, rejecting an added vertex if it creates a third neighbor at an existing vertex, has more than two chosen neighbors, or closes a cycle by joining previously connected chosen neighbors. The other explicitly computes every induced degree and the vertices and edges of each connected component; a connected component is accepted exactly when its edge count is one less than its vertex count. The procedures agree on every subset, and identify \(49743\) simplices including the empty set. The counts by dimension \(-1,0,\ldots,9\) are
\[
(1,18,153,816,2970,7506,12786,13896,8703,2642,252).
\]
Direct testing of maximal faces gives the three facet counts stated above.

**Step 2: certified Morse matchings.** The code uses the standard elementary vertex toggle: in a fixed vertex order, match a remaining face not containing the current vertex with its union with that vertex, if both remain. Perform the procedure independently in increasing and decreasing vertex orders. In each case the matching has \(24826\) pairs and exactly \(91\) augmented critical faces: \(16\) of dimension \(6\), \(33\) of dimension \(7\), \(36\) of dimension \(8\), and \(6\) of dimension \(9\). Construct the directed Hasse graph by orienting matched incidence edges upward and all unmatched edges downward. A full topological-sort check visits all \(49743\) faces and all \(322092\) incidences, proving that each matching is acyclic. The empty simplex is paired with a zero-simplex; discarding only that augmented pair produces an ordinary CW Morse model with one zero-cell and the indicated positive-dimensional critical cells.

**Step 3: exact integral boundaries.** Orient each simplex by increasing vertex index. For a matched lower face \(\sigma\) and upper face \(\tau\), the signed boundary relation \(\partial\tau=\pm\sigma+\sum\pm\sigma'\) gives the standard algebraic discrete-Morse elimination rule. Recursively eliminating the matched pairs in the acyclic gradient graph yields the Morse boundary between critical cells. Both vertex orders independently give the same structural outcome:
\[
C_9\cong\mathbb Z^6\xrightarrow{\;0\;}
C_8\cong\mathbb Z^{36}\xrightarrow{\;0\;}
C_7\cong\mathbb Z^{33}\xrightarrow{\;d_7\;}
C_6\cong\mathbb Z^{16}.
\]
The integer \(16\times33\) matrix for \(d_7\) has \(19\) nonzero coefficients, and the executable certificate explicitly selects \(16\) columns whose square minor is a signed permutation matrix. Thus this minor has determinant \(\pm1\), so \(d_7\) is surjective over \(\mathbb Z\) with primitive image and free kernel of rank \(33-16=17\). Both \(d_8\) and \(d_9\) vanish exactly, not merely modulo a prime. The reduced integral homology is therefore as displayed, with no torsion.

**Step 4: connectivity.** The ordinary Morse CW model has one zero-cell and no cells of dimensions \(1\) through \(5\), so it is \(5\)-connected. As \(d_7\) is surjective, its sixth reduced homology is zero. The first applicable Hurewicz isomorphism forces \(\pi_6=0\); hence the original complex is \(6\)-connected.

## Verification
The standalone standard-library script `artifacts/verify.py` reconstructs the product graph, exhaustively compares both face predicates, proves both matchings acyclic by complete directed-Hasse topological sorts, computes exact signed integral Morse differentials, and verifies primitive unit minors. Independently of Morse theory, it also reduces the original unreduced simplicial boundary matrices over \(\mathbb F_2\). The original boundary ranks for differentials out of dimensions \(5,6,7,8,9\) are respectively \(5216,7570,6326,2360,246\); these give mod-two Betti ranks \(17,36,6\) in degrees \(7,8,9\), consistent with the integral result. Reproduce with `python3 artifacts/verify.py`; its JSON output should equal `artifacts/verify.out`. Exact integer signed minors, not this mod-two check, exclude integral torsion. The program uses no external packages, downloaded datasets, or stochastic choices.

## Relationship to prior work
Andrés Carnero Bravo introduced the forest filtration and in Question 44 specifically asked for the positive-level homotopy type of categorical triple products \(K_2\times K_m\times K_n\) [1]. His Theorem 42 concerns two-factor categorical products and Corollary 43 requires a second factor \(K_2\), which is absent here. The earlier independence-complex classification for the triple product describes \(\mathcal F_0\), not \(\mathcal F_2\) [2]. Forest-filtration results for lexicographic graph products concern a different adjacency rule [3]. The alternative notation \(C_6\times K_3\) is a cycle–complete categorical product, not the standalone cycle complex or the Cartesian prism. The previously calculated first forest-filtration stage of this exact graph is a single-dimensional sphere wedge; the present second stage has three adjacent nonzero homology degrees, so its answer is not implied by that earlier result. This resolves the integral homology and connectivity of a natural unresolved finite instance, but not the full general homotopy-type question.

## Limitations
The assertion is specific to exactly three factor sizes \(2,3,3\) and filtration level \(2\). It determines integral homology and connectivity, not a full homotopy decomposition, persistence maps, or a general formula for \(K_2\times K_m\times K_n\). In particular, vanishing Morse differentials alone does not rule out higher unstable attaching maps from nine-cells. Searches and comparisons of the cited primary texts reveal no covering calculation, but absence of an equivalent computation in unindexed literature is not proven. All computations are finite and exhaustive within the specified \(18\)-vertex complex.

## References
[1] Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first posted 2023-07-25), introduction, Theorem 42, Corollary 43 and Question 44. https://arxiv.org/abs/2307.13271

[2] Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first posted 2023-07-23), especially Section 4. https://arxiv.org/abs/2307.12401

[3] Andrés Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321 (first posted 2023-07-26), Section 5. https://arxiv.org/abs/2307.14321
