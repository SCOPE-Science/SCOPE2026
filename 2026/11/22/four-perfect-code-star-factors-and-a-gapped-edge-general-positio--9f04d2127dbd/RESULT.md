# Four perfect-code star factors and a gapped edge-general-position complex on the Möbius–Kantor graph

## Finding

Let \(M\) be the Möbius–Kantor graph. The polynomial counting its edge-general-position subsets by size is

\[
\begin{aligned}
\Psi_M(z)={}&1+24z+276z^2+1832z^3+7362z^4+17712z^5\\
&+24468z^6+18240z^7+7017z^8+1576z^9\\
&+300z^{10}+48z^{11}+4z^{12}.
\end{aligned}
\]

The inclusion-maximal-subset polynomial is

\[
\Phi_M(z)=792z^7+1329z^8+336z^9+36z^{10}+4z^{12}.
\]

There are exactly \(78,860\) admissible edge sets. The largest have size \(12\); there are precisely four, corresponding to the four efficient dominating codes

\[
C_i=\{a_i,a_{i+4},b_{i+2},b_{i+6}\},\qquad i=0,1,2,3.
\]

For each \(i\), the optimum edge set is \(X_i=\{e\in E(M):e\text{ meets }C_i\}\). Every pair of distinct optimum edge sets intersects in exactly four edges. The batch-replacement graph on optimum sets (where two sets are adjacent when at most \(k\) edges of one can be replaced simultaneously by the same number of new edges) is \(4K_1\) for \(1\le k\le7\), and \(K_4\) for \(k\ge8\). Every size-eleven admissible set has exactly one optimum extension; in particular, there is no inclusion-maximal set of size eleven despite the existence of inclusion-maximal sets of sizes seven through ten and twelve.

## Assumptions and scope

The labelled simple graph is \(M=\operatorname{GP}(8,3)\): its vertices are \(a_i,b_i\) for \(i\in\mathbb{Z}/8\mathbb{Z}\), and its 24 edges are \(a_i a_{i+1}\), \(a_i b_i\), and \(b_i b_{i+3}\), each with indices modulo eight. An *edge-general-position set* \(X\subseteq E(M)\) has no three distinct selected edges on one shortest path in \(M\). The polynomial \(\Psi_M(z)\) sums \(z^{|X|}\) over all such sets, including the empty set; \(\Phi_M(z)\) sums over those that are inclusion-maximal, not necessarily maximum in cardinality. All counts use the 24 distinct labelled edges, without quotienting by graph symmetries.

## Proof

**1. A structural bound.** The defining adjacency rules give a connected cubic graph on 16 vertices, of girth six and diameter four; the finite distance and cycle checks are also repeated in the attached verifiers. Every simple three-edge path is a geodesic: if its endpoints had a path of length at most two, the union would contain a cycle of length at most five. Thus an edge-general-position set induces a graph with no three-edge path. As the ambient graph is triangle-free, each connected selected-edge component is a star of at most three edges (allowing isolated vertices as zero-edge stars). If there are \(c\) components in this spanning forest, then \(|X|=16-c\). Every component has at most four vertices, so \(c\ge4\) and \(|X|\le12\). Equality forces four disjoint copies of \(K_{1,3}\), with their centers forming an efficient dominating set: the four closed neighborhoods partition all 16 vertices.

**2. There are exactly four possible center sets.** Let an efficient dominating set have \(x\) centers among the outer vertices and \(y\) among the inner vertices. Its disjoint radius-one neighborhoods cover the outer and inner shores exactly once. Consequently \(3x+y=8\) and \(x+3y=8\), hence \(x=y=2\). Up to a dihedral relabelling, the two outer centers are \(a_0,a_d\) with cyclic distance \(d=3\) or \(d=4\); smaller distances produce overlapping outer neighborhoods. If \(d=3\), the only uncovered outer vertices are \(a_5,a_6\), forcing inner centers \(b_5,b_6\). Then \(b_0\) is covered both by \(a_0\) and by \(b_5\), a contradiction. If \(d=4\), the uncovered outer vertices are \(a_2,a_6\), forcing \(b_2,b_6\), whose inner closed neighborhoods together with those reached by \(a_0,a_4\) partition the eight inner vertices. Rotations produce exactly the four codes \(C_i\), \(i=0,1,2,3\).

**3. The four stars are admissible.** For a fixed \(C_i\), pairs of its centers are at distances three or four. For pairs at distance three, every neighbor of either center is at distance two from the other center; this follows by direct substitution into the three adjacency rules and is also independently tested in the verifiers. In any geodesic of length at most four, there can be at most two centers. If it contains one center, at most two path edges touch that center. If it contains two centers at distance four, they are the two endpoints of a four-edge geodesic, again contributing at most two selected edges. If it contains two centers at distance three and three incident edges, one center must be an internal vertex and the other an endpoint of a four-edge path. The external endpoint neighboring the internal center would then be at distance four from the other center, contradicting the preceding distance-two property. Hence no geodesic contains three edges of \(X_i\). These four sets achieve the bound and exhaust the maxima.

