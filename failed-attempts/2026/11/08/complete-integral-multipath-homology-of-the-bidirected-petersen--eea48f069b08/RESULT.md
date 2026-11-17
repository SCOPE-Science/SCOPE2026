# Complete integral multipath homology of the bidirected Petersen graph

## Finding

For the Petersen graph \(P=\operatorname{KG}(5,2)\), let \(D=\overleftrightarrow P\) denote the digraph containing both directed arcs for each undirected graph edge. Its multipath complex \(X(D)\) has vertices equal to directed arcs of \(D\) and simplices equal to sets of arcs forming vertex-disjoint directed simple paths. Then

\[
\widetilde H_i(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{12},&i=4,\\
\mathbb Z,&i=5,\\
\mathbb Z^{44},&i=6,\\
\mathbb Z^{94},&i=7,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular the reduced integral homology is torsion-free. There are \(59{,}203\) faces including the empty face, and the reduced Euler characteristic is \(-39\).

## Assumptions and scope

The vertex set of \(P\) is the set of two-element subsets of \(\{0,1,2,3,4\}\), ordered lexicographically. Two distinct vertices are adjacent precisely when their subsets are disjoint. Thus \(P\) has ten vertices and fifteen edges. Include each edge in both directions and sort the resulting thirty arcs lexicographically. A subset of arcs is a multipath if and only if every original vertex has indegree at most one and outdegree at most one and the chosen directed graph has no directed cycle. An isolated vertex is permitted. A face with \(k\) arcs has simplex dimension \(k-1\), including the empty face in degree \(-1\). All homology here is reduced simplicial homology over \(\mathbb Z\).

## Proof

**Complete face enumeration.** Enumerate each allowable arc subset by recursion in increasing arc order. A candidate arc \((u,v)\) is admitted only when the current outdegree of \(u\) and indegree of \(v\) are zero and following current outgoing arcs from \(v\) does not reach \(u\). This is an exact membership test: the degree restrictions ensure components are directed paths or directed cycles, and the final condition forbids the latter. Because every subset has one increasing arc order, this recursion enumerates every face exactly once. As a separate exhaustive enumeration, process the thirty arcs one at a time, keeping both the omit and include branches; on each include branch independently test degree restrictions and topologically sort the resulting digraph. The enumerations agree face-for-face. The numbers of faces in dimensions \(-1,0,\ldots,8\) are

\[
(1,30,360,2240,7860,15912,18280,11160,3120,240).
\]

**Acyclic integral reductions.** For a fixed order of the thirty arc coordinates, process coordinates successively. At coordinate \(a\), pair each still-unmatched face omitting \(a\) with its face obtained by adding \(a\), provided that second face exists and is also unmatched. Each pair has simplicial incidence \(\pm1\). The code checks acyclicity, rather than assuming it: orient every matched Hasse incidence upward and every other Hasse incidence downward, and topologically sort the entire directed Hasse graph. Both ascending and descending coordinate orders yield all \(333{,}390\) Hasse incidences with no directed cycle. The resulting acyclic matchings constitute integral chain homotopy reductions.

For the ascending reduction, the numbers of critical cells in dimensions \(3,4,5,6,7\) are \((1,19,63,106,100)\); all other dimensions have zero critical cells. The descending reduction has critical counts \((2,33,71,99,98)\) in the same dimensions. The alternating signed simplicial boundary uses increasing arc-coordinate orientation.

**Reduced integral boundaries.** The included checker constructs exact Morse boundaries by eliminating matched pairs with unit incidence. Let \(\sigma\) be matched as the lower face of \(\tau\). With incidence \([\sigma:\tau]\in\{\pm1\}\), its projection to the critical chain group satisfies

\[
\pi(\sigma)=-[\sigma:\tau]^{-1}
\sum_{\substack{\beta\subset\tau\\ \beta\ne\sigma\\ |\beta|=|\sigma|}}
[\beta:\tau]\,\pi(\beta).
\]

Critical faces project identically, and matched upper faces project to zero. The acyclicity check ensures that this recursive elimination terminates. For a critical face \(c\), the Morse boundary is obtained by projecting its ordinary signed simplicial boundary. All boundary compositions are checked to be zero.

For the ascending reduction, the ranks of the degree \(4,5,6,7\) boundaries are \((1,6,56,6)\). For the descending reduction they are \((2,19,51,4)\). Each reduced boundary was subjected to integral elementary row and column operations using only unit pivots, until the residual matrix was zero. Therefore *all* nonzero Smith invariant factors of every differential are exactly one, and there is no integral torsion. The resulting reduced Betti number formula \(b_i=c_i-r_i-r_{i+1}\) gives precisely \(b_4=12\), \(b_5=1\), \(b_6=44\), \(b_7=94\), with every other reduced Betti number zero. All critical degree-eight cells disappear in the matching, so the top simplicial degree does not contribute homology.

## Verification

Run `python3 verify_petersen_multipath.py` with a standard Python interpreter. It independently enumerates all faces twice, verifies both complete Hasse-diagram orientations have no cycles, constructs both signed integral Morse chain complexes, checks that consecutive boundaries compose to zero, and performs integral unit-pivot elimination. A third calculation obtains all ranks of the **unreduced** augmented simplicial boundary matrices over \(\mathbb F_2\) directly from faces; its Betti numbers match the integral calculation. The zero-reduced-Euler-check is \(12-1+44-94=-39\). The exact output is included as `verification_output.txt`. These computations are finite exhaustive proofs for the explicitly defined ten-vertex graph; no extrapolation to an infinite graph family is made.

## Relationship to prior work

The path-poset and multipath-complex construction and its relationship to simplicial homology appear in Caputi–Collari–Di Trani (2021 preprint / later journal work). Caputi–Collari–Di Trani–Smith (arXiv:2208.04656, first posted August 9, 2022) treats directed paths, polygons, small grids, transitive tournaments and decompositions into dynamical modules, but its inspected results do not give the bidirected Petersen calculation. Caputi–Collari–Ramos (arXiv:2401.01248) proves bounded-torsion results for classes of quivers and a matching-complex comparison for digraphs without oriented cycles. That comparison does not apply: every edge of \(D\) provides a directed two-cycle. Caputi–Collari–Smith (arXiv:2601.05670) determines homology for bidirectional polygonal digraphs, whereas the underlying Petersen graph is cubic, not a cycle. Calculations for the ordinary Petersen matching complex, higher-independence complex, and discrete Morse complex concern different simplicial constructions and do not imply these Betti numbers. The displayed integral Betti vector was not found in the inspected sources; this is a best-knowledge originality assessment, not a proof of uniqueness against all literature.

## Limitations

This is a complete computation of **integral homology**, not a classification of the entire homotopy type. In particular, torsion-free homology alone does not prove a wedge-of-spheres decomposition. The theorem is only about the fully bidirected Petersen graph, not arbitrary orientations or other cubic graphs. Bibliographic coverage is limited by indexing and accessibility; independently authored equivalent computations may exist.

## References

1. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206 (first posted October 21, 2021); doi:10.1007/s10801-022-01180-9.
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the Homotopy Type of Multipath Complexes*, arXiv:2208.04656v1 (August 9, 2022), subsequently in *Mathematika* 70 (2024), e12235.
3. L. Caputi, C. Collari, E. Ramos, *The Weak Categorical Quiver Minor Theorem and Its Applications: Matchings, Multipaths, and Magnitude Cohomology*, arXiv:2401.01248v1 (January 2, 2024).
4. L. Caputi, C. Collari, J. P. Smith, *Multipath Complexes of Bidirectional Polygonal Digraphs*, arXiv:2601.05670v1 (January 9, 2026).
