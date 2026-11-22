# Six perfect matchings govern the \(6\)-metric bases of the Petersen line graph

## Finding

Let \(P\) be the Petersen graph and let \(H=L(P)\) be its line graph, with fifteen vertices corresponding to the fifteen edges of \(P\). For \(1\leq k\leq 10\), let \(\dim_k(H)\) be the minimum cardinality of a subset \(S\) of \(V(H)\) such that every pair of different vertices \(u,v\) is distinguished by at least \(k\) members of \(S\), meaning \(d_H(s,u)\ne d_H(s,v)\). The **entire exact sequence**, including the number of vertex-labeled minimizing sets, is:

| \(k\) | \(\dim_k(H)\) | Number of minimum \(k\)-metric bases |
|---:|---:|---:|
| 1 | 4 | 960 |
| 2 | 5 | 408 |
| 3 | 7 | 3,480 |
| 4 | 8 | 1,815 |
| 5 | 9 | 375 |
| 6 | 10 | 6 |
| 7 | 12 | 455 |
| 8 | 13 | 105 |
| 9 | 14 | 15 |
| 10 | 15 | 1 |

There is no \(k\)-metric generator for \(k\geq11\). At \(k=6\), the six minimum ten-element bases are **exactly the complements of the six perfect matchings of the original Petersen graph**, regarding a matching as five vertices in \(H\). For each \(7\leq k\leq10\), **every** \((k+5)\)-vertex subset of \(H\) is a minimum \(k\)-metric basis. Thus the two successive sharp jumps occur between \(k=2,3\) and \(k=6,7\), and the six-fold matching rigidity at the latter boundary abruptly gives way to universal optimality.

## Assumptions and scope

All graphs are finite, simple, connected, undirected, unweighted, with shortest-path distance. The Petersen graph is the generalized Petersen graph \(GP(5,2)\). An explicit labeling of its ten vertices is given by the fifteen edges below, indexed consecutively from zero; these fifteen indices are the vertices of \(H\):

```
(0,1), (0,4), (0,5), (1,2), (1,6),
(2,3), (2,7), (3,4), (3,8), (4,9),
(5,7), (5,8), (6,8), (6,9), (7,9)
```

Two indices are adjacent in \(H\) precisely if their corresponding edges share an endpoint in \(P\). This presentation is specified completely and has no dependence on external graph packages. All counts distinguish subsets of the fifteen *labeled* vertices and are not quotiented by graph automorphisms. The theorem concerns the line-graph metric, not the original Petersen metric nor vertex-to-edge metric distance on \(P\).

## Proof

**1. The bisector certificate.** For any distinct \(u,v\in V(H)\), define the equidistance set
\[
E(u,v)=\{w\in V(H):d_H(w,u)=d_H(w,v)\}.
\]

The fifteen indexed original edges determine a fixed four-regular graph \(H\). Breadth-first search from each index computes its full \(15\times15\) integer distance table. The following finite statements are verified by direct integer loops in *both* standalone implementations in this package:

- There are \(\binom{15}{2}=105\) unordered pairs \(\{u,v\}\).
- Their 105 bisectors \(E(u,v)\) are pairwise distinct.
- **Every one of the 105 bisectors has exactly five vertices.** Consequently, every pair has exactly ten distinguishing vertices, so the maximum possible \(k\) is exactly ten.

These assertions are exact certificates for this one finite graph: the algorithms build each adjacency from the fifteen original edges, compute all shortest paths independently, and test all 105 pair cases. No inference from a sample is made.

**2. From bisectors to robustness.** For every vertex subset \(S\), its guaranteed number of distinguishing landmarks is
\[
\rho(S)=\min_{u\neq v}|S\setminus E(u,v)|
=|S|-\max_{u\neq v}|S\cap E(u,v)|.
\]

Therefore \(S\) is a \(k\)-metric generator exactly when \(\rho(S)\ge k\). The code enumerates **all 32,768 subsets** \(S\subseteq V(H)\), computes \(\rho(S)\) from all 105 exact bisectors, and keeps the smallest size and count for every \(k\). The two separately written algorithms reproduce and assert precisely the ten rows of the displayed table. Every lower bound for \(1\le k\le6\), and the exact counts of optima, are thereby supported by complete exhaustive integer certificates, not only upper-bound constructions.

