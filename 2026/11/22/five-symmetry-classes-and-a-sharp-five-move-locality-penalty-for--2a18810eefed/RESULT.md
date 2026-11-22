# Five symmetry classes and a sharp five-move locality penalty for Pappus-graph power domination

## Finding
Let \(G\) be the eighteen-vertex Pappus graph defined below. The minimum power-domination number is \(\gamma_P(G)=3\). There are exactly \(486\) minimum power-dominating three-sets. Under one-vertex token jumping (TJ), their reconfiguration graph is connected, has \(7128\) edges, and has radius and diameter \(3\). Under edge-constrained token sliding (TS), the same \(486\) states form a connected graph with \(1620\) edges, radius \(7\), and diameter \(8\).

Exactly \(54\) states have TS eccentricity \(7\); the other \(432\) have TS eccentricity \(8\). The full family splits into five orbits of sizes \(108,108,108,108,54\) under an explicit \(216\)-element group of graph automorphisms. The five corresponding (orbit size, TJ degree, TS degree, TS eccentricity) profiles are
\[
(108,28,7,8),\ (108,29,8,8),\ (108,29,6,8),\ (108,28,5,8),\ (54,36,8,7).
\]

For all unordered pairs of distinct minimum sets \(S,T\), the distribution of \(d_{\mathrm{TS}}(S,T)-d_{\mathrm{TJ}}(S,T)\) is:

| Extra slides | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Number of pairs | 9423 | 29808 | 42174 | 28026 | 7938 | 486 |

In particular, the **sharp locality penalty is five**, and exactly \(486\) pairs attain it. The unconstrained TJ distance equals its Johnson-graph lower bound \(|S\setminus T|\) except for exactly \(162\) unordered pairs; each exceptional pair has lower bound \(2\) and actual distance \(3\).

## Assumptions and scope
The graph is finite, simple, and undirected. Let \(\mathbb F_3=\{0,1,2\}\). Its vertices are nine points \(P_{x,y}\) for \(x,y\in\mathbb F_3\), and nine lines \(X_a,Y_b,D_c\) for \(a,b,c\in\mathbb F_3\). The edges are exactly \(P_{x,y}X_x\), \(P_{x,y}Y_y\), and \(P_{x,y}D_{y-x}\), with subscripts read modulo three. This is the incidence graph of the affine plane of order three with one parallel class removed; the checkable LCF representation \([5,7,-7,7,-7,-5]^3\) and an explicit isomorphism are supplied in `verify_lcf.py`.

For all vertex subsets \(S\), first observe \(N[S]\). Repeatedly observe any vertex that is the unique still-unobserved neighbor of an observed vertex. A **power-dominating set** is an \(S\) for which this process eventually observes every vertex. Minimum means minimum cardinality, not inclusion minimality. The TJ graph has one vertex per minimum set and an edge if the two sets differ by replacing one selected vertex. The TS graph requires the removed and added vertices to be adjacent in \(G\). Both graphs use *only* minimum power-dominating sets as intermediate states.

For reproducible vertex labels, index \(P_{x,y}\) by \(3x+y\), \(X_a\) by \(9+a\), \(Y_b\) by \(12+b\), and \(D_c\) by \(15+c\). Thus all reported sets in numeric notation refer to the same labelled graph.

## Proof
This is a complete finite computational proof with small explicit search spaces, and the two independent programs are part of the proof. The decisive algorithms are described here so their exhaustiveness does not rely on unexplained output.

**Minimum solutions.** A forced observation step is monotone: observing an additional vertex cannot invalidate a previous observation. Because there are exactly \(18\) vertices, the closure procedure terminates after at most \(18\) strict expansions. At a fixed point it is equivalent to the standard power-domination closure; in particular, a set succeeds if and only if this fixed point comprises all \(18\) vertices. Enumerating all \(\binom{18}{1}=18\) singletons and \(\binom{18}{2}=153\) pairs gives no successful set. Enumerating all \(\binom{18}{3}=816\) triples gives exactly \(486\) successful triples. This proves both the minimum size and the exact state set without assuming any untested patterns.

**Transitions.** Every move between distinct three-element sets is uniquely characterized by a removed element \(u\in S\setminus T\) and an inserted element \(v\in T\setminus S\). Therefore \(|S\triangle T|=2\) is the necessary and sufficient TJ test, and adjoining the condition \(uv\in E(G)\) is the necessary and sufficient TS test. Exhaustively applying these predicates to every state pair yields, respectively, \(7128\) and \(1620\) unordered edges. No other allowed transitions exist.

