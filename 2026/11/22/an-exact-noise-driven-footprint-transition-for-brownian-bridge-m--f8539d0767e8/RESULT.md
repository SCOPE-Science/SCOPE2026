# An exact noise-driven footprint transition for Brownian-bridge moment sensing

## Finding
Fix a window width \(0<h<1\) and a measurement-noise variance \(\eta\geq0\). Let \(B\) be the standard Brownian bridge on \([0,1]\), and estimate its signed first polynomial moment
\[
J=\int_0^1(2s-1)B_s\,ds
\]
from exactly one noisy, normalized interval average
\[
Y_c=\frac1h\int_{c-h/2}^{c+h/2}B_s\,ds+\varepsilon,
\qquad c\in[h/2,1-h/2],\qquad \varepsilon\sim N(0,\eta),
\]
with independent noise. Under squared loss the Bayes estimator is the conditional mean. Write
\[
L_h=\frac{h(2-h)}4,\qquad
S(h,\eta)=12\eta(1-2h)+h(3h^2-5h+1).
\]
**Complete optimal-placement law.** If \(S(h,\eta)\leq0\), the complete set of globally optimal window centers is exactly \(\{h/2,1-h/2\}\): every optimal window touches an endpoint. If \(S(h,\eta)>0\), there is a unique \(z_*\in(L_h,1/4)\) solving
\[
N_{h,\eta}(z_*)=0,
\quad N_{h,\eta}(z)=8(1-4z)(z+\eta-h/6)
-4(4z-h^2)(z+\eta-h/6)-(1-4z)(4z-h^2),
\]
and the complete set of global optima is the reflected pair
\[
c_\pm=\frac{1\pm\sqrt{1-4z_*}}2.
\]
The transition has the sharp geometry
\[
h_0=\frac{5-\sqrt{13}}6=0.232408120756\ldots .
\]
For \(0<h<h_0\), the optimum is strictly interior for all \(\eta\geq0\). For \(h_0<h<1/2\), the optimal windows touch the boundary precisely when
\[
\eta\leq\eta_c(h):=\frac{h(5h-3h^2-1)}{12(1-2h)}.
\]
At \(h=h_0\), only zero noise gives boundary windows. For \(1/2\leq h<1\), boundary windows are optimal for all noise levels. Whenever the optimal center is interior it moves strictly toward the midpoint as \(\eta\) increases. At large noise its left-hand center approaches
\[
c_\infty(h)=\frac{1-\sqrt{(1-h^2)/3}}2\quad(0<h<1/2);
\]
for \(h\geq1/2\), it remains at \(h/2\).

The transition is not merely a local stationarity statement: it compares all admissible windows, including both endpoint-touching placements. For instance, with \(h=0.25\) and \(\eta=0.2\), the left optimal center is approximately \(0.1968174683\), yielding \(27.69\%\) more posterior variance reduction than an endpoint-touching window. The result is an *exact global one-measurement design theorem*, not a multiple-sensor or adaptive-design theorem.

## Assumptions and scope
The bridge has covariance \(K(s,t)=\min(s,t)-st\). The target \(J\) is a real, centered, square-integrable linear functional of the entire path. The observation is the **average**, not the unnormalized integral, over a contiguous window of known fixed width \(h\); a complete window must remain inside \([0,1]\). The additive independent Gaussian noise has known variance \(\eta\geq0\). Width is not optimized and noise does not change with window location or width. The risk is the unconditional expected squared error of the optimal conditional-mean estimator, equivalently the Gaussian posterior variance. The complete set of optimizers is stated for each fixed \((h,\eta)\) in the indicated domain. No approximation or grid discretization is involved in the theorem.

