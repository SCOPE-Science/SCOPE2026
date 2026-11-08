# A sharp double-connectivity example on a five-dimensional simplicial sphere

## Finding

Let \(A\) and \(B\) be disjoint four-element sets and let \(X=\partial\Delta(A)*\partial\Delta(B)\), the join of two tetrahedral boundaries. It is a triangulated \(5\)-sphere. Write \(D^2(X)\) for the simplicial *double*: its vertices are two-element faces of \(X\), and its simplices are pairwise disjoint collections of such pairs whose union belongs to \(X\).

There is an integral homotopy equivalence
\[
\boxed{\left|D^2(X)\right|\simeq \left(\bigvee^{15}S^1\right)\vee\left(\bigvee^{78}S^2\right).}
\]
In particular \(\pi_1(|D^2(X)|)\) is a free group of rank \(15\), and \(\widetilde H_1\cong\mathbb Z^{15}\), \(\widetilde H_2\cong\mathbb Z^{78}\), with other reduced integral homology zero. The double is connected but not simply connected. The general weak Cohen–Macaulay connectivity guarantee for the double of a \(5\)-sphere is only connectivity \(0\), and the example realizes that bound sharply on a non-simplex simplicial sphere.

## Assumptions and scope

The sets \(A,B\) have cardinality exactly four; the symbol \(\partial\Delta(A)\) means all proper subsets of \(A\), including the empty face, and similarly for \(B\). An allowed union in \(X\) cannot contain all of \(A\) or all of \(B\). The result is ordinary, nonequivariant *integral homotopy*, not merely a Betti-number calculation. The double is the construction of Lesh–Schreiner–Wahl (Definition 2.1, with \(r=2\)).

## Proof

**1. Partition the double.** The \(28\) vertices of \(D^2(X)\) are the two-element subsets of \(A\sqcup B\). Call a pair *internal* if contained in \(A\) or contained in \(B\) (six choices on each side), and *cross* if it uses one point on each side (sixteen choices). Because a four-element internal union is not allowed, a simplex has at most one internal pair from each side. A three-pair simplex uses exactly six underlying points, hence three from \(A\) and three from \(B\). It is consequently either (i) three cross pairs, or (ii) one cross pair and one internal pair from each side. These are all possible maximal two-simplices.

Let \(C\) be the subcomplex of the cross-pair simplices. It is exactly the two-skeleton of the ordinary \(4\)-by-\(4\) chessboard complex \(\Delta_{4,4}\). Let \(Y\) consist of the simplices using at most one cross pair. Its internal-pair vertices span the complete bipartite graph \(K_{6,6}\), with shores \(\binom A2\) and \(\binom B2\). For each cross pair \((a,b)\), the link within \(Y\) is the graph \(K_{3,3}\) on the internal pairs avoiding \(a\) and avoiding \(b\). Thus \(Y\) is obtained from \(K_{6,6}\) by coning off sixteen specified \(K_{3,3}\) subgraphs. Directly from the allowable faces,
\[
D^2(X)=Y\cup C,\qquad Y\cap C=\{(a,b):a\in A,\ b\in B\},
\]
where the intersection is a discrete set of sixteen vertices (with their empty simplex).

**2. Each of \(Y\) and \(C\) is simply connected.** The theorem of Björner–Lovász–Vrećica–Živaljević states that the ordinary chessboard complex \(\Delta_{m,n}\) is \(\bigl(\min\{m,n,\lfloor(m+n+1)/3\rfloor\}-2\bigr)\)-connected. For \(m=n=4\) this is \(1\)-connected; passing to its two-skeleton does not alter its fundamental group. Hence \(C\) is simply connected.

