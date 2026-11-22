# Noisy two-knot observation of planar Brownian-bridge stochastic area has a unique nonmonotone spacing law

## Finding
Let \(B=(B^1,B^2)\) be a standard planar Brownian bridge on \([0,1]\), with independent coordinates and \(B_0=B_1=0\). Define the *doubled signed stochastic area*
\[
 A=\int_0^1 B_t^1\,\mathrm d B_t^2-\int_0^1 B_t^2\,\mathrm d B_t^1,
\]
with Itô integration (equivalently Stratonovich integration, since the cross-variation is zero). For chosen \(0\le s\le t\le1\), observe \(Y_s=B_s+\varepsilon_s\) and \(Y_t=B_t+\varepsilon_t\), where the four scalar errors are independent \(N(0,\eta)\), independent of the bridge, and \(\eta\ge0\). Estimate \(A\) by its exact conditional expectation and minimize its unconditional squared risk.

For every \(\eta\ge0\), the unique ordered globally optimal design is \((s,t)=(x_\eta,1-x_\eta)\), with \(0<x_\eta<1/2\). At \(\eta=0\), \(x_0=1/3\). At \(\eta>0\), \(x_\eta\) is the unique root in \((0,1/2)\) of
\[
 2(1-3x)\eta^2+x(3-12x+8x^2)\eta+x^2(1-2x)(1-3x)=0.
\]
Writing \(x_c\) for the unique real root of \(16x^3-8x^2+4x-1=0\), the outer gap \(x_\eta\) decreases strictly from \(1/3\) to
\[
 x_c=0.32389943563052119274\ldots
\]
and increases strictly back to \(1/3\) as \(\eta\) tends to infinity. Its unique minimum occurs at
\[
 \eta_c=-\frac{x_c(3-12x_c+8x_c^2)}{4(1-3x_c)}
 =0.13592225317301909039\ldots.
\]
Thus the optimal pair moves strictly outward from the noiseless trisection points for every finite positive noise level, yet returns toward those points at high noise. In the conventional half-area normalization, both risk and variance reductions are divided by four; the optimal times do not change.

For \(s<t\), put \(D=s(t-s)(1-t)\), \(T=s(1-s)+t(1-t)\). The complete risk formula is
\[
 R_\eta(s,t)=\frac13-\frac{2D^2}{D+\eta T+\eta^2},
\]
with the continuous boundary conventions (at \(\eta=0\), if the Gram matrix is singular, the captured information is zero). The conditional-mean estimator itself is
\[
 \widehat A=\frac{D}{D+\eta T+\eta^2}
 (Y_s^1Y_t^2-Y_s^2Y_t^1).
\]

## Assumptions and scope
The two time locations are deterministic and fixed before the path is seen. Both spatial coordinates are measured at both times; all four scalar observation errors have common variance \(\eta\). The two-coordinate Brownian bridge is standard with unit diffusion, fixed zero endpoints and independent axes. The estimator is unrestricted among measurable functions of the four observations, because a conditional expectation minimizes mean squared error. The claim does not cover adaptive times, unequal or correlated noise, additional samples, or general Lévy-driven paths.

## Proof
**1. Area projection and exact risk.** Condition on the two noiseless knots \(B_s,B_t\). On each of the three intervening intervals, the conditional mean path is the straight segment between its known endpoints and the residual is an independent zero-endpoint Gaussian bridge in each spatial coordinate. Mixed terms and the residual antisymmetric Itô area have conditional mean zero. The oriented polygon through \(0,B_s,B_t,0\) therefore has conditional area
\[
 \mathbb E[A\mid B_s,B_t]=B_s^1B_t^2-B_s^2B_t^1.
\]
The covariance matrix for either spatial coordinate at the knots is
\[
 K=\begin{pmatrix}s(1-s)&s(1-t)\\s(1-t)&t(1-t)\end{pmatrix},
 \qquad \det K=D,\quad\operatorname{tr}K=T.
\]
For noisy observations its covariance is \(C=K+\eta I_2\). Gaussian regression gives conditional knot means \(KC^{-1}(Y_s^i,Y_t^i)^\mathsf T\). As the spatial coordinate systems are independent, taking the conditional expectation of their cross-product gives the displayed estimator with coefficient \(\det(KC^{-1})=D/\det C\). The variance of the cross-product of two independent centered Gaussian coordinate pairs with covariance \(C\) is \(2\det C\). Hence \(\operatorname{Var}(\widehat A)=2D^2/\det C\). The bridge semimartingale equation \(\mathrm dB_t=\mathrm dW_t-B_t(1-t)^{-1}\mathrm dt\) cancels its drifts in the antisymmetric area. Itô isometry yields \(\mathbb E A^2=2\int_0^1t(1-t)\,\mathrm dt=1/3\). Orthogonal projection in \(L^2\) proves the risk formula. At coincident or endpoint knots, one observation direction is deterministic or duplicated and supplies no antisymmetric area information, consistently giving reduction zero.

**2. Global centering, including asymmetric designs.** Introduce positive gaps \(a=s\), \(b=t-s\), \(c=1-t\) with \(a+b+c=1\). Let \(u=a+c\) and \(v=ac\), so \(b=1-u\), \(D=v(1-u)\) and \(T=u(1-u)+2v\). For every fixed \(u\in(0,1)\), the information reduction apart from the factor two is
\[
 F(u,v)=\frac{v^2(1-u)^2}{(1-u+2\eta)v+\eta u(1-u)+\eta^2}.
\]
It is strictly increasing in \(v>0\). The unique largest feasible \(v\) is \(u^2/4\), attained precisely when \(a=c\). No asymmetric design can be globally optimal. Write \(s=x,t=1-x\), with \(0<x<1/2\); then \(D=x^2(1-2x)\), \(T=2x(1-x)\).