## Proof
**1. Exact prior covariance and risk.** By Fubini and the bridge covariance, the cross-covariance function \(g(t)=\operatorname{Cov}(J,B_t)\) solves the Dirichlet Green equation \(-g''(t)=2t-1\), \(g(0)=g(1)=0\), giving
\[
g(t)=\frac{t(1-t)(2t-1)}6,\qquad \operatorname{Var}(J)=\int_0^1(2t-1)g(t)\,dt=\frac1{180}.
\]
For \(a=c-h/2\) and \(b=c+h/2\), integration of the cubic \(g\) over \([a,b]\) yields
\[
G_h(c):=\operatorname{Cov}(J,Y_c)
=\frac{(2c-1)(4c(1-c)-h^2)}{24}.
\]
Writing \(B_t=W_t-tW_1\) for a standard Brownian motion \(W\), the variance of its interval average is \(a+h/3-c^2=c(1-c)-h/6\). Therefore
\[
D_h(c):=\operatorname{Var}(Y_c)=c(1-c)-h/6+\eta>0.
\]
The strict inequality follows because a positive-length interior Brownian-bridge integral has positive variance; it also holds for boundary-touching windows, even with \(\eta=0\). Gaussian conditioning gives the exact estimator and risk
\[
\widehat J_c=\frac{G_h(c)}{D_h(c)}Y_c,\qquad
R_h(c)=\frac1{180}-\frac{(2c-1)^2(4c(1-c)-h^2)^2}
{576[c(1-c)-h/6+\eta]}.
\]

