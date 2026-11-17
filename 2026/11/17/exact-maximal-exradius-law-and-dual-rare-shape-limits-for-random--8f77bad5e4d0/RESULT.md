# Exact maximal-exradius law and dual rare-shape limits for random cyclic triangles

## Finding

Take three independent points uniform by arclength on a Euclidean circle of radius one. Let \(r_1,r_2,r_3\) be the three **exradii** (radii of the circles tangent externally to one side of the inscribed triangle and the extensions of its other two sides), and put \(L=\max_i r_i\). The following gives the complete distribution of \(L\), and two qualitatively different, sharp rare-event laws at its endpoints.

For \(3/2<t<4\), let
\[
 m(u)=\min\{u,2\pi-3u\},\quad c(u)=\cos(u/2),\quad
 z_t(u)=\frac{t}{2c(u)}-c(u),\qquad 0\le u\le 2\pi/3,
\]
and define the nonnegative section length
\[
 b_t(u)=
 \begin{cases}
 0,&z_t(u)\le\cos(m(u)/2),\\
 m(u)-2\arccos(z_t(u)),&\cos(m(u)/2)<z_t(u)<1,\\
 m(u),&z_t(u)\ge1.
 \end{cases}
\]
Then the exact cumulative distribution function is
\[
 \boxed{\Pr(L\le t)=\frac6{\pi^2}\int_0^{2\pi/3}b_t(u)\,du,\quad 3/2<t<4.}
\]
It is zero for \(t\le3/2\) and one for \(t\ge4\), and it is strictly increasing in between. There are no atoms. The **sharp endpoint probabilities** are
\[
 \boxed{\Pr(L<3/2+\varepsilon)\sim\frac3{\pi^2}\varepsilon^2,\qquad
 \Pr(L>4-\varepsilon)\sim\frac2{\pi\sqrt3}\varepsilon
 \quad(\varepsilon\downarrow0).}
\]

The rare shapes can also be identified **jointly in total variation**:

* **Near the minimum.** Write the three interior angles as \(A_i=\pi/3+\delta_i\), so \(\sum\delta_i=0\). Conditional on \(L<3/2+\varepsilon\), the vector
\[
 \left(\frac13-\frac{\delta_i}{\sqrt3\,\varepsilon}\right)_{i=1}^3
\]
converges in total variation to \(\operatorname{Dirichlet}(1,1,1)\) on the simplex \(d_i\ge0,\sum d_i=1\). The displayed prelimit vector sums to one (and is supported in a vanishing neighborhood of the simplex, rather than exactly on it). The normalized excess \((L-3/2)/\varepsilon\) converges to \(\operatorname{Beta}(2,1)\).

* **Near the supremum.** Let \(I\) be the index of the largest angle, and write the other angles in cyclic order as \(B,C\). Conditional on \(L>4-\varepsilon\), define
\[
 X_\varepsilon=\frac{B+C/2}{\sqrt\varepsilon},\qquad
 Y_\varepsilon=\frac{\sqrt3\,C}{2\sqrt\varepsilon}.
\]
Then \((I,X_\varepsilon,Y_\varepsilon)\) converges in total variation to a uniform index in \(\{1,2,3\}\), independent of a uniformly distributed point in the unit circular sector \(\{(x,y):x^2+y^2<1,\ 0<\arg(x+iy)<\pi/3\}\). In polar coordinates, the limit sector angle is uniform on \((0,\pi/3)\), independent of the squared radius, which is uniform on \((0,1)\). Thus \((4-L)/\varepsilon\) conditioned on the same event converges to \(\operatorname{Uniform}(0,1)\).

## Assumptions and scope

The three sample points are independent, with **uniform normalized arclength** on the circumference, not area-uniform in the disk. The circumradius is exactly one; results for any radius \(R>0\) follow by multiplying every exradius and threshold by \(R\). A triangle formed by three distinct random circle points is nondegenerate almost surely. Labels of the three angles are tied to a fixed sampled point and the circular order; the index of the largest angle is unique almost surely. All inequalities in rare-event conditions can be made non-strict without changing their probabilities.

