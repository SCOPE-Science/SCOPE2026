# Sharp all-dimensional convexity interval and curvature-rank loci of hyperoctahedral quartic support bodies

## Finding

For every integer \(d\ge4\), let \(u=(u_1,\ldots,u_d)\in S^{d-1}\subset\mathbb R^d\) and put
\[
Y_d(u)=\sum_{i=1}^d u_i^4-\frac{3}{d+2},\qquad h_{d,\varepsilon}(u)=1+\varepsilon Y_d(u).
\]
The homogeneous extension of \(h_{d,\varepsilon}\) is the support function of a full-dimensional convex body if and only if
\[
\boxed{-\frac{2(d+2)}{3(3d+4)}\ \le\ \varepsilon\ \le\ \frac{d+2}{3(d+3)}.}
\]
Every body in the closed interval is centrally symmetric and strictly convex. Throughout the open interval its curvature-radius tensor \(\nabla^2_S h+hI\) is positive definite. At the positive endpoint its rank is zero at exactly the \(2d\) coordinate-axis normals \(\pm e_i\), and is full elsewhere. At the negative endpoint its rank is \(d-2\) at precisely the \(4\binom d2\) signed normals \((\pm e_i\pm e_j)/\sqrt2\), \(i<j\), and is full elsewhere.

Write \(K_{d,\varepsilon}\) for the corresponding body and \(\kappa_d\) for the volume of the Euclidean unit ball. Each member has the same mean width as the unit ball, and its volume obeys the exact second-order law
\[
\boxed{\frac{\operatorname{Vol}_d(K_{d,\varepsilon})}{\kappa_d}=
1-\frac{36d(d-1)(d+3)}{(d+2)^2(d+4)(d+6)}\varepsilon^2+O_d(\varepsilon^3).}
\]
In fact the volume is a polynomial in \(\varepsilon\) of degree at most \(d\), throughout the admissible interval. The two sharp convexity thresholds tend to \(-2/9\) and \(1/3\) as \(d\to\infty\).

## Assumptions and scope

All coordinates and inner products are standard Euclidean ones. The curvature-radius tensor is defined on the tangent space \(u^\perp\) of the unit sphere. The support function refers to the one-homogeneous extension \(H(x)=\|x\|_2 h(x/\|x\|_2)\) for \(x\ne0\), \(H(0)=0\). The theorem covers every integer \(d\ge4\) and every real \(\varepsilon\). Curvature-rank claims concern this normal-coordinate tensor, not a positive-area planar facet. The \(O_d\) coefficient may depend on fixed \(d\), and the volume expansion is local about \(\varepsilon=0\). No formula for every higher-degree coefficient of the volume polynomial is claimed.

## Proof

**1. Curvature quadratic form.** Set \(F(u)=\sum_i u_i^4\), \(c=3/(d+2)\), and let \(u,v\in\mathbb R^d\) satisfy \(\|u\|=\|v\|=1\), \(u\cdot v=0\). Directly differentiating the great circle \(u\cos t+v\sin t\) yields
\[
Q_d(u,v):=(\nabla^2_S Y_d+Y_dI)_u[v,v]
=12\sum_i u_i^2v_i^2-3\sum_i u_i^4-c.
\]
Put \(a=\sum_i u_i^2v_i^2\), \(b=\sum_i u_i^4\), \(g=\sum_i v_i^4\), and \(x_i=u_i^2\), \(y_i=v_i^2\). Then \(a\ge0\), \(b\le1\). Hence \(Q_d\ge-3-c\), with equality only when \(u\) is a coordinate-axis normal, where every tangent direction attains equality.

**2. Sharp universal upper bound.** Bessel's inequality for the orthonormal pair \(u,v\) gives \(x_i+y_i\le1\) for each \(i\). Consequently
\[
a+g=\sum_i y_i(x_i+y_i)\le1,
\quad 2a\le b+g,
\quad a\le\sum_i x_i(1-x_i)=1-b.
\]
In particular \(3a\le1+b\). To establish the fourth independent inequality \(a\le1/2\), write \(z_i=u_iv_i\). Orthogonality gives \(\sum_i z_i=0\), while Cauchy gives \(\sum_i|z_i|\le1\). Positive and negative masses are therefore each at most \(1/2\), so
\[
a=\sum_i z_i^2\le(1/2)^2+(1/2)^2=1/2.
\]
Equality forces exactly two nonzero \(z_i\), of opposite signs and magnitude \(1/2\), and equality in Cauchy's inequality. Thus, up to signed coordinate permutations, \(u=(e_1+e_2)/\sqrt2\) and \(v=(e_1-e_2)/\sqrt2\).

If \(b\le1/2\), then \(4a-b=(3a-b)+a\le1+1/2\). If \(b\ge1/2\), then \(4a-b\le4(1-b)-b\le3/2\). We have proved
\[
\boxed{-3-c\le Q_d(u,v)\le\frac92-c,}
\]
for **every** orthonormal \(u,v\). The lower bound is attained exactly at axis normals and the upper bound exactly at signed two-coordinate face diagonals with the complementary tangent direction. These equality classifications apply in every \(d\ge4\); they are not extrapolated from any finite test.

