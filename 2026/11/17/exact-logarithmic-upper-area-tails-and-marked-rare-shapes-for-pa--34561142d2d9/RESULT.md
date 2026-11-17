# Exact logarithmic upper-area tails and marked rare shapes for parallelogram-boundary triangles

## Finding

Let \(P\) be any nondegenerate Euclidean parallelogram of area \(S>0\), adjacent side lengths \(a,b>0\), and interior angle strictly between zero and \(\pi\). Choose three points independently from normalized **Euclidean boundary arclength**, and write \(A\) for their triangle's ordinary Euclidean area. Put
\[
u=\frac{a}{2(a+b)},\qquad v=\frac{b}{2(a+b)},\qquad u+v=\frac12.
\]
For every \(0<\varepsilon<1/2\), define
\[
H(\varepsilon)=\varepsilon^2\log(1/\varepsilon)
 +(3-4\varepsilon+\varepsilon^2)\log(1-\varepsilon)
 +3\varepsilon-\tfrac52\varepsilon^2.
\]
**The entire near-maximum area tail is exactly**
\[
\boxed{\Pr\bigl(A>\tfrac S2(1-\varepsilon)\bigr)
   =\tfrac34\varepsilon^2+6uv\,H(\varepsilon).}\tag{1}
\]
The positive expansion
\[
H(\varepsilon)=\varepsilon^2\log(1/\varepsilon)
 +\sum_{k=4}^{\infty}\frac{2(k-3)}{k(k-1)(k-2)}\varepsilon^k
\tag{2}
\]
shows that **all rhombi, and only rhombi, maximize (1) among parallelograms** for every fixed threshold in the stated interval. Its unattained infimum, as the side-length ratio degenerates, is \(3\varepsilon^2/4\). The complete area law, normalized by \(S\), is independent of the parallelogram's angle at every fixed pair \(a,b\). In particular, the singular expansion is
\[
\boxed{\Pr\bigl(A>\tfrac S2(1-\varepsilon)\bigr)
 =6uv\varepsilon^2\log(1/\varepsilon)
 +\tfrac34\varepsilon^2+\tfrac12uv\varepsilon^4+O_{a,b}(\varepsilon^5).}\tag{3}
\]
There is **no cubic term**, and the first nonlogarithmic quadratic coefficient is shape-independent.

There is also a marked conditional theorem. Condition on the event in (1) as \(\varepsilon\downarrow0\). With probability tending to one, the three points lie on three different sides. Let \(M\) be the missing side. Each of the two sides of length \(a\) is missing with limiting probability \(v\); each of the two sides of length \(b\) is missing with limiting probability \(u\). Given the side set, the three sampled-point label assignments are asymptotically equiprobable. Apply a fixed square symmetry in affine unit-square coordinates so the occupied sides are bottom, right, and top, in that order, with vertices \((x,0),(1,y),(z,1)\). Define
\[
X_\varepsilon=\frac{x(1-y)}{\varepsilon},\qquad
Z_\varepsilon=\frac{yz}{\varepsilon},\qquad
R_\varepsilon=\frac{\log(1/\min\{y,1-y\})}{\log(1/\varepsilon)},
\]
and let \(B_\varepsilon\) record whether \(y<1/2\) or \(y>1/2\). Assign arbitrary sentinel marks on the negligible exceptional configurations. Then the marked conditional law converges **in total variation** to independent variables: the described missing-side and label marks; a fair two-valued branch mark; a \(\operatorname{Uniform}[0,1]\) logarithmic mark; and
\[
\boxed{(X,Z,1-X-Z)\sim\operatorname{Dirichlet}(1,1,1).}\tag{4}
\]
Consequently, the normalized area deficit \((S/2-A)/[(S/2)\varepsilon]\), conditional on (1), tends in total variation to \(\operatorname{Beta}(2,1)\). The marked theorem concerns a fixed nondegenerate parallelogram; no joint thin-shape/rare-threshold uniformity is asserted.

