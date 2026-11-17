# Exact bisector displacement and non-Gaussian Voronoi volume splitting in Euclidean balls

## Finding

Let \(d\ge2\) be an integer, let \(B_d\subset\mathbb R^d\) be the closed Euclidean unit ball, and independently choose \(X,Y\) according to normalized Lebesgue volume on \(B_d\). The perpendicular bisector between the sites has the signed central displacement
\[
H_d=\frac{\|X\|^2-\|Y\|^2}{2\|X-Y\|}.
\]
The sign is taken with respect to the unit normal \((X-Y)/\|X-Y\|\); its distribution is symmetric. Put \(\kappa_j=\pi^{j/2}/\Gamma(j/2+1)\). The exact density of \(H_d\) is
\[
 f_d(h)=\frac{2^d d\kappa_{d-1}}{\kappa_d}
 \int_0^{1-|h|}r^{d-1}\bigl[1-(r+|h|)^2\bigr]^{(d-1)/2}\,dr,
 \qquad |h|<1,
\]
and is zero outside \([-1,1]\). In particular, in three dimensions,
\[
 f_3(h)=\frac35(4+|h|)(1-|h|)^4\mathbf 1_{\{|h|<1\}}.
\]

Let \(V_X=\{z\in B_d:\|z-X\|\le\|z-Y\|\}\) and \(V_Y=B_d\setminus V_X\) up to a null boundary. Define their **signed normalized volume imbalance**
\[
 I_d=\frac{\operatorname{vol}(V_X)-\operatorname{vol}(V_Y)}{\kappa_d}.
\]
Then exactly
\[
 I_d=-2c_d\int_0^{H_d}(1-t^2)^{(d-1)/2}\,dt,
 \qquad c_d=\frac{\kappa_{d-1}}{\kappa_d}.
\]
Thus the preceding density determines the complete finite-dimensional law of the two cell volumes. In dimension three, \(I_3=-(3H_3-H_3^3)/2\) and
\[
 \mathbb E[I_3^2]=\frac{421}{4200},\qquad
 \operatorname{Var}\!\left(\frac{\operatorname{vol}(V_X)}{\kappa_3}\right)=\frac{421}{16800}.
\]

As \(d\to\infty\), both of the following hold in **total variation**:
\[
 dH_d\ \longrightarrow\ \operatorname{Laplace}(0,1/\sqrt2),
 \qquad
 \sqrt d\,I_d\ \longrightarrow\ \operatorname{Laplace}(0,1/\sqrt\pi).
\]
Here \(\operatorname{Laplace}(0,b)\) has Lebesgue density \(x\mapsto e^{-|x|/b}/(2b)\). In particular, the fluctuations of two-site Voronoi volume balance in high-dimensional balls are Laplace rather than Gaussian.

## Assumptions and scope

The two sites are independent and identically distributed with **uniform volume** in the unit ball. Voronoi regions are intersected with that same ball. Dimensions are integers \(d\ge2\), and the asymptotic parameter is dimension, not the number of sites. The orientation of the signed hyperplane normal fixes the sign of \(H_d\) and \(I_d\); reversing labels changes both signs. Coincident sites and bisector ties have probability zero. No other sites, nonuniform densities, or random external tessellations are included.

## Proof

**1. Bisector and exact density.** Set \(M=(X+Y)/2\) and \(D=(X-Y)/2\). The linear map \((M,D)\mapsto(X,Y)=(M+D,M-D)\) has absolute Jacobian \(2^d\). Write \(D=ru\), with \(r\ge0\), \(u\in S^{d-1}\), and decompose \(M=hu+w\), where \(w\perp u\). By direct expansion,
\[
 \frac{\|X\|^2-\|Y\|^2}{2\|X-Y\|}=
 \frac{4M\cdot D}{4\|D\|}=h.
\]
The constraints \(\|X\|,\|Y\|\le1\) are equivalent to
\[
 \|w\|^2+(r+|h|)^2\le1.
\]
The \((d-1)\)-dimensional volume of the allowed \(w\)-slice is therefore \(\kappa_{d-1}[1-(r+|h|)^2]^{(d-1)/2}\) for \(0\le r\le1-|h|\), and zero otherwise. Polar integration in \(D\), including sphere area \(d\kappa_d\), and division by \(\kappa_d^2\) give the displayed density. This is a probability density directly from a bijective change of variables, without an unverified normalization factor.

At \(h=0\), setting \(s=r^2\) produces the beta integral
\[
 f_d(0)=\frac{2^{d-2}d^2\Gamma(d/2)^2}
 {\sqrt\pi\,\Gamma(d+1/2)}.
\]
For \(d=3\), direct polynomial integration of the exact formula gives
\[
 f_3(h)=18\int_0^{1-|h|}r^2\bigl[1-(r+|h|)^2\bigr]\,dr
 =\frac35(4+|h|)(1-|h|)^4.
\]

**2. Cell-volume transform and three-dimensional moment.** Let \(u=(X-Y)/\|X-Y\|\). Comparing squared distances shows that \(V_X\) is the half-ball \(\{z\in B_d:z\cdot u\ge H_d\}\). Every central section of a unit ball is rotationally equivalent; its normalized signed-coordinate density is \(c_d(1-t^2)^{(d-1)/2}\) on \((-1,1)\). The two normalized half-ball volumes differ by the stated integral with a negative sign. For \(d=3\), \(c_3=3/4\), giving \(I_3=-(3H_3-H_3^3)/2\). A single polynomial integral proves
\[
 2\int_0^1\frac35(4+h)(1-h)^4
 \left(\frac{3h-h^3}{2}\right)^2\,dh=\frac{421}{4200}.
\]
Since exchanging the labels negates \(I_3\), its mean is zero. The cell share \((1+I_3)/2\) accordingly has variance \(421/16800\).

