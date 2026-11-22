# The sharp three-point spherical-code endpoint and its Beta–Dirichlet shape law

## Finding

Fix an integer \(d\geq3\). Sample \(U_1,U_2,U_3\) independently according to normalized surface measure on the Euclidean unit sphere \(S^{d-1}\subset\mathbb R^d\). Define the smallest intrinsic angular separation
\[
\Theta_d=\min_{1\le i<j\le3}\arccos(U_i\cdot U_j).
\]
The maximum possible separation is \(\theta_*=2\pi/3\). As \(h\downarrow0\),
\[
\boxed{\Pr\{\Theta_d>2\pi/3-h\}=C_dh^{(d+2)/2}(1+o(1)),\qquad
C_d=\frac{2^{3-d}3^{(5d-2)/4}\Gamma(d/2)}{d(d+2)\pi^{3/2}\Gamma((d-1)/2)}.}
\]
For example, \(C_3=3^{9/4}/(10\pi)\), and the exponent for points on the ordinary two-sphere is \(5/2\). This is the near-packing endpoint of the canonical three-particle hard-cap partition function, not a many-point small-angle extreme-value law.

The rare event also determines a limiting marked geometry. Put \(q_h=\cos(2\pi/3-h)\), \(\delta_h=q_h+1/2\), and, for the three pair labels \(ij=12,13,23\),
\[
t_{ij}=\frac{q_h-U_i\cdot U_j}{\delta_h}.
\]
Conditionally on \(\Theta_d>2\pi/3-h\), the vector \((t_{12},t_{13},t_{23})\) converges **in total variation** to the density
\[
\boxed{g_d(t_1,t_2,t_3)=\frac{\Gamma((d+4)/2)}{3^{(d+2)/2}\Gamma((d-2)/2)}
 (3-t_1-t_2-t_3)^{(d-4)/2}}
\]
on \(t_i>0\) and \(\sum_i t_i<3\), with zero density outside. In the limiting law, if \(T=\sum_i t_i\), then independently
\[
T/3\sim\operatorname{Beta}\!\left(3,\frac{d-2}{2}\right),\qquad
(t_1/T,t_2/T,t_3/T)\sim\operatorname{Dirichlet}(1,1,1).
\]
These are statements for every *fixed* integer \(d\ge3\). They do not assert any uniform error bound in growing dimension.

## Assumptions and scope

All three points are independent and rotation-invariant; the distribution is uniform over the full unit sphere, not a latitude circle, hemisphere, or spherical cap. Angular distance is the shorter great-circle distance in \([0,\pi]\), not Euclidean chord distance or a spherical triangle's internal angle. The strict and non-strict versions of the event agree for \(h>0\) by continuity. At \(h=0\), probability is zero. For fixed dimension the limiting constants and marked densities are explicit, finite and positive.

## Proof

**1. The optimal configuration and localization.** Write \(x=U_1\cdot U_2\), \(y=U_1\cdot U_3\), \(z=U_2\cdot U_3\). Since
\[
0\le\|U_1+U_2+U_3\|^2=3+2(x+y+z),
\]
at least one pair has inner product at least \(-1/2\). Thus \(\Theta_d\le2\pi/3\). Equality forces all three inner products to be \(-1/2\), hence \(U_1+U_2+U_3=0\) and the three points form a planar regular triple. This also proves that the endpoint event localizes all three pair products near \(-1/2\): when \(x,y,z<q_h=-1/2+\delta_h\), the sum inequality gives \(-1/2-2\delta_h\le x,y,z< -1/2+\delta_h\).

**2. The exact Gram distribution.** Let \(D(x,y,z)=1+2xyz-x^2-y^2-z^2\), the determinant of the three-by-three pairwise Gram matrix. The joint density of \((x,y,z)\) for \(d\ge3\), relative to ordinary Lebesgue measure, is
\[
f_d(x,y,z)=A_dD(x,y,z)^{(d-4)/2}\mathbf1_{\{D>0\}},\qquad
A_d=\frac{\Gamma(d/2)^2}{\pi^{3/2}\Gamma((d-1)/2)\Gamma((d-2)/2)}.
\]
Indeed, \(x\) and \(y\) have independent one-coordinate densities \(c_d(1-s^2)^{(d-3)/2}\), with \(c_d=\Gamma(d/2)/(\sqrt\pi\Gamma((d-1)/2))\). Conditionally on \((x,y)\), \(z=xy+\sqrt{(1-x^2)(1-y^2)}\,W\), where \(W\) is the first coordinate of a uniform point of \(S^{d-2}\). Applying its normalized beta density and the Jacobian gives precisely \(A_d\). For \(d=3\), the exponent \(-1/2\) describes an integrable Gram-boundary singularity.