## Assumptions and scope

All three points are independent and identically distributed under arclength divided by perimeter \(2(a+b)\); boundary corners have probability zero. The area is unsigned, and a triangle is allowed to be degenerate, although degeneracy does not affect the stated upper-tail event. The maximum possible triangle area in any parallelogram is \(S/2\). The exact identity (1) holds for every fixed \(a,b>0\), every parallelogram angle strictly between zero and \(\pi\), and every \(\varepsilon\) strictly between zero and one half. The asymptotic and marked statements take \(\varepsilon\downarrow0\) with \(a,b\) fixed.

An affine map from the unit square to the parallelogram preserves area ratios and uniform positions **conditional on the selected side**. It does not preserve the relative masses of the four sides; those masses are exactly \(u,v,u,v\). This distinction is essential to the shape-ordering conclusion.

## Proof

**1. Affine parametrization and exhaustive side patterns.** Represent the parallelogram as \(p+s e_1+t e_2\), for \(s,t\in[0,1]\), with \(\lVert e_1\rVert=a\), \(\lVert e_2\rVert=b\), and \(S=|\det(e_1,e_2)|\). Uniform physical arclength on a side corresponds to a uniform value of its unit-square coordinate. Each horizontal side has selection probability \(u\), each vertical side probability \(v\). The maximum possible normalized doubled triangle area is one, since the oriented determinant is separately affine in each of the three point positions and its absolute maximum is reached at a triple of square corners, where it equals one.

There are four exhaustive side-occupancy patterns: all three on different sides, two on one side and the third on the opposite side, two on one side and the third on an adjacent side, and all three on one side. Their probabilities are respectively
\[
6uv,\qquad6(u^3+v^3),\qquad6uv,\qquad2(u^3+v^3),
\]
which sum to one by \(u+v=1/2\). The last pattern has zero triangle area.

**2. Exact conditional tail for each pattern.** For three distinct sides, a unit-square symmetry gives the ordered positions \((x,0),(1,y),(z,1)\) with \(x,y,z\) independent uniform on \([0,1]\). The doubled triangle area is
\[
1-W,\qquad W=x(1-y)+yz.
\]
For \(0<\varepsilon<1/2\), at a fixed \(y\), the planar measure of \(\{(x,z):W<\varepsilon\}\) is
\[
q_\varepsilon(y)=\begin{cases}
\dfrac{\varepsilon-y/2}{1-y},&0<y<\varepsilon,\\[3pt]
\dfrac{\varepsilon^2}{2y(1-y)},&\varepsilon\le y\le1-\varepsilon,\\[3pt]
\dfrac{\varepsilon-(1-y)/2}{y},&1-\varepsilon<y<1.
\end{cases}
\]
The first branch follows by integrating \(0<x<(\varepsilon-yz)/(1-y)\) for \(0<z<1\); the middle branch is an untruncated right triangle after rescaling; the last follows by symmetry. Hence the exact conditional tail is
\[
F(\varepsilon)=\int_0^1q_\varepsilon(y)dy
=(1-2\varepsilon)\log(1-\varepsilon)+\varepsilon
 +\varepsilon^2\log\frac{1-\varepsilon}{\varepsilon}.
\tag{5}
\]

With two sampled points on one side and the third on the opposite side, the doubled normalized area is \(|U-V|\), for independent uniform \(U,V\). Since its distribution has upper tail \(\varepsilon^2\), this occupancy pattern contributes \(\varepsilon^2\) conditionally. With two points on one side and the third on an adjacent side, doubled normalized area is \(|U-V|H\), where \(U,V,H\) are independent uniform \([0,1]\). As \(|U-V|\) has density \(2(1-d)\), the conditional tail is
\[
J(\varepsilon)=\int_{1-\varepsilon}^1
 2(1-d)\left(1-\frac{1-\varepsilon}{d}\right)dd
 =-\varepsilon^2+2\varepsilon+2(1-\varepsilon)\log(1-\varepsilon).
\tag{6}
\]
Multiplying (5), the opposite-side tail, and (6) by their exhaustive occupancy probabilities proves
\[
\Pr\bigl(A>\tfrac S2(1-\varepsilon)\bigr)
 =6uv[F(\varepsilon)+J(\varepsilon)]
  +6(u^3+v^3)\varepsilon^2.
\tag{7}
\]
The identity \(u^3+v^3=1/8-3uv/2\) and elementary rearrangement give (1).