**4. Exact face and facet counts.** Index the 24 edges lexicographically by their ordered endpoints \(0,\ldots,15\), with \(a_i=i\), \(b_i=8+i\). Enumerate every shortest path by breadth-first distances followed by distance-increasing path traversal. Every forbidden triple of edges comes from some shortest path; deduplication gives exactly 192 distinct triples. If \(g(S)\) indicates that an edge-index subset \(S\) avoids all forbidden triples, set \(g(\varnothing)=1\). For nonempty \(S\), with highest index \(j\) and \(T=S\setminus\{j\}\), use the exact recursion

\[
g(S)=g(T)\prod_{\{p,q,j\}\in\mathcal{H}}\big(1-\mathbf{1}[\{p,q\}\subseteq T]\big),
\]

where \(\mathcal{H}\) is the 192-element forbidden-triple family. There are exactly \(2^{24}\) masks, and this recurrence checks every one; it does not extrapolate from a sample. Counting valid masks by cardinality gives \(\Psi_M\). A valid mask is inclusion-maximal exactly when adjoining any one missing edge makes it invalid. Applying this test to every valid mask gives \(\Phi_M\). The independent recursive verifier rebuilds all geodesics and counts valid subsets by another traversal rather than reusing the mask recurrence.

**5. Eleven-edge stability and exchanges.** The face polynomial gives 48 eleven-edge sets, while the four optima each contain twelve distinct eleven-edge subsets. Their pairwise intersections have cardinality four, so no eleven-edge subset can belong to two optima. Therefore the 48 sets of size eleven are exactly the twelve subsets of each optimum and extend uniquely. Direct comparison of the four explicitly listed \(X_i\) gives \(|X_i\cap X_j|=4\) whenever \(i\ne j\), hence replacing one by another requires exactly eight deletions and eight additions. This proves the batch-replacement transition and the one-edge immobility of every maximum configuration.

## Verification

The attached `verify.py` constructs the graph using only the standard Python library, independently enumerates its distance-increasing geodesics, generates the 192 forbidden triples, and uses an increasing-index backtracking traversal to enumerate valid masks. It then checks all single-edge extensions, all four efficient dominating codes, and the pairwise intersections of optimum sets. Its complete expected output starts with `VERIFY_OK`.

The attached `verify_fast.cpp` builds the same graph from its modular definition but uses a separate C++17 implementation: it enumerates all \(2^{24}\) masks using the highest-edge recursion and independently checks the same two polynomial coefficient arrays. It prints `VERIFY_FAST_OK`. Reproduce with `python3 verify.py` and `c++ -O3 -std=c++17 verify_fast.cpp -o verify_fast && ./verify_fast`. Both source files are complete and require no downloaded graph tables.

## Relationship to prior work

Manuel, Prabha and Klavžar introduced edge general position and determined its maximum for trees, hypercubes and rectangular path grids; their theorems do not specialize to the non-tree, non-grid Möbius–Kantor graph. Tian, Klavžar and Tan later analyzed extremal parameter values and block graphs, which do not supply this graph's face and facet census. Klavžar and Tan studied Fibonacci and Lucas cubes, a different family of partial cubes. This finding instead concerns the exact face complex on a fixed symmetric cubic graph, with a complete optimizer classification and batch-exchange threshold. The literature comparison does not establish universal publication priority; remaining risks are described in the review.

## Limitations

The theorem is specific to the 16-vertex \(\operatorname{GP}(8,3)\). The exact intermediate coefficients and facet counts are certified by fully specified exhaustive finite algorithms; the structural upper bound and optimizer classification have independent mathematical proofs. No infinite-family formula, independent external validation, or exhaustive priority certification is claimed. The batch move rule allows simultaneous replacement of the same number of edges and requires only that the endpoints be maximum edge-general-position sets, not that intermediate partial replacements remain valid.

## References

1. P. Manuel, R. Prabha, and S. Klavžar, *Edge General Position Problem*, arXiv:2105.04292v1 (first public 2021-05-10), https://arxiv.org/abs/2105.04292.
2. J. Tian, S. Klavžar, and E. Tan, *Extremal edge general position sets in some graphs*, arXiv:2302.01587 (first public 2023-02-03), https://arxiv.org/abs/2302.01587.
3. S. Klavžar and E. Tan, *Edge general position sets in Fibonacci and Lucas cubes*, arXiv:2304.10114v1 (first public 2023-04-20), https://arxiv.org/abs/2304.10114.
4. E. W. Weisstein, *Möbius-Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html (graph identification and alternative presentations; not a source for the new enumerators).
