# Three-seed cascade geometry on the Heawood line graph

## Finding
Let \(H\) be the fourteen-vertex Heawood graph, the point–line incidence graph of the Fano plane. Let \(G=L(H)\) be its twenty-one-vertex, four-regular line graph. Under synchronous two-neighbor bootstrap activation on \(G\), the minimum contagious seed size is exactly three. Of the \(\binom{21}{3}=1330\) triples, exactly \(392\) activate every vertex; their completion times are four, five and six rounds, with respective counts \(56,168,168\).

An exact geometric criterion classifies these triples. Interpret each vertex of \(G\) as an edge (flag) of \(H\). Any contagious triple consists of three pairwise vertex-disjoint edges of \(H\). Between the six endpoints of these three seed edges, call an edge of \(H\) joining different seed edges a *cross-edge*. A matching triple succeeds precisely in the following three cases:

1. Three cross-edges, one connecting each pair of seed edges: \(56\) triples, four rounds.
2. Two cross-edges forming a path through the three seed edges, with their endpoints on **opposite ends** of the central seed edge: \(168\) triples, five rounds.
3. Exactly one cross-edge: \(168\) triples, six rounds.

Every other triple fails. In particular, two cross-edges touching the **same endpoint** of the central seed edge do **not** cause complete activation. Thus the probability of complete activation from a uniformly chosen three-vertex seed set is exactly \(392/1330=28/95\).

For independent initial activation of each vertex with probability \(p\), the exact all-seed reliability polynomial is
\[
P(p)=\sum_{k=0}^{21} c_k p^k(1-p)^{21-k},
\]
where \((c_0,\ldots,c_{21})\) equals
\[
(0,0,0,392,4326,18606,53088,115776,203364,293916,352716,352716,293930,203490,116280,54264,20349,5985,1330,210,21,1).
\]
In particular \(P(1/2)=261345/262144\). Among *all* successful seed configurations, six is the largest number of synchronous activation rounds required.

## Assumptions and scope
The Fano-plane points are \(0,\ldots,6\), with seven lines \(\{j,j+1,j+3\}\) (indices modulo seven). The Heawood graph \(H\) has the seven point vertices and seven line vertices, joined by incidence. Its line graph \(G=L(H)\) has one vertex for each of the twenty-one point–line flags; two flags are adjacent if they share a point or share a line. Every vertex of \(G\) has degree four. For an initial seed set \(S\subseteq V(G)\), set \(S_0=S\) and
\[
S_{t+1}=S_t\cup\{v\in V(G):|N_G(v)\cap S_t|\ge2\}.
\]
An activated vertex remains activated. Complete activation means \(S_t=V(G)\) for some finite integer \(t\); completion time is the least such \(t\). All claims refer to this fixed graph and rule, with no randomness beyond the optional initial-seed sampling.

## Proof
**Minimum seed size.** The empty set and singleton seeds cannot grow. For every two flags there are only two geometric possibilities: their underlying Heawood edges meet, or are vertex-disjoint. In the first case, activation fills at most their common three-edge star, and stops. In the second case, the original girth-six incidence graph has at most one cross-edge between the two underlying edges; at most that connecting edge and then two other edges become activated. Thus two seeds activate at most five of twenty-one vertices. A three-seed example is described below, establishing the minimum once the classification is proved.

**Exhaustive geometric classification.** There are \(1330\) unordered triples of flags. Exactly \(686\) contain a pair whose Heawood edges share an endpoint. The remaining \(644\) are three-edge matchings. Two different matching edges admit at most one cross-edge, since two cross-edges would create a four-cycle in \(H\). Hence the cross-edge graph on the three seed edges has zero, one, two, or three edges. With two cross-edges there is a unique central seed edge, and the two attachment points are either the same endpoint or opposite endpoints. These cases are exhaustive.

The independent finite-state recurrence, evaluated for *every* unordered triple, has the following exact census. The code defining the recurrence and enumerating the entire finite domain is included as `check_line_heawood.py`.