In terms of \(t_i\ge0\), put \(u_i=1-t_i\), \(T=\sum t_i\) and \(\delta=\delta_h\). The exact change of variables \((x,y,z)=(-1/2+\delta u_1,-1/2+\delta u_2,-1/2+\delta u_3)\) has Jacobian \(\delta^3\) and yields
\[
D=\frac32\delta(3-T)-\delta^2\left(\sum_i u_i^2+\sum_{i<j}u_iu_j\right)+2\delta^3u_1u_2u_3.
\]
The support satisfies \(0\le t_i\le3\) and \(T\le3\). For interior points of this simplex, the rescaled unnormalized density converges pointwise to \(A_d(3/2)^{(d-4)/2}(3-T)^{(d-4)/2}\), after factoring \(\delta^{(d+2)/2}\). Pointwise convergence alone is insufficient to normalize the density at \(d=3\); the independent cap-lens calculation below supplies the exact total mass, followed by Scheffé's lemma.

**3. Independent cap-lens evaluation of the total mass.** Let \(\alpha=\arccos(U_1\cdot U_2)\), with probability density \(c_d\sin^{d-2}\alpha\). The two inequalities involving \(U_3\) place it in the intersection of spherical caps of radius \(r=\pi-\theta\), centered at \(-U_1,-U_2\) and separated by \(\alpha\). This lens is empty for \(\alpha>2r\); the first pair itself requires \(\alpha>\theta\). Therefore for \(\theta=2\pi/3-h\),
\[
\Pr(\Theta_d>\theta)=\frac{c_d}{\omega_{d-1}}
\int_\theta^{2r}\sin^{d-2}\alpha\;L_d(r,\alpha)\,d\alpha,
\qquad\omega_{d-1}=\frac{2\pi^{d/2}}{\Gamma(d/2)},
\]
where \(L_d(r,\alpha)\) denotes the *unnormalized surface area* of the intersection of those two caps. Note \(2r-\theta=3h\).

We derive the needed lens asymptotic rather than assume it. In geodesic normal coordinates at the tangency point between two equal caps, let \(z\in\mathbb R^{d-2}\) be transverse coordinates and \(s=2r-\alpha\downarrow0\) their axial overlap. The two spherical boundary graphs follow from the spherical law of cosines and have combined permitted axial width
\[
\bigl[s-\cot(r)|z|^2+o(s+|z|^2)\bigr]_+.
\]
The volume element equals \(1+o(1)\) in this chart. After \(z=\sqrt{s\tan r}\,w\), the lens lies in a uniformly shrinking chart and its measure is
\[
L_d(r,2r-s)=\frac{2\kappa_{d-2}}d
(\tan r)^{(d-2)/2}s^{d/2}(1+o(1)),\qquad
\kappa_{d-2}=\frac{\pi^{(d-2)/2}}{\Gamma(d/2)},
\]
uniformly for \(r\) in a small compact neighborhood of \(\pi/3\), by the explicit integral \(\int_{|w|<1}(1-|w|^2)dw=2\kappa_{d-2}/d\). Thus integration over \(s\in[0,3h]\), using \(\sin\alpha\to\sin(2\pi/3)=\sqrt3/2\) and \(\tan r\to\sqrt3\), gives
\[
\Pr(\Theta_d>2\pi/3-h)=\frac{c_d}{\omega_{d-1}}
\left(\frac{\sqrt3}{2}\right)^{d-2}
\frac{2\kappa_{d-2}}d\,3^{(d-2)/4}
\frac{(3h)^{(d+2)/2}}{(d+2)/2}\,[1+o(1)].
\]
Substituting the stated gamma normalizations simplifies this expression to the claimed \(C_dh^{(d+2)/2}\), without requiring a nonuniform Gram-boundary expansion.

