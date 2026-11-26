# Conditional joint shape of the two acute angles in a random cyclic polygon

## Finding

Let \(n\geq 4\) independent points be sampled uniformly from a circle and joined in their circular order to form a convex cyclic polygon. Conditional on the event \(A_n=2\) that exactly two of its interior angles are acute, call those adjacent angles \(\alpha\) and \(\beta\), in either cyclic order, and set
\[
 U=\frac{\pi/2-\alpha}{\pi},\qquad V=\frac{\pi/2-\beta}{\pi}.
\]
Their joint density, with respect to ordinary two-dimensional Lebesgue measure, is
\[
 f_n(u,v)=2(n-1)(n-2)\bigl(1-2\max(u,v)\bigr)^{n-3},\quad 0<u,v<1/2,
\]
and vanishes outside this square. In particular, if \(M=\max(U,V)\) and \(R=\min(U,V)/M\), then the two quantities are independent and
\[
 2M\sim\operatorname{Beta}(2,n-2),\qquad R\sim\operatorname{Uniform}(0,1).
\]
Consequently \(n(U,V)\) converges in distribution to the density \(2e^{-2\max(x,y)}\) on the positive quadrant; \(nM\) converges to \(\operatorname{Gamma}(2,\text{rate }2)\). A finite-sample consequence is
\[
 \operatorname{Corr}(U,V)=\frac{3(n-3)}{7n-9}\longrightarrow\frac37.
\]
The scalar probability of the conditioning event is \(\Pr(A_n=2)=n2^{2-n}\), a classical geometric counting fact rather than the novelty claim.

## Assumptions and scope

The points are independent, identically distributed by normalized arclength on one circle, almost surely distinct, and the polygon connects them in circular order. All angles are the ordinary interior angles of the resulting convex polygon. No distributional assumption on the circle's radius is needed. Strictly acute means less than \(\pi/2\); right-angle ties have probability zero. The result holds for every integer \(n\ge4\), conditional on an event of positive probability. The first and second deficit coordinates may be swapped; the joint law is symmetric.

## Proof

Write the normalized circular gaps between successive sampled vertices as \(G_1,\ldots,G_n\), whose sum is one. Upon choosing a cyclically uniform starting vertex, the gap vector is \(\operatorname{Dirichlet}(1,\ldots,1)\). The inscribed-angle theorem identifies the angle at vertex \(i\) as \(\pi(1-G_{i-1}-G_i)\). Thus its right-angle deficit is \(G_{i-1}+G_i-1/2\), and positivity characterizes an acute angle.

Two nonadjacent acute vertices would require two disjoint two-gap sums greater than one half, which is impossible because the gaps sum to one. Any three distinct vertices include a nonadjacent pair when \(n\ge4\), so at most two acute vertices occur. Therefore precisely two acute vertices, whenever present, are adjacent and define a unique neighboring vertex pair, without overcounting.

For one fixed neighboring pair, set the three successive gaps surrounding its two vertices to \(X,Y,Z\). Their joint density is
\[
 (n-1)(n-2)(n-3)(1-X-Y-Z)^{n-4}
\]
for \(X,Y,Z>0\) with \(X+Y+Z<1\). The two deficits are \(u=X+Y-1/2\) and \(v=Y+Z-1/2\). Set \(s=Y-1/2\), so \(X=u-s\), \(Z=v-s\), and the leftover total gap is \(1/2-u-v+s\). The Jacobian has absolute value one. For \(0<u,v<1/2\), the allowable range is
\[
 u+v-1/2<s<\min(u,v).
\]
Integration in \(s\) produces the unnormalized marked-pair joint density
\[
 q_n(u,v)=(n-1)(n-2)(1/2-\max(u,v))^{n-3}.
\]
Its integral over \((0,1/2)^2\) is \(2^{2-n}\), so the probability of any two acute vertices is \(n2^{2-n}\), since there are \(n\) cyclic neighboring pairs and at most one succeeds. Dividing the marked-pair density by this pair probability yields the stated \(f_n\).

For \(m=\max(u,v)\) and \(r=\min(u,v)/m\), the two triangular portions of the square together give Jacobian \(2m\). Their joint density becomes
\[
 f_{M,R}(m,r)=4(n-1)(n-2)m(1-2m)^{n-3},
 \quad 0<m<1/2,\quad 0<r<1.
\]
Setting \(t=2m\) turns the first factor into \((n-1)(n-2)t(1-t)^{n-3}\), the \(\operatorname{Beta}(2,n-2)\) density; the second factor is uniform in \(r\). This proves exact independence. Its standard beta-to-gamma scaling, or the displayed density after replacing \((u,v)\) by \((x/n,y/n)\), proves the joint limiting density and gamma maximum.

For completeness, integrating the density gives \(\mathbb E U=3/(4n)\), \(\mathbb E U^2=1/[n(n+1)]\), and \(\mathbb E UV=3/[4n(n+1)]\). Consequently \(\operatorname{Cov}(U,V)=3(n-3)/[16n^2(n+1)]\) and \(\operatorname{Var}(U)=(7n-9)/[16n^2(n+1)]\), giving the displayed positive correlation. All boundary and tie events have probability zero.

## Verification

The standalone standard-library program `CHECK.py` independently expands and integrates the piecewise-polynomial density using exact rational arithmetic, compares two independent moment formulas for \(4\le n\le24\) and powers through four, verifies the beta/uniform moment factorization and explicit correlation, and samples the underlying circular gap process for three small sample sizes. It reports 1,251 successful assertions. This finite check is auxiliary: the preceding integrations and transformations establish the theorem for all \(n\) and its infinite-sample limit.

## Relationship to prior work

The December 3, 2005 Putnam competition problem A6 and R. Lockhart's solution establish the geometry that acute angles in a uniformly sampled cyclic polygon occur only singly or as an adjacent pair and compute the probability of at least one. The same solution explicitly integrates the *scalar* event that a prescribed pair is simultaneously acute, without giving the two-angle joint conditional density. S. R. Finch's *Random Cyclic Quadrilaterals* (first arXiv version October 3, 2016), Section 2, derives a bivariate tent density for adjacent angles of a four-vertex cyclic polygon, which implies the \(n=4\) special case here; Section 4 analyzes angles in the five-vertex case. These finite-order cases are credited. The contribution assessed here is the general all-sample-size rare-event conditional angle-pair density, its exact beta–uniform factorization, and joint large-polygon law, rather than the prior scalar event probability or the four-vertex special case.

## Limitations

The claim concerns only points sampled independently and uniformly on one circle, conditioned on exactly two acute angles. It does not cover nonuniform angular sampling, random points in a disk, or polygons with general correlated vertices. It does not assert a quantitative rate in the limiting distribution. The historic literature search did not uncover an all-\(n\) expression for this particular conditional marked pair, but the event geometry and Dirichlet transformation are elementary; an older equivalent formulation could still exist.

## References

1. William Lowell Putnam Mathematical Competition, Problem A6 (December 3, 2005); Richard Lockhart, *Solutions to the 66th William Lowell Putnam Mathematical Competition*, pp. 3–4, https://www.sfu.ca/~lockhart/richard/Putnam2005Sol.pdf.
2. Steven R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510, first posted October 3, 2016, Sections 2 and 4, https://arxiv.org/abs/1610.00510.
