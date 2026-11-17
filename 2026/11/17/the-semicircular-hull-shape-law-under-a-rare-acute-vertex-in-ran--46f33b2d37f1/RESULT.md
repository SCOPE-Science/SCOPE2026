# The semicircular-hull shape law under a rare acute vertex in random cyclic polygons

## Finding
Let \(n\ge5\) independent uniformly sampled points on the unit circle define a convex cyclic polygon \(K_n\), and let \(\mathcal E_n\) denote the event that at least one interior angle is acute. Rotate the polygon so a designated acute vertex lies at \(1\) on the circle, choosing the unique acute vertex when it exists, and a measurable acute vertex otherwise. Conditional on \(\mathcal E_n\), the rotated polygon converges in distribution in Hausdorff distance to
\[
 K(U)=\operatorname{conv}\left(\{1\}\cup\{e^{it}:\pi(1-U)\le t\le\pi(2-U)\}\right),\quad U\sim\operatorname{Unif}(0,1).
\]
Moreover, if \(S_n\) is the sum of the two adjacent normalized circular gaps at that acute vertex, then, jointly,
\[
 (K_n,n(S_n-1/2))\ \Longrightarrow\ (K(U),E),\qquad E\sim\operatorname{Exp}(2),\quad E\perp U.
\]
The limiting area \(A_\infty\) and perimeter \(P_\infty\) have the joint representation
\[
 A_\infty=\frac\pi2+\sin(\pi U),\qquad P_\infty=\pi+2\left[\sin\left(\frac{\pi U}{2}\right)+\cos\left(\frac{\pi U}{2}\right)\right].
\]
In particular, for \(0\le x\le1\),
\[
 \Pr(A_\infty\le\pi/2+x)=\frac2\pi\arcsin x,
 \qquad \lim_{n\to\infty}\mathbb E[\operatorname{area}(K_n)\mid\mathcal E_n]=\frac\pi2+\frac2\pi,
\]
\[
 \lim_{n\to\infty}\mathbb E[\operatorname{perimeter}(K_n)\mid\mathcal E_n]=\pi+\frac8\pi.
\]
The angle-event probability and the zero/one/two acute-count formulas used below are *previously known* (Putnam 2005, Problem A6), and are not the new result.

## Assumptions and scope
Sample independent angles from uniform measure on \([0,2\pi)\), sort them cyclically, and connect consecutive points by straight Euclidean chords. Acute means strictly less than \(\pi/2\). The normalized gaps are positive, sum to one, and have \(\operatorname{Dirichlet}(1,\ldots,1)\) law. The result is an asymptotic conditional theorem as the number of vertices tends to infinity; no claim of finite-size equality for the limiting area law is made. All area and perimeter values refer to the Euclidean polygon and the unit-circle scale. The mark for the negligible event of two acute vertices may be chosen measurably by any deterministic rule.

## Proof
Let \(G_i\) be the circular gap from vertex \(i\) to vertex \(i+1\), measured in turns. The inscribed-angle theorem gives the exact acute criterion \(G_{i-1}+G_i>1/2\). Nonadjacent acute vertices are impossible, and three acute vertices are impossible. The classical Putnam count calculation gives
\[
 \Pr(\mathcal E_n)=\frac{n(n-2)}{2^{n-1}},\qquad
 \Pr(\text{two acute vertices}\mid\mathcal E_n)=\frac2{n-2}.
\]
For a fixed labelled vertex, write its adjacent gaps as \(A,B\). Dirichlet aggregation gives \(S=A+B\sim\operatorname{Beta}(2,n-2)\) and \(U=A/S\sim\operatorname{Unif}(0,1)\), with independence; the acute event is precisely \(S>1/2\), so this independence persists under conditioning. The beta survival probability is
\[
 \Pr(S>s)=(1-s)^{n-2}[1+(n-2)s].
\]
Therefore, for every fixed \(t\ge0\),
\[
 \Pr(n(S-1/2)>t\mid S>1/2)=\frac{(1/2-t/n)^{n-2}[1+(n-2)(1/2+t/n)]}{(1/2)^{n-2}[1+(n-2)/2]}\longrightarrow e^{-2t}.
\]
The probability of a second acute vertex, conditional on the first labelled one, is \(4/n\): the two possible neighboring joint events each have unconditional probability \(2^{2-n}\), while one labelled acute event has probability \(n2^{1-n}\). Thus conditioning additionally on uniqueness perturbs the law of \((S,U)\) by at most \(4/n\) in total variation. Given uniqueness, symmetry identifies the selected acute vertex with a uniformly randomly labelled acute vertex. Because the multiple-acute event under \(\mathcal E_n\) itself has probability \(2/(n-2)\), the limiting \((U,n(S-1/2))\) are independent \(\operatorname{Unif}(0,1)\) and \(\operatorname{Exp}(2)\), respectively.

