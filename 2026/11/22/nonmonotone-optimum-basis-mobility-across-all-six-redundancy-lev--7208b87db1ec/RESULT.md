# Nonmonotone optimum-basis mobility across all six redundancy levels of the Frucht graph

## Finding

Let \(F\) be the twelve-vertex Frucht graph. For a positive integer \(k\), a set \(S\subseteq V(F)\) is a \(k\)-metric generator when every two distinct vertices have different distances to at least \(k\) members of \(S\). A smallest such set is a \(k\)-metric basis.

The graph admits bases at precisely the redundancy levels \(1\le k\le6\). For these levels, their exact minimum cardinalities are \((2,4,5,7,9,11)\), and the numbers of minimum bases are \((2,73,7,35,39,6)\).

Two minimum bases are token-jump adjacent if they differ by deleting one landmark and installing one elsewhere. They are token-slide adjacent if the removed and newly installed vertices are adjacent in \(F\). The complete optimum-configuration enumeration is:

| \(k\) | \(\dim_k(F)\) | Number of bases | Jump edges | Jump component orders | Slide edges | Slide component orders |
| ---: | ---: | ---: | ---: | --- | ---: | --- |
| 1 | 2 | 2 | 1 | 2 | 0 | 1, 1 |
| 2 | 4 | 73 | 314 | 73 | 101 | 68, 3, 1, 1 |
| 3 | 5 | 7 | 7 | 6, 1 | 0 | seven isolated vertices |
| 4 | 7 | 35 | 96 | 34, 1 | 38 | 16, 15, 1, 1, 1, 1 |
| 5 | 9 | 39 | 158 | 39 | 50 | 28, 9, 1, 1 |
| 6 | 11 | 6 | 15 | 6 | 5 | 5, 1 |

Thus jump connectivity of all optimal configurations across increasing fault tolerance follows the **nonmonotone** pattern connected, connected, disconnected, disconnected, connected, connected. In particular, stronger distance-distinguishing redundancy can restore optimum-basis mobility lost at intermediate levels. At \(k=6\), the jump graph is \(K_6\), yet one of these six optimum configurations remains slide-isolated.

The connected jump component radii and diameters, in decreasing order of component sizes, are respectively \((1,1)\) for \(k=1\); \((3,5)\) for \(k=2\); \((2,3)\) for the six-vertex component at \(k=3\); \((3,5)\) at \(k=4\); \((3,4)\) at \(k=5\); and \((1,1)\) at \(k=6\). Singleton components have radius and diameter zero. Complete slide-component metrics are reported by the standalone verifiers.

## Assumptions and scope

All vertices are labelled by the integers \(0,1,\ldots,11\). Define the edge set by the Hamiltonian cycle \(i(i+1\bmod12)\) and the usual LCF chords with signed offsets
\[
(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2).
\]
The resulting simple cubic graph has eighteen edges and is the standard Frucht graph. Distances are ordinary unweighted shortest-path lengths. All \(66\) unordered vertex pairs must be distinguished, including pairs containing one or two selected landmarks. The recolouring graphs contain exactly the minimum-cardinality \(k\)-metric generators, without intermediate nonoptimal configurations. A jump changes exactly one selected vertex to one unselected vertex; a slide additionally requires an edge joining those two vertices.

## Proof

For every unordered pair \(u,v\), form its distinguishing-vertex mask
\[
D(u,v)=\{w\in V(F):d(u,w)\ne d(v,w)\}.
\]
A subset \(S\) is a \(k\)-metric generator if and only if \(|S\cap D(u,v)|\ge k\) for all \(66\) pairs. This equivalence is the defining condition, not an approximation. Breadth-first shortest paths on the explicit twelve-vertex graph supply the sixty-six masks. Direct inspection of their sizes gives \(\min_{u\ne v}|D(u,v)|=6\); the full vertex set attains sixfold separation, while no set can attain sevenfold separation. Hence exactly \(k=1,\ldots,6\) are feasible.

For each of the six levels, enumerate **every one** of the \(2^{12}=4096\) vertex masks. Test all sixty-six conditions with the exact integer population count, then retain exactly those valid masks having the smallest population count. This produces all six minima and all basis counts in the table, ruling out smaller solutions by complete enumeration.

Next, for every retained base \(S\), every selected \(u\in S\), and every unselected \(v\notin S\), form \(T=(S\setminus\{u\})\cup\{v\}\). Keep the unordered edge \(ST\) precisely when \(T\) is also a retained base. For slides, additionally require \(uv\in E(F)\). Each resulting finite graph is fully reconstructed. Breadth-first search from each vertex determines all connected components, each component's radius, and each component's diameter; the enumerations yield the tabulated values. In particular, at level six all six bases are eleven-subsets of a twelve-element set, making every pair jump-adjacent.

There are no unexamined subsets, pairs, permissible changes, or shortest paths in this finite graph. Two independent implementations use separately constructed shortest-path matrices and independently implemented adjacency constructions. The complete claims are about this one labelled graph and its six feasible redundancy levels, not about arbitrary cubic graphs.

## Verification

The self-contained sources `verify_python.py` (Python 3.10 or newer) and `verify_cpp.cpp` (C++17) reproduce all six records and the per-component radius/diameter values. Run `python3 verify_python.py` and `c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp`. Standard output from both must match the bundled `CERTIFICATE.txt` byte-for-byte. The two programs were run and matched. Graph construction was additionally checked for twelve cubic vertices and eighteen edges, and independently compared with the standard Frucht graph generator by an isomorphism test. The checks are exhaustive on the fully specified finite object, not statistical sampling.

## Relationship to prior work

Estrada-Moreno, Rodríguez-Velázquez and Yero introduced \(k\)-metric generators and proved the general criterion for the maximum feasible \(k\), but did not provide this Frucht-graph six-level basis census or its reconfiguration graphs. Subsequent archived work analyzes computational complexity and graph products, rather than these exact optimum configurations. Published work on Frucht-graph zero forcing concerns a different predicate and does not imply these distance-distinguishing bases. Published \(k\)-metric hierarchies of crown graphs address a different family with different constraints and counts. The graph's small order and absence of nontrivial automorphisms makes it a natural benchmark for the interaction of fault-tolerant localization and landmark mobility.

## Limitations

The theorem is a finite exact classification of the Frucht graph, not a monotonicity statement for all graphs. The proof is computer-assisted finite exhaustion; both programs and their exact outputs are supplied for reproducibility. This work does not assert that every feasible intermediate configuration, when allowed to exceed optimum size, is disconnected in the same way. Indexed and full-text literature comparisons cannot rule out every unindexed prior numerical table or equivalent classification, and independent audit remains unperformed.

## References

1. A. Estrada-Moreno, J. A. Rodríguez-Velázquez, I. G. Yero, *The k-metric dimension of a graph*, arXiv:1312.6840 (first public version 24 December 2013), https://arxiv.org/abs/1312.6840 .
2. A. Estrada-Moreno, J. A. Rodríguez-Velázquez and collaborators, archived research on determining the k-metric dimension, arXiv:1401.0342, https://arxiv.org/abs/1401.0342 .
3. A. Estrada-Moreno, J. A. Rodríguez-Velázquez and collaborators, *The k-metric dimension of lexicographic product graphs*, arXiv:1410.7287, https://arxiv.org/abs/1410.7287 .
4. NetworkX, *frucht_graph*, reference generator and graph construction, https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.frucht_graph.html .
5. Publicly indexed independent results on \(k\)-metric bases of crown graphs and on Frucht-graph zero-forcing configurations; their different mathematical constraints do not imply this classification.
