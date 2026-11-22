# A sharp Cauchy–Gaussian boundary law for circular Poisson-to-von-Mises approximation

## Finding

Let \(P_r(\theta)=(1-r^2)/(1-2r\cos\theta+r^2)\), \(0<r<1\), and let
\(V_{\kappa,\phi}(\theta)=\exp(\kappa\cos(\theta-\phi))/I_0(\kappa)\), \(\kappa\geq0\), \(\phi\in\mathbb R/(2\pi\mathbb Z)\), be mean-one densities relative to Haar probability measure \(d\theta/(2\pi)\) on the circle. The modified Bessel functions are \(I_n\).

For every \(r\), the best squared \(L^2\) approximation error
\[
 E(r)=\min_{\kappa\geq0,\ \phi}\|P_r-V_{\kappa,\phi}\|_{L^2(d\theta/2\pi)}^2
\]
is attained with \(\kappa>0\) and uniquely aligned center \(\phi=0\) (modulo \(2\pi\)). No uniqueness of the minimizing concentration \(\kappa\) for fixed \(r\) is asserted.

Define \(x_*\) as the unique positive solution of
\[
 (1+2x^2)e^{x^2}\operatorname{erfc}(x)-\frac{2x}{\sqrt\pi}=\frac{1}{2\sqrt2},
\]
and put \(c_*=2x_*^2\) and
\[
 F_*=1+\sqrt{2\pi}x_*-4\sqrt\pi x_*e^{x_*^2}\operatorname{erfc}(x_*).
\]
Then \(x_*=0.508782734688\ldots\), \(c_*=0.517719742233\ldots\), and \(F_*=0.0705689390522\ldots\). **For every selection \(\kappa_r\) of global minimizing concentrations**, as \(r\uparrow1\),
\[
 (1-r)^2\kappa_r\longrightarrow c_*,\qquad
 (1-r)E(r)\longrightarrow F_*.
\]
The constants are universal and sharp for this specified fixed-target, free-von-Mises-scale problem.

Let \(\kappa_r^{\mathrm{mom}}\) be the unique parameter satisfying the first circular moment equation \(I_1(\kappa)/I_0(\kappa)=r\). Then
\[
 \kappa_r^{\mathrm{mom}}\sim\frac{1}{2(1-r)},\quad
 (1-r)\|P_r-V_{\kappa_r^{\mathrm{mom}},0}\|_2^2\longrightarrow1,
\]
so the asymptotic moment-matching squared error divided by the optimal squared error is \(1/F_*=14.1705403741\ldots\).

## Assumptions and scope

All parameter limits are real; \(r\uparrow1\) means \(0<r<1\) tends to one. The Poisson and von-Mises functions have integral one with respect to normalized Haar measure, rather than ordinary Lebesgue measure. There is no amplitude fitting: the densities themselves are compared. Their centers and the von-Mises concentration are permitted to vary, but the target Poisson radius is fixed. The asymptotic concerns the concentrated-kernel boundary, not a small-time stochastic limit or a claim of equality under a different divergence.

## Proof

**1. Alignment and finite-parameter attainment.** The Fourier coefficients of \(P_r\) are \(r^{|n|}\), and those of \(V_{\kappa,\phi}\) are \(I_{|n|}(\kappa)e^{-in\phi}/I_0(\kappa)\). For \(\kappa>0\), the coefficients \(I_n(\kappa)\) are strictly positive for \(n\geq1\). Thus the cross term \(\langle P_r,V_{\kappa,\phi}\rangle\) is strictly maximized at \(\phi=0\) modulo \(2\pi\), by the positive first harmonic and \(\cos(n\phi)\leq1\). The error is continuous for finite \(\kappa\), and tends to infinity as \(\kappa\to\infty\), because \(\|V_\kappa\|_2^2=I_0(2\kappa)/I_0(\kappa)^2\sim\sqrt{\pi\kappa}\) while \(\langle P_r,V_\kappa\rangle\leq\|P_r\|_\infty\) for fixed \(r\). The error derivative at \(\kappa=0\) is \(-2r<0\); hence every minimizer has positive concentration and aligned center.

**2. Boundary scaling.** Write \(\delta=1-r\). If \(\delta^2\kappa\to c\in(0,\infty)\) and \(\theta=\delta y\), the two scaled profiles converge in \(L^2(\mathbb R,dy/(2\pi))\), after extending by zero outside \((-\pi/\delta,\pi/\delta]\), to
\[
 p(y)=\frac{2}{1+y^2},\qquad
 v_c(y)=\sqrt{2\pi c}\,e^{-cy^2/2}.
\]
For the Poisson profile, pointwise convergence and the bound \(\delta P_r(\delta y)\leq C/(1+y^2)\) for \(r\) sufficiently close to one give dominated convergence. For von Mises, the standard \(I_0(\kappa)\sim e^\kappa/\sqrt{2\pi\kappa}\) and \(1-\cos\theta\geq2\theta^2/\pi^2\) for \(|\theta|\leq\pi\) give a Gaussian dominating function when \(c\) stays in a compact positive interval. These bounds also establish uniformity of this convergence on compact \(c\)-sets.