The limiting marked distributions concern the **specific rescaled random angles** in the two rare-event regimes, not excenter locations or area-uniform point models. Total variation for prelimit transformed vectors refers to ordinary two-dimensional measures on their respective affine planes; the prelimit near-minimum vector has coordinate sum exactly one, although its coordinates can be slightly negative before the limit.

## Proof

**1. Exact angle measure.** Designate the first sampled point as a circular anchor. Relative to it, sort the other two independent uniform angular coordinates. The three clockwise gaps, divided by \(2\pi\), have the \(\operatorname{Dirichlet}(1,1,1)\) distribution. By the inscribed-angle theorem, the three interior angles \(A_1,A_2,A_3\) are these gaps multiplied by \(\pi\), up to a fixed cyclic permutation. Their joint density in coordinates \((A_1,A_2)\), with \(A_3=\pi-A_1-A_2\), is therefore \(2/\pi^2\) on the open angle simplex. Taking the smallest absolute polar angle as anchor instead would incorrectly size-bias one gap; no such anchoring is used here.

**2. Exact geometry and order.** For circumradius one the standard exradius identities are
\[
 r_1=4\sin(A_1/2)\cos(A_2/2)\cos(A_3/2),
 \qquad r_2,r_3\text{ given cyclically.}
\]
They follow, for instance, from \(r_i=\Delta/(s-a_i)\), the sine law and half-angle identities, where \(\Delta\) is triangle area and \(s\) is semiperimeter. The ratio
\[
 \frac{r_i}{r_j}=\frac{\tan(A_i/2)}{\tan(A_j/2)}
\]
shows that the largest exradius is opposite the largest angle. Denote this angle by \(A=\pi-B-C\), leaving \(B,C\le A\). Set \(u=B+C\), \(v=B-C\). The admissible domain is
\[
 0<u<2\pi/3,\qquad |v|<m(u)=\min\{u,2\pi-3u\}.
\]
Using the product-to-sum identity,
\[
 L=4\cos(u/2)\cos((u+v)/4)\cos((u-v)/4)
 =2\cos(u/2)[\cos(u/2)+\cos(v/2)].
\]
There are three equally weighted choices for the largest-angle index. The Jacobian from \((B,C)\) to \((u,v)\) is \(1/2\); thus the density on the displayed domain is \(3/\pi^2\,du\,dv\). Its mass is one since \(\int_0^{2\pi/3}m(u)\,du=\pi^2/6\).

**3. Exact CDF and support.** For a fixed \(u\), the right-hand side for \(L\) is even in \(v\) and strictly decreases with \(|v|\) on \((0,m(u))\). The inequality \(L\le t\) is equivalent to \(\cos(v/2)\le z_t(u)\). According as \(z_t(u)\) is below \(\cos(m(u)/2)\), between that and one, or at least one, the admissible \(|v|\)-length equals \(0\), \(2[m(u)-2\arccos z_t(u)]\), or \(2m(u)\). Integrating against density \(3/\pi^2\) proves the formula. The maximum \(L<4\) follows immediately from the three half-angle factors. For the minimum, at fixed \(u\) the smallest allowed \(L\) is
\[
 L_{\min}(u)=
 \begin{cases}
 4\cos^2(u/2),&0\le u\le\pi/2,\\
 2\sin^2u,&\pi/2\le u\le2\pi/3.
 \end{cases}
\]
Its minimum is \(3/2\), achieved only at \(u=2\pi/3,v=0\), i.e. at the equilateral angle triple. Values arbitrarily near four occur when one angle tends to \(\pi\). Connectedness and continuity of the angular simplex, together with the nonconstant smooth expression away from a lower-dimensional set, show the CDF is continuous and strictly increasing on \((3/2,4)\); there can be no atom because its positive-level sets are one-dimensional analytic curves except possibly isolated critical points, and the function is not constant on any open set.

