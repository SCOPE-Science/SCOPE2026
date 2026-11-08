# Exact all-order Minkowski-averaging profiles of orthotope face skeleta

## Finding

Let \(n\ge1\), \(\ell_1,\ldots,\ell_n>0\), and let the orthotope be \(B=\prod_{j=1}^{n}[0,\ell_j]\). For an integer \(0\le k\le n\), let \(S_k(B)\) denote the closed \(k\)-skeleton: the union of all closed faces of dimension at most \(k\). For every integer \(N\ge1\), form the equal-weight Minkowski average
\[
M_N=\left\{\frac{y^{(1)}+\cdots+y^{(N)}}{N}:y^{(t)}\in S_k(B)\text{ for every }t\right\}.
\]
Set \(G_{j,N}=\{a\ell_j/N:a\in\{0,\ldots,N\}\}\), \(m=\max\{n-Nk,0\}\), and \(\delta_j(x)=\operatorname{dist}(x_j,G_{j,N})\). Write \(\delta_{(1)}(x)\le\cdots\le\delta_{(n)}(x)\) for the sorted coordinate distances. Then the **exact finite-order set** is
\[
\boxed{M_N=\bigl\{x\in B:\#\{j:x_j\notin G_{j,N}\}\le Nk\bigr\}.}\tag{1}
\]
For every \(x\in B\) and each \(1\le p<\infty\), its exact distance to this nonconvex average is
\[
\boxed{\operatorname{dist}_{p}(x,M_N)
=\left(\sum_{j=1}^{m}\delta_{(j)}(x)^p\right)^{1/p}.}\tag{2}
\]
For \(p=\infty\), the distance is zero when \(m=0\), and equals \(\delta_{(m)}(x)\) when \(m>0\). Let \(\ell_{[1]}\le\cdots\le\ell_{[n]}\) be the increasing rearrangement of side lengths. Since \(M_N\subseteq B=\operatorname{conv}(M_N)\), the exact \(\ell_p\) Hausdorff distance to the convex hull is
\[
\boxed{d_{H,p}(M_N,B)=\frac1{2N}\left(\sum_{j=1}^{m}\ell_{[j]}^{p}\right)^{1/p},\qquad1\le p<\infty.}\tag{3}
\]
For \(p=\infty\) it is zero when \(m=0\), and otherwise equals \(\ell_{[m]}/(2N)\). In particular, **every positive-dimensional skeleton fills the box at the sharp order**
\[
\boxed{M_N=B\ \Longleftrightarrow\ Nk\ge n,}\tag{4}
\]
and the least such \(N\) is \(\lceil n/k\rceil\) when \(k\ge1\). For the vertex skeleton \(k=0\), no finite average equals \(B\).

The exact stratification also gives \(\dim_{\mathrm H}M_N=\min\{n,Nk\}\). Thus when \(Nk<n\), every such average has **zero ambient \(n\)-dimensional volume**, although its Hausdorff distance to the full box is explicitly finite and tends to zero when \(k=0\) as the order grows. For the *unit cube* and \(m>0\), the farthest points are exactly the \(N^n\) simultaneous coordinate grid-cell centers when \(1\le p<\infty\). In the \(\ell_\infty\) metric, a point is farthest precisely when at least \(Nk+1\) of its coordinates are grid-cell centers.

## Assumptions and scope

All quantifiers in (1)–(4) are universal for integers \(n\ge1\), \(0\le k\le n\), \(N\ge1\), arbitrary strictly positive real side lengths, and \(1\le p\le\infty\). No lattice or rationality restriction is imposed. Distances use the usual coordinate \(\ell_p\) norms in the displayed orthogonal coordinates. A face of dimension at most \(k\) may have at most \(k\) coordinates strictly between its two endpoints; every other coordinate is exactly an endpoint. The closed skeleton includes all subfaces and vertices. The empty sum in (2) and (3) is zero, and the \(\ell_\infty\) statements are given separately to cover \(m=0\) without an undefined order statistic. The convex hull of each \(M_N\) is the entire box because every vertex of \(B\) belongs to \(S_k(B)\) and hence to \(M_N\).

## Proof

**1. Exact structure of the average.** Every summand \(y^{(t)}\in S_k(B)\) has at most \(k\) coordinate entries in the open intervals \((0,\ell_j)\). In each coordinate \(j\), if every summand entry is an endpoint, the output is an element of \(G_{j,N}\). Thus each coordinate of the average that is *not* in its grid requires at least one summand that is non-endpoint in that coordinate. The total available non-endpoint positions over all summands is at most \(Nk\), proving the forward inclusion in (1).

Conversely, fix \(x\in B\) with at most \(Nk\) off-grid coordinates. For each off-grid coordinate, write \(Nx_j/\ell_j=a_j+\theta_j\) with \(a_j\in\{0,\ldots,N-1\}\) an integer and \(0<\theta_j<1\). Choose one of the \(N\) summand rows to contain the single non-endpoint entry \(\theta_j\ell_j\); put \(\ell_j\) into any \(a_j\) other rows, and put zero into the remaining rows. It is possible to distribute the off-grid coordinates so that each row receives at most \(k\) of these non-endpoint entries, because there are at most \(Nk\) such coordinates and no other coupling restriction. For every grid coordinate \(x_j=a_j\ell_j/N\), put \(\ell_j\) into exactly \(a_j\) rows and zero into the remaining rows; this works also at both endpoints, including \(a_j=N\). The resulting \(N\) rows belong to \(S_k(B)\) and average to \(x\). This proves (1) for all edge cases.

**2. Pointwise distance.** By (1), membership in \(M_N\) means that all but at most \(Nk\) coordinates belong to their grids. Consequently at least \(m=\max(n-Nk,0)\) coordinates must be changed to grid points. If a coordinate \(j\) is changed to the grid, the least possible absolute displacement is precisely \(\delta_j(x)\); a coordinate left free needs no change. These displacements minimize each coordinate independently. For finite \(p\), minimize the sum of the \(p\)th powers of the displacements by selecting the \(m\) smallest \(\delta_j\), proving (2). For the sup norm, the analogous minimum over \(m\)-element subsets is their smallest possible maximum, which is \(\delta_{(m)}\). If \(m=0\), (1) already gives \(M_N=B\).

**3. Sharp Hausdorff bound.** Each coordinate grid divides \([0,\ell_j]\) into \(N\) equal intervals, so \(0\le\delta_j(x)\le\ell_j/(2N)\). Because the sum of the \(m\) smallest nonnegative \(p\)th powers, or the \(m\)th smallest nonnegative number, is monotone in every coordinate, the pointwise formulas imply the upper bounds in (3) and in its \(\ell_\infty\) counterpart. Choose for every coordinate any one of its \(N\) grid-cell midpoint values \(x_j=(a_j+1/2)\ell_j/N\), \(a_j=0,\ldots,N-1\). Then \(\delta_j(x)=\ell_j/(2N)\) simultaneously for every coordinate, attaining the stated bounds. The Hausdorff distance equals the maximum point-to-set distance because \(M_N\subset B\). This proves (3) and the sup-norm formula.

**4. Saturation and dimension.** If \(Nk\ge n\), the condition in (1) is vacuous and \(M_N=B\). If \(Nk<n\), take any point all of whose coordinates are off-grid; it lies in \(B\setminus M_N\). Hence the threshold is necessary and sufficient, including \(k=0\). Formula (1) is a finite union of coordinate affine cells of dimensions at most \(Nk\), with at least one cell of dimension exactly \(Nk\) when \(0\le Nk<n\): fix \(n-Nk\) coordinates at grid points and let the other \(Nk\) vary freely in open subintervals. Therefore its Hausdorff dimension is exactly \(Nk\) below threshold and \(n\) afterward. In particular it has zero ambient volume below threshold.

**5. Exact farthest-point sets for the unit cube.** If all \(\ell_j=1\) and \(m>0\), all coordinate distances obey \(\delta_j\le1/(2N)\). For \(p<\infty\), attaining the maximum sum of the \(m\) smallest \(p\)th powers forces *all* \(n\) distances to equal \(1/(2N)\). Hence the farthest points are exactly the \(N^n\) Cartesian products of grid-cell midpoints. In the sup norm, the \(m\)th smallest distance attains \(1/(2N)\) if and only if at least \(n-m+1=Nk+1\) coordinates attain that distance, giving the asserted full farthest-point locus. All claims follow. \(\square\)

## Verification

The standalone standard-library script `checker.py` independently builds finite Minkowski sumsets from discretized face points and compares their membership with the grid-stratum condition for \(1\le n\le4\), \(0\le k\le n\), and \(1\le N\le3\). It then tests the coordinate-order-statistic squared-distance formula by an independent exhaustive search over constrained-coordinate choices, and checks the sharp anisotropic radius upper bound and attainment for three rectangular side-length profiles. Run `python3 checker.py`: its actual output is `PASS: 28065 exact assertions`. All arithmetic is integral or rational. The infinite and continuous statements are proved in the preceding five steps; finite checks are not claimed to be exhaustive over real points, dimensions, orders, or norms.

## Relationship to prior work

Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition* (arXiv:2606.10815v1, first publicly posted 2026-06-09), supplies sharp universal dimension-order phenomena and a raised-simplex obstruction, rather than grid-stratum identities or all-order distance formulas for cubical skeleta. The present complete, exact per-order profile has a different source geometry and includes finite filling, which cannot follow from a universal statement about strict decrease at a particular order.

Fradelizi, Madiman, Marsiglietti, and Zvavitch, *The convexification effect of Minkowski summation* (arXiv:1704.05486), especially Sections 1 and 7, establish general Hausdorff-distance inequalities, eventual monotonicity, and asymptotic bounds for Minkowski averages. Those inequalities bound rather than determine the coordinatewise shape of \(M_N\) or sharp distances at all finite orders. Their earlier *Do Minkowski averages get progressively more convex?* (arXiv:1512.03718) addresses related general nonconvexity questions, not this explicit orthotope skeleton classification.

Meyer, *Finite convexification by Minkowski summation* (arXiv:2610.26744v1, first posted 2026-10-19), studies **a fixed nonconvex set plus a scaled convex summand**. Its exposed-face and covering-radius criteria do not assert an exact repeated-average formula for a nonconvex skeleton. Existing explicit results for **simplex** skeleta concern different face geometry; in particular, an all-\(N\) orthotope grid-stratum characterization cannot be inferred by substituting a simplex. An exact raised-simplex Hausdorff example also uses an entirely different compact set. Searches for equivalences under the terms cubical skeleton, hypercube face skeleton, Minkowski self-sum, iterated Minkowski average, and Hausdorff convexification identified no known covering theorem, but historical priority cannot be guaranteed by indexed search alone.

## Limitations

The formula relies on a Cartesian product of intervals and coordinate \(\ell_p\) norms; it does not assert the same explicit metric profile for arbitrary affine images, nonorthogonal parallelotopes, simplices, arbitrary polytopes, or arbitrary norms. No general monotonicity claim about all nonconvex sets or a best universal Hausdorff contraction constant is derived. For \(Nk<n\), the average has zero ambient volume, so the exact Hausdorff profile is not an assertion of volumetric convergence. Exhaustive priority over unindexed or inaccessible literature is not claimed, and independent mathematical validation remains outstanding.

## References

1. P. van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1 (first posted 2026-06-09), https://arxiv.org/abs/2606.10815 .
2. M. Fradelizi, M. Madiman, A. Marsiglietti, A. Zvavitch, *The convexification effect of Minkowski summation*, arXiv:1704.05486 (first posted 2017-04-18; later published in EMS Surveys in Mathematical Sciences), https://arxiv.org/abs/1704.05486 .
3. M. Fradelizi, M. Madiman, A. Marsiglietti, A. Zvavitch, *Do Minkowski averages get progressively more convex?*, arXiv:1512.03718, https://arxiv.org/abs/1512.03718 .
4. M. Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1 (first posted 2026-10-19), https://arxiv.org/abs/2610.26744 .