**3. Six-fold perfect-matching rigidity.** At level \(k=6\), exactly six ten-vertex subsets satisfy \(\rho(S)\ge6\). Their five-element complements are computed explicitly. Independently, the code exhausts the \(\binom{15}{5}=3003\) five-subsets of original edges and retains those that cover each of the ten Petersen vertices once. There are exactly six such perfect matchings, and the two collections of five-subsets are identical. This proves the geometric interpretation, not merely coincidence in the counts.

**4. Universal high-robustness phase.** Since each bisector has five vertices, any \(S\) of size \(k+5\) distinguishes every vertex pair at least \(k\) times. Exhaustive enumeration additionally proves that no eleven-subset is \(7\)-resolving: equivalently every eleven-subset contains at least one entire five-element bisector (all \(\binom{15}{11}=1365\) possibilities are checked). Hence \(\dim_7(H)=12\). In every graph, deleting one member of a \((k+1)\)-metric generator leaves a \(k\)-metric generator, giving \(\dim_{k+1}(H)\ge\dim_k(H)+1\) for finite values. Starting at \(k=7\), the eleven-set obstruction and this monotonicity give the lower bound \(\dim_k(H)\ge k+5\), matching the universal construction through \(k=10\). Every \((k+5)\)-subset then qualifies, yielding \(\binom{15}{k+5}\) minima.

## Verification

Run in one directory after extracting the accompanying files:

```
python3 -S verify_petersen_python.py
g++ -std=c++17 -O2 verify_petersen_cpp.cpp -o verify_cpp
./verify_cpp
```

Both scripts recompute the entire line graph from the literal Petersen edge list, perform integer breadth-first shortest paths, construct the 105 equalizer sets, and exhaust all \(2^{15}\) potential landmark configurations. They independently check the exact ten-element cardinality sequences and perfect-matching complements. The Python implementation also separately checks that every eleven-set contains a bisector. Successful captured outputs are supplied as `verify_petersen_python.out` and `verify_petersen_cpp.out`. The scripts use no network, external data, or third-party modules. A compiler supporting C++17 is required for the second implementation.

## Relationship to prior work

The general \(k\)-metric dimension definition and complexity theory are established by Yero, Estrada-Moreno and Rodríguez-Velázquez (first posted 2014-01-01). Beardon and Rodríguez-Velázquez (2016) introduce the bisector formulation and compute the complete dimension sequence **of the Petersen graph itself**, not its line graph. In particular the present result's full sequence is not an implication of that different graph's results. Bailey's earlier table addresses ordinary metric dimension of small distance-regular graphs, not the \(k\)-level minimizer counts for this fifteen-vertex line graph. Guo and coauthors (2020) study fault-tolerant resolving bases of **line graphs of necklace and prism graphs**, not the Petersen line graph. A published complete zero-forcing-set classification of the Petersen line graph and an exact locating-dominating-code classification concern distinct, non-equivalent invariants; neither implies the present distance-signature conditions. The bisector size-five and all-105-distinct certificate, the complete robust-dimension sequence, and especially the six-perfect-matching minimum-basis characterization are the central new finite observations.

## Limitations

The theorem concerns exactly \(L(P)\), not arbitrary line graphs or all generalized Petersen graphs. The finite exhaustive proof has fixed and fully accessible input but is computational, rather than a symbolic parameter-uniform proof. It does not claim historical uniqueness: unindexed work or an uninspected full text could contain the same exact table or equivalent classification. Ordinary scholarly independent validation has not been performed.

## References

1. I. G. Yero, A. Estrada-Moreno and J. A. Rodríguez-Velázquez, *On the complexity of computing the \(k\)-metric dimension of graphs*, first public arXiv submission 2014-01-01. https://arxiv.org/abs/1401.0342
2. A. F. Beardon and J. A. Rodríguez-Velázquez, *On the \(k\)-metric Dimension of Metric Spaces*, first arXiv submission 2016-03-13; Example 5.4 treats the Petersen graph. https://arxiv.org/abs/1603.04049
3. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, first public arXiv submission 2013-12-17. https://arxiv.org/abs/1312.4973
4. X. Guo, M. Faheem, Z. Zahid and W. Nazeer, *Fault-Tolerant Resolvability in Some Classes of Line Graphs*, first published 2020-09-26. https://doi.org/10.1155/2020/1436872
5. *The minimum zero-forcing exchange graph of the Petersen line graph* (2026), different invariant. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-minimum-zero-forcing-exchange-graph-of-the-petersen-line-gra--4e6c2c9b2a97
6. *Petersen edge-location domination: ten complete bipartite obstructions* (2026), different invariant. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-petersen-edge-location-domination-ten-complete-bipartite-obstruc--5291df073dcf