**3. Positive series and shape ordering.** Use \(\log(1-\varepsilon)=-\sum_{k\ge1}\varepsilon^k/k\) to expand (1). The linear, quadratic, and cubic contributions to the bracket other than \(\varepsilon^2\log(1/\varepsilon)\) cancel. For every integer \(k\ge4\), its coefficient equals
\[
-\frac3k+\frac4{k-1}-\frac1{k-2}
 =\frac{2(k-3)}{k(k-1)(k-2)}>0.
\]
This proves (2) and (3). Because \(uv=ab/[4(a+b)^2]\) is uniquely maximal at \(a=b\) and has unattained infimum zero as a side-length ratio degenerates, strict positivity of \(H\) gives the exact shape ordering and all equality claims for fixed \(\varepsilon\). The affine argument in Step 1 shows why the angle has no effect on the normalized law.

**4. Exceptional occupancy vanishes conditionally.** By (5), \(F(\varepsilon)\sim\varepsilon^2\log(1/\varepsilon)\). Equations (6) and (7) show that opposite-side patterns contribute only \(O(\varepsilon^2)\) and adjacent-side patterns only \(O(\varepsilon^3)\). Within the distinct-side pattern, the intervals \(y<\varepsilon\) and \(y>1-\varepsilon\) also have total event measure \(O(\varepsilon^2)\). Consequently, conditioned on the event, the probability of being in a canonical distinct-side chart with \(\varepsilon\le y\le1-\varepsilon\) tends to one. For a fixed missing side, the side-selection probability is proportional to the product of the three other side masses, giving \(v\) for each horizontal missing side and \(u\) for each vertical missing side. Labels are exchangeable, so their six assignments are conditionally equiprobable.

**5. Exact central-region factorization and total-variation limit.** On \(\varepsilon\le y\le1-\varepsilon\) and \(W<\varepsilon\), make the change of variables
\[
X=\frac{x(1-y)}{\varepsilon},\qquad Z=\frac{yz}{\varepsilon}.
\]
The image is exactly the open simplex \(X,Z>0\), \(X+Z<1\), and the conditional Jacobian for \((x,z)\) is \(\varepsilon^2/[y(1-y)]\). Thus \((X,Z,1-X-Z)\) is **exactly** \(\operatorname{Dirichlet}(1,1,1)\), independent of \(y\) and the discrete side labels, when conditioned on this central event. The central \(y\)-density is proportional to \(1/[y(1-y)]\). By reflection about \(1/2\), the branch is fair and independent of the simplex. On either branch, letting \(L=\log(1/\varepsilon)\), the density of \(R=\log(1/\min\{y,1-y\})/L\) is exactly
\[
\frac{L}{\log((1-\varepsilon)/\varepsilon)}\,
\frac{1}{1-\varepsilon^{R}}
\mathbf1_{\{\log2/L\le R\le1\}},
\]
which converges to the unit-uniform density in \(L^1\) on \([0,1]\). The total conditional mass excluded in Step 4 tends to zero; extending the central factorization by arbitrary sentinel values therefore yields convergence of the **full marked law in total variation**. Since \(X+Z\sim\operatorname{Beta}(2,1)\), the normalized area-deficit assertion follows as well. This completes the proof.

## Verification

