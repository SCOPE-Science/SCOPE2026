# Three sharp aperture regimes for coordinatewise stability of Euclidean circular-cone projections

## Finding
For every real \(\kappa>0\) and integer \(d\ge2\), define the closed Euclidean circular cone
\[
K_{\kappa,d}=\{(t,x)\in\mathbb R\times\mathbb R^d:t\ge\kappa\|x\|_2\}
\]
and let \(Q_{\kappa,d}\) be its **Euclidean** nearest-point projector. Its sharp Lipschitz modulus in the coordinate maximum norm is
\[
L_{\kappa,d}=\sup_{z\ne w}\frac{\|Q_{\kappa,d}(z)-Q_{\kappa,d}(w)\|_\infty}{\|z-w\|_\infty}
=\max\{1,A_{\kappa,d},B^-_{\kappa,d},B^+_{\kappa,d}\},
\]
where
\[
\begin{aligned}
A_{\kappa,d}&=\frac{\kappa^2+\kappa\sqrt d}{1+\kappa^2},\\
B^-_{\kappa,d}&=\frac1{1+\kappa^2}\max_{0\le a\le1}\bigl(\kappa a+a^2+\sqrt{d-1}\,a\sqrt{1-a^2}\bigr),\\
B^+_{\kappa,d}&=1+\frac1{1+\kappa^2}\max_{0\le a\le1}\bigl(\kappa a-\kappa^2a^2+\kappa^2\sqrt{d-1}\,a\sqrt{1-a^2}\bigr).
\end{aligned}
\]
All scalar maxima exist. The three nontrivial branches come respectively from an axial output, a spatial output on the polar side of the cone's smooth projection region, and a spatial output on the cone side.

In addition, at every fixed aperture \(\kappa>0\),
\[
\lim_{d\to\infty}\frac{L_{\kappa,d}}{\sqrt d}
=\frac{\max\{1/2,\kappa,\kappa^2/2\}}{1+\kappa^2}.
\]
For sufficiently large spatial dimensions, the uniquely largest of the three row-type branches is \(B^-\) when \(0<\kappa<1/2\), \(A\) when \(1/2<\kappa<2\), and \(B^+\) when \(\kappa>2\). The aperture values \(1/2\) and \(2\) are sharp phase boundaries for the leading growth; this statement does not resolve finite-dimensional branch ties at either boundary.

## Assumptions and scope
All vectors and matrices are real, \(d\ge2\) counts **spatial** coordinates (ambient dimension \(d+1\)), and \(\kappa>0\). The approximation is in the Euclidean metric; only the **measurement of perturbations** uses \(\ell_\infty\). Changing the cone aperture is not a Euclidean isometry, and its resulting projector is not a simple coordinate conjugate of standard Lorentz-cone projection. The result is an exact supremum of two-point quotients; local derivatives yield sharpness without requiring an extremizing distinct pair.

## Proof
**1. Explicit Euclidean projector.** Put \(r=\|x\|_2\). Orthogonal minimization in the two-dimensional meridian plane gives
\[
Q_{\kappa,d}(t,x)=\begin{cases}
(t,x),&t\ge\kappa r,\\
0,&t\le-r/\kappa,\\
(\kappa\rho,\rho x/r),&-r/\kappa<t<\kappa r,
\end{cases}\qquad
\rho=\frac{\kappa t+r}{1+\kappa^2}.
\]
For the middle case \(r>0\). Indeed, the nearest candidate on the slanted boundary \(s=\kappa v\) minimizes \((t-\kappa v)^2+(r-v)^2\) over \(v\ge0\); the unconstrained minimizer is \(\rho\), and the two remaining cases are respectively a feasible interior point and a nonpositive boundary minimizer at the apex. This also agrees with the Hilbert projection variational inequality, so the formula is globally valid.

**2. Jacobian and reduction to two faces.** Within the open middle region write \(u=x/r\), so \(\|u\|_2=1\), and
\[
c=\frac{1+\kappa t/r}{1+\kappa^2}\in(0,1).
\]
Direct differentiation gives
\[
DQ_{\kappa,d}(t,x)=
\begin{pmatrix}
\dfrac{\kappa^2}{1+\kappa^2}&\dfrac{\kappa u^{\mathsf T}}{1+\kappa^2}\\[4pt]
\dfrac{\kappa u}{1+\kappa^2}&cI_d+\bigl(\dfrac1{1+\kappa^2}-c\bigr)uu^{\mathsf T}
\end{pmatrix}.
\]
Every matrix entry is affine in \(c\). Because the induced \(\ell_\infty\)-operator norm is a maximum of absolute row sums and therefore convex in the entries, the supremum over \(0<c<1\) equals the larger of the endpoint limits \(c=0\) and \(c=1\). Each endpoint is approachable inside the middle region with any fixed unit \(u\). The derivatives in the other two open regions are respectively the identity and zero.

To pass from derivatives to a global Lipschitz inequality, note that Euclidean metric projection is globally Euclidean nonexpansive, hence locally absolutely continuous on every line segment. For a generic segment the two cone-boundary crossing equations are not identically satisfied, so the segment meets the two switching hypersurfaces only at finitely many parameters, and the ordinary chain rule and integration bound the output difference by the largest induced row norm times the input \(\ell_\infty\) length. Arbitrary segments follow by approximating their endpoints with generic segments and using continuity. Conversely, a Jacobian in any open middle-region point is the first-order limit of difference quotients, and a sign vector of any maximizing row attains that row's induced norm infinitesimally. Thus the global modulus is exactly the largest of the identity norm and the middle-region supremum.

