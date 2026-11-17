# The five-level four-simplex spectrum of the extremal nine-vertex four-polytope

## Finding

Let \(P\subset\mathbb R^4\) be the maximum-volume nine-vertex polytope inscribed in the Euclidean unit three-sphere. Its uniqueness up to orthogonal motion and its realization as the orthogonal free sum of a regular square and a regular pentagon are established in Medgyes (2026). Write \(\mathcal V(P)\) for the multiset of four-dimensional volumes of the \(\binom95=126\) simplices obtained by choosing five distinct vertices, and set \(V=\operatorname{vol}_4(P)\). Then the **complete relative volume spectrum**, with multiplicities, is

\[
\begin{array}{c|ccccc}
\operatorname{vol}_4(\Delta)/V &0&(\sqrt5-1)/20&(5-\sqrt5)/40&1/10&\sqrt5/20\\
\hline
\text{multiplicity}&46&20&20&20&20.
\end{array}
\]

In particular the largest volume of **any** four-simplex contained in \(P\), allowing arbitrary points rather than only vertices, is exactly

\[
\max_{\Delta\subseteq P}\operatorname{vol}_4(\Delta)
=\frac{\sqrt5}{20}\operatorname{vol}_4(P)
=\frac{\sqrt5}{24}\sin\frac{2\pi}{5}.
\]

Exactly twenty five-vertex subsets attain the maximum. Each uses two adjacent vertices of the square and three pentagon vertices with cyclic spacing pattern \((1,2,2)\), up to cyclic permutation. No classification of all (possibly non-vertex-supported) maximizing inscribed simplices is asserted.

## Assumptions and scope

The ambient metric is standard Euclidean distance. We use the fixed coordinate representative

\[
A_j=(\cos(\pi j/2),\sin(\pi j/2),0,0),\quad 0\le j<4,
\]
\[
B_k=(0,0,\cos(2\pi k/5),\sin(2\pi k/5)),\quad 0\le k<5,
\]

and \(P=\operatorname{conv}\{A_j,B_k\}\). The word spectrum refers to unordered five-element vertex subsets, counting a zero volume when affine dependence occurs. Multiplicities are for labelled vertices, not symmetry orbits. Let \(s=\sin(2\pi/5)\) and \(t=\sin(\pi/5)\). Medgyes proves \(V=5s/6\); this volume is **prior work**.

## Proof

**Orthogonal determinant splitting.** For points \(a_i\) in the first coordinate plane and \(b_i\) in the second, the standard augmented affine determinant \(\det[(1,x_i)]\) is alternating and multilinear. If a five-vertex subset takes three points from the square and two from the pentagon, block row reduction gives

\[
\operatorname{vol}_4\operatorname{conv}\{a_1,a_2,a_3,b_1,b_2\}
=\frac1{12}\operatorname{area}\operatorname{conv}\{a_1,a_2,a_3\}\,|\det(b_1,b_2)|.
\]

Similarly, for two square points and three pentagon points,

\[
\operatorname{vol}_4\operatorname{conv}\{a_1,a_2,b_1,b_2,b_3\}
=\frac1{12}|\det(a_1,a_2)|\,\operatorname{area}\operatorname{conv}\{b_1,b_2,b_3\}.
\]

The coefficient is \(2/24\): one factor is twice a planar triangle area, while the other is a planar determinant. Equivalently these formulas follow by expanding the four-dimensional difference determinant along the two orthogonal coordinate blocks.

**The \(3+2\) split.** Each of the four square triangles has area \(1\). Among the ten unordered pairs of regular-pentagon vertices, five are adjacent and have determinant magnitude \(s\), and five are nonadjacent and have magnitude \(t\). Thus \(3+2\) contributes twenty simplices of volume \(s/12\) and twenty of volume \(t/12\).