**4. Lower-end exponent and Dirichlet mark.** Write \(A_i=\pi/3+\delta_i\) with \(\sum\delta_i=0\). Uniform Taylor expansion near the unique minimizer gives
\[
 r_i=\frac32+\sqrt3\,\delta_i+O\left(\sum_j\delta_j^2\right),\qquad
 L-\frac32=\sqrt3\max_i\delta_i+O\left(\sum_j\delta_j^2\right).
\]
The bound \(\max_i\delta_i\ge\frac12\max_i|\delta_i|\), valid when three real numbers sum to zero, ensures that the sublevel event \(L-3/2<\varepsilon\) lies in a ball of radius \(O(\varepsilon)\), rather than merely a \(\sqrt\varepsilon\)-neighborhood. Indeed the remainder is quadratic and the unique global minimum gives localization, so the linear bound absorbs it in a sufficiently small neighborhood. Rescale \(\delta_i=\varepsilon h_i\) and take \((h_1,h_2)\) coordinates. The defining event converges to \(\sum h_i=0\), \(h_i<1/\sqrt3\), whose closure is a triangle with vertices \((1/\sqrt3,1/\sqrt3,-2/\sqrt3)\) and permutations. Its coordinate area is \(9(1/\sqrt3)^2/2=3/2\). Multiplying by the original density \(2/\pi^2\) and the Jacobian \(\varepsilon^2\) proves the coefficient \(3/\pi^2\). The domain indicators converge almost everywhere on a fixed compact set with uniform densities; normalized densities therefore converge in \(L^1\), proving total variation for the affine transformed vector. The map \(d_i=1/3-h_i/\sqrt3\) sends this triangle to the unit simplex with uniform density, i.e. \(\operatorname{Dirichlet}(1,1,1)\). For this distribution \(\Pr(\min d_i\ge a)=(1-3a)^2\) for \(0\le a\le1/3\), so the normalized excess converges to \(1-3\min d_i\sim\operatorname{Beta}(2,1)\).