**3. Exact row optimization.** The top (axial) absolute row sum is
\[
\frac{\kappa^2+\kappa\|u\|_1}{1+\kappa^2},
\]
whose sharp supremum is \(A_{\kappa,d}\) by Cauchy--Schwarz and an equal-magnitude spatial vector. For a spatial row \(i\), let \(a=|u_i|\), \(S=\sum_{j\ne i}|u_j|\). At the two endpoint faces its absolute row sums are
\[
R_i(0)=\frac{\kappa a+a^2+aS}{1+\kappa^2},\qquad
R_i(1)=1+\frac{\kappa a-\kappa^2a^2+\kappa^2aS}{1+\kappa^2}.
\]
For each \(a\in[0,1]\), Cauchy--Schwarz yields \(S\le\sqrt{d-1}\sqrt{1-a^2}\), with equality for equal magnitudes on the other \(d-1\) coordinates. The coefficients of \(S\) are nonnegative, so maximizing over \(a\) proves the exact \(B^-\) and \(B^+\) formulas. All upper bounds are sharp derivative suprema by the preceding paragraph.

**4. Three asymptotic aperture regimes.** The elementary exact maximum
\[
\max_{0\le a\le1}a\sqrt{1-a^2}=1/2
\]
occurs at \(a=1/\sqrt2\). The remaining terms \(\kappa a+a^2\) and \(\kappa a-\kappa^2a^2\) are bounded uniformly in \(d\), and \(\sqrt{d-1}=\sqrt d+O(d^{-1/2})\). Consequently, as \(d\to\infty\) at each fixed \(\kappa\),
\[
A_{\kappa,d}=\frac{\kappa}{1+\kappa^2}\sqrt d+O_\kappa(1),\quad
B^-_{\kappa,d}=\frac1{2(1+\kappa^2)}\sqrt d+O_\kappa(1),\quad
B^+_{\kappa,d}=\frac{\kappa^2}{2(1+\kappa^2)}\sqrt d+O_\kappa(1).
\]
Taking the maximum proves the claimed limit. Comparing \(1/2\), \(\kappa\), and \(\kappa^2/2\) gives the three open aperture ranges with strict leading-order gaps, and these gaps dominate every \(O_\kappa(1)\) remainder once \(d\) is large. This proves eventual unique dominance of the stated row type. No assertion is made about which branch wins at either equality aperture. \(\square\)

## Verification
Run `python3 verify.py` using only the Python standard library. The script re-evaluates the exact Euclidean projector and its middle-region Jacobian at 5,250 deterministic sampled configurations, checks the induced row-sum bound and first-order differences, and checks all three distinct eventual active branch types and convergence toward the analytically obtained growth coefficient. It also confirms the known \(\kappa=1,d=4\) value. These are finite numerical consistency tests: the global optimization and infinite-dimensional-limit assertions follow from the preceding analytical proof, not sampling or extrapolation.

## Relationship to prior work
The standard \(\kappa=1\) coordinate-maximum Lipschitz classification was previously established in *Sharp coordinatewise Lipschitz transition for Euclidean Lorentz-cone projection* (2026 research record); our formula recovers that case, but that statement expressly excludes changes of cone aperture. The previously published *Exact planar stability and nonexpansivity rigidity for \(\ell_p\) projections onto scaled Lorentz cones* treats **nearest points measured in the \(\ell_p\) ambient metric**, rather than Euclidean nearest points evaluated in the coordinate maximum metric; its planar result and higher-dimensional qualitative nonexpansivity statements do not imply the present precise all-dimensional modulus or the three aperture thresholds. Németh (2012) and Németh--Zhang (2014) investigate cone orders and Hilbert projections, and Bello Cruz et al. (2016) give generalized Jacobian formulas for the standard second-order cone; their inspected results do not establish this variable-aperture \(\ell_\infty\)-sensitivity classification. This comparison cannot exclude an independently derived but unindexed equivalent result.

## Limitations
The result applies only to real finite-dimensional Euclidean projections on rotationally symmetric circular cones with scalar aperture and \(d\ge2\), measured in the coordinate maximum norm. It does not give an elementary closed expression for the one-variable maxima at every fixed \((\kappa,d)\), nor settle the finite-dimensional winning branch at the two limiting transition apertures. It does not cover general noncircular cones, arbitrary coordinate weights, or non-Euclidean nearest-point maps. Earlier conic-programming sensitivity work not fully accessible may contain equivalent special cases; historical novelty remains provisional pending specialist review.

## References
1. S. Z. Németh, *A duality between metric projection onto a convex cone and metric projection onto dual in Hilbert spaces*, arXiv:1212.5438, first posted 2012-12-21, https://arxiv.org/abs/1212.5438 .
2. S. Z. Németh and G. Zhang, *Extended Lorentz cones and mixed complementarity problems*, arXiv:1405.7835, first posted 2014-05-30, https://arxiv.org/abs/1405.7835 .
3. J. Y. Bello Cruz, O. P. Ferreira, S. Z. Németh, and L. F. Prudente, *A semismooth Newton method for projection equations and linear complementarity problems with respect to second-order cone*, arXiv:1605.09463, first posted 2016-05-31, https://arxiv.org/abs/1605.09463 .
4. *Sharp coordinatewise Lipschitz transition for Euclidean Lorentz-cone projection*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-coordinatewise-lipschitz-transition-for-euclidean-lorentz--2d1b9aa4230e .
5. *Exact planar stability and nonexpansivity rigidity for \(\ell_p\) projections onto scaled Lorentz cones*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-planar-stability-and-nonexpansivity-rigidity-for-ell-p-pro--fbfc40872e9c .
