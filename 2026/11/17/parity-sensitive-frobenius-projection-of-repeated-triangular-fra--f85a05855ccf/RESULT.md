# Parity-sensitive Frobenius projection of repeated triangular fractional matchings

## Finding

For each integer \(r\geq 1\), put \(n=3r\) and partition \([n]\) into \(r\) disjoint triples. Let \(A_r\) be the symmetric doubly stochastic \(n\times n\) matrix with zero diagonal, entry \(1/2\) between different vertices of the same triple, and zero entries between triples. Let \(\mathcal I_n\) be the convex hull of the symmetric permutation matrices, equivalently the permutation matrices of all involutions of \([n]\). Distances use the ambient Frobenius norm \(\|X\|_F^2=\sum_{i,j}X_{ij}^2\).

**Theorem.** For every integer \(r\geq1\), the squared Euclidean distance from the repeated fractional-triangle vertex to the involution polytope is
\[
\operatorname{dist}_F(A_r,\mathcal I_{3r})^2=
\begin{cases}
\displaystyle \frac r6+\frac{r}{3(3r-2)},&r\text{ even},\\[4pt]
\displaystyle \frac r6+\frac{r+2}{9r},&r\text{ odd}.
\end{cases}
\]
There is a **unique** nearest matrix \(Y_r\). Its entries are constant within three classes: diagonal entries \(a_r\); off-diagonal entries within one of the designated triples \(b_r\); and entries joining different triples \(c_r\). They are
\[
(a_r,b_r,c_r)=
\begin{cases}
\displaystyle\left(\frac1{3(3r-2)},\frac13,\frac1{3(3r-2)}\right),&r\text{ even},\\[5pt]
\displaystyle\left(\frac1{3r},\frac13,\frac1{9r}\right),&r\text{ odd}.
\end{cases}
\]
For \(r=1\), the inter-triple class is empty and \(c_r\) is immaterial.

An exact parity-sensitive correction survives beyond the leading term:
\[
\operatorname{dist}_F(A_r,\mathcal I_{3r})^2=
\begin{cases}
\displaystyle\frac r6+\frac19+\frac2{27r}+O(r^{-2}),&r\text{ even},\\[4pt]
\displaystyle\frac r6+\frac19+\frac2{9r},&r\text{ odd}.
\end{cases}
\]
In contrast, projecting each triple separately to the three-dimensional involution polytope incurs squared error \(r/2\). Allowing transpositions between triples therefore reduces the leading error by a factor of three.

## Assumptions and scope

The involution polytope \(\mathcal I_n\) is *not* the full polytope of symmetric doubly stochastic matrices. The latter contains \(A_r\), which is a vertex because its nonzero support consists of disjoint odd cycles. This can also be checked directly: any nonnegative symmetric stochastic matrix supported on the same disjoint triangles must assign \(1/2\) to each triangle edge. The theorem concerns the distance of this distinguished infinite family of fractional vertices to the *integral* involution hull, not the Hausdorff distance of the two entire polytopes.

An involution decomposes into fixed points and unordered transpositions. Its permutation matrix has one diagonal unit for each fixed point and two symmetric off-diagonal units for each transposition. This convention is essential to the Frobenius normalization.

## Proof

**Construction of an attainable candidate.** In each of the \(r\) triples, independently choose one of its three unordered pairs uniformly and transpose the two selected vertices. One unpaired vertex remains exposed in each triple. Match the \(r\) exposed vertices by an auxiliary random involution on the triple indices.

When \(r\) is even, choose the identity auxiliary involution with probability \(p=1/(3r-2)\); otherwise choose a uniformly random perfect matching of the indices. Each index is fixed with probability \(p\); each distinct pair of indices is transposed with probability \((1-p)/(r-1)=3/(3r-2)\). When \(r\) is odd, use a uniformly random auxiliary involution having exactly one fixed index and a perfect matching on the others. Each index is fixed with probability \(1/r\); each distinct pair is transposed with probability \(1/r\). The latter construction also applies when \(r=1\).

Every outcome is a genuine involution on \([3r]\). The expectation of its permutation matrix therefore belongs to \(\mathcal I_{3r}\). Its diagonal entries equal one third of the auxiliary fixed-point probability; its within-triple off-diagonal entries equal \(1/3\); its inter-triple entries equal one ninth of the auxiliary pair-transposition probability. Hence this expectation is exactly the stated \(Y_r\).