**4. The complete limiting marked density.** Since \(\delta_h=\sqrt3h/2+O(h^2)\), the Gram formula of step 2 divided by \(\delta_h^{(d+2)/2}\) converges pointwise for \(t_i>0\), \(T<3\). Its integral over the full limiting simplex is
\[
A_d(3/2)^{(d-4)/2}J_d,\qquad
J_d=\int_{t_i>0,T<3}(3-T)^{(d-4)/2}\,dt_1dt_2dt_3
=\frac{3^{(d+2)/2}\Gamma((d-2)/2)}{\Gamma((d+4)/2)}.
\]
The lens computation in step 3 shows, after replacing \(h\) by \(\delta_h\), that the *total* scaled mass converges to exactly this integral, as also confirmed by direct gamma simplification. Normalize these nonnegative densities by the event probability. They now converge pointwise almost everywhere to \(g_d\) and both the approximating and limiting functions integrate to one; **Scheffé's lemma** yields convergence in \(L^1\), hence in total variation. This also handles the integrable singularity for \(d=3\) without a false uniform-dominance claim.

Finally, set \(T=t_1+t_2+t_3\), \(w_i=t_i/T\). The Jacobian is \(T^2\) on the two-dimensional simplex of \((w_1,w_2,w_3)\), while \(g_d\) depends only on \(T\). Consequently \(w\) is uniform on the unit two-simplex, independent of \(T\). The density of \(T/3\) is proportional to \(u^2(1-u)^{(d-4)/2}\), exactly \(\operatorname{Beta}(3,(d-2)/2)\). All assertions follow.

## Verification

The accompanying standalone `verify.py` implements an **independent exact two-dimensional conditional beta integral** for the probability, checks the gamma normalization of the Gram and cap-lens calculations in dimensions \(3,4,5,6,9\), and evaluates four decreasing thresholds in dimensions \(3,4,5\). All 12 numerical probability-to-asymptotic ratios approach one, and the checker prints `ALL_CHECKS_PASSED`. These are finite numerical cross-checks only; the proof of the infinite limit is the preceding geometry and Scheffé argument. The only dependencies are Python, NumPy and SciPy.

## Relationship to prior work

The deterministic optimal three-point separation \(2\pi/3\) belongs to classical spherical-code packing (Rankin, 1955). Moran (1979) studied shortest distances in general random spherical point sets and gave bounds, while Cai–Fan–Jiang (2013) and Brauchart–Reznikov–Saff–Sloan–Wang–Womersley (first preprint 2015) study asymptotic separation in many-point or varying-dimensional regimes. Jenssen–Joos–Perkins (2018) introduce the canonical hard-cap partition function but their highlighted exponential abundance estimates concern different parameters, rather than the fixed-three-point endpoint. Neither a known optimal code nor a large-sample small-distance law implies the new exact three-particle rare-event coefficient or its conditional Beta–Dirichlet shape density. The closed coefficient and marked endpoint law are the claims assessed here, not the classical packing optimum, Gram density, or known large-sample results.

## Limitations

The result requires independent rotationally uniform samples, exactly three points, fixed ambient integer \(d\ge3\) and a threshold approaching \(2\pi/3\) from below. It does not establish a dimension-uniform remainder, a full closed elementary CDF at all angles, analogues for nonuniform sampling, or the near-optimum packing measure for four or more points. Numerical tests are not a substitute for the analytic proof. Historical priority is necessarily provisional because inaccessible or incompletely indexed older geometric-probability sources may contain an equivalent formulation. No independent mathematical audit has been performed.

## References

- R. A. Rankin, “The Closest Packing of Spherical Caps in n Dimensions,” *Proceedings of the Glasgow Mathematical Association* 2 (1955), 139–144, https://doi.org/10.1017/S2040618500033219.
- P. A. P. Moran, “The closest pair of N random points on the surface of a sphere,” *Biometrika* 66 (1979), 158–162, https://doi.org/10.1093/biomet/66.1.158.
- T. Cai, J. Fan, T. Jiang, “Distributions of Angles in Random Packing on Spheres,” *JMLR* 14 (2013), 1837–1864, https://arxiv.org/abs/1306.0256.
- J. S. Brauchart, A. B. Reznikov, E. B. Saff, I. H. Sloan, Y. G. Wang, R. S. Womersley, “Random Point Sets on the Sphere—Hole Radii, Covering, and Separation,” first public version December 23, 2015, https://arxiv.org/abs/1512.07470 (primary classification 52C17, 52A22).
- M. Jenssen, F. Joos, W. Perkins, “On kissing numbers and spherical codes in high dimensions,” *Advances in Mathematics* 335 (2018), 307–321, https://doi.org/10.1016/j.aim.2018.07.001.
