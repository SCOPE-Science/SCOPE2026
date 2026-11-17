# Forty-five three-spheres in the third non-matching complex of the Möbius–Kantor graph

## Finding

Let \(G=\operatorname{GP}(8,3)\) be the sixteen-vertex Möbius–Kantor graph. Its third non-matching complex is the simplicial complex on the twenty-four **edges** of \(G\) whose faces are the edge subsets with no matching of size three. Its exact integral homotopy type is

\[
\boxed{\operatorname{NM}_3(G)\simeq\bigvee^{45}S^3.}
\]

A fully specified acyclic discrete-Morse matching has one critical vertex and exactly forty-five critical three-cells. Consequently \(\widetilde H_3(\operatorname{NM}_3(G);\mathbb Z)\cong\mathbb Z^{45}\), all other reduced integral homology vanishes, and the fundamental group is trivial. This is a nonequivariant statement.

## Assumptions and scope

The graph has vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/8\mathbb Z\), with undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). This is a simple, connected, cubic bipartite graph with sixteen vertices and twenty-four edges. In the supplied program the first eight vertices represent \(u_i\), the next eight represent \(v_i\), and the twenty-four **undirected graph edges** are ordered lexicographically by their sorted integer endpoint pairs. Face bit \(j\) represents graph edge \(j\) in this order.

For an edge subset \(F\subseteq E(G)\), let \(\nu(F)\) be the maximum cardinality of a set of pairwise vertex-disjoint graph edges contained in \(F\). The abstract simplicial complex in question has faces precisely \(\{F\subseteq E(G):\nu(F)<3\}\), including the empty face in augmented enumeration. No assertion is made for other thresholds or other generalized Petersen graphs.

## Proof

**Exact domain enumeration.** The minimal nonfaces are exactly the three-edge matchings of \(G\), because \(\nu(F)\ge3\) is equivalent to the containment of three pairwise vertex-disjoint graph edges. There are \(1{,}096\) such triples, obtained by testing all \(\binom{24}{3}\) edge triples for six distinct endpoints. The included checker enumerates **all** faces recursively in increasing edge-index order, forbidding precisely these triples. It independently constructs the same complex by taking all subsets of the incident-edge unions of two graph vertices. Equality of these two face sets also follows abstractly from König's theorem: in a bipartite graph, an edge subset has matching number at most two if and only if two (or fewer) graph vertices cover all its edges.

The checker obtains \(3{,}149\) augmented faces and the nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,276,928,1224,600,96).
\]
The resulting Euler characteristic is \(-44\), consistent with the claimed wedge, but the Euler characteristic alone is not used to establish the homotopy type.

**Complete acyclic matching.** Initialize the set of all \(3{,}149\) augmented faces as unmatched. For \(j=0,1,\ldots,23\), inspect all currently unmatched faces \(\sigma\) in increasing integer bit-mask order. Whenever bit \(j\) is absent from \(\sigma\) and \(\sigma\cup\{j\}\) is also currently unmatched, pair those two faces and permanently remove both from subsequent stages. This deterministic procedure produces exactly \(1{,}552\) disjoint face pairs. The only unmatched augmented faces are forty-five four-element edge subsets, hence forty-five simplices of dimension three.

Orient every cover relation of the entire augmented face Hasse diagram downward unless it belongs to the stated matching, in which case orient it upward. The checker independently constructs all \(11{,}832\) directed covers and topologically sorts this graph, visiting all \(3{,}149\) faces. Thus the matching is acyclic, a complete finite verification rather than a heuristic. The empty face is paired with a singleton. Removing that single pair from the matching and restricting to nonempty faces leaves one critical zero-cell and forty-five critical three-cells, and the directed graph of the remaining \(11{,}808\) nonempty-face covers is again acyclic by a separate exhaustive topological sort.

By the integral discrete-Morse CW theorem, the geometric realization is homotopy equivalent to a CW complex with one zero-cell, forty-five three-cells and no other cells. Every three-cell is attached to the point that forms the two-skeleton; hence that CW complex is a wedge of forty-five three-spheres. There are no higher attaching maps or torsion possibilities in this CW model, proving the full claim.

## Verification

Run `python3 verify_nm3_mobius_kantor.py` using only the Python standard library. The program regenerates graph edges, verifies cubic bipartiteness, computes all \(1{,}096\) forbidden triples, enumerates the full face set in two independent ways, executes the precise sequential matching, verifies all directed Hasse covers and the acyclicity of both augmented and ordinary matchings, and checks the critical dimensions and Euler characteristic. It prints `ALL_CHECKS_PASS` only if all assertions succeed. The included `verification_nm3_mobius_kantor.txt` reproduces an actual successful run of that exact program.

The finite enumeration is exhaustive for this specific twenty-four-edge graph. The mathematical inference from the verified matching to integral homotopy type invokes the ordinary discrete-Morse theorem and is not an extrapolation from sampled data.

## Relationship to prior work

Linusson, Shareshian and Welker determine complete-graph and complete-bipartite non-matching homotopy types, not the corresponding complex of this sparse graph. Holmsen and Lee prove a general bipartite homological vanishing bound: for threshold three, reduced homology vanishes in dimensions at least four, but the bound neither determines the rank \(45\) nor forces a wedge of spheres. Shan and Wang establish top-degree homological injectivity under bipartite edge additions, and hence nonvanishing when a sufficiently long even cycle is present. The exact rank, integral homotopy and explicit Morse structure of this graph are not consequences of those conclusions.

Published calculations for the Heawood and Petersen non-matching complexes concern distinct graphs; for the third threshold their sphere multiplicities are \(36\) and \(9\), respectively. A calculation of the Möbius–Kantor *total three-cut* complex gives forty-five ten-spheres, but that is a complex on **graph vertices** with facets complementary to independent triples; it is not the twenty-four-edge non-matching complex here, and no implication between their reported homotopy types was established. In particular, the matching numerical multiplicity does not imply the present topological classification.

## Limitations

This is a precise single-graph, single-threshold result, not an all-parameter theorem. It does not compute equivariant homology, describe canonical sphere generators or establish a complete filtration for other matching thresholds. Exhaustive finite verification and a standard homotopy theorem establish this instance, not an independent external mathematical audit. Literature checks cannot rule out every unindexed or inaccessible equivalent calculation.

## References

1. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley–Reisner ideals*, arXiv:2609.02621, first public posting 2026-09-02, https://arxiv.org/abs/2609.02621. Theorems 2.1 and 2.3.
2. A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270, first public posting 2020-03-25, https://arxiv.org/abs/2003.11270. Theorems 1.1–1.2.
3. S. Linusson, J. Shareshian and V. Welker, *Complexes of Graphs with Bounded Matching Size*, Journal of Algebraic Combinatorics 27 (2008), 331–349, DOI 10.1007/s10801-007-0092-1; first preprint arXiv:math/0410345, 2004-10-15. Theorem 1.4.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
5. *Complete integral non-matching homotopy filtration of the Heawood graph*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-integral-non-matching-homotopy-filtration-of-the-heawoo--8c61a8d39b4a.
6. *Nine three-spheres and the full symmetry character of the Petersen non-matching complex*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-nine-three-spheres-and-the-full-symmetry-character-of-the-peters--03efedc17432.
7. *The total three-cut complex of the Möbius–Kantor graph is a wedge of forty-five ten-spheres*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-total-3-cut-complex-of-the-m-bius-kantor-graph-is-bigvee-45--4936eeabcd8f.