**3. Total-variation limit for bisector displacement.** Define
\[
 w_d(r)=r^{d-1}(1-r^2)^{(d-1)/2},\qquad 0<r<1,
\]
and let \(\nu_d\) be its normalized probability law. The function \(\log r+\tfrac12\log(1-r^2)\) has a unique global maximum at \(r_*=1/\sqrt2\), so elementary Laplace concentration yields \(\nu_d\Rightarrow\delta_{r_*}\). For every fixed real \(z\), dividing the displayed density at \(z/d\) by its value at zero gives an expectation with respect to \(\nu_d\) of
\[
 \left[1-\frac{2r|z|/d+z^2/d^2}{1-r^2}\right]_+^{(d-1)/2},
\]
where \([a]_+=\max\{a,0\}\). The integrand is bounded by one and converges locally uniformly near \(r_*\) to \(\exp[-r|z|/(1-r^2)]\). Concentration of \(\nu_d\) proves
\[
 \frac{f_d(z/d)}{f_d(0)}\longrightarrow e^{-\sqrt2|z|}.
\]
The gamma-ratio formula for \(f_d(0)\), with Stirling's formula, gives \(f_d(0)/d\to1/\sqrt2\). Thus the density of \(dH_d\) converges pointwise on \(\mathbb R\) to \(e^{-\sqrt2|z|}/\sqrt2\). This limiting function integrates to one, so Scheffé's lemma yields total-variation convergence.

**4. Total-variation limit for volume imbalance.** Write \(Z_d=dH_d\) and define the strictly decreasing differentiable transformation, for \(|z|<d\),
\[
 T_d(z)=-\frac{2c_d}{\sqrt d}\int_0^z
 \left(1-\frac{s^2}{d^2}\right)^{(d-1)/2}\,ds.
\]
By construction \(T_d(Z_d)=\sqrt d\,I_d\). Since \(c_d/\sqrt d\to1/\sqrt{2\pi}\), both \(T_d(z)\to-\sqrt{2/\pi}\,z\) and \(T_d'(z)\to-\sqrt{2/\pi}\) locally uniformly for fixed \(z\). The transforms are continuous, strictly monotone bijections from \((-d,d)\) to \((-\sqrt d,\sqrt d)\). For each fixed \(y\), their inverse images converge to \(-y\sqrt{\pi/2}\). The change-of-variables formula therefore makes the densities of \(T_d(Z_d)\) converge pointwise to
\[
 \frac{\sqrt\pi}{2}e^{-\sqrt\pi|y|}.
\]
This is a probability density. A second application of Scheffé's lemma proves the claimed total-variation limit. Neither step relies on an unjustified exchange of asymptotic probabilities at moving boundaries.

## Verification

A standalone file `checker.py` independently reconstructs the density integral and normalizes it numerically in dimensions 2 through 6; verifies the exact three-dimensional polynomial at multiple offsets and its moments using independent simulation; and tests both Laplace laws with independently generated random points in dimensions 64, 128 and 256. It prints `TWO_SITE_VORONOI_CHECKS_OK` on success. The infinite-dimensional convergence is established analytically above, not inferred from finite simulations.

## Relationship to prior work

Devroye, Györfi, Lugosi and Walk (2015), *On the measure of Voronoi cells*, study a cell of a Voronoi partition generated by a **growing number** of sites, conditional on a given site's location, and characterize an infinite-site limit and dimension-dependent moments. Their Theorems 1–3 concern a different asymptotic regime and do not imply the finite-two-site bisector density or its dimension-scaled Laplace imbalance law. Hoerrmann, Hug, Reitzner and Thäle (2014), *Poisson polyhedra in high dimensions*, study zero cells of Poisson hyperplane processes and stationary Poisson-Voronoi cells, not a uniform-ball partition by two sites. Geometric background on ordinary point-pair distances, spherical caps and stochastic integral geometry does not by itself give the stated two-site signed law. The novelty claim is restricted to the combined finite-dimensional density and its two total-variation limits, not to the elementary definition of a Voronoi bisector, the beta integral, or Scheffé's lemma.

## Limitations

The result is specific to a Euclidean ball and two volume-uniform independent sites. A fixed-dimension law for arbitrary convex bodies, inhomogeneous sites, or more than two sites is not established. No finite-dimensional quantitative total-variation convergence rate is asserted. A proof internal to the note checks the stated formulas, but no independent mathematical audit or exhaustive historical priority certification has been performed. Unindexed equivalent formulations in earlier geometrical probability literature remain possible.

## References

1. J. Hoerrmann, D. Hug, M. Reitzner and C. Thäle, *Poisson polyhedra in high dimensions*, initial arXiv submission 2014-03-31, https://arxiv.org/abs/1403.8017.
2. L. Devroye, L. Györfi, G. Lugosi and H. Walk, *On the measure of Voronoi cells*, arXiv:1512.04267v1, submitted 2015-12-14, https://arxiv.org/html/1512.04267v1.
3. R. Schneider and W. Weil, *Stochastic and Integral Geometry*, Springer, 2008; background only.
