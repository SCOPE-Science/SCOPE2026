# Mixed circle and three-sphere homotopy in the four-cube geodesic general-position complex

## Finding
For the four-dimensional binary hypercube \(Q_4\), define \(\mathrm{GP}(Q_4)\) to be the abstract simplicial complex of graph-geodesic general-position vertex sets: no three distinct selected vertices lie on a common shortest path of \(Q_4\). Then
\[
|\mathrm{GP}(Q_4)|\simeq\left(\bigvee^{40}S^1\right)\vee\left(\bigvee^{9}S^3\right).
\]
The face-vector in dimensions 0 through 4 is \((16,120,160,120,16)\), and there are no higher-dimensional faces.

## Assumptions and scope
The vertices are exactly the sixteen four-bit strings, identified with integers 0 through 15 in least-significant-bit-first order. Graph distance is Hamming distance \(d(a,b)=\operatorname{popcount}(a\mathbin{\mathrm{xor}}b)\). A subset is a face exactly when it contains no triple \(\{a,b,c\}\) with \(d(a,b)=d(a,c)+d(c,b)\), for some choice of the middle vertex \(c\). No result for cubes of dimension greater than four is asserted.

## Proof
**1. Exact description of the complex.** For any three distinct vertices, one lies on a geodesic between the other two precisely when one of the three Hamming-distance equalities holds. Exhaustively iterate the \(\binom{16}{3}=560\) unordered triples using integer arithmetic. Exactly 400 are forbidden. A nonempty subset \(\sigma\subseteq\{0,\ldots,15\}\) is a face if and only if none of these 400 forbidden triples is contained in \(\sigma\). Direct enumeration of all \(2^{16}-1\) nonempty subsets gives exactly 432 faces, distributed as \((16,120,160,120,16)\) by simplex dimension.

**2. Explicit complete acyclic matching.** Identify each face with its 16-bit characteristic mask. Use the fixed pivot order

`12, 0, 11, 3, 8, 5, 4, 9, 15, 6, 7, 13, 1, 10, 2, 14`.

Initially mark all nonempty faces unmatched. At each pivot vertex \(v\) in this order, simultaneously pair every currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both faces remain unmatched. Remove both faces from further consideration. The pairs are unambiguous because the added pivot uniquely determines each partner. This gives 191 pairs and 50 critical faces: one vertex, forty edges, zero triangles, nine tetrahedral (three-dimensional) faces, and zero four-dimensional faces.

To check acyclicity, form the *entire* Hasse digraph on the 432 nonempty faces, with one edge per codimension-one incidence. Orient every matched incidence upward and every other incidence downward. The included exact verifier constructs every incidence explicitly and applies Kahn's topological-sort algorithm. It processes all 432 vertices; hence there is no directed cycle. This is an exhaustive, finite acyclicity certificate, not a sampling experiment.

**3. Homotopy identification.** Forman's discrete Morse theorem gives a CW complex with exactly one 0-cell, forty 1-cells, no 2-cells, nine 3-cells and no other cells, homotopy equivalent to the simplicial complex. Its 1-skeleton is a bouquet of forty circles. Because the bouquet is a \(K(F_{40},1)\), its second homotopy group vanishes, so each 3-cell attaching map \(S^2\to\bigvee^{40}S^1\) is nullhomotopic. Attaching the nine 3-cells therefore wedges on nine 3-spheres, proving the displayed integral homotopy equivalence.

## Verification
Run the standalone Python 3 standard-library script `q4_gp_verifier.py`. It recomputes all forbidden triples from Hamming distance, all faces, the 191 matching pairs, all codimension-one face incidences, and a complete topological sort of the reversed-matching Hasse digraph. The program asserts every stated count and prints `PASS` only after all tests. The Euler characteristic independently checks as \(16-120+160-120+16=-48=1-40-9\). This finite exhaustive certificate fully covers the stated sixteen-vertex object.

## Relationship to prior work
Korže and Vesel (2023, Section 4) investigate **maximum cardinalities** of graph-geodesic general-position sets in hypercubes, including exact small-dimensional values obtained using SAT, but do not identify the homotopy type of the simplicial complex of *all* such sets. Klavžar, Rall and Yero (2020 preprint; 2021 journal publication) study graph-geodesic general \(d\)-position sets and their extremal/cardinality properties. The present result computes a different, finer integral topological invariant for a fixed natural cube. Related recorded results on the four-cube concern ordinary independence, higher independence, cut, dominance, or metric Rips complexes, whose face conditions are different; none implies this claim. No assertion of global bibliographic uniqueness is made.

## Limitations
The finding concerns exactly \(Q_4\) and its ordinary graph-geodesic general-position complex, not the Euclidean no-three-collinear complex, an independence complex, the geodesic number alone, or higher-dimensional hypercubes. The exhaustive certificate provides a finite proof for this fixed graph. No formula for \(Q_d\) as \(d\to\infty\), independent peer verification or generalization is claimed. Literature coverage is limited by indexing and inspected accessible sources.

## References
- S. Klavžar, D. F. Rall, I. G. Yero, *General d-position sets*, arXiv:2005.08095 (first posted 2020-05-16); *Ars Mathematica Contemporanea* 21 (2021), P1.03, DOI:10.26493/1855-3974.2384.77d.
- D. Korže, A. Vesel, *General Position Sets in Two Families of Cartesian Product Graphs*, *Mediterranean Journal of Mathematics* 20 (2023), article 203, DOI:10.1007/s00009-023-02416-z, published 2023-05-06.
- R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
