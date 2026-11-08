# Seven seven-spheres and the complete symmetry character of the Möbius–Kantor dominance complex

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph, and let \(\operatorname{Dom}(M)\) be its vertex-dominance complex. There is an integral homotopy equivalence
\[
\operatorname{Dom}(M)\simeq\bigvee^{7} S^{7}.
\]
Its full graph-automorphism group \(A=\operatorname{Aut}(M)\), of order \(96\), acts on the sole nonzero reduced rational homology group with the complete character tabulated below. In particular,
\[
\dim_{\mathbb Q}\widetilde H_7(\operatorname{Dom}(M);\mathbb Q)^A=0,
\qquad
\langle\chi_7,\chi_7\rangle_A=4.
\]
Consequently, the complexified seven-dimensional homology representation is multiplicity-free, with four inequivalent nontrivial irreducible constituents. This is a representation-theoretic statement; no integral irreducible decomposition or equivariant homotopy splitting is asserted.

## Assumptions and scope
Use sixteen vertices \(u_i=i\) and \(v_i=8+i\), where \(i\in\{0,\ldots,7\}\), with indices read modulo \(8\). The edges are exactly \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), for every \(i\). Thus \(M\) is connected, cubic, has \(24\) edges, and has girth \(6\).

A set \(D\) dominates a graph if every vertex is in \(D\) or adjacent to a member of \(D\). A subset \(F\subseteq V(M)\) belongs to \(\operatorname{Dom}(M)\) exactly when \(V(M)\setminus F\) dominates \(M\). Equivalently, no four-element closed neighborhood \(N_M[x]\) is contained in \(F\). The empty face is included. Vertex labels in the verification program are fixed as above; a bit mask denotes the corresponding subset.

## Proof
**1. Exact faces.** The closed-neighborhood criterion follows directly from the definition: \(V(M)\setminus F\) fails to dominate precisely when some vertex and all three of its neighbors lie in \(F\). The two independently implemented predicates in `verify.py` agree on every one of the \(2^{16}\) subsets. The complex has \(32,391\) faces including the empty face. Its face counts for dimensions \(-1,0,\ldots,11\) are
\[
(1,16,120,560,1804,4176,6976,8208,6462,3136,832,96,4).
\]

**2. Exhaustive acyclic Morse matching.** Start with the entire face set \(R\), including the empty face, and visit vertex labels \(i=0,\ldots,15\) in order. At stage \(i\), for every still-remaining face \(F\) not containing \(i\) for which \(F\cup\{i\}\) also remains, match \(F\) with \(F\cup\{i\}\), deleting both from \(R\). These pairs are disjoint at each stage. The numbers of pairs at the sixteen stages are
\[
(13668,1357,564,315,215,49,17,7,0,0,0,0,0,0,0,0).
\]
The initial stage pairs the empty face with vertex \(0\). Discard *only this pair* from the matching on the ordinary nonempty face poset, leaving \(0\) as an unmatched vertex. Exactly seven other unmatched faces remain, each with eight vertices, and their masks are
\[
(13110,21930,26214,39322,43606,52428,65280).
\]
There are \(16,191\) retained pairs, one critical \(0\)-simplex, and seven critical \(7\)-simplices. For each nonempty covering pair \(F\subset F\cup\{i\}\), orient its covering edge upward when it is a retained matched pair and downward otherwise. `verify.py` constructs **all** \(218,672\) such edges and exhaustively performs a topological sort on all \(32,390\) nonempty faces. Every face is removed by the sort. Thus the oriented Hasse graph is acyclic, providing a finite complete certificate for Forman's discrete-Morse condition, not a heuristic search.

The discrete-Morse CW theorem now gives a complex with exactly one \(0\)-cell and seven \(7\)-cells and no other cells. Each attaching map has target the \(0\)-skeleton, hence is constant, so that CW complex is a wedge of seven \(7\)-spheres. This proves the **integral homotopy** claim, not only an equality of Betti numbers. The maximum simplex dimension \(11\) does not alter this conclusion.

**3. Full automorphism representation.** A standard-library backtracker assigns images to all sixteen vertices, requiring preservation of adjacency *and nonadjacency* to every already assigned vertex. It finds exactly \(96\) permutations, checks every permutation on every ordered vertex pair, and checks closure and inversion, so it exhausts the full automorphism group. Conjugation gives thirteen classes.

For an automorphism \(g\), a simplex \(F\) contributes its oriented permutation sign if \(gF=F\). Define
\[
L(g)=-1+\sum_{\substack{\emptyset\ne F\in\operatorname{Dom}(M)\\gF=F}}
(-1)^{|F|-1}\operatorname{sgn}(g|_F),
\]
where the \(-1\) is the augmentation-chain trace. The simplicial Hopf trace formula and Step 2 imply \(L(g)=(-1)^7\chi_7(g)=-\chi_7(g)\). Exhaustive enumeration of invariant faces, with orientation signs, therefore determines the character for **every** one of the \(96\) automorphisms. The thirteen conjugacy classes, sorted by their sizes, vertex cycle types, character and lexicographically least representatives, have the following values:

| Class index | Size | Cycle lengths on sixteen vertices | \(\chi_7\) |
|---:|---:|:---|---:|
| 1 | 1 | 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 | 7 |
| 2 | 1 | 2,2,2,2,2,2,2,2 | 7 |
| 3 | 2 | 4,4,4,4 | -1 |
| 4 | 6 | 2,2,2,2,2,2,2,2 | 3 |
| 5 | 6 | 4,4,4,4 | 3 |
| 6 | 8 | 3,3,3,3,1,1,1,1 | 1 |
| 7 | 8 | 6,6,2,2 | 1 |
| 8 | 8 | 12,4 | -1 |
| 9 | 8 | 12,4 | -1 |
| 10 | 12 | 2,2,2,2,2,2,1,1,1,1 | -3 |
| 11 | 12 | 2,2,2,2,2,2,2,2 | 1 |
| 12 | 12 | 8,8 | -1 |
| 13 | 12 | 8,8 | -1 |

This table disambiguates repeated cycle types using the corresponding ordered class representatives printed under `CLASS` in `verification-output.txt`, and thereby defines all character values without a dependency on a graph-automorphism database. The weighted class sum of \(\chi_7\) is zero and the weighted sum of \(\chi_7^2\) is \(384\). Dividing by \(|A|=96\) yields respectively zero fixed vectors and character self-inner product four. A complex representation with self-inner product four has either four distinct multiplicity-one irreducibles or one multiplicity-two irreducible. The latter is impossible here because the total dimension \(7\) is odd. Thus there are four distinct irreducibles, none the trivial representation.

## Verification
`verify.py` uses Python 3.9 or newer and solely the standard library. Running `python verify.py` prints the full face vector, the full stage matching profile, the seven critical-face masks, the exhaustive directed Hasse-graph acyclicity result, mod-two augmented simplicial boundary ranks, the exhaustive \(96\)-automorphism group, thirteen class representatives and character values, and the final sentinel `MOBIUS_KANTOR_DOMINANCE_CERTIFICATE_PASS`.

As an independent homology check, simplicial chain groups are constructed from the same face set in a separate boundary-reduction stage and **all** mod-two augmented boundary matrices are reduced by bitset Gaussian elimination. Ranks in degrees \(0\) to \(11\) are \((1,15,105,455,1349,2827,4149,4059,2396,740,92,4)\), with reduced Betti number \(7\) only in degree \(7\). These ranks corroborate, but are not used as a substitute for, the integral Morse proof.

The graph, facets, matching and character are completely specified by the code and by fixed vertex labels. No numerical approximations, partial homology enumerations or external solvers enter the proof. The class table is rational character information, not a claim of an integral module isomorphism.

## Relationship to prior work
Ehrenborg and Hetyei introduced the dominance complex and proved a sphere theorem for **forests**. Marietti and Testa, in the preprint first public March 12, 2007, develop a core reduction and prove in their Theorem 8.1 that forest dominance complexes collapse to cross-polytope boundaries. The Möbius–Kantor graph has cycles and is not a forest, so these statements do not compute the present complex.

Taylan's archived matching-tree framework includes dominance complexes of **chordal graphs**, a class that excludes the Möbius–Kantor graph because it has induced cycles of length six. Matsushita and Wakatsuki (2023 preprint, 2024 revision) prove the general identity \(\operatorname{Dom}(G)^{\vee}=\mathcal N(\overline G)\) and investigate several cycle, chordal and path-product examples. That duality is an equivalent *formulation*, but by itself supplies neither the seven-sphere decomposition nor the thirteen-class character. Relevant indexed records for the Möbius–Kantor graph address its independence, matching or cut complexes; these have different defining faces and do not imply this dominance result.

## Limitations
The statement is for this particular sixteen-vertex labeled graph. No theorem for all generalized Petersen graphs, arbitrary cubic bipartite incidence graphs, integral irreducible lattice decomposition, or equivariant homotopy equivalence is claimed. The absence of a matching indexed result is not proof of publication priority; unindexed work or a theorem deriving the classification implicitly is a residual risk. Verification is reproducible self-review, not independent certification.

## References
1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, doi:10.1016/j.ejc.2005.04.010, Section 7.
2. M. Marietti and D. Testa, *Cores of simplicial complexes*, arXiv:math/0703351v1 (first public 2007-03-12), especially Section 8, Theorem 8.1. https://arxiv.org/abs/math/0703351
3. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (first public 2015-01-27), especially Sections 2 and 5. https://arxiv.org/abs/1501.06754
4. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (first public 2023-12-05), Theorem 1.1 and Sections 4–6. https://arxiv.org/abs/2312.02639