The identity \(\int_{\mathbb R} e^{-cy^2/2}(1+y^2)^{-1}dy=\pi e^{c/2}\operatorname{erfc}(\sqrt{c/2})\), together with \(\|p\|_2^2=1\) and \(\|v_c\|_2^2=\sqrt{\pi c}\), gives the limiting objective
\[
 F(c)=1+\sqrt{\pi c}-2\sqrt{2\pi c}\,e^{c/2}\operatorname{erfc}(\sqrt{c/2}).
\]
Here each squared norm and product is taken with \(dy/(2\pi)\). In particular, \(\delta\|P_r-V_{\kappa,0}\|_2^2\to F(c)\).

**3. Unique minimizer of the limiting profile.** Let \(x=\sqrt{c/2}\), \(Q(x)=e^{x^2}\operatorname{erfc}(x)\), and \(H(x)=(xQ(x))'=(1+2x^2)Q(x)-2x/\sqrt\pi\). Integration by parts yields
\[
 H(x)=\frac{1}{2\sqrt\pi}\int_0^\infty y^2e^{-xy-y^2/4}\,dy.
\]
Consequently \(H\) is continuous, strictly decreasing from \(H(0)=1\) to zero, and
\[
 \frac{d}{dx}F(2x^2)=\sqrt{2\pi}-4\sqrt\pi H(x).
\]
The derivative changes sign exactly once, from negative to positive, at \(H(x_*)=1/(2\sqrt2)\). Thus \(c_*=2x_*^2\) is the unique global minimizer of \(F\), with \(0<F_*<1\).

**4. Tightness of all finite-problem minimizers.** The finite circle identities are
\[
 \|P_r\|_2^2=\frac{1+r^2}{1-r^2},\qquad
 \|V_\kappa\|_2^2=\frac{I_0(2\kappa)}{I_0(\kappa)^2}.
\]
If \(\delta^2\kappa\to0\), then \(\delta\|V_\kappa\|_2^2\to0\) (using boundedness at finite \(\kappa\) and the Bessel asymptotic at infinity), and Cauchy–Schwarz forces \(\delta\langle P_r,V_\kappa\rangle\to0\). Hence the scaled error tends to one. If \(\delta^2\kappa\to\infty\), then \(\delta\|V_\kappa\|_2^2\to\infty\), whereas \(\delta\langle P_r,V_\kappa\rangle\leq\delta\|P_r\|_\infty=1+r\leq2\); the scaled error diverges. Since the trial choice \(\kappa=c_*/\delta^2\) has scaled error tending to \(F_*<1\), any sequence of true minimizers must have its rescaled concentrations in a compact subset of \((0,\infty)\). Compact-uniform convergence from step 2 and uniqueness from step 3 force all their limit points to equal \(c_*\), and also force the minimum scaled errors to \(F_*\).

**5. Contrast with first-moment matching.** The ratio \(I_1(\kappa)/I_0(\kappa)\) is strictly increasing from zero to one, by its interpretation as the expectation of \(\cos\theta\) under the von-Mises law and differentiation giving its positive variance. The standard large-\(\kappa\) expansion \(I_1(\kappa)/I_0(\kappa)=1-1/(2\kappa)+O(\kappa^{-2})\) gives \(\kappa_r^{\mathrm{mom}}\sim[2\delta]^{-1}\). Thus \(\delta^2\kappa_r^{\mathrm{mom}}\to0\), and step 4 proves the stated asymptotic error ratio.

## Verification

The standalone standard-library checker `verify.py` numerically solves the uniquely characterized critical equation, independently evaluates its positive Laplace-integral representation, and checks circle integrals and optimized concentrations for several finite radii. Run `python3 verify.py` from the directory containing this document. The checker verifies \(c_*=0.517719742233\ldots\), \(F_*=0.0705689390522\ldots\), and the approach to the predicted scaling. Its finite computations do not prove the continuum or all-radius statements, which are proved above.

## Relationship to prior work

Lewis (2021) compares circular probability distributions using Stein/Wasserstein bounds, including von Mises, wrapped normal, and wrapped Cauchy models; the comparison is not a best \(L^2\) density-fit asymptotic. Ameijeiras-Alonso (2024) studies optimal bandwidths for sample-based circular kernel density estimation, not the deterministic free-scale \(L^2\) projection of one concentrated density onto another. Hundrieser, Klatt and Munk (2021) study circular optimal-transport statistics, likewise using a different objective. A separate heat-to-Poisson \(L^2\) calibration result optimizes the Cauchy scale for a fixed Gaussian-type target. The present theorem fixes the Cauchy target and optimizes the Gaussian-type width; rescaling relates the two limiting errors only after a nonconstant scale factor, so the earlier optimizer and constant do not imply the present ones.

## Limitations

No uniqueness of the finite-radius optimal concentration is claimed. The theorem does not assert that von-Mises approximation is optimal among all positive circular kernels, and it says nothing about Wasserstein, KL, or total-variation minimizers. The asymptotic constants are quoted numerically only as evaluations of unique exact equations, not as independent certificates of priority. Novelty comparisons are best-knowledge, with the usual residual risk from unindexed or inaccessible older literature; independent verification has not been performed.

## References

1. A. Lewis, *Stein's Method for Probability Distributions on \(\mathbb S^1\)*, first posted 27 May 2021, https://arxiv.org/abs/2105.13199 .
2. J. Ameijeiras-Alonso, *A reliable data-based smoothing parameter selection method for circular kernel estimation*, Statistics and Computing 34 (2024), article 73, https://doi.org/10.1007/s11222-024-10384-x .
3. S. Hundrieser, M. Klatt, A. Munk, *The Statistics of Circular Optimal Transport*, first posted 29 March 2021, https://arxiv.org/abs/2103.15426 .