**Global nearest-point certificate.** Let \(Q\) be an arbitrary involution permutation matrix. Let \(I\) be the number of its transpositions lying entirely within one designated triple, \(C\) the number joining different triples, and \(F\) the number of fixed vertices. Necessarily
\[
0\le I\le r,\qquad F+2(I+C)=3r,\qquad F\ge0.
\]
If \(r\) is odd, then \(F\ge1\). Put \(R=A_r-Y_r\), and abbreviate the diagonal and inter-triple entries of \(Y_r\) by \(a,c\). Since its within-triple entries are \(1/3\), a direct summation over matrix coordinates yields
\[
\langle R,Q\rangle=-aF+\frac I3-2cC
=-3ra+\left(2a+\frac13\right)I+2(a-c)C.
\]

For even \(r\), we have \(a=c>0\); the displayed expression strictly increases with \(I\) and is maximal when \(I=r\). Every involution used in the candidate mixture has exactly one internal transposition in each triple, hence attains this same maximum. By linearity, for every involution matrix \(Q\),
\[
\langle A_r-Y_r,Q-Y_r\rangle\le0.
\]

For odd \(r\), we have \(a=1/(3r)\) and \(c=1/(9r)\), so \(a-c>0\). Parity of the total number of vertices gives \(F\ge1\), hence
\[
C\le\frac{3r-1}{2}-I.
\]
Substitution in the scalar product produces an upper bound strictly increasing in \(I\), since the coefficient of \(I\) is \(1/3+2/(9r)>0\). Consequently the upper bound is maximized at \(I=r\) and \(C=(r-1)/2\), or equivalently \(F=1\). Every involution used in the odd candidate mixture has exactly these counts, including the case \(r=1\). Therefore the identical projection inequality holds for all involution matrices \(Q\).

All members of \(\mathcal I_{3r}\) are convex combinations of these matrices, so the projection inequality holds for every \(Z\in\mathcal I_{3r}\). The Euclidean projection characterization proves that \(Y_r\) is a nearest point to \(A_r\). Strict convexity of squared Frobenius distance proves uniqueness.

**Distance calculation.** Every triple contributes three diagonal and six ordered off-diagonal entries. There are \(9r(r-1)\) ordered inter-triple positions. Thus
\[
\|A_r-Y_r\|_F^2=3r a^2+6r\left(\frac12-\frac13\right)^2+9r(r-1)c^2.
\]
Substituting the appropriate \(a,c\) gives the two rational formulas. Their asymptotic expansions follow by elementary division. A single triangle has squared error \(1/2\), so independent blockwise projections incur \(r/2\), whereas the exact unrestricted projection has leading term \(r/6\).

## Verification

The accompanying `verify_triangle_projection.py` uses exact rational arithmetic to verify the row sums, nonnegativity, symmetry, squared-distance identities, primal mixture marginals, and every possible count-based projection inequality for \(1\le r\le25\). It also exhaustively checks all \(142852\) involution matrices through \(r=4\), with equality witnesses, and independently solves three full matching-blossom constrained quadratic programs for \(r=1,2,3\). Reproduce with `python verify_triangle_projection.py` (NumPy and SciPy required only for the last three numerical QPs). Finite tests corroborate the proof and are not an infinite-domain argument.

## Relationship to prior work

Brualdi and Cao classify extreme points of symmetric doubly stochastic polytopes using loops, edges, and odd cycles and identify symmetric permutation matrices. That classification supplies the conceptual source for the repeated fractional-triangle family; it does not supply the present Euclidean projection formula, its inter-triple optimum, or the parity-dependent correction. The distinction between a fractional matching relaxation and an integral matching polytope is standard; this theorem quantifies a canonical repeated minimal obstruction under the matrix Frobenius metric. A related published result on Euclidean radii and diameters of matching relaxations studies different extrema and does not provide the nearest-point projection calculated here.

## Limitations

This theorem addresses only the explicit vertices \(A_r\), and no statement is made about a global Hausdorff distance, other fractional vertices, arbitrary cost metrics, or other Schatten norms. Its historical priority is provisional; an older formulation under symmetric assignment, involution matching, or least-squares terminology may remain unidentified. No independent mathematical audit has been performed.

## References

1. R. A. Brualdi and L. Cao, *Symmetric, Hankel-Symmetric, and Centrosymmetric Doubly Stochastic Matrices*, arXiv:1712.03129v1, first publicly posted 2017-12-08; Acta Mathematica Vietnamica 43 (2018), 675–700. https://arxiv.org/abs/1712.03129
2. J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910, first posted 2023-06-20. https://arxiv.org/abs/2306.11910 (context for integral and fractional matching polytope descriptions in bipartite settings; not a claim about the present nonbipartite projection).
