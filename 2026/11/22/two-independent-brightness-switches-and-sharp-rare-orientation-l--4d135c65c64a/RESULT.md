# Two independent brightness switches and sharp rare-orientation laws for right square pyramids

## Finding
For the solid right square pyramid \(P_h=\operatorname{conv}(\{(\pm1,\pm1,0)\}\cup\{(0,0,h)\})\) with \(h>0\), let \(B_h(U)\) be the planar orthogonal-projection area along \(U\) Haar-uniform on \(S^2\). The exact least and greatest projected areas are
\[
m(h)=\min\left\{h,\frac{4h}{\sqrt{h^2+2}}\right\},\qquad M(h)=\max\{4,\sqrt{2h^2+4}\}.
\]
The global least-bright direction family switches at \(h=\sqrt{14}\), independently of the greatest-bright family switching at \(h=\sqrt6\). For each fixed \(h>0\), the endpoint laws as \(\varepsilon\downarrow0\) are
\[
\Pr(B_h\le m(h)+\varepsilon)=C_-(h)\varepsilon^2+o(\varepsilon^2),\qquad
\Pr(B_h\ge M(h)-\varepsilon)=C_+(h)\varepsilon
\]
(the latter equality is exact on some nonempty terminal interval), where
\[
C_-(h)=\begin{cases}
\dfrac8{9\pi h},&h<\sqrt{14},\\
\dfrac8{\pi\sqrt{14}},&h=\sqrt{14},\\
\dfrac{(h^2+2)^{7/2}}{16\pi h(h^2-2)^2},&h>\sqrt{14},
\end{cases}\quad
C_+(h)=\begin{cases}
\dfrac14,&h<\sqrt6,\\
\dfrac54,&h=\sqrt6,\\
\dfrac4{\sqrt{2h^2+4}},&h>\sqrt6.
\end{cases}
\]
At the least-bright transition, the conditional mass associated with the four horizontal minimizers tends to \(1/9\) and with the eight oblique minimizers to \(8/9\). In particular the two threshold phenomena are mathematically distinct rather than one critical aspect ratio.

## Assumptions and scope
Lengths are Euclidean, the square base is \([-1,1]^2\), and height \(h>0\) is measured perpendicular to its plane. Orthographic projection is onto the plane perpendicular to the unit viewing vector. Directions \(U\) and \(-U\) are counted separately as uniform points of \(S^2\), which gives the same area law as unoriented views. Probability is normalized by sphere area \(4\pi\). The height is fixed for the displayed endpoint laws; a separate joint scaling is given below.

## Proof
**Exact facet projection formula.** The base facet has area vector \((0,0,-4)\). The outward area vectors of the four lateral triangular facets are \((\pm h,0,1)\) and \((0,\pm h,1)\). Cauchy's polyhedral projection formula (half the sum of absolute scalar products with facet area vectors) yields, for \(x=|U_1|,\ y=|U_2|,\ c=|U_3|\),
\[
B_h(U)=2c+\max(c,hx)+\max(c,hy)
=\max\{4c,3c+hx,3c+hy,2c+hx+hy\}.
\tag{1}
\]
**Global maximum.** Every term on the right of (1) is a linear functional on the positive unit octant. Their Euclidean coefficient norms are \(4,\sqrt{h^2+9},\sqrt{h^2+9},\sqrt{2h^2+4}\). The middle value never strictly dominates both others: when it exceeds \(4\), necessarily \(h^2>7\) and then \(\sqrt{2h^2+4}>\sqrt{h^2+9}\). Thus the maximum is \(M(h)\). For \(h<\sqrt6\) only \(\pm e_3\) maximize; for \(h>\sqrt6\) exactly the eight sign patterns of \((h,h,2)/\sqrt{2h^2+4}\) maximize; at equality all ten do. Each maximal linear branch is unique away from sign flips.

**Global minimum.** Work in the nonnegative octant. The homogeneous sublevel polytope \(Q_h=\{(x,y,c)\ge0:B_h(x,y,c)\le1\}\) is the intersection of \(4c\le1\), \(3c+hx\le1\), \(3c+hy\le1\), \(2c+hx+hy\le1\) and the three coordinate halfspaces. Its vertices, enumerated by independent active triples, are the origin,
\[
(1/h,0,0),\ (0,1/h,0),\ (0,0,1/4),\
(1/(4h),0,1/4),\ (0,1/(4h),1/4),\
(1/(4h),1/(4h),1/4).
\]
The greatest norm of a vertex is \(\max\{1/h,\sqrt{h^2+2}/(4h)\}\); all other listed vertices have strictly smaller norm. A strictly convex squared norm on a polytope achieves its maximum only at vertices (any nontrivial convex combination has strictly smaller squared norm than the corresponding weighted mean of endpoint squares). Homogeneity gives \(m(h)\) as the reciprocal of that maximum. Horizontal minima are the four directions \(\pm e_1,\pm e_2\). Oblique minima are the eight sign patterns of \((1,1,h)/\sqrt{h^2+2}\). Their equality occurs precisely at \(h^2=14\). This also proves exhaustive classification of all minimizers.

