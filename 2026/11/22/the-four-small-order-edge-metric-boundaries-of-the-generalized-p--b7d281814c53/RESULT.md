# The four small-order edge-metric boundaries of the generalized Petersen family \(P(n,3)\)

## Finding
For every integer \(n\ge7\), the edge metric dimension of the simple cubic generalized Petersen graph \(P(n,3)\) is
\[
\beta_e(P(n,3))=\begin{cases}3,&n\in\{9,10\},\\4,&n=7,8\text{ or }n\ge11.\end{cases}
\]
At the four formerly excluded orders \(n=7,8,9,10\), the respective numbers of minimum edge-resolving landmark subsets are exactly \(469,368,18,160\). Hence the three-landmark exceptions form a finite two-order island immediately before the published stable range.

## Assumptions and scope
For integers \(n\ge7\), set \(V=\{u_i,v_i: i\in\mathbb Z/n\mathbb Z\}\). Give \(P(n,3)\) the outer edges \(\{u_i,u_{i+1}\}\), spokes \(\{u_i,v_i\}\), and inner edges \(\{v_i,v_{i+3}\}\), with indices cyclic. These are \(3n\) distinct undirected edges. The distance from landmark vertex \(w\) to edge \(e=\{a,b\}\) is \(\delta(w,e)=\min(d(w,a),d(w,b))\), with \(d\) ordinary shortest-path graph distance. A set \(S\subseteq V\) resolves the edges if, for every two distinct edges, some \(w\in S\) gives different values of \(\delta\). No weighting, vertex-visibility or edge-to-edge distance is used.

## Proof
For each \(n\in\{7,8,9,10\}\) take the explicitly specified \(2n\)-vertex, \(3n\)-edge graph, obtain the integer shortest-path matrix by breadth-first search, and form its vertex-by-edge matrix \(M\), where \(M[w,e]=\delta(w,e)\). For any \(k\)-subset \(S\) of landmark rows, it resolves precisely when the \(3n\) column vectors of \(M\) restricted to \(S\) are all distinct. The accompanying `verify_exhaustive.cpp` enumerates **every** subset of cardinalities two, three and four in lexicographic order and directly compares all pairs of edge signatures. The exhaustive counts are:

| \(n\) | Resolving pairs | Resolving triples | Resolving four-sets |
|---:|---:|---:|---:|
| 7 | 0 | 0 | 469 |
| 8 | 0 | 0 | 368 |
| 9 | 0 | 18 | 1359 |
| 10 | 0 | 160 | 3200 |

Thus each of the four boundary minima follows: existence is exhibited by a positive count, and smaller candidate sizes fail, because resolving is upward-closed under adjoining landmarks. In the index convention where integers \(0,\ldots,n-1\) denote \(u_0,\ldots,u_{n-1}\), and integers \(n,\ldots,2n-1\) denote \(v_0,\ldots,v_{n-1}\), explicit resolving witnesses are respectively \(\{0,1,2,7\}\), \(\{0,1,2,11\}\), \(\{0,12,13\}\), and \(\{0,2,13\}\). The 2020 theorem of Wang, Wang and Zhang independently proves \(\beta_e(P(n,3))=4\) for every \(n\ge11\), closing the stated infinite-range formula without extrapolating finite enumeration.

## Verification
Compile `verify_exhaustive.cpp` with `g++ -O2 -std=c++17 verify_exhaustive.cpp -o verify_gp3` and run `./verify_gp3`; exact expected output is embedded in `cpp_results.txt`. Independently run `python verify_networkx.py` (requires NetworkX), which constructs the edges independently, uses NetworkX all-pairs shortest paths, and tests every row-subset by signature uniqueness; its output is `python_results.txt`. The two programs agree on all four minimum subset counts and witnesses, using separate edge-ordering and test implementations. The C++ checker also records all resolving 4-subsets for the two three-landmark cases. These are finite exhaustive tests for exactly the four orders, not an infinite proof.

## Relationship to prior work
Wang, Wang and Zhang, arXiv:2005.08038 (first publicly posted 2020-05-16, later in Journal of Combinatorial Optimization), prove the stable \(n\ge11\) part but do not cover the four orders enumerated here. The 2023 article *Edge Resolvability in Generalized Petersen Graphs* studies \(GP(2\ell+1,\ell)\) mainly for \(\ell\ge11\) and \(GP(2\ell,\ell)\) for large \(\ell\), not the present fixed-inner-step small-order census; the family overlaps in its graph notation at \(n=7\), but its published main statements do not supply the minimum-set counts. The 2018 generalized-Petersen work addresses fixed steps one and two, with a lower bound for other steps. Distinguish these ordinary edge-metric results from vertex metric dimension, size-restricted edge resolving variants and double generalized Petersen graphs.

## Limitations
The finite counts are exhaustive only for \(7\le n\le10\). The classification for \(n\ge11\) uses the separately credited published theorem. This does not claim a complete edge-resolving polynomial or automorphism orbit census. Literature search does not establish absolute priority; independent mathematical auditing has not been performed.

## References
- D. G. L. Wang, M. M. Y. Wang, S. Zhang, *The edge metric dimension of the generalized Petersen graph \(P(n,3)\) is 4*, arXiv:2005.08038 (first posted 2020-05-16); Journal of Combinatorial Optimization 43 (2022), 460–496, doi:10.1007/s10878-021-00780-8.
- *Edge Resolvability in Generalized Petersen Graphs*, Symmetry 15 (2023), article 1633, doi:10.3390/sym15091633.
- V. Filipovic, A. Kartelj, J. Kratica, *Edge metric dimension of some generalized Petersen graphs*, arXiv:1807.00580 (2018).
