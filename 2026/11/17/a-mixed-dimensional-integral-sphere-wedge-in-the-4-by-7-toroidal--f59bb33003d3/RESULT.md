# A mixed-dimensional integral sphere wedge in the \(4\)-by-\(7\) toroidal hard-square complex

## Finding
Let \(G=C_4\square C_7\), where both cycle factors have their ordinary graph edges and both directions have periodic boundary conditions. For the simplicial complex \(K=\operatorname{Ind}(G)\) of vertex-independent subsets,
\[
 |K|\simeq S^5\vee S^5\vee S^6.
\]
In particular, its only nonzero reduced integral homology is \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^2\) and \(\widetilde H_6(K;\mathbb Z)\cong\mathbb Z\); there is no torsion. The alternating face sum \(\widetilde\chi(K)=-1\) agrees with the known coprime-torus Euler-characteristic calculation, but that numerical invariant does not determine these two distinct homology degrees.

## Assumptions and scope
The vertex set is \(\mathbb Z/4\mathbb Z\times\mathbb Z/7\mathbb Z\). Distinct vertices \((a,b)\) and \((c,d)\) are adjacent exactly when \(c=a\pm1\pmod4\) and \(d=b\), or \(d=b\pm1\pmod7\) and \(c=a\). A simplex is any subset containing no adjacent vertices. The statement concerns this particular \(28\)-vertex Cartesian-product graph, not the categorical product of cycles or an open/cylindrical grid. All homotopy and integral homology statements are nonequivariant.

## Proof
We give a finite, exhaustive, reproducible discrete-Morse proof. Encode vertex \((a,b)\) by bit \(7a+b\) in an integer mask. The graph has \(28\) vertices of degree four and \(56\) edges. Complete recursive enumeration of all independent masks, including the empty face, produces \(96{,}433\) faces. Their simplex counts by dimensions \(-1,0,1,\ldots,11\) are respectively
\[
 (1,28,322,1988,7266,16464,23786,22540,14602,6748,2198,448,42).
\]
A deterministic matching repeatedly scans vertices in priority order
\[
(20,1,14,12,18,5,0,16,27,9,22,10,26,13,7,24,19,15,23,17,21,8,6,4,2,25,11,3)
\]
and pairs each still-unmatched **nonempty** face omitting that vertex to its still-unmatched independent coface obtained by adding it. Faces are only paired once. This gives \(48{,}214\) matched pairs, and exactly four critical faces: the empty face, one vertex, two dimension-five faces with integer masks \(41960481\) and \(67127817\), and one dimension-six face with mask \(36307268\).

For complete acyclicity, orient every face-cover arrow upward, except matched covers downward. Form the entire directed Hasse graph of \(623{,}476\) cover relations and run Kahn elimination. All \(96{,}433\) faces are eliminated, proving acyclicity without sampling. Forman's discrete-Morse theorem therefore provides a CW complex with one zero-cell, two five-cells and one six-cell, homotopy equivalent to \(|K|\).

It remains to establish the integer attaching degrees of the six-cell, not merely its rational ranks. Orient simplices by increasing vertex-bit position. For each matched pair \(\sigma^5\subset\tau^6\), projection of the face \(\sigma\) to the free abelian group on critical five-cells is determined recursively by the signed incidence rule
\[
 P(\sigma)=-[\tau:\sigma]^{-1}\sum_{\sigma'\subset\tau,\ \sigma'\ne\sigma}[\tau:\sigma']P(\sigma').
\]
Here \(P\) is the identity on critical five-cells, and vanishes on dimension-five cells matched downward to dimension four. The directed acyclicity makes the recursion finite. Exhaustive signed path evaluation, exploring \(4{,}403\) faces of dimension five, yields
\[
 P(\partial \sigma^6_{\mathrm{critical}})=(0,0).
\]
Thus both integral attaching degrees are exactly zero. The five-skeleton is \(S^5\vee S^5\); since it is four-connected, Hurewicz gives \(\pi_5(S^5\vee S^5)\cong H_5(S^5\vee S^5;\mathbb Z)\cong\mathbb Z^2\). The degree-zero attaching map is nullhomotopic. Attaching the six-cell therefore produces \(S^5\vee S^5\vee S^6\), proving the claimed integral homotopy equivalence.

## Verification
The accompanying standard-library-only program `verify_torus4x7.py` is a complete executable proof certificate: it generates the graph, enumerates all independent sets, reproduces the face vector, both discrete-Morse matchings and their exact signed boundary matrices, and checks acyclicity by exhaustive traversal of the oriented Hasse graph. It requires no downloaded data, randomness, or third-party packages. Run `python3 verify_torus4x7.py` and compare with `verification_output.txt`.

As a separately ordered cross-check, the priority sequence
\[
(15,17,6,20,19,21,23,7,10,25,14,24,4,2,12,1,26,11,16,27,5,9,18,0,13,22,8,3)
\]
yields one critical vertex, five critical dimension-five faces and four critical dimension-six faces. Its signed degree-six-to-five Morse matrix is
\[
\begin{pmatrix}
0&-1&0&0&1\\
-1&0&0&-1&0\\
1&0&-1&0&0\\
0&0&1&1&0
\end{pmatrix}.
\]
A top-left three-by-three minor is a unit, and the last row is minus the sum of the second and third rows. Thus its integral boundary has rank three with primitive image, independently yielding ranks two and one in degrees five and six. This cross-check verifies homology; the first, stronger matching and its zero attachment additionally verify the integral homotopy type.

## Relationship to prior work
Jonsson's 2006 theorem considers precisely the doubly periodic square-grid graph and calculates the Euler characteristic, including the coprime side-length phenomenon. For this pair of sides, it implies \(\widetilde\chi=-1\), but does **not** imply the integral wedge decomposition or either separate Betti number. Bousquet-Mélou, Linusson and Nevo compute homotopy types for different open/cylindrical boundary conditions and identify the toric homotopy case as outside their treatment. Adamaszek studies cylindrical grids and other lattice examples; Okura treats grid-graph operations and certain open/cylindrical cases. Published exact homotopy records for other square tori, such as the \(4\)-by-\(4\), \(5\)-by-\(5\), and \(5\)-by-\(6\) cases, concern different graph sizes and do not imply this case. In particular, the seven-cycle categorical product with a four-color complete graph is a different graph product.

## Limitations
The result is for the single specified graph and is nonequivariant. It does not classify the integral action of torus symmetries, persistence across other sizes, or larger families of tori. Finite exhaustive computation is a valid proof only because all faces, covers and matching paths were generated and exhaustively checked; it should not be extrapolated to infinitely many grid sizes. Publication priority beyond the inspected literature and accessible published records has not been independently established. Independent mathematical validation has not been performed.

## References
1. Jakob Jonsson, *Hard Squares with Negative Activity and Rhombus Tilings of the Plane*, **Electronic Journal of Combinatorics** 13 (2006), R67; first public publication 2006-08-07. https://doi.org/10.37236/1093
2. Mireille Bousquet-Mélou, Svante Linusson, Eran Nevo, *On the Independence Complex of Square Grids*, first posted 2007-01-30, arXiv:math/0701890. https://arxiv.org/abs/math/0701890
3. Michał Adamaszek, *Hard Squares on Cylinders Revisited*, first posted 2012-02-08, arXiv:1202.1655. https://arxiv.org/abs/1202.1655
4. Kengo Okura, *Simple Homotopy Types of Independence Complexes of Graphs Involving Grid Graphs*, first posted 2019-08-25, arXiv:1908.09356. https://arxiv.org/abs/1908.09356
