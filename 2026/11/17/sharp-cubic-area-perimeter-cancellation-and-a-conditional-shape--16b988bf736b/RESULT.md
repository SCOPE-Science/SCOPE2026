# Sharp cubic area–perimeter cancellation and a conditional shape law for cyclic polygons

## Finding

Fix an integer \(m\ge3\). Let \(m\) points be sampled independently and uniformly by arclength on the unit circle, and let \(P\) and \(A\) be the perimeter and Euclidean area of their convex cyclic polygon. Set
\[
a=\frac{\pi}{m},\quad s=\sin a,\quad c=\cos a,\quad P_*=2ms,\quad A_*=msc,
\]
\[
D_P=P_*-P,\qquad D_A=A_*-A,\qquad R=D_A-2cD_P.
\]
The leading quadratic deviations of area and perimeter are proportional, but their first uncancelled term is *cubic*. Precisely,
\[
\lim_{\eta\downarrow0}\;\sup_{\substack{\text{inscribed cyclic }m\text{-gons}\\0<D_P\le\eta}}
\frac{|R|}{D_P^{3/2}}
= C_m:=\frac{2\sqrt{s}}{3}\frac{m-2}{\sqrt{m(m-1)}}.
\]
The constant is sharp. To attain either extremal sign asymptotically, perturb one regular angular gap in one direction and all remaining gaps equally in the opposite direction.

For the random polygon, begin at its first sampled vertex, traverse counterclockwise, and write its successive positive angular gaps as \(\gamma_1,\ldots,\gamma_m\), with sum \(2\pi\). Put
\[
Z_\varepsilon=\sqrt{\frac{s}{4\varepsilon}}\left(\gamma_1-\frac{2\pi}{m},\ldots,\gamma_m-\frac{2\pi}{m}\right),
\quad H_m=\left\{z\in\mathbb R^m:\sum_i z_i=0\right\}.
\]
Conditional on \(D_P\le\varepsilon\), the law of \(Z_\varepsilon\) converges **in total variation** to normalized Euclidean volume on the unit ball \(B_m=\{z\in H_m:\|z\|\le1\}\). Jointly, **in distribution**,
\[
\left(Z_\varepsilon,\frac{R}{\varepsilon^{3/2}}\right)
\Longrightarrow\left(Z,-\frac{2\sqrt{s}}{3}\sum_{i=1}^m Z_i^3\right),
\qquad Z\sim\operatorname{Uniform}(B_m).
\]
The second component is nondegenerate and symmetric, has support \([-C_m,C_m]\), and has exact variance
\[
V_m=\frac{8s(m-1)(m-2)}{3m(m+1)(m+3)(m+5)}.
\]
In particular, the conditional second moments of \(R/\varepsilon^{3/2}\) converge to \(V_m\); for triangles \(V_3=\sqrt3/216\). The previously known leading small-perimeter-deficit probability is not part of the novelty claim.

## Assumptions and scope

All limits take \(\varepsilon\downarrow0\) or \(\eta\downarrow0\) with the number of vertices \(m\) fixed. The \(m\) sampled points are independent, distributed uniformly on the unit circumference, and distinct almost surely. Perimeter is the sum of their chords in cyclic order and area is ordinary unsigned Euclidean area. The signed quantity \(R\) is not itself a deficit and may have either sign. The total-variation assertion concerns the gap *vector*; the joint residual assertion is weak convergence, not an asserted total-variation convergence of transformed scalar variables.

## Proof

1. **Gaps and exact geometry.** Rotating the first labelled sampled point to angle zero and sorting the other \(m-1\) relative angles shows that \((\gamma_i/(2\pi))_{i=1}^m\) has the symmetric \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution. Thus it has constant density on the open gap simplex. Write \(\delta_i=\gamma_i-2a\), so \(\delta\in H_m\). The exact chord and shoelace identities are
\[
P=2\sum_i\sin(a+\delta_i/2),\qquad A=\frac12\sum_i\sin(2a+\delta_i).
\]
All expressions are smooth near \(\delta=0\).

2. **Strict localization.** By strict concavity of \(x\mapsto\sin(x/2)\) on \((0,2\pi)\), Jensen's inequality makes the equal-gap configuration the unique maximizer of \(P\) on the closed gap simplex. Hence \(D_P\to0\) forces \(\delta\to0\). Taylor expansion, using \(\sum_i\delta_i=0\), gives uniformly near zero
\[
D_P=\frac{s}{4}\sum_i\delta_i^2+\frac{c}{24}\sum_i\delta_i^3+O_m(\|\delta\|^4),
\]
\[
D_A=\frac{\sin(2a)}4\sum_i\delta_i^2+\frac{\cos(2a)}{12}\sum_i\delta_i^3+O_m(\|\delta\|^4).
\]
Consequently
\[
R=-\frac{s^2}{12}\sum_i\delta_i^3+O_m(\|\delta\|^4),
\qquad D_P\sim\frac{s}{4}\|\delta\|^2.
\]

3. **Sharp deterministic coefficient.** For unit vectors \(u\in H_m\), maximize \(|\sum_i u_i^3|\). Lagrange multipliers show that any nonconstant extremizer has at most two distinct coordinates, since every coordinate solves the same quadratic. If \(k\) coordinates have the larger value and \(m-k\) the smaller, their cubic sum is \((m-2k)/\sqrt{mk(m-k)}\) for the appropriate orientation. Its absolute maximum over \(1\le k\le m-1\) is \((m-2)/\sqrt{m(m-1)}\), achieved precisely for \(k=1\) or \(m-1\) (up to permutation). Combining this with the expansions yields the claimed upper coefficient. Perturbations \(\delta=t u\) along such extremizers, with \(t\downarrow0\), prove sharpness.