For \(Y\), the fundamental group is a quotient of that of the base graph \(K_{6,6}\), because the sixteen new pieces are cones on connected subgraphs. Every loop in a complete bipartite graph is generated, up to homotopy, by its four-edge circuits. Write such a circuit as \(P-Q-P'-Q'-P\), where \(P,P'\in\binom A2\) and \(Q,Q'\in\binom B2\). If \(P\cap P'\ne\emptyset\) and \(Q\cap Q'\ne\emptyset\), their unions use at most three points on each side. Choose \(a\in A\setminus(P\cup P')\) and \(b\in B\setminus(Q\cup Q')\). The circuit is in the \(K_{3,3}\) subgraph coned off by cross pair \((a,b)\), so it is nullhomotopic in \(Y\). If \(P\cap P'=\emptyset\), choose a two-element pair \(U\) containing one point of each of \(P,P'\), and split the original square by the two-edge path through \(U\); this expresses its class as a product of two squares whose \(A\)-pairs intersect. If \(Q\cap Q'=\emptyset\), perform the analogous split on the \(B\)-side. Thus every square is a product of coned-off squares, proving \(\pi_1(Y)=0\). Both subcomplexes are connected.

**3. Their homotopy types.** A face count gives for \(C\) exactly \(16\) vertices, \(72\) edges and \(96\) triangles, and for \(Y\) exactly \(28\) vertices, \(132\) edges and \(144\) triangles. In both cases the Euler characteristic is \(40\). Both are connected simply connected two-dimensional CW complexes. Their integral second homology is free because it is a subgroup of the free cellular group in dimension two; connectedness and simple connectivity give vanishing first homology. Therefore each has \(H_2\cong\mathbb Z^{39}\). By Hurewicz, a basis of these integral classes has sphere representatives, and the homological Whitehead theorem gives
\[
|C|\simeq\bigvee^{39}S^2,\qquad |Y|\simeq\bigvee^{39}S^2.
\]

**4. Glue over the discrete intersection.** The inclusions of the discrete sixteen-point intersection are cofibrations, so the ordinary union models its homotopy pushout. For connected \(Y\) and \(C\), gluing them along \(16\) points is homotopy equivalent to their wedge plus \(16-1=15\) circles (choose paths joining the identified points and contract connecting spanning trees). Substituting the two sphere-wedge descriptions proves the displayed homotopy equivalence. No rationalization, unproved cancellation or extrapolation is involved.

## Verification

The standalone `check_double.py` enumerates all disjoint pair collections directly from the eight underlying vertices, partitions faces into \(C\) and \(Y\), checks their intersection is precisely sixteen vertices, checks each of the sixteen coned \(K_{3,3}\) link graphs, and independently computes reduced mod-\(p\) Betti numbers for \(p=2,101,103\). It obtains face vectors \((28,204,240)\), \((16,72,96)\), and \((28,132,144)\) for the full complex, \(C\), and \(Y\). The mathematical proof, not these finite-field computations, establishes the integral homotopy assertion.

## Relationship to prior work

Lesh, Schreiner and Wahl (2025 preprint, revised 2026) define \(D^r(X)\), prove a general weak Cohen–Macaulay connectivity bound and note sharpness for full simplices through complete-graph matching complexes. Their relevant statements do not give this non-simplex sphere example or its mixed-dimensional integral homotopy type. Björner, Lovász, Vrećica and Živaljević (1994) prove the chessboard connectivity used in step 2; that theorem is explicitly an input, not a claimed contribution. This finding strengthens a bound-sharpness observation with a complete homotopy decomposition for a natural join of two sphere boundaries.

## Limitations

The exact wedge decomposition is proved only for the join of two tetrahedral boundaries, not arbitrary spheres or all joins of simplex boundaries. The general doubling theorem and the classical chessboard connectivity result are prerequisites. No naturality or symmetry-equivariant splitting is asserted. A differently indexed computation of this particular double could still exist.

## References

1. K. Lesh, B. Schreiner, N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436 (first submitted June 12, 2025), Definition 2.1 and Theorem A; https://arxiv.org/html/2506.10436v2 .
2. A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society 49 (1994), 25–39; doi:10.1112/jlms/49.1.25 .