Conditional on the two marked gaps, the remaining \(n-2\) normalized gaps form an independent Dirichlet vector scaled by \(1-S\). For any fixed \(\delta>0\), its largest entry tends to zero in probability by the union bound and the beta one-coordinate tail, at an exponential rate. Thus the other polygon vertices become dense on the complementary circular arc of length \(2\pi(1-S)\), which converges to a semicircle. Rotating the acute vertex to the point \(1\), the complementary arc begins at angle \(2\pi B\) and ends at angle \(2\pi(1-A)\). Since \((A,B)\to(U/2,(1-U)/2)\) under an appropriate convention, the limiting arc is \([\pi(1-U),\pi(2-U)]\). If the convention exchanges \(A\) and \(B\), the result is identical after replacing \(U\) by \(1-U\), which is also uniform. Continuity of convex hull in Hausdorff distance proves the joint geometric convergence.

The limiting arc contributes exactly a half-disk of area \(\pi/2\), with diameter joining its antipodal endpoints. The apex adds a triangle of base length two and perpendicular height \(\sin(\pi U)\), hence area \(\sin(\pi U)\). The boundary comprises a semicircle and two apex-to-endpoint chords, giving the displayed perimeter formula. The arcsine CDF follows by elementary change of variables. As areas and perimeters are uniformly bounded by \(\pi\) and \(2\pi\), convergence in distribution also yields convergence of the displayed expectations.

## Verification
The supplementary Python script `conditional_shape_checks.py` tests the classical acute-count probabilities against independent Dirichlet simulations at five polygon sizes and checks area and perimeter against the proposed conditional limit through exact conditional beta-tail inversion at sizes 30, 80 and 200. All tests pass. The random simulations corroborate limiting geometry but do not replace the Dirichlet/convex-hull proof.

## Relationship to prior work
The finite-sample acute-angle count and event probability are established by Putnam 2005 Problem A6. Those results give no conditional Hausdorff limit for the entire random polygon and no joint nondegenerate limiting area/perimeter law. Finch (2016) treats geometric distributions for fixed small cyclic polygons, and Koroleva–Nikitin (2013) treat unconditional extremes of randomly inscribed polygon areas and perimeters. The conditional rare-event degeneration here is different from those models and from unconditional large-\(n\) approximation to the disk. No claim is made that merely recomputing the Putnam probability is new.

## Limitations
The theorem is limited to independent circular-uniform samples and conditioning on at least one acute Euclidean interior angle. The result does not cover noncircular curves, weighted sampling, quantitative rates in Hausdorff distance, or independent proof of historical priority. The first-order event probability and acute-angle counts are known prior results; the claimed contribution is the conditional marked geometric limit and its area/perimeter consequences.

## References
- William Lowell Putnam Mathematical Competition (2005), Problem A6 and published solutions. Accessible worked solution: https://studyres.com/doc/1202631/problem-a6---art-of-problem-solving
- Steven R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510 (first posted 2016-10-03), https://arxiv.org/abs/1610.00510
- Elena V. Koroleva and Yakov Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (first posted 2013-01-07), https://arxiv.org/abs/1301.1360
