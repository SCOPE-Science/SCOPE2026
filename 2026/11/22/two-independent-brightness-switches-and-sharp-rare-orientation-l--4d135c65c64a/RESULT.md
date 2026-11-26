# Least-bright directions and sharp lower orientation tails of right square pyramids

## Finding

Let \(P_h=\operatorname{conv}(\{(\pm1,\pm1,0)\}\cup\{(0,0,h)\})\), with \(h>0\), and let \(B_h(U)\) be its orthographic projected area onto the plane perpendicular to the unit vector \(U\). Its least projected area is
\[
m(h)=\min\left\{h,\frac{4h}{\sqrt{h^2+2}}\right\}.
\]
The minimizing directions are \(\pm e_1,\pm e_2\) below \(h_0=\sqrt{14}\) and the eight independent sign choices of \((1,1,h)/\sqrt{h^2+2}\) above it. At \(h=h_0\) both families minimize, with no other minimizers. For \(U\) uniform on \(S^2\) and fixed \(h\),
\[
\Pr(B_h(U)\le m(h)+\varepsilon)=C_-(h)\varepsilon^2+o(\varepsilon^2),\qquad
C_-(h)=\begin{cases}
8/(9\pi h),&h<h_0,\\
8/(\pi h_0),&h=h_0,\\
(h^2+2)^{7/2}/[16\pi h(h^2-2)^2],&h>h_0.
\end{cases}
\]
At \(h_0\), conditional on this low-brightness event, the shares in fixed disjoint neighborhoods of the horizontal and oblique families tend to \(1/9\) and \(8/9\), respectively.

For fixed \(\lambda\in\mathbb R\), \(x\ge0\), and \(t_+=\max(t,0)\), the joint limit is
\[
\begin{aligned}
&\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\Pr\{B_{h_0+\lambda\varepsilon}(U)\le m(h_0+\lambda\varepsilon)+x\varepsilon\}\\
&\quad=\frac{8}{9\pi h_0}(x-7\lambda_+/8)_+^2
+\frac{64}{9\pi h_0}(x-7(-\lambda)_+/8)_+^2.
\end{aligned}
\]

## Assumptions and scope

Lengths and areas are Euclidean; the centered square base has side length two. The probability measure is sphere area divided by \(4\pi\), so antipodal unit directions are counted separately. This gives the same area law as uniform unoriented directions. The asymptotic at fixed \(h\) is separate from the pointwise crossover above. Only the least-brightness result and its probability laws are claimed here; the known greatest-brightness classification is a comparator.

## Proof

**Brightness and global minimum.** The outward facet area vectors are \((0,0,-4)\), \((\pm h,0,1)\), and \((0,\pm h,1)\). Cauchy's projection formula gives, with \(a=|U_1|, b=|U_2|, c=|U_3|\),
\[
B_h(U)=2c+\max(c,ha)+\max(c,hb)=\max\{4c,3c+ha,3c+hb,2c+ha+hb\}. \tag{1}
\]
Extend the right-hand side homogeneously to the nonnegative octant. At a height \(c\in[0,1/4]\), its unit sublevel in coordinates \((ha,hb)\) is the polygon given by nonnegativity, each coordinate at most \(1-3c\), and their sum at most \(1-2c\). Its vertices are \((0,0),(1-3c,0),(1-3c,c),(c,1-3c),(0,1-3c)\), with duplicates at the endpoints. Each of these is affine in \(c\), so the full polytope is the convex hull of the vertices at the two endpoint heights. In \((a,b,c)\) coordinates those points are
\[
(0,0,0),\ (1/h,0,0),\ (0,1/h,0),\ (0,0,1/4),\
(1/(4h),0,1/4),\ (0,1/(4h),1/4),\ (1/(4h),1/(4h),1/4).
\]
Their largest norm is \(\max(1/h,\sqrt{h^2+2}/(4h))\); all vertices other than the two horizontal candidates and the last vertex are strictly shorter than the last. Strict convexity of squared norm excludes any nontrivial convex combination of distinct points among the maximizers. By homogeneity, the minimum on the sphere is the reciprocal of this norm, and the minimizing directions are the normalized farthest vertices and their sign reflections. The two lengths agree exactly at \(h^2=14\).

**Horizontal contribution.** Near \(e_1\) write \((y,z)=(U_2,U_3)\), so \(U_1=\sqrt{1-y^2-z^2}\). Equation (1) gives the expansion about the local value \(h\)
\[
B_h-h=2|z|+\max(|z|,h|y|)+O(y^2+z^2).
\]
The linear part is positive away from the origin and bounds a positive multiple of \(|y|+|z|\). Its planar unit sublevel has area \((4/h)\int_0^{1/3}(1-2z)\,dz=8/(9h)\). The surface Jacobian tends to one. Scaling the chart by \(\varepsilon\) and using the coercive linear part to bound all scaled points near the minimum gives the coefficient \(8/(9\pi h)\) for four such directions after dividing by \(4\pi\).