**3. Convexity and endpoints.** The tangential Hessian of the one-homogeneous extension is \(I+\varepsilon(\nabla^2_S Y_d+Y_dI)\) divided by \(\|x\|\). Thus its positive semidefiniteness is equivalent to \(1+\varepsilon Q_d(u,v)\ge0\) for all orthonormal pairs. Substituting the two sharp extrema gives exactly the displayed closed \(\varepsilon\)-interval; outside it the Hessian has a negative direction, excluding any support function. On that interval \(h_{d,\varepsilon}>0\) because \(1/d\le F(u)\le1\) and the two endpoint multipliers give strictly positive minima. Hence convexity of the homogeneous extension along lines through the origin follows from evenness and positivity, as it does away from the origin from its Hessian.

At \(u=\pm e_i\), all tangent eigenvalues of \(\nabla^2_S Y_d+Y_dI\) equal \(-3-c\). At a two-coordinate diagonal, the tangent direction inside those two coordinates has eigenvalue \(9/2-c\), while the remaining \(d-2\) tangent directions each have eigenvalue \(-3/2-c\). Both rank assertions follow, and the sharp equality classification of Step 2 excludes any other degenerate normals. The homogeneous support function is differentiable at every nonzero direction, so each exposed supporting face is a singleton; consequently the convex bodies are strictly convex even at the endpoints.

**4. Mean width and volume.** Since \(F\) has sphere average \(3/(d+2)\), \(Y_d\) has mean zero. Each support function is even, hence its mean directional width \(2\int h\) equals that of the unit ball. The polynomial \(Y_d\) is a spherical harmonic of degree four: indeed \(\Delta_S Y_d=-4(d+2)Y_d\). The normalized spherical fourth-degree moment is
\[
\mathbb E(Y_d^2)=\frac{24(d-1)}{(d+2)^2(d+4)(d+6)},
\]
obtained from \(\mathbb E(u_i^8)=105/[d(d+2)(d+4)(d+6)]\) and \(\mathbb E(u_i^4u_j^4)=9/[d(d+2)(d+4)(d+6)]\), \(i\ne j\). The standard support-coordinate identity is
\[
\operatorname{Vol}_d(K_{d,\varepsilon})=
\frac1d\int_{S^{d-1}}(1+\varepsilon Y_d)\det\big(I+\varepsilon(\nabla^2_SY_d+Y_dI)\big)\,d\sigma.
\]
First variation gives zero because \(\mathbb E Y_d=0\). Second variation gives
\[
\frac{V''(0)}{V(0)}=
 d\mathbb E\big[Y_d(\Delta_S+(d-1))Y_d\big]
=-3d(d+3)\mathbb E(Y_d^2).
\]
Dividing by two yields the stated coefficient. The determinant is polynomial in \(\varepsilon\) of degree \(d-1\), and multiplication by \(h\) gives degree at most \(d\). Continuity extends the identity to the closed admissible interval.

## Verification

The independent executable `verify_quartic_nd.py` requires Python 3 and NumPy and runs without network access. It performs exact fraction checks of the endpoint eigenvalues and second-volume coefficient for \(3\le d\le200\), reproduces the independently known three-dimensional special case as a boundary comparison, and tests the global quadratic-form bounds for 24,000 random orthonormal pairs in eight dimensions. The program reports `QUARTIC_ND_SUPPORT_PASS exact_dimensions=198 random_tangent_pairs=24000 d3_volume_consistency=1`. These finite calculations are corroboration; the two-case algebraic inequality in Step 2 proves the infinite-dimensional-index statement.

## Relationship to prior work

Antunes–Bogosel (first publicly posted 2018-09-01) develops support-function convexity and spherical-harmonic shape optimization, specifically focusing on dimensions two and three; it does not provide this all-\(d\) quartic sharp range. Mathis–Meroni provides further smooth-support-function constructions in the fiber-body setting, rather than this general-dimensional sharp curvature-rank classification. A publicly available three-dimensional octahedral-quartic result proves the \(d=3\) values \(-10/39\) and \(5/18\) and an exact cubic volume formula. Those three-dimensional values are **not claimed as new**: the present theorem is scoped to every \(d\ge4\), and its proof includes an all-dimensional bound \(a\le1/2\) that does not follow by replacing the ambient dimension in the earlier three-dimensional spectral calculation. General support-function perturbation criteria are classical but do not, without a separate sharp minimax calculation, determine the extremal tangent pairs and endpoint ranks for this particular family.

## Limitations

This does not classify arbitrary hyperoctahedrally invariant support functions or multi-harmonic perturbations. The volume statement is a sharp second-order expansion, not a tabulation of all \(d\) polynomial coefficients. Strict convexity at the two curvature-degenerate endpoints does not imply positive curvature there. The published-priority assessment may miss an equivalent formulation in historical multidimensional spherical-harmonic or anisotropic Wulff literature; independent validation has not been performed.

## References

1. P. R. S. Antunes and B. Bogosel, *Parametric Shape Optimization using the Support Function*, arXiv:1809.00254, first version 2018-09-01; Sections 2–3. https://arxiv.org/abs/1809.00254
2. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406, first version 2021-05-26; Section 4. https://arxiv.org/abs/2105.12406
3. *Sharp convexity and volume of the octahedral quartic support family*, publicly available three-dimensional predecessor, `2026/10/18/SCOPE-sharp-convexity-and-volume-of-the-octahedral-quartic-support-fam--600ddd0fea2b/RESULT.md` (three-dimensional scope only). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-convexity-and-volume-of-the-octahedral-quartic-support-fam--600ddd0fea2b
