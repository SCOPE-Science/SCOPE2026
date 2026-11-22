# Three geometric types and a uniform seven-move exchange radius for weak-total metric bases of \(GP(8,3)\)

## Finding
Let \(G=GP(8,3)\), the sixteen-vertex Möbius–Kantor graph. Use the **resolving** convention for a weak-total resolving set: a vertex set \(W\) must resolve every pair of vertices by graph distances, and for every selected vertex \(w\in W\) and unselected vertex \(x\notin W\), some other selected vertex distinguishes \(w\) from \(x\).

The weak-total metric dimension of \(G\) is exactly \(5\). There are exactly \(192\) minimum weak-total resolving sets, partitioned into three orbits under the full automorphism group of order \(96\). The three orbits have sizes \(48,48,96\), distinguished by the induced subgraphs on the five selected vertices: respectively five isolated vertices, a three-vertex path with two isolates, and the disjoint union of a three-vertex path and an edge.

Under a *token jump*, one selected vertex may be replaced by one unselected vertex, with the resulting set still a minimum weak-total resolving set. The resulting \(192\)-vertex exchange graph is connected, five-regular, has \(480\) edges and diameter and radius both equal to \(7\). Every state has the same ordered distance profile
\[
(1,5,14,40,74,42,14,2)
\]
for distances \(0\) through \(7\), despite the three distinct host-graph symmetry orbits. Its exact maximum shortest-path relocation cost is thus seven jumps.

For context, the stronger fault-tolerant resolving condition has minimum cardinality \(6\) with exactly \(336\) minima on this graph. The complete inclusion-minimal weak-total spectrum has cardinality counts \(192,1080,192,2\) at set sizes \(5,6,7,8\), respectively. The cardinality-generating polynomial of **all** resolving weak-total sets is
\[
\begin{aligned}
R_{wt}(G;z)={}&192z^{5}+2712z^{6}+8288z^{7}+11966z^{8}\\
&+11328z^{9}+8008z^{10}+4368z^{11}+1820z^{12}\\
&+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]

## Assumptions and scope
Vertices are \(u_i,v_i\) for \(i\in\{0,\ldots,7\}\), with indices interpreted modulo \(8\). Edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). The checker represents \(u_i\) by integer \(i\) and \(v_i\) by integer \(i+8\). All graph distances are ordinary unweighted shortest-path distances. The conclusion concerns this specific finite simple undirected graph, not all generalized Petersen graphs.

The word *weak-total* follows the original 2012 definition that requires resolution. A 2016 article studies a strictly weaker **pure** weak-total condition that drops the resolving requirement, and explicitly acknowledges this distinction in its Discussion. The latter is not the invariant evaluated here. In particular, the eight antipodal vertex pairs satisfy the pure two-landmark criterion on this graph, but none of those two-element sets resolves it.

## Proof
Fix a selected subset \(W\) and for every unordered vertex pair \(\{a,b\}\) define the separating mask
\[
D(a,b)=\{t\in V(G): d(a,t)\ne d(b,t)\}.
\]
Then the defining conditions are equivalent to requiring \(\lvert W\cap D(a,b)\rvert\ge1\) for *every* pair, and the stronger \(\lvert W\cap D(a,b)\rvert\ge2\) whenever exactly one of \(a,b\) belongs to \(W\). The stronger bound is necessary because the selected endpoint itself always distinguishes the pair and cannot be its own backup. It is sufficient because at least one additional selected witness remains. This is an exact finite characterization, not a heuristic.

The property is upward closed: if a new landmark is added, old selected/unselected comparisons retain their witnesses, while any comparison with the newly selected landmark and a remaining unselected vertex has a witness among the old landmarks by the original resolving property. Therefore a satisfying subset is inclusion-minimal precisely when deleting any one selected vertex violates the property.

The C++17 checker constructs all \(24\) edges from the three displayed edge rules, independently computes the \(16\times16\) distance matrix by breadth-first search, constructs all \(120\) pair-separation masks, and tests all \(2^{16}=65536\) subsets using the preceding exact criterion. This proves the minimum size, every cardinality coefficient and the inclusion-minimal spectrum. Applying the two-witness condition to *all* vertex pairs, including pairs of unselected vertices, proves the reported fault-tolerant minimum and count.