| Three-seed geometry | Triple count | Complete activation | Rounds if complete |
|---|---:|---|---:|
| Seed edges not a matching | 686 | No | — |
| Matching, no cross-edge | 84 | No | — |
| Matching, one cross-edge | 168 | Yes | 6 |
| Matching, two cross-edges at opposite ends of central edge | 168 | Yes | 5 |
| Matching, two cross-edges at same end of central edge | 168 | No | — |
| Matching, three cross-edges | 56 | Yes | 4 |

This is an exact finite proof, not a sampling estimate: each of the \(\binom{21}{3}\) subsets is generated once, and each synchronous update computes all twenty-one neighbor counts by integer bit operations until an absorbing configuration occurs. Independently, `verify_line_heawood.cpp` realizes the Fano plane by cyclic triples, checks all \(2^{21}\) possible initial sets, and obtains the identical three-seed counts and completion times. The Python checker constructs the Fano plane by kernels of nonzero linear functionals on \(\mathbb F_2^3\), giving a distinct incidence representation. Both model constructions have twenty-one flags, each with four neighbors.

**The exact random-seed law.** Since the C++ recurrence visits each of the \(2^{21}\) initial masks exactly once, the number \(c_k\) of successful seeds with size \(k\) is precisely its reported integer coefficient. Weighting each size-\(k\) set by \(p^k(1-p)^{21-k}\) gives the displayed polynomial, and summing its coefficients gives \(P(1/2)=261345/262144\). The same finite-state census records a maximum successful completion time of six rounds.

## Verification
With a C++17 compiler, run `g++ -std=c++17 -O2 verify_line_heawood.cpp -o verify_line_heawood` and then `./verify_line_heawood`. This enumerates all \(2^{21}=2097152\) initial configurations and reports the full cardinality polynomial and maximum completion time. Run `python3 check_line_heawood.py` with Python 3.8 or newer. It independently checks the six three-seed geometric classes, their exact cardinalities and their activation times, using no third-party dependencies. The integer tables are asserted inside the Python program and reconstructed separately by the C++ program. Neither computation uses floating point arithmetic.

## Relationship to prior work
Classical two-neighbor bootstrap percolation is defined in the work of Balogh and Pittel on random regular graphs and in Freund, Poloczek and Reichman's work on contagious sets. Marcilon and Sampaio study maximum infection time on grid graph families. These results supply the model and motivating questions but not the fixed Fano-incidence line-graph classification or the complete twenty-one-site reliability polynomial. Gerbner and collaborators study a *different* point-only line-percolation rule in finite projective planes: an activated line then activates all its constituent points. That operation is not the two-neighbor flag activation rule treated here. Other studies of the Heawood graph's minimum feedback vertex sets and zero forcing concern different graphs or propagation rules, and cannot be identified with the present finding merely from numerical coincidences. The exact Fano-plane incidence geometry itself is standard and not claimed as new.

## Limitations
This theorem is a complete finite-size result for the specified twenty-one-vertex graph. It does not establish any theorem for line graphs of larger incidence structures, probabilistic transmission failure, heterogeneous vertex thresholds, asynchronous update durations, or spectral/mixing properties. The exact rational counts and geometric criterion are established with a fully specified finite exhaustive certificate, rather than a general symbolic proof for arbitrary graph order. Historical priority is assessed against the accessible literature and indexed results, not proved absolutely; an unindexed equivalent census may exist.

## References
- J. Balogh and B. G. Pittel, *Bootstrap percolation on the random regular graph*, Random Structures & Algorithms 30 (2007), 257–286, first published 2006-12-13. https://doi.org/10.1002/rsa.20158
- D. Freund, M. Poloczek, and D. Reichman, *Contagious Sets in Dense Graphs*, arXiv:1503.00158 (2015). https://arxiv.org/abs/1503.00158
- T. Marcilon and R. Sampaio, *The maximum time of 2-neighbour bootstrap percolation in grid graphs and some parameterized results*, arXiv:1508.06847 (2015). https://arxiv.org/abs/1508.06847
- D. Gerbner, B. Keszegh, G. Mészáros, B. Patkós and M. Vizer, *Line Percolation in Finite Projective Planes*, arXiv:1608.00531 (2016). https://arxiv.org/abs/1608.00531
- E. W. Weisstein, *Heawood Graph*, MathWorld. https://mathworld.wolfram.com/HeawoodGraph.html
