# Curvature-controlled far-separation law for Gaussian Fock localization cross-traces

## Finding

Let \(A,B\) be two fixed smooth strictly convex planar observation windows. For large positive horizontal separation, their Gaussian Bargmann–Fock localization operators have a mixed trace depending to leading order only on the distance between the two facing horizontal support points, their transverse displacement, and the two local boundary curvatures:

\[
\operatorname{tr}(T_A T_{B+d e_1})
=\frac{e^{-L^2-\eta^2}}{4\pi\sqrt{\kappa_A\kappa_B}\,L^3}(1+o(1)),\quad d\to\infty.
\]

For disks of fixed radii \(R,S>0\), this specializes to

\[
\operatorname{tr}(T_{D_R}T_{D_S+d e_1})
=\frac{\sqrt{RS}}{4\pi}\frac{e^{-(d-R-S)^2}}{(d-R-S)^3}(1+o(1)).
\]

This quantitatively measures the cross-interaction or mixed energy of two spatially separated Gaussian localization measurements. Neither a spectral-gap estimate nor an operator-norm asymptotic is asserted.

## Assumptions and scope

Identify \(\mathbb R^2\simeq\mathbb C\). Work with the analytic Bargmann–Fock space \(\mathcal F^2\) with norm \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). Its normalized coherent kernel is \(k_z(w)=e^{w\bar z-|z|^2/2}\). For every bounded measurable \(E\), define the positive trace-class localization operator

\[
T_E f=\frac1\pi\int_E\langle f,k_z\rangle k_z\,dA(z).
\]

Assume \(A,B\) are nonempty bounded strictly convex domains, with \(C^3\) boundaries and strictly positive curvatures in neighborhoods of their unique support points \(a\in\partial A\) maximizing the first coordinate and \(b\in\partial B\) minimizing it. Define \(\kappa_A,\kappa_B>0\) as the unsigned Euclidean curvatures at these points, \(L=d+b_x-a_x\), \(\eta=b_y-a_y\). The result concerns fixed \(A,B\) and \(d\to+\infty\), so \(L>0\) eventually. No assumption on the relative vertical position is imposed. This is a pointwise asymptotic for each fixed pair, not uniform across degenerating curvatures or moving shapes.

## Proof

**1. Coherent-state trace identity.** Since \(\langle k_z,k_w\rangle\) has modulus \(e^{-|z-w|^2/2}\), Fubini and the finite trace-class integral of positive rank-one forms yield

\[
\operatorname{tr}(T_A T_{B+d e_1})
=\frac1{\pi^2}\int_A\int_{B+d e_1} e^{-|z-w|^2}\,dA(w)\,dA(z).
\]

For fixed bounded windows this is a finite, strictly positive real quantity.

**2. Localization at the two horizontal extreme points.** Horizontal separation of points in the two windows is at least \(L\). By strict convexity, the only pair of limiting points that realizes this minimum horizontal separation is \((a,b+d e_1)\). For any fixed sufficiently small neighborhoods \(U\) of \(a\) and \(V\) of \(b\), compactness and uniqueness of the extremes give a \(\delta>0\) such that for points outside \(U\times(V+d e_1)\), horizontal separation is at least \(L+\delta\). Their contribution is bounded by a fixed area constant times \(e^{-(L+\delta)^2}\), hence it is \(o(e^{-L^2}L^{-3})\). This uses compact closures; boundary sets of zero area cause no issue.