An independent Python checker reconstructs the graph and distances using a distance-code definition, checks all \(65536\) subsets, and enumerates the full \(96\)-element automorphism group by graph isomorphism. It proves the three disjoint orbit sizes and induced shapes. The canonical orbit representatives in integer vertex labels are:

| Induced structure | Representative \(W\) | Orbit size |
|---|---|---:|
| Five isolates | \(\{2,4,7,8,9\}\) | 48 |
| Three-vertex path and two isolates | \(\{0,2,7,8,9\}\) | 48 |
| Three-vertex path and one edge | \(\{0,2,3,8,10\}\) | 96 |

For exchange geometry, the Python checker builds precisely those edges \(W,W'\) between minimum sets satisfying \(\lvert W\triangle W'\rvert=2\), then runs breadth-first search from every one of the \(192\) states. Each state is confirmed to reach all others with distance counts \((1,5,14,40,74,42,14,2)\); in particular the graph is connected, five-regular and self-centered with sharp diameter \(7\). These finite exhaustive computations constitute the exact certificate for the stated finite claims.

## Verification
Run `python3 check_python.py` with NetworkX installed, or compile `check_cpp.cpp` using `c++ -std=c++17 -O2 -Wall -Wextra check_cpp.cpp -o check_cpp` and execute `./check_cpp`. Each implementation builds the graph from its edge rules rather than loading any precomputed data. The C++ checker uses pairwise bitmasks, whereas the Python checker uses distance-code comparisons. Both enumerate the full \(65536\)-subset space. The Python program additionally computes automorphisms and every exchange-graph distance. All assertions passed on the decoded files in this package.

## Relationship to prior work
Javaid, Iftikhar and Salman (2012) introduce weak-total resolvability with a resolving-set condition and compare it with fault-tolerant bases; Javaid et al. (2014, arXiv:1408.0649v1) investigate trees and general bounds, including the two-coordinate code criterion. Neither inspected source gives the complete Möbius–Kantor classification.

Casel, Estrada-Moreno, Fernau and Rodríguez-Velázquez (2016) study what they explicitly rename *pure weak-total resolvability* in their Discussion: they do not insist on outside/outside resolution. Their results on general bounds, fans, wheels, Cartesian and lexicographic products cannot be substituted into the resolving version here. They do not classify \(GP(8,3)\) by optimum shapes and exchange geometry. Previously indexed results on Möbius–Kantor identifying codes, ordinary zero forcing, and secure domination use non-equivalent predicates, so even matching symmetry orders or exchange parameters do not imply this result.

## Limitations
This is a finite exhaustive theorem about one graph, not an infinite family. The proof is computationally complete only because all sixteen-vertex subsets and all automorphisms/exchange states are exhaustively traversed. The code requires NetworkX for one of two independent implementations. No formal proof assistant or external independent audit was used. Unindexed historical computations or unpublished results could still predate the classification; searches do not establish absolute global priority.

## References
- I. Javaid, F. Iftikhar, and M. Salman, *Total resolvability in graphs*, Middle-East Journal of Scientific Research 11 (2012), 1649–1658, DOI: 10.5829/IDOSI.MEJSR.2012.11.12.1750.
- I. Javaid, M. Salman, M. Murtaza, F. Iftikhar, and M. Imran, *Weak total resolving sets in graphs*, arXiv:1408.0649v1, publicly dated 2014-08-04, https://arxiv.org/pdf/1408.0649.
- K. Casel, A. Estrada-Moreno, H. Fernau, and J. A. Rodríguez-Velázquez, *Weak total resolvability in graphs*, Discussiones Mathematicae Graph Theory 36 (2016), 185–210, DOI: 10.7151/dmgt.1853; notably Discussion §6 distinguishes pure and resolving definitions.
- E. W. Weisstein, *Möbius-Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html (graph identification and classical structure).