**Shortest paths and bounds.** For each state \(s\), breadth-first search starts with the singleton reached set \(\{s\}\), and at each subsequent level adds precisely all adjacent states not previously reached. Induction on the level proves that first arrival gives the exact shortest-path length; the procedure also decides connectivity. Computing all \(486\) BFS rows in both graphs proves the claimed radii, diameters, eccentricity frequencies and all-pairs histograms. In particular, the TJ distance histogram at distances \(1,2,3\) is \((7128,43902,66825)\), while the TS distance histogram at distances \(1,2,3,4,5,6,7,8\) is \((1620,6480,18063,31644,33912,20358,5454,324)\). Each histogram sums to \(\binom{486}{2}=117855\). Comparing the distances pairwise proves the exact penalty distribution and the \(162\) TJ exceptions.

The worst-case penalty is realized, for example, by \(S=\{0,1,3\}\) and \(T=\{4,11,14\}\): \(d_{\mathrm{TJ}}(S,T)=3\) and \(d_{\mathrm{TS}}(S,T)=8\). A shortest TJ path is \(\{0,1,3\}\), \(\{0,1,11\}\), \(\{1,11,14\}\), \(\{4,11,14\}\). A shortest TS path is \(\{0,1,3\}\), \(\{1,3,12\}\), \(\{3,12,13\}\), \(\{10,12,13\}\), \(\{6,10,13\}\), \(\{10,11,13\}\), \(\{4,10,11\}\), \(\{4,5,11\}\), \(\{4,11,14\}\). Every state in these paths passes the exact power-domination test. As an example of the TJ detour, \(\{0,1,3\}\) and \(\{0,2,4\}\) share one vertex but require three TJ moves instead of two.

**Symmetries.** `verify_affine.py` supplies five explicit permutations, verifies that each preserves every edge, and generates their composition-closure of exactly \(216\) distinct automorphisms. Acting on all \(486\) minimum sets partitions them into exactly five disjoint orbits, with the profiles given in the finding. This also identifies the \(54\) TS centers as a single symmetry orbit, rather than merely a coincidental count.

## Verification
Run `python3 verify_affine.py` and `python3 verify_lcf.py` from the same directory. Both use only the Python standard library. The first works with integer neighborhood bitmasks, simultaneous forcing waves, generated group symmetries, and per-state BFS. The second independently constructs the standard LCF graph, checks a full explicit incidence-graph isomorphism, applies a sequential fair forcing rule, builds transitions by scanning all unordered state pairs, and independently performs every BFS. Both assert the complete results above, rather than merely printing sample values. The computations cover all \(816\) triples, both smaller cardinalities, all legal exchanges, and all \(117855\) unordered pairs of distinct optimal sets.

## Relationship to prior work
Bjorkman, Bozeman, Ferrero, Flagg, Grood, Hogben, Jacob, and Reinhart initiated a general framework for power-domination reconfiguration, including TJ graphs and families of examples (first public preprint 2022-01-05). This finite result specializes to a different natural graph and, unlike a general reconfiguration definition, determines its entire minimum-sensor geometry, the TS distances and the sharp TJ-versus-TS penalty. The 2023 shortest-dominating-set reconfiguration work treats ordinary domination rather than power domination, and trees and interval graphs rather than this cubic incidence graph. A separate exact Pappus study of *semitotal* domination involves a different feasible-family definition and does not imply the power-domination closure test or these reconfiguration distances. Exact older equivalent finite computations cannot be ruled out solely by indexed search.

## Limitations
The theorem concerns exactly the labelled Pappus graph, with two specified relocation rules; it does not imply analogous formulas for all incidence graphs, cubic symmetric graphs, other budgets, or ordinary domination. It is a computer-assisted complete finite classification rather than a general symbolic theorem. The reproducibility programs provide a transparent exhaustive certificate; no formal proof assistant or independent human mathematical audit was performed. An unindexed earlier computation may exist.

## References
1. B. Bjorkman et al., *Power domination reconfiguration*, first public arXiv preprint 2022-01-05, https://arxiv.org/abs/2201.01798 .
2. J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv 2023-07-20, https://arxiv.org/abs/2307.10847 .
3. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html .
4. An exact Pappus-graph semitotal-domination reconfiguration study (different graph predicate), published repository record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-nine-frozen-total-codes-and-a-mobile-semitotal-domination-sector--229c8647b6e8 .