**3. Boundary normal coordinates.** Near \(a\), let \(s=y-a_y\). The right boundary is the graph \(x=a_x-f_A(s)\), where \(f_A(0)=f_A'(0)=0\) and \(f_A(s)=\kappa_A s^2/2+O(|s|^3)\). Interior points are \(z=(a_x-f_A(s)-u,a_y+s)\), \(u\ge0\). Near \(b+d e_1\), set \(t=y-b_y\). The left boundary is \(x=d+b_x+f_B(t)\), \(f_B(t)=\kappa_B t^2/2+O(|t|^3)\); interior points are \(w=(d+b_x+f_B(t)+v,b_y+t)\), \(v\ge0\). The coordinate Jacobians are exactly one. Shrinking these neighborhoods makes \(f_A(s)\ge c_As^2\) and \(f_B(t)\ge c_Bt^2\), for positive constants.

The exact squared separation in these coordinates is

\[
|w-z|^2=(L+u+v+f_A(s)+f_B(t))^2+(\eta+t-s)^2.
\]

**4. Four-variable Laplace scaling.** Substitute \(u=U/L\), \(v=V/L\), \(s=S/\sqrt L\), \(t=T/\sqrt L\). The Jacobian is \(L^{-3}\). Pointwise for fixed nonnegative \(U,V\) and real \(S,T\),

\[
|w-z|^2-L^2\longrightarrow
2U+2V+\kappa_A S^2+\kappa_B T^2+\eta^2.
\]

Moreover, since \(u,v\ge0\), \(f_A,f_B\ge0\), and the transverse square is nonnegative, the rescaled exponential is bounded by \(e^{-2U-2V-2c_AS^2-2c_BT^2}\), an integrable majorant independent of \(d\). Extend the localized domain indicator by zero to the full product \(\mathbb R_+^2\times\mathbb R^2\), and apply dominated convergence. Thus

\[
\lim_{d\to\infty}e^{L^2}L^3\operatorname{tr}(T_A T_{B+d e_1})
=\frac{e^{-\eta^2}}{\pi^2}
\left(\int_0^\infty e^{-2U}dU\right)^2
\int_{\mathbb R}e^{-\kappa_AS^2}dS
\int_{\mathbb R}e^{-\kappa_BT^2}dT
=\frac{e^{-\eta^2}}{4\pi\sqrt{\kappa_A\kappa_B}}.
\]

The exponentially small contribution outside the local support neighborhoods was removed in step 2. This completes the proof.

**5. Disks.** For \(A=D_R\), \(B=D_S\) centered at the origin, \(a=(R,0)\), \(b=(-S,0)\), \(L=d-R-S\), \(\eta=0\), \(\kappa_A=1/R\), and \(\kappa_B=1/S\). Substitute into the general formula.

## Verification

The standalone reproducibility script `check_disk_asymptotic.py` computes the disk mixed trace independently through the radial overlap area of two disks and a scaled modified-Bessel integral, avoiding direct underflow. It checks both equal and unequal radii and a fixed transverse offset. In the equal-radius case with \(R=S=1\), the ratios of the exact numerical integral to the stated asymptotic for \(L=5,10,20,40,80\) are approximately \(0.7223,0.8599,0.9304,0.9654,0.9828\); they tend to one. For the unequal radii \(R=0.6\), \(S=1.3\), the analogous ratios are approximately \(0.7144,0.8560,0.9286,0.9645,0.9823\). With transverse offset \(\eta=2.4\), the ratios at \(L=40,80,160\) are approximately \(1.2458,1.1213,1.0602\). These finite examples verify normalization and scale, not the quantified infinite limit. The infinite-domain assertion is proved by dominated convergence in the preceding steps.

To reproduce: install Python 3 with SciPy, then run `python check_disk_asymptotic.py`. For the analytic steps, the Fock coherent-state overlap and two Gaussian integrals suffice; no external computation is required.

## Relationship to prior work

Nicola and Riccardi (arXiv:2401.04659, first public 2024-01-09) study quantitative Hilbert–Schmidt isoperimetry for Gaussian localization, using a self-overlap integral of the same form when both windows coincide. The present statement instead treats two different *fixed* convex windows receding from one another, resolving their exponentially small cross-trace, third-power prefactor, transverse displacement and curvature coefficient. Feichtinger, Halvdansson and Luef (arXiv:2308.04985, first public 2023-08-09) supply general measure–operator convolution and mixed-state Gabor-multiplier machinery, not this specific far-separation asymptotic. Older localization-product frameworks may encompass the trace identity as a starting point but do not by that identity alone imply the sharp local-curvature coefficient. This is a best-knowledge comparison, not an exhaustive historical-priority certification.

## Limitations

The result requires fixed bounded convex windows with nondegenerate curvature at their horizontal extreme points. Flat facing facets, corners, vanishing curvature, moving domains, or windows whose geometry changes with separation can have different polynomial powers and constants. The result concerns the mixed trace rather than singular values, principal eigenvalues, operator norms, stochastic fluctuation laws, or nonlinear stability. The method uses classical Laplace concentration; originality is claimed for this exact combined localization statement, not for the Laplace method or the coherent-state trace identity.

## References

- F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert–Schmidt norm of localization operators*, first public 9 January 2024, arXiv:2401.04659, https://arxiv.org/abs/2401.04659 .
- H. Feichtinger, E. Halvdansson and F. Luef, *Measure-operator convolutions and applications to mixed-state Gabor multipliers*, first public 9 August 2023, arXiv:2308.04985, https://arxiv.org/abs/2308.04985 .
- E. Cordero and K. Gröchenig, *Time-frequency analysis of localization operators*, J. Functional Analysis (2003), https://doi.org/10.1016/S0022-1236(03)00166-6 .