**The \(2+3\) split.** Four square pairs are adjacent, with determinant magnitude \(1\); two pairs are opposite, with determinant zero. The ten pentagon triangles split into five consecutive triples (cyclic gap pattern \((1,1,3)\)) of area \((2s-t)/2\), and five triples of cyclic gap pattern \((1,2,2)\) of area \((s+2t)/2\). Therefore adjacent square pairs give twenty volumes \((2s-t)/24\) and twenty volumes \((s+2t)/24\), whereas the two opposite square pairs paired with each of the ten pentagon triples give twenty zero volumes.

**Remaining splits.** With at most one point from either of the two coordinate planes, the affine span of the five points has dimension at most three. In detail, the possible \((\#A,\#B)\) splits \((0,5)\), \((1,4)\), and \((4,1)\) contribute respectively \(1\), \(20\), and \(5\) zero volumes. Together with the twenty opposite-pair cases, this yields \(46\) zeros. There are no \((5,0)\) cases. The total count is \(46+4\cdot20=126\), so the classification is exhaustive.

**Normalization and strict ordering.** Dividing the four positive values by \(V=5s/6\) and using \(t/s=2\sin(\pi/5)/(2\sin(2\pi/5))=1/(2\cos(\pi/5))=(\sqrt5-1)/2\) yields, in increasing order,

\[
\frac{\sqrt5-1}{20},\quad\frac{5-\sqrt5}{40},\quad\frac1{10},\quad\frac{\sqrt5}{20}.
\]

The inequalities are strict; for example \(0<\sqrt5-1< (5-\sqrt5)/2<2<\sqrt5\). The maximum is contributed exactly by adjacent square pairs and cyclic \((1,2,2)\) pentagon triples, giving \(4\cdot5=20\) vertex subsets.

**Unrestricted inscribed simplices.** For arbitrary five points \(x_0,\ldots,x_4\in P\), their unsigned affine determinant is separately an absolute value of an affine function in each \(x_j\) when the other four points are fixed. The maximum of an absolute affine function on \(P\) is attained at a vertex of \(P\). Replacing the five points one after another by vertices without decreasing the determinant proves that the maximum over all contained four-simplices equals the maximum over vertex-supported ones. This argument proves equality of the maxima but does not assert that all maximizers are vertex-supported.

## Verification

Run `python3 verify.py` next to this document. The script separately enumerates all \(126\) vertex subsets, computes each determinant using a signed \(4\times4\) permutation expansion, verifies the five levels and their \((46,20,20,20,20)\) multiplicities, checks the golden-ratio normalizations, and checks the maximizing vertex pattern. It uses only the Python standard library. Floating-point checks are consistency evidence; the proof above supplies the exact universal assertion and the unrestricted-simplex reduction.

## Relationship to prior work

Medgyes (2026, arXiv:2611.10078v1, Theorem 7.1) determines the unique maximum-volume nine-vertex inscribed four-polytope and its total volume. This is the **input**, not part of the new claim. The same work studies signed facet-volume formulae for the orthogonal join; it does not classify volumes of the \(126\) five-vertex simplices nor their maximum contained-simplex fraction. Other published exact simplex spectra concern different convex bodies, including the regular 24-cell, regular 600-cell, and products of a simplex with a parallelogram. Those statements do not specialize to the square–pentagon **free sum** (a hull of polytopes in orthogonal subspaces). Exact determinant partition by two-plane vertex counts is the additional argument used here.

## Limitations

The full multiplicity spectrum is confined to the unique maximum-volume nine-vertex inscribed four-polytope, not every nine-vertex four-polytope. The count of twenty maximizers concerns **vertex subsets only**; continuous families of non-vertex-supported maximal simplices are not ruled out. No new bound on the volume of arbitrary nine-vertex four-polytopes is claimed. Historical priority remains provisional, especially for equivalent older descriptions of simplex-volume spectra of regular polygonal free sums.

## References

Medgyes, Csaba. *The inscribed 4-polytope of maximal volume with nine vertices*. arXiv:2611.10078v1, submitted 2026-11-06. https://arxiv.org/html/2611.10078v1

Medgyes, Csaba. *Inscribed 4-polytopes of maximal volume with seven and eight vertices*. arXiv:2610.26886v1, submitted 2026-10-12. https://arxiv.org/abs/2610.26886
