# A three-sphere in the Desargues middle-level Vietoris–Rips filtration

## Finding

Let \(G\) be the Desargues graph \(\operatorname{GP}(10,3)\), and give its vertex set the graph shortest-path metric. The **inclusive** Vietoris–Rips complex \(K_r=\operatorname{VR}_{\le r}(V(G))\) has the following complete integral homotopy filtration:

\[
K_r\simeq
\begin{cases}
\bigvee^{19}S^0, & 0\le r<1,\\
\bigvee^{11}S^1, & 1\le r<2,\\
\bigvee^{19}S^2, & 2\le r<3,\\
S^3, & 3\le r<4,\\
S^9, & 4\le r<5,\\
\ast, & r\ge5.
\end{cases}
\]

The degree-zero notation in the first line means twenty isolated vertices. The previously known scale-two wedge is included for completeness but **is not claimed as novel**. The new substantive assertion is the **scale-three three-sphere**, proved by an exact acyclic matching on its entire face poset, together with the complete integral persistence conclusion.

Precisely, the positive-degree reduced integral intervals are eleven \([1,2)\) intervals in degree one, nineteen \([2,3)\) intervals in degree two, a single \([3,4)\) interval in degree three, and a single \([4,5)\) interval in degree nine. There are nineteen reduced degree-zero intervals \([0,1)\). Every reduced integral homology group is free and all nonzero within-stage persistence maps are the identity under the canonical identification of the unchanged complex.

## Assumptions and scope

The vertex set is \(\{u_i,v_i: i\in\mathbb Z/10\mathbb Z\}\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), where subscripts are reduced modulo ten. Vertex labels for the reproducibility code are \(u_i=i\) and \(v_i=10+i\). Distances are shortest-path integers (not Euclidean chordal lengths or an intrinsic Čech radius). There are no unstated genericity assumptions. The filtration uses closed thresholds, so a simplex is present exactly when every pair of its vertices has distance at most \(r\).

There is also an exact isometry to the size-two and size-three subsets of \([5]\) with symmetric-difference distance. The included verifier provides all twenty labeled subsets and checks all 400 ordered pair distances against the graph metric. Consequently the scale-two case lies within the scope of Feng–Nukala's prior theorem, which explicitly determines its 19 two-spheres.

## Proof

**Graph metric and end stages.** Breadth-first search on the explicit cubic graph establishes that its 190 unordered vertex pairs occur at distances 1 through 5 with multiplicities \(30,60,60,30,10\), respectively. Its 30 distance-one edges and 20 vertices have cycle rank \(30-20+1=11\); girth six ensures the scale-one clique complex is the graph. The ten distance-five pairs form a perfect matching: each vertex has exactly one antipode at distance five. Thus \(K_4\) is the clique complex of a complete graph with exactly those ten disjoint pairs missing, namely the join of ten two-point complexes, \(S^0*\cdots*S^0\cong S^9\). At threshold five every edge appears and the Rips complex is a simplex.

**Exact scale-two certificate.** Generate all strictly increasing vertex tuples whose entries are pairwise at graph distance at most two. The face numbers in dimensions zero through three are \((20,90,120,30)\), totaling 260 nonempty faces. Process vertices in the deterministic order

`0,10,1,11,2,12,3,13,4,14,5,15,6,16,7,17,8,18,9,19`.

At each vertex, simultaneously pair each currently unmatched simplex not containing that vertex with its one-vertex extension when both are currently unmatched, then delete both from the available set. This yields 120 pairs, one unmatched zero-simplex and nineteen unmatched two-simplices. Check every codimension-one containment, directing unpaired incidences downward and paired incidences upward. Exhaustive topological sorting processes all 260 nonempty faces, so the matching is acyclic, not merely a numerical Morse count. The resulting Morse CW complex has one zero-cell and nineteen two-cells and no one-cells, hence is \(\bigvee^{19}S^2\). This independently corroborates, rather than replaces, the prior scale-two theorem.

**The new scale-three certificate.** The same exact enumeration at radius three gives face numbers

\[(20,150,540,1000,960,450,80)\]

in dimensions zero through six, totaling **3,200 nonempty faces**. With the same deterministic ordered element-matching algorithm, there are exactly **1,599 disjoint pairs** and only **two** critical simplices: one zero-simplex and one three-simplex. A complete directed Hasse-graph test checks every immediate face relation and verifies that all 3,200 vertices of the directed graph are removed by a topological sort. Hence there are no closed gradient paths. Discrete Morse theory supplies a CW homotopy model with one zero-cell and one three-cell, so no attaching map is possible other than the constant map to the point: \(K_3\simeq S^3\) *integrally*, not merely by field-valued ranks. This is the key structural assertion.

**Persistence maps.** Each integer interval has an unchanged complex, so its internal maps are identities. At consecutive thresholds the only nonzero reduced homology groups lie in distinct degrees; therefore inclusion maps on positive-degree homology vanish at each transition. The graph becomes connected at threshold one, killing all nineteen reduced degree-zero classes. These facts yield exactly the interval decomposition above, with no torsion and no unverified infinite-range extrapolation.

## Verification

Run `python3 verify.py` using a standard Python 3 interpreter; no external packages or data files are needed. It constructs the 20-vertex graph and computes all shortest-path distances, verifies the 5-cube middle-layer isometry and the five distance-shell multiplicities, generates every face at scales two and three, replays every matching pair, and certifies directed-Hasse acyclicity by exhaustive topological sorting. The recorded run finishes with `VERIFY_OK`, with critical counts \(\{0:1,2:19\}\) at scale two and \(\{0:1,3:1\}\) at scale three. The code is a complete finite certificate for these specific complexes, not a sampling experiment and not a proof of statements about larger middle-level graphs.

## Relationship to prior work

Feng and Nukala (2023, arXiv:2302.14664), Theorem 13, already show that the Rips complex on the size-two and size-three subsets of a five-element set at scale two is a wedge of nineteen two-spheres. That result **covers the scale-two statement here** under the explicit metric isometry and is not counted as new. Feng (2023, arXiv:2305.07084), Lemma 13, describes the maximal simplices for a general two-adjacent-level subset at scale three, but neither that lemma nor the paper's full-hypercube homotopy theorem implies a sphere homotopy type for this *specific induced 20-vertex subspace*. The present matching upgrades these structural descriptions to the exact three-sphere and completes the graph's metric persistence.

Another published computation of the Desargues graph concerns an intrinsic **Čech nerve** at radius three halves, not this graph-metric Vietoris–Rips complex; it has different simplices and does not imply the stated \(S^3\). The independence complex of the Desargues graph is likewise a different construction. Similar graph-metric Rips computations for the Tutte–Coxeter graph and finite-projective-plane incidence graphs do not include this vertex set or scale-three stage.

## Limitations

The result is specific to the Desargues 20-vertex graph and its shortest-path metric, not all generalized Petersen graphs or all middle-level graphs. This is a same-author mathematical and computational review, not an independent external audit. No full classification for arbitrary adjacent Boolean levels is asserted. Equivalent unpublished or unindexed calculations remain possible; the reported originality assessment is limited to the source material compared.

## References

1. Z. Feng and N. C. P. Nukala, *On Vietoris–Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664 (first submitted February 28, 2023), Theorem 13. https://arxiv.org/abs/2302.14664
2. Z. Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (first submitted May 11, 2023), Lemma 13 and Theorem 24. https://arxiv.org/abs/2305.07084
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, discrete Morse matching theorem.