**3. Uniqueness for each noise variance.** Maximizing \(F_\eta(x)=D^2/(D+\eta T+\eta^2)\) is equivalent, under the bijection \(y=x/(1-2x)>0\), to maximizing \(y^4/Q_\eta(y)\), where
\[
 Q_\eta(y)=(1+2y)^3\left[y^2+2\eta y(1+y)(1+2y)+\eta^2(1+2y)^3\right].
\]
For \(\eta>0\), all seven coefficients \(q_0,\ldots,q_6\) of this degree-six polynomial are strictly positive. The stationary polynomial \(4Q_\eta-yQ_\eta'\) has positive coefficients in degrees \(0,1,2,3\), zero in degree \(4\), and negative coefficients in degrees \(5,6\). By Descartes' rule it has exactly one positive root (existence follows from the opposite end signs). The objective vanishes at both ends, so this root is the unique maximum. For \(\eta=0\), \(F_0=D\) is uniquely maximized at \(x=1/3\). Direct differentiation for \(\eta>0\) gives the claimed stationary polynomial. At any optimum \(x<1/3\), since at and above \(1/3\) both \(D'\le0\) and \(T'>0\), making \(F'_\eta<0\).

**4. Exact nonmonotonicity and unique turning point.** The stationary polynomial is quadratic in \(\eta\), with positive leading and constant coefficients when \(0<x<1/3\). Its coefficient of \(\eta\) is negative only when
\[
 x>x_b=\frac{3-\sqrt3}{4}.
\]
Within \((x_b,1/3)\) its discriminant, after removing the positive factor \(x^2\), is
\[
 (3-12x+8x^2)^2-8(1-3x)^2(1-2x)
 =(4x-1)(16x^3-8x^2+4x-1).
\]
The cubic on the right is strictly increasing on the whole real line because its derivative \(48x^2-16x+4\) is everywhere positive. Its unique real zero \(x_c\) lies between \(x_b\) and \(1/3\). The discriminant is negative below \(x_c\), and it vanishes precisely at \(x_c\) for the single positive value \(\eta_c\) displayed above. Thus no positive-noise design has \(x<x_c\); \(x_c\) is attained at exactly one \(\eta\). The unique-optimizer function is continuous and differentiable by its nondegenerate one-dimensional maximum. Taking \(\eta\downarrow0\) and \(\eta\to\infty\) in the objective gives \(x\to1/3\) at each end. Its only possible stationary point as a function of \(\eta\) is the discriminant-zero pair, so it strictly decreases and then strictly increases as claimed.

## Verification
The accompanying `check.py` symbolically checks the rational derivative, covariance determinant, stationary discriminant and transformed polynomial, and numerically locates \(x_c\), \(\eta_c\). It also performs 7,000 fixed-seed supplementary global comparisons over random time pairs, at seven noise levels. These numerical comparisons are diagnostic, not the proof of global optimality; steps 1–4 are the proof. Run `python check.py` with SymPy and mpmath installed.

## Relationship to prior work
Foster and Habermann (arXiv:2102.10095, publicly posted 19 February 2021), Sections 1 and 5 and the appendix, study Fourier and polynomial Brownian-bridge expansions and their Lévy-area approximation errors, including comparison with path-based schemes; they do not formulate a two-noisy-time placement optimum. Kastner and Rößler (2022), especially Sections 2–5, compare Fourier/Milstein/Wiktorsson/Mrongowius–Rößler iterated-integral algorithms and computational costs, rather than where two noisy planar path observations should be located. Jelinčič et al. (arXiv:2308.02452) investigate generative Lévy-area sampling conditional on increments, not this observation-design criterion; the abstract and available opening material were inspected, but not its entire manuscript. The classical piecewise-linear conditional-area identity is used as a premise here, not claimed as new. The specific noise-dependent, globally optimal two-knot spacing law and its unique turning point are the contribution evaluated in this note.

## Limitations
The independent same-model correctness and literature assessment is not a publication-priority certification; mathematically equivalent unindexed results may exist. The change in optimal spacing is modest: the nearest-to-endpoint outer gap is about \(0.323899\) instead of \(1/3\), and the relative captured-information gain over fixed trisection at the turning noise level is approximately \(0.00365715\). The finding identifies optimal sampling times, not an improved general strong SDE convergence rate, or the best approximation among arbitrary Gaussian linear observations. The zero-noise singular boundary cases follow by direct conditioning, not by substituting \(0/0\) in a formula.

## References
- James Foster and Karen Habermann, *Brownian bridge expansions for Lévy area approximations and particular values of the Riemann zeta function*, arXiv:2102.10095 (first public 2021-02-19), https://arxiv.org/abs/2102.10095 ; Cambridge Core full text https://doi.org/10.1017/S096354832200030X .
- Felix Kastner and Andreas Rößler, *An analysis of approximation algorithms for iterated stochastic integrals and a Julia and Matlab simulation toolbox*, *Numerical Algorithms* (first published 2022-12-12), https://doi.org/10.1007/s11075-022-01401-z .
- Andraž Jelinčič, Jiajie Tao, William F. Turner, Thomas Cass, James Foster and Hao Ni, *Generative Modelling of Lévy Area for High Order SDE Simulation*, arXiv:2308.02452 (2023-08-04), https://arxiv.org/abs/2308.02452 .
