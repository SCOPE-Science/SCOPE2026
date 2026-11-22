# Exact Euclidean chord spectrum and sparse diameter graph of the first mixed constrainahedron

## Finding

For the canonical integer-coordinate realization of the constrainahedron \(C(3,4)\), the 108 vertices determine exactly 174 distinct nonzero squared Euclidean chord lengths among \(\binom{108}{2}=5778\) unordered pairs. The squared diameter is \(430\), attained by four pairs. Its diameter graph is \(P_3\sqcup P_3\) together with 102 isolated vertices. The second-largest squared length is \(424\), also attained by four pairs; the gap to the diameter is exactly \(6\). The complete 174-row multiplicity table is the attached `CHORD_SPECTRUM.csv`.

## Assumptions and scope

We use the specific Bottman–Poliakova realization (Definition 4.4 and Theorem 4.1 in arXiv:2208.14529v1), **not** the different Chapoton–Pilaud Minkowski-shuffle realization of the same combinatorial type. There are three vertical lines, four horizontal lines and five adjacent-line collision labels \(m_1,m_2,l_1,l_2,l_3\). Coordinate order is \((x_1,x_2,y_1,y_2,y_3)\). All distances are ambient standard Euclidean distances in \(\mathbb R^5\), equivalently intrinsic distances in the affine hyperplane of coordinate sum \(27\). Vertex pairs are unordered and distinct.

## Proof

**Exhaustive vertex generation.** For each of the \(5!=120\) total collision orders, begin with three singleton vertical components and four singleton horizontal components. At collision \(m_i\) or \(l_j\), the corresponding adjacent components have sizes \(W_1\) and \(W_2\). Define the opposite-direction thickness to be \(T=1+\sum_B\binom{|B|}{2}\), summed over connected components \(B\) formed by previously performed collisions in the other direction. Assign that coordinate \(W_1W_2T\) and merge the two components. This is the source's exact coordinate formula. Its Theorem 4.1 and the normal-fan argument at the end of Section 4 show that the normal fan coarsens the braid fan: each total collision order selects a vertex, and every vertex is selected by at least one order. The procedure therefore enumerates **all** vertices, rather than merely sampling them. In this case the 120 orders give 108 distinct vectors, independently agreeing with the published 108-vertex census (Chapoton–Pilaud, Table 10). Each vector has coordinate sum 27, in agreement with Bottman–Poliakova, Lemma 4.2.

**Exact finite determination.** Sort and deduplicate those 108 integral vectors. For each unordered pair \(\{u,v\}\), compute \(\|u-v\|_2^2=\sum_{i=1}^5(u_i-v_i)^2\) in exact integer arithmetic. All \(108\cdot107/2=5778\) pairs appear exactly once. The 174-row file records, for each distance, its entire multiplicity. Direct integer tally verifies it has exactly 174 distinct lengths, sums to 5778, has largest key 430 of multiplicity four and second-largest key 424 of multiplicity four. The complete four diameter pairs, in the above coordinate order, are:

- \((1,6,2,16,2)\) with \((14,2,4,1,6)\);
- \((1,6,2,16,2)\) with \((14,2,6,1,4)\);
- \((6,1,2,16,2)\) with \((2,14,4,1,6)\);
- \((6,1,2,16,2)\) with \((2,14,6,1,4)\).

Consequently their degree sequence on the six nonisolated vertices is \((2,2,1,1,1,1)\), and the two degree-two vertices are nonadjacent. Hence the diameter graph is \(2P_3\) with 102 isolates. Finally, the diameter of the full convex hull is attained at vertices: for any pair of convex combinations, convexity of the squared norm in each variable implies no greater distance than the largest vertex-pair distance. Thus this is the **polytope diameter**, not just a sampled-vertex statistic.

## Verification

`CHECKER.py` is self-contained and requires only Python's standard library and `CHORD_SPECTRUM.csv` in the same directory. It independently constructs all 120 order profiles via interval block decomposition, verifies the 108 unique points and constant coordinate sum, traverses all 5778 pairs in integer arithmetic, compares the **entire** reconstructed distance-count dictionary to the CSV, and tests the maximum/runner-up shells and the diameter graph degree pattern. The preparatory enumeration used a separately implemented union-find method and gave the identical 108-vector set. The calculation is finite and exhaustive; no interpolation or numerical approximation enters the claim.

## Relationship to prior work

Bottman–Poliakova (2022), Section 4, supplies the exact realization and proof of its generalized-permutahedron normal fan. Chapoton–Pilaud, Table 10, records that \(C(3,4)\) has 108 vertices, but their separate additive vertex-coordinate construction defines a geometrically different realization; no Euclidean distance conclusion is transferred between the two. The closest indexed result, *Singleton collision facets determine the inball of the Bottman–Poliakova constrainahedron*, concerns **inradius and tangent facets**, not long vertex-to-vertex chords. Searches for the exact 430 diameter, the full chord distribution and equivalent metric descriptors yielded no identified covering statement. This is a priority assessment, not a proof of global novelty.

## Limitations

This is a finite exact metric classification of one distinguished low-dimensional realization, not a formula for all \(C(m,n)\). Euclidean chord lengths are not invariant under arbitrary affine changes of realization. The total 108 vertex count and geometric coordinate construction are prior results; the new assertion is the exact 174-level metric census and diameter-graph classification. An unindexed earlier computation is a residual priority risk. Independent mathematical review has not occurred.

## References

1. N. Bottman and D. Poliakova, *Constrainahedra*, arXiv:2208.14529v1 (first public 2022-08-30), Section 4, Definition 4.4 and Theorem 4.1; https://arxiv.org/html/2208.14529v1.
2. F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, Section 4 and Table 10; https://www.lix.polytechnique.fr/~pilaud/documents/publications/ChapotonPilaud_ShufflesDeformedPermutahedra.pdf.
3. *Singleton collision facets determine the inball of the Bottman–Poliakova constrainahedron*, published research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singleton-collision-facets-determine-the-inball-of-the-bottman-p--2ad33fc827f4 (indexed summary only; full record was not accessible during comparison).