**5. Upper-end exponent and sector mark.** The only ways to approach \(L=4\) are the three vertices of the angle simplex, where one angle tends to \(\pi\) and the others to zero. Near the vertex \(A=\pi\) put \(B=y,C=z\) so \(A=\pi-y-z\). Uniformly as \(y,z\to0\),
\[
 L=4\cos((y+z)/2)\cos(y/2)\cos(z/2)
 =4-(y^2+yz+z^2)+O((y+z)^4).
\]
The quadratic form \(Q(y,z)=y^2+yz+z^2\) is positive definite. Let \(Y=y/\sqrt\varepsilon\), \(Z=z/\sqrt\varepsilon\). The event \(L>4-\varepsilon\) converges, in each simplex corner, to \(Y,Z>0\) with \(Y^2+YZ+Z^2<1\); the relevant sublevel sets remain in a fixed compact region after rescaling by positive definiteness, uniqueness of the three maxima, and the quartic remainder. The linear map \((Y,Z)\mapsto(X,Y')=(Y+Z/2,\sqrt3 Z/2)\) has constant Jacobian and maps the quadratic form to \(X^2+Y'^2\). The first quadrant becomes the circular sector of angle \(\pi/3\). Its original \((Y,Z)\)-area is \(\pi/(3\sqrt3)\). Three corner contributions, angular density \(2/\pi^2\), and Jacobian \(\varepsilon\) give \(3(2/\pi^2)(\pi/(3\sqrt3))\varepsilon=2\varepsilon/(\pi\sqrt3)\). Normalized indicator densities again converge in \(L^1\) on a compact set. Exchangeability gives a uniform corner index, independent of the limiting uniform-sector point. Polar coordinates in a uniform sector have independent uniform angle and squared radius. The last assertion follows since \((4-L)/\varepsilon\to X^2+Y'^2\) under this conditioning.

## Verification

Run `python exradius_check.py` after installing the packages in `requirements.txt`. The checker independently computes all three exradii from Cartesian chord lengths, a determinant area and the semiperimeter, compares this calculation with the half-angle formula, integrates the one-dimensional CDF numerically, and tests six interior CDF values against independent random polar-point samples. It also compares endpoint ratios and performs finite-sample diagnostics of the upper-end uniform-sector marks. The tested implementation printed `MAXIMAL_EXRADIUS_EXACT_CDF_AND_MARKED_TAILS_OK`. These finite tests are corroboration only; the distributional and total-variation conclusions follow from the exact simplex density and local sublevel-domain arguments above.

For scale, the exact integral yields \(\Pr(L\le2)\approx0.095449528\), \(\Pr(L\le3)\approx0.597104809\), and \(\Pr(L\le3.8)\approx0.925231522\). The leading endpoint coefficients are \(3/\pi^2\approx0.303963551\) and \(2/(\pi\sqrt3)\approx0.367552597\).

## Relationship to prior work

Wu, Yue and Chu [1] study sharp deterministic inequalities involving exradii, the circumradius and the inradius, and explicitly provide the half-angle exradius formulas. The deterministic sharp bound \(\max_i r_i\ge3R/2\) is a classical problem attributed to Erdős [2], **not** claimed here. Edelman and Strang [3] distinguish the uniform-angle triangle law from Gaussian vertex sampling, which is a different random model; their uniform-angle discussion is background to the present simplex measure.

The published *Full inradius law and two contrasting tails of random cyclic triangles* [4] concerns the **incircle** radius rather than the largest **excircle** radius. Its exact CDF and its logarithmic/linear tails do not imply the formulas here; even knowledge of the sum of exradii via the classical identity \(r_1+r_2+r_3-r=4R\) does not determine their maximum. The published *Excentral transport and universal shape ordering for acute random cyclic triangles* [5] concerns an affine transformation of triangle-angle **shapes**, not the largest original exradius under the full law. Both published proofs were inspected and compared with the present event inequalities and endpoint domains. Published random-triangle size distributions for independent side-direction sampling [6] use a different measure and normalization.

The contribution claimed here is the **exact full CDF of the largest exradius** together with sharp, different endpoint exponents and two complete conditional marked-shape limits. The classical exradius formula, angular simplex law and deterministic support bound are cited inputs, not discoveries. Historical searches are necessarily bounded; equivalent results may exist in uncatalogued literature.

## Limitations

The theorem uses three independent circumference-uniform points and fixed circumradius, and asserts no analogous formula for points chosen uniformly in a disk, fixed-perimeter random triangles, or other angular densities. Numerical endpoint ratios are finite-resolution diagnostics rather than proof. The conditional marks are expressed in terms of angles and their prescribed ordering, not spatial excenter locations. The formula for the entire CDF is an exact one-dimensional quadrature, not an asserted elementary primitive. The given sources support a best-knowledge historical comparison, not a claim that all historical triangle-geometry literature was exhaustively searched. No independent mathematical audit has been performed.

## References

[1] S.-H. Wu, H.-P. Yue and Y.-M. Chu, *Sharp bounds for cyclic sums of the ratio of the exradius to the sides of a triangle*, Journal of Inequalities and Applications 2015, article 386, published 8 December 2015. DOI:10.1186/s13660-015-0921-z. https://link.springer.com/article/10.1186/s13660-015-0921-z

[2] *A Paul Erdős problem: If a triangle has circumradius \(R\) and largest exradius \(r_a\), then \(2r_a\ge3R\)*, public mathematical discussion, 11 May 2018. https://math.stackexchange.com/questions/2776274

[3] A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, first posted 9 January 2015. https://arxiv.org/abs/1501.03053

[4] *The full inradius law and two contrasting tails of random cyclic triangles*, publicly available research finding (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-the-full-inradius-law-and-two-contrasting-tails-of-random-cyclic--f4fa44ae752a/RESULT.md

[5] *Excentral transport and universal shape ordering for acute random cyclic triangles*, publicly available research finding (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-excentral-transport-and-universal-shape-ordering-for-acute-rando--d66cc98a9db3/RESULT.md

[6] D. J. Daley, S. Ebert and R. J. Swift, *Size distributions in random triangles*, Journal of Applied Probability 51A (2014), 283–295, DOI:10.1239/jap/1417528481. https://doi.org/10.1239/jap/1417528481