4. **Rare-event conditional shape.** Since \(D_P\ge (s/8)\|\delta\|^2\) for sufficiently small \(\delta\), the event \(D_P\le\varepsilon\) lies within \(\|\delta\|=O_m(\sqrt\varepsilon)\). Under the displayed scaling, its feasible set differs from the unit ball in \(H_m\) by a radial boundary displacement \(O_m(\sqrt\varepsilon)\). Because the gap-simplex density is constant and the linear coordinate Jacobian is constant, the normalized conditional densities converge in \(L^1\); this proves the asserted total-variation convergence of \(Z_\varepsilon\). Substituting \(\delta=\sqrt{4\varepsilon/s}\,Z_\varepsilon\) into the cubic expansion yields, uniformly on the conditional event,
\[
\frac{R}{\varepsilon^{3/2}}=-\frac{2\sqrt s}{3}\sum_i(Z_\varepsilon)_i^3+O_m(\sqrt\varepsilon),
\]
which proves the joint weak limit. The same bounds give convergence of second moments.

5. **Exact limiting variance.** Let \(d=m-1\), \(\Pi=I_m-\mathbf1\mathbf1^{\mathsf T}/m\), and \(Z\) be uniform on the unit ball of \(H_m\). Rotational invariance of this ball, or the Gaussian sixth-moment pairing formula followed by radial integration, gives
\[
\mathbb E\left[\left(\sum_iZ_i^3\right)^2\right]
=\frac{6\sum_{i,j}\Pi_{ij}^{3}}{(d+2)(d+4)(d+6)}.
\]
The terms proportional to \(\sum_{i,j}\Pi_{ij}\) vanish because \(\Pi\mathbf1=0\). Direct substitution of \(\Pi_{ii}=(m-1)/m\), \(\Pi_{ij}=-1/m\) for \(i\ne j\), gives \(\sum_{i,j}\Pi_{ij}^{3}=(m-1)(m-2)/m\). Multiplication by \(4s/9\) produces \(V_m\). Reflection \(Z\mapsto-Z\) gives symmetry; nonconstancy of the cubic and the sharp third-moment bound give nondegeneracy and full support \([-C_m,C_m]\).

## Verification

To reproduce the numerical and symbolic checks, run `python checks/cyclic_cubic_check.py` with Python 3, NumPy and SymPy installed. The standalone file `checks/cyclic_cubic_check.py` symbolically verifies the cubic cancellation coefficient, samples uniformly from the appropriate hyperplane unit balls to check sixth-moment constants for \(m=3,4,5,6,9\), and compares the finite-perturbation exact sine formulas against the sharp limiting coefficient at decreasing perturbation scales. Its verified success marker is `CYCLIC_POLYGON_CUBIC_CHECKS_OK`. Numerical experiments check arithmetic, not the asymptotic theorem; all asymptotic and sharpness assertions follow from the proof above.

As a consistency check, the same conditional-ball computation reproduces the already-published perimeter endpoint coefficient
\[
\Pr(D_P\le\varepsilon)\sim
\frac{(m-1)!}{\sqrt m\,\Gamma((m+1)/2)(\pi s)^{(m-1)/2}}\,\varepsilon^{(m-1)/2}.
\]
This scalar coefficient is cited, not presented as new.

## Relationship to prior work

Koroleva and Nikitin (2013) proved individual endpoint laws for perimeters and areas of random inscribed polygons by localization to a quadratic ellipsoid. Their displayed expansions bound higher-order remainders but do not provide the signed *joint* cubic residual, its sharp extremizers, or its conditional distribution and variance. Indrei and Nurbekyan (2014) prove stability inequalities for general polygons and bound quadratic isoperimetric deficits; their conclusions do not identify this cubic cancellation in the unit-circumradius cyclic ensemble. Published results about fluctuations of randomly thinned regular polygons and many-vertex random cyclic polygons use a distinct side-count regime; their scalar limits do not imply the fixed-\(m\), near-maximum cubic law. Earlier work on the scalar perimeter/area endpoint probabilities is explicitly excluded from the originality claim.

## Limitations

The result concerns fixed side count, unit-circumradius cyclic polygons with independent uniform angular points. Its constants and remainder estimates are not uniform as \(m\to\infty\); no result for nonuniform endpoint sampling, other convex curves or general noncyclic polygons is asserted. The total-variation mode of convergence is proved only for the scaled gap vector, with joint weak convergence for the residual. Bibliographic priority beyond the inspected sources is not independently certified.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1 (first public 2013-01-07), https://arxiv.org/abs/1301.1360.
2. E. Indrei and L. Nurbekyan, *On the Stability of the Polygonal Isoperimetric Inequality*, arXiv:1402.4460v1 (first public 2014-02-18), https://arxiv.org/abs/1402.4460.
3. S. Wang, Z. Li and W.-Q. Xu, *Nonlinear random extrapolation estimates of pi under Dirichlet distributions*, Journal of Numerical Analysis and Approximation Theory 52 (2023), 273–294, https://ictp.acad.ro/jnaat/journal/article/view/1360/1463 (continuous polygon estimators in the many-vertex regime).