**Upper tail, exactly.** Near any isolated maximizing direction, (1) reduces to the single supporting linear functional \(v\cdot U\) of norm \(M\). Thus \(B_h(U)\ge M-\varepsilon\) near that point is a spherical cap with area exactly \(2\pi\varepsilon/M\) for \(0\le\varepsilon\) sufficiently small. Compactness and strict separation from all other directions ensure that, for sufficiently small \(\varepsilon>0\), these caps are disjoint and exhaust the event. There are respectively \(2,10,8\) maximum points in the three regimes, proving \(C_+(h)\) including exact equality.

**Lower tail at a horizontal minimizer.** Near \(e_1\) use local surface coordinates \((y,z)=(U_2,U_3)\), \(U_1=\sqrt{1-y^2-z^2}\), with Jacobian \(1+O(y^2+z^2)\). Equation (1) becomes
\[
B_h-h=2|z|+\max(|z|,h|y|)+O(y^2+z^2).
\]
The planar region \(2|z|+\max(|z|,h|y|)\le\varepsilon\) has exact area \(8\varepsilon^2/(9h)\), obtained by integrating the two triangular and trapezoidal slices. Thus four horizontal minima contribute \(\frac8{9\pi h}\varepsilon^2+o(\varepsilon^2)\).

**Lower tail at an oblique minimizer.** Set \(D=h^2+2\), \(p=hU_1-U_3\), \(q=hU_2-U_3\) in the positive octant around \(u_0=(1,1,h)/\sqrt D\). The sphere surface Jacobian in \((p,q)\) is \(1/(h\sqrt D)+O(|p|+|q|)\). Differentiating \(U_1^2+U_2^2+U_3^2=1\) yields \(\mathrm dU_3=-(\mathrm dp+\mathrm dq)/D\) at \(u_0\). The locally exact max structure of (1) gives
\[
B_h-m(h)=(1-\alpha)(p_++q_+)+\alpha((-p)_++(-q)_+)+O(p^2+q^2),\quad\alpha=4/D.
\]
For \(h\ge\sqrt{14}\) both coefficients are positive. The planar unit sublevel has area \(1/[2\alpha^2(1-\alpha)^2]\), by adding four quadrant triangles. Multiplying by the Jacobian and eight equivalent minima and dividing by \(4\pi\) gives \(C_-(h)=D^{7/2}/[16\pi h(h^2-2)^2]\). At \(h=\sqrt{14}\), this equals \(64/(9\pi\sqrt{14})\), and adding the horizontal contribution \(8/(9\pi\sqrt{14})\) proves the critical coefficient and the mass weights \(1/9,8/9\). All expansions are uniform on compact scaled local charts, and global extremum isolation excludes omitted regions.

**Joint near-critical crossover.** Define \(a_+=\max(a,0)\) and \(h_0=\sqrt{14},\ h_1=\sqrt6\). For every fixed real \(\lambda\) and nonnegative \(x\), the same local arguments and derivatives of competing extremal values give
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-2}
\Pr\{B_{h_0+\lambda\varepsilon}\le m(h_0+\lambda\varepsilon)+x\varepsilon\}
=\frac8{9\pi h_0}(x-7\lambda_+/8)_+^2
+\frac{64}{9\pi h_0}(x-7(-\lambda)_+/8)_+^2,
\]
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-1}
\Pr\{B_{h_1+\lambda\varepsilon}\ge M(h_1+\lambda\varepsilon)-x\varepsilon\}
=\frac14(x-h_1\lambda_+/2)_+
+(x-h_1(-\lambda)_+/2)_+.
\]
Here the derivative gap of the two competing minima at \(h_0\) is \(1-1/8=7/8\), while the derivative gap of the competing maxima at \(h_1\) is \(h_1/2\). This finishes the global and probabilistic statements.

## Verification
The included `CHECK.py` independently evaluates (1) against direct convex-hull projected areas and checks polytope vertices, exact endpoint coefficients and transition formulas. The checker uses only Python's standard library; random tests are deterministic. Numerical samples are diagnostics, not replacements for the analytic exhaustive proof and limiting arguments.

## Relationship to prior work
Cauchy's projection formula is classical and is used as the starting identity; its reuse is not presented as novel. Vickers and Brown (2001) give projected-area distributions for several classical particles, including a regular tetrahedron and a circular cone, but the square pyramid, its two distinct extremum switches, and the sharp endpoint constants are not supplied in the inspected material. Vickers (1996) develops ellipsoid and cylinder projections. Slepian (2011) reviews the average-projection-area identity, rather than directionwise extrema or rare-area laws. Published right-pyramid research on visibility of all vertices and central/affine section side counts concerns different statistics: those results neither determine nor imply the formulas here. All historical-priority conclusions are provisional.

## Limitations
The exact probability laws assume Haar-uniform orthographic directions and a right pyramid with a centered square base; translating, skewing or changing the base can change thresholds. Fixed-height endpoint laws are not asserted uniformly for arbitrarily diverging crossover parameters. The crossover statements are pointwise in their displayed fixed parameters. Publication priority beyond inspected texts has not been independently verified.

## References
- G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proceedings of the Royal Society A **457** (2001), 283–306, https://doi.org/10.1098/rspa.2000.0667.
- G. T. Vickers, *The projected areas of ellipsoids and cylinders*, Powder Technology **86** (1996), 195–200, https://doi.org/10.1016/0032-5910(95)03049-2.
- Z. Slepian, *The Average Projected Area Theorem – Generalization to Higher Dimensions*, original preprint 2011-09-03, https://arxiv.org/abs/1109.0595.