**Oblique contribution.** Use the positive octant and put \(D=h^2+2\), \(u_0=(1,1,h)/\sqrt D\), \(p=hU_1-U_3\), and \(q=hU_2-U_3\). The cross product of the two coordinate gradients is \((h,h,h^2)\), with dot product \(h\sqrt D\) against \(u_0\). Thus the surface element in the local chart is \((1/(h\sqrt D)+O(|p|+|q|))\,dp\,dq\). Differentiating the unit-sphere equation at \(u_0\) gives \(dU_3=-(dp+dq)/D\). Now (1) is \(4U_3+p_++q_+\). Writing \(\alpha=4/D\), the resulting expansion about the oblique value \(4h/\sqrt D\) is
\[
B_h-4h/\sqrt D=(1-\alpha)(p_++q_+)+\alpha((-p)_++(-q)_+)+O(p^2+q^2).
\]
For \(h\ge h_0\), and in a neighborhood below \(h_0\) as well, both linear weights are positive. In a quadrant with weights \(s,t\) the planar unit sublevel is a triangle of area \(1/(2st)\). Summing the four triangles gives \(1/[2\alpha^2(1-\alpha)^2]\). Multiplying by the surface Jacobian at zero, eight sign choices, and \(1/(4\pi)\) gives \(D^{7/2}/[16\pi h(h^2-2)^2]\). At \(h_0\) this equals \(64/(9\pi h_0)\). The only global minima are the classified points; compactness excludes the complement of their neighborhoods for small enough \(\varepsilon\). This proves the fixed-height constants and critical weights.

**Moving height.** The branch values \(h\) and \(4h/\sqrt{h^2+2}\) have derivatives \(1\) and \(8/(h^2+2)^{3/2}=1/8\) at \(h_0\). At \(h=h_0+\lambda\varepsilon\), their respective excesses over the global minimum are \((7\lambda_+/8)\varepsilon+O(\varepsilon^2)\) and \((7(-\lambda)_+/8)\varepsilon+O(\varepsilon^2)\). Both local expansions hold with uniform remainders near \(h_0\); their linear parts bound norm uniformly below there, and their Jacobians vary continuously. Continuity and compactness localize the event to the two families at the transition. In each chart centered at its direction for the current height, rescale the coordinates by \(\varepsilon\). The limiting sublevel is that of its positive homogeneous linear part at the level \(x\) minus the corresponding excess coefficient. Boundaries have planar measure zero, including when this level is zero; if negative, the limiting contribution vanishes. The chart areas are the critical coefficients times the squares of the positive parts of those levels, as asserted.

## Verification

The global proof and local sublevel calculations establish the limiting assertions. The accompanying `CHECK.py` is a finite diagnostic: it compares (1) with direct convex-hull projection, checks extremal candidates and bounds at sample directions, and checks numerical identities at the transition. It does not prove the polytope enumeration, the tail asymptotics or the crossover. That script also includes upper-brightness checks as background comparisons.

## Relationship to prior work

Cauchy's polyhedral projection formula is classical. The same-object rectangular-pyramid result [1] contains the square case for the **greatest** brightness: its formula and disjoint spherical caps give the square-case upper switch at \(\sqrt6\) and exact linear upper tail. These are credited as context, not claimed as contributions here. The present lower switch at \(\sqrt{14}\), exact quadratic coefficient, conditional weights, and joint lower limit address the opposite extremum; neither the maximal norm of the supporting vectors nor their top caps determines the farthest vertices of the unit sublevel or their local linear cusps. This is also distinct from caliper width: the companion square-pyramid width law [2] concerns distance between supporting planes, not shadow area. The accessible abstract of [3] discusses projected-area or joint area-perimeter laws for several ellipsoidal, cylindrical and conical particles; it does not establish coverage of this lower-tail theorem, and the full text was not inspected here. A mean projected-area identity [4] is a first-moment formula, not an endpoint statement. Priority beyond the passages checked is not established.

## Limitations

No classification is asserted for skewed or nonsquare bases. The law uses Haar-uniform orthographic directions. The moving-height limit is pointwise for fixed \(\lambda,x\), not uniform for parameters varying without bound.

## References

1. [*Three-phase brightest-shadow geometry and exact endpoint tails of right rectangular pyramids*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-three-phase-brightest-shadow-geometry-and-exact-endpoint-tails-o--07110a88f45f), Finding and proof §§3–4.
2. [*Two sharp width transitions and critical rare-orientation crossovers for right square pyramids*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-two-sharp-width-transitions-and-critical-rare-orientation-crosso--781beb3c7296), Finding and assumptions.
3. G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proc. R. Soc. A **457** (2001), 283–306. https://doi.org/10.1098/rspa.2000.0667
4. Z. Slepian, *The Average Projected Area Theorem – Generalization to Higher Dimensions*. https://arxiv.org/abs/1109.0595