The standalone `check_parallelogram_boundary_tail.py` independently evaluates (7) by piecewise one-dimensional quadrature rather than reusing the antiderivative, and directly generates random Cartesian boundary triples for three aspect ratios and three shears, testing the area event geometrically. It also checks the first asymptotic terms at a much smaller threshold. Run `python3 check_parallelogram_boundary_tail.py`; dependencies and numerical tolerances are in `requirements.txt` and the script. A completed execution printed `PARALLELOGRAM_BOUNDARY_LOG_TAIL_AND_DIRICHLET_MARK_OK`. Finite simulation is corroboration, not a proof of the analytic limit; the integration and density arguments above provide that proof.

## Relationship to prior work

Koroleva and Nikitin [1] investigate maximal-area random polygons **on the unit circle**, including the small deficit of inscribed triangles and large-sample extreme-value laws; their circular shape and smooth maximizer do not give the side-occupancy mixture or logarithmic singularity of a parallelogram boundary. The classical random-triangle literature surveyed by Henze [2] and MathWorld [3] concerns **area-uniform interior points**, not the singular boundary-arclength measure; Henze computes an area law for a parallelogram under interior sampling. The exact six-coordinate conditional law in a previously published square result [4] also uses **area-uniform interior** points, for which the upper-tail exponent is five rather than two. Its logarithmic-split geometry is related but its statement does not imply (1)–(4).

The published boundary-parallelogram work [5] supplies exact **expected convex-hull area** and rhombus extremality for fixed sample count, but it does not imply an upper-tail distribution, its strict ordering at every near-maximal threshold, the universal nonlogarithmic correction, or the marked conditional law. The published rectangle-boundary acute-triangle formula [6] uses the same sampling measure but an angle indicator, not triangle area. Reitzner, Schütt, and Werner [7] study large-sample boundary-polytopes via expected face counts and volume deficits as the sample size tends to infinity, not a fixed-three-point rare upper area event. Searches for exact square-perimeter area distributions, near-maximal boundary triangles, the relevant shape ordering, and their marked logarithmic laws returned no dominating statement. This is a provisional best-knowledge originality assessment, not a claim of exhaustive historical priority.

## Limitations

Identity (1) is asserted only for the upper-area range \(0<\varepsilon<1/2\); it does not describe the complete distribution for smaller-area thresholds. The shape ordering holds among nondegenerate parallelograms and is not an ordering for all convex quadrilaterals. The conditional theorem fixes positive side lengths before sending the threshold to zero and makes no claim for a simultaneous long-thin limit. Its total-variation convergence has no explicit quantitative rate. Historical priority is provisional because not every older geometric-probability treatment is accessible or fully indexed. Independent mathematical validation has not been performed.

## References

[1] E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, initially posted 2013-01-07. https://arxiv.org/abs/1301.1360

[2] N. Henze, *Random Triangles in Convex Regions*, Journal of Applied Probability 20 (1983), 111–125, DOI:10.2307/3213725. Accessible abstract specifies sampling uniformly **inside** a convex region.

[3] E. W. Weisstein, *Square Triangle Picking*, MathWorld, https://mathworld.wolfram.com/SquareTrianglePicking.html. The exact area law described there is for points inside the square; it cites Henze (1983), Trott (1998), and earlier work.

[4] *A Dirichlet–uniform shape law for nearly maximal random triangles in a square*, public scientific result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-dirichlet-uniform-shape-law-for-nearly-maximal-random-triangle--d6973284aaff.

[5] *Finite-sample boundary-hull area of parallelograms: rhombus extremality and a thin-shape crossover*, public scientific result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-finite-sample-boundary-hull-area-of-parallelograms-rhombus-extre--9f7cfa62890c.

[6] *Acute-triangle law and a seven-halves transition for random rectangle-boundary triples*, public scientific result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-acute-triangle-law-and-a-seven-halves-transition-for-random-rect--be00a8406645.

[7] M. Reitzner, C. Schütt, and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, first posted 2019-11-14. https://arxiv.org/abs/1911.05917