**2. One-variable global reduction.** By reflection, it suffices to optimize on \(c\in[h/2,1/2]\). Set \(z=c(1-c)\), which increases strictly on that half-interval from \(L_h=h(2-h)/4\) to \(1/4\). Since \(4z-h^2\geq2h(1-h)>0\), minimizing risk is equivalent to maximizing
\[
F_{h,\eta}(z)=\frac{(1-4z)(4z-h^2)^2}{z+\eta-h/6},\qquad L_h\leq z\leq1/4.
\]
The denominator is strictly positive. Direct differentiation shows
\[
F'_{h,\eta}(z)=\frac{(4z-h^2)N_{h,\eta}(z)}{(z+\eta-h/6)^2}.
\]
The derivative-sign polynomial has \(N''_{h,\eta}(z)=-64\), and satisfies
\[
N_{h,\eta}(L_h)=\frac{2(1-h)}3S(h,\eta),
\quad N_{h,\eta}(1/4)=-\frac{(1-h^2)(12\eta+3-2h)}3<0,
\]
\[
N'_{h,\eta}(L_h)=4(1-6h+4h^2-12\eta).
\]
If \(S(h,\eta)>0\), the strictly concave quadratic \(N\) starts positive and ends negative, so it has exactly one zero in \((L_h,1/4)\), positive before and negative afterward. Hence \(F\) has exactly one global maximum in the open interval, with its two reflected center realizations. If \(S(h,\eta)\leq0\), then necessarily \(h\geq h_0=(5-\sqrt{13})/6\). On \([h_0,1)\) one has \(4h^2-6h+1<0\), hence \(N'(L_h)<0\) and, since \(N''=-64\), the polynomial is strictly decreasing on the entire admissible interval. Thus \(N(z)<0\) for every \(z>L_h\). The sole maximizer in \(z\) is \(L_h\), corresponding to the two endpoint-touching windows. This proves all global and equality cases, including the threshold.

**3. Geometry and noise monotonicity.** The polynomial \(3h^2-5h+1\) changes sign inside \((0,1)\) only at \(h_0\). For \(h\geq1/2\), both terms of \(S(h,\eta)\) are nonpositive and the second is strictly negative. For \(h_0<h<1/2\), solving \(S=0\) gives precisely \(\eta_c(h)>0\), with the claimed strict inequalities. At an interior optimum, the logarithmic derivative of \(F\) is
\[
\partial_z\log F=-\frac4{1-4z}+\frac8{4z-h^2}-\frac1{z+\eta-h/6}.
\]
Its derivative with respect to \(\eta\) is strictly positive. At the unique interior maximum, its derivative with respect to \(z\) is strictly negative, because \(N\) crosses from positive to negative and the crossing is simple. Implicit differentiation therefore gives \(dz_*/d\eta>0\), and hence the left center moves strictly toward \(1/2\). If \(h_0<h<1/2\), it remains at the boundary until \(\eta_c(h)\), then moves inward. At the threshold the onset is linear:
\[
c_-(h,\eta)-h/2=
\frac{2(1-2h)}{6h-4h^2-1+12\eta_c(h)}
(\eta-\eta_c(h))+O((\eta-\eta_c(h))^2)
\]
for \(\eta\downarrow\eta_c(h)\) from above; the coefficient is positive. This follows from the simple root \(N(L_h,\eta_c)=0\) and the nonzero derivative \(N_z(L_h,\eta_c)<0\).

**4. Large-noise limit.** Dividing \(F_{h,\eta}\) by the common factor \(1/\eta\) reduces the limiting maximization to \((1-4z)(4z-h^2)^2\). Its unique unconstrained maximum occurs at \(z_\infty=(2+h^2)/12\). The difference
\[
z_\infty-L_h=\frac{(1-h)(1-2h)}6
\]
is positive exactly when \(h<1/2\). The preceding uniqueness theorem, or uniform convergence on the compact admissible interval, then gives \(z_*\to z_\infty\) for \(h<1/2\) and boundary selection otherwise. Converting back to the center yields the displayed \(c_\infty(h)\).

## Verification
The standalone file `verify.py` performs exact SymPy checks of the derivative factorization, the endpoint signs, the second derivative, the bridge integral covariance and the prior variance. It also compares closed covariance and interval-average variance identities against independently discretized double integrals of the original bridge kernel using 320-point Gauss–Legendre quadrature, and performs 259 independent integral, optimizer and phase-test comparisons. The accompanying `verification_output.txt` records a successful execution. Exact identities corroborate the corresponding proof steps; finite grids and floating-point tests do not constitute proofs of global optimality or real-parameter uniqueness. The algebraic concavity and sign argument above supplies the infinite-domain proof.

## Relationship to prior work
Xi, Briol and Girolami (2018) develop Bayesian quadrature for related integrals and the general conditional-Gaussian posterior variance formula. Foster, Lyons and Oberhauser (2019) analyze Brownian polynomial moments and optimal polynomial path approximations, including a bridge covariance expansion. Hendriks, Jidling, Wills and Schön (2018) work with Gaussian processes under line-integral observations, but focus on accurate squared-exponential kernel covariance evaluation. Travelletti, Ginsbourger and Linde (2021/2022) treat general linear-operator observations and sequential Gaussian-process designs at large scale. None of these inspected results provides this sharp fixed-width one-interval **placement** phase diagram for a Brownian-bridge signed moment. The general Gaussian conditioning formula supplies the risk expression, but not the global classification, its width/noise threshold, or the monotone location response without additional analysis.

Related public results on two iid noiseless **point** observations for Brownian-bridge ordinary integration, and on exact polynomial reconstruction from three **overlapping interval averages**, concern different objectives and measurement families. They do not imply the present one-window optimal sensor location under fixed width and noise. Related point-reading polynomial-moment designs also do not fix a spatial footprint. Earlier specialized optimal-design literature could contain a disguised equivalent formulation, so historical priority is not independently certified.

## Limitations
The noise is additive independent Gaussian with location-independent variance and the observation is exactly one normalized contiguous interval average of fixed width. The target is one specified signed polynomial moment of a standard, exactly normalized Brownian bridge. The theorem does not optimize width, number of sensors, noise-dependent sensor cost, alternative kernel smoothness, simultaneous moments, non-Gaussian priors or arbitrary nonlinear reconstructions. The optimal estimator is a conditional mean under the stated prior, not a frequentist guarantee for every deterministic path. The prior literature comparison supports a bounded originality assessment, not exhaustive publication priority.

## References
1. X. Xi, F.-X. Briol and M. Girolami, *Bayesian Quadrature for Multiple Related Integrals*, arXiv:1801.04153, first public 2018-01-12. https://arxiv.org/abs/1801.04153
2. J. Foster, T. Lyons and H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998, first public 2019-04-15. https://arxiv.org/abs/1904.06998
3. J. N. Hendriks, C. Jidling, A. Wills and T. B. Schön, *Evaluating the squared-exponential covariance function in Gaussian processes with integral observations*, arXiv:1812.07319, first public 2018-12-18. https://arxiv.org/abs/1812.07319
4. C. Travelletti, D. Ginsbourger and N. Linde, *Uncertainty Quantification and Experimental Design for Large-Scale Linear Inverse Problems under Gaussian Process Priors*, arXiv:2109.03457, first public 2021-09-08. https://arxiv.org/abs/2109.03457
5. *An exact overlap-optimal three-segment quadratic histopolation rule*, accessible public RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-an-exact-overlap-optimal-three-segment-quadratic-histopolation-r--6b64b371a801/RESULT.md
6. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, accessible public RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4/RESULT.md
