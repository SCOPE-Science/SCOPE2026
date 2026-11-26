# Unique noise-calibrated sensing time for Ornstein–Uhlenbeck quadratic energy

## Finding
For every mean-reversion strength \(\lambda>0\) and finite observation-noise variance \(\eta\ge0\), there is exactly one deterministic observation time \(x_{\lambda,\eta}\in(0,1)\) that minimizes posterior mean-square error in estimating the accumulated quadratic energy \(Q=\int_0^1 X_t^2\,dt\) of the zero-start Ornstein–Uhlenbeck diffusion \(dX_t=-\lambda X_t\,dt+dW_t\), observed through \(Y_x=X_x+\varepsilon\) with independent \(\varepsilon\sim N(0,\eta)\). The optimal time lies **strictly after the midpoint**, increases **strictly** with \(\eta\), and converges as \(\eta\to\infty\) to a unique interior time determined by a scalar transcendental equation.

Set \(q=e^{-2\lambda}\) and for \(0\le x\le1\) define
\[
V(x)=\frac{1-e^{-2\lambda x}}{2\lambda},\qquad
H(x)=\frac{2+2q-(4\lambda x+2+q)e^{-2\lambda x}-q e^{2\lambda x}}{8\lambda^3},
\]
\[
D(x)=\frac{4\lambda x+q-q e^{4\lambda x}}{4\lambda^2},\qquad
G_{\eta}(x)=(V(x)+\eta)D(x)-H(x).
\]
The **unique** zero of \(G_{\eta}\) in \((1/2,1)\) is \(x_{\lambda,\eta}\). This equation is globally unambiguous, including when \(\eta=0\). The optimal estimator is
\[
\widehat Q_x=\mathbb E Q+\frac{H(x)}{(V(x)+\eta)^2}\bigl(Y_x^2-(V(x)+\eta)\bigr),
\]
and the exact minimum mean-square error is
\[
R_{\lambda,\eta}^{*}=\frac{4\lambda+8\lambda q-5+4q+q^2}{8\lambda^4}
-2\left(\frac{H(x_{\lambda,\eta})}{V(x_{\lambda,\eta})+\eta}\right)^2.
\]
For any finite \(\eta\), the optimum lies strictly between \(1/2\) and \(x_{\lambda,\infty}\), the unique root in \((1/2,1)\) of
\[
4\lambda x=q(e^{4\lambda x}-1).
\]
In particular, no finite-noise optimum equals the last observation time or the midpoint.

## Assumptions and scope
The horizon is fixed to \([0,1]\), the scalar Ornstein–Uhlenbeck process is initialized deterministically at zero, the diffusion coefficient is one, and \(\lambda>0\) is known. Exactly one nonadaptive, scalar **value** observation is taken at a predetermined time in \([0,1]\); its Gaussian noise is independent of the driving Brownian motion and has constant known variance \(\eta\ge0\), independent of observation time. The estimator is the conditional expectation given this observation, which minimizes risk among all measurable estimators with finite second moment. The design criterion is unconditional Bayes mean-square risk for the path-integrated **square**, not pointwise trajectory reconstruction or an unknown-parameter likelihood.

At \(x=0\), the signal is deterministically zero and conveys no information; define its posterior risk to be \(\operatorname{Var}(Q)\), including for \(\eta=0\), where the displayed fraction is interpreted only for \(x>0\).

## Proof
**Gaussian covariance and energy conditioning.** The stochastic convolution
\[
X_t=\int_0^t e^{-\lambda(t-s)}\,dW_s
\]
has covariance
\[
K(t,x)=\frac{e^{-\lambda|t-x|}-e^{-\lambda(t+x)}}{2\lambda}
=\begin{cases}
 e^{-\lambda x}\sinh(\lambda t)/\lambda,&t\le x,\\
 e^{-\lambda t}\sinh(\lambda x)/\lambda,&t\ge x.
\end{cases}
\]
Its observation variance is \(v_x=V(x)+\eta\). Standard Gaussian conditioning gives
\[
\mathbb E[X_t^2\mid Y_x]=V(t)-\frac{K(t,x)^2}{v_x}+\frac{K(t,x)^2Y_x^2}{v_x^2}.
\]
Integrating yields the claimed estimator, since \(H(x)=\int_0^1K(t,x)^2\,dt\). As \(Y_x\sim N(0,v_x)\), \(\operatorname{Var}(Y_x^2)=2v_x^2\), giving
\[
\operatorname{Var}(\mathbb E[Q\mid Y_x])=2\left(H(x)/v_x\right)^2.
\]
Also \(\operatorname{Var}(Q)=2\int_0^1\!\int_0^1 K(s,t)^2\,ds\,dt=2\int_0^1H(x)\,dx\), which is exactly the stated rational-exponential expression. Thus global risk minimization is equivalent to global maximization of \(M_{\eta}(x)=H(x)/(V(x)+\eta)\).

**An exactly one-crossing derivative.** Direct integration of the displayed piecewise covariance gives the stated \(H\). Elementary differentiation gives the nonstandard identity
\[
V'(x)=e^{-2\lambda x}>0,\qquad H'(x)=V'(x)D(x),\qquad D'(x)=\frac{1-e^{4\lambda x-2\lambda}}{\lambda}.
\]
Hence
\[
M_{\eta}'(x)=\frac{V'(x)}{(V(x)+\eta)^2}\,G_{\eta}(x),\qquad
G_{\eta}'(x)=(V(x)+\eta)D'(x).
\]
Now \(G_{\eta}(0)=0\). Its derivative is strictly positive for \(0<x<1/2\), vanishes only at \(x=1/2\), and is strictly negative for \(1/2<x<1\). In particular \(G_{\eta}(1/2)>0\). At the other endpoint, \(D(1)<0\), because \(e^{2\lambda}-e^{-2\lambda}>4\lambda\), so \(G_{\eta}(1)<0\). It follows by continuity and strict decrease that \(G_{\eta}\) has exactly one zero in \((1/2,1)\). The displayed derivative of \(M_{\eta}\) is strictly positive before this zero and strictly negative after it. Also \(M_{\eta}(0)=0\) by continuity, including for \(\eta=0\). Therefore the zero is the **unique global minimizer of risk over the entire closed design interval**.

**Strict noise dependence and limiting location.** At the unique zero \(x_{\lambda,\eta}\),
\[
D(x_{\lambda,\eta})=\frac{H(x_{\lambda,\eta})}{V(x_{\lambda,\eta})+\eta}>0,
\]
while \(D'(x_{\lambda,\eta})<0\). Implicit differentiation of \(G_{\eta}(x_{\lambda,\eta})=0\) yields
\[
\frac{\partial x_{\lambda,\eta}}{\partial\eta}
=-\frac{D(x_{\lambda,\eta})}{(V(x_{\lambda,\eta})+\eta)D'(x_{\lambda,\eta})}>0.
\]
Because \(D(1/2)>0\), \(D(1)<0\), and \(D'<0\) on \((1/2,1)\), it has a unique root \(x_{\lambda,\infty}\) there. Every finite-\(\eta\) root has \(D>0\), hence lies strictly below \(x_{\lambda,\infty}\). Passing to the limit in \(G_{\eta}=0\) divided by \(\eta\), using boundedness of \(H\) and \(V\), identifies the limit uniquely as this root. Substituting the definition of \(D\) gives its stated equation.

**Brownian limiting consistency.** As \(\lambda\downarrow0\), the covariance converges to \(\min(s,t)\), while \(V(x)\to x\), \(H(x)\to x^2-2x^3/3\), and \(\operatorname{Var}(Q)\to1/3\). The limiting optimal time for finite \(\eta\) is the unique positive root
\[
4x^2+(6\eta-3)x-6\eta=0,
\quad\text{namely}\quad
x_{0,\eta}=\frac{3-6\eta+\sqrt{(6\eta-3)^2+96\eta}}8.
\]
In particular, the noiseless Brownian limit is \(3/4\), distinct from the one-site linear-integral design. This is a consistency check, not an assertion about all Ornstein–Uhlenbeck initial laws.

## Verification
The accompanying standalone `verify.py` reconstructs the piecewise covariance integrals symbolically; verifies the exact identities for \(H,H',D',\operatorname{Var}(Q)\) and the Brownian limit; independently evaluates 25 covariance-square integrals by numerical quadrature; and performs 19,932 supplementary comparisons across 12 damping values, 11 noise levels and 151 competing times per combination. The symbolic identities are algebraic checks; the actual infinite-parameter uniqueness and monotonicity proof is the preceding derivative-sign argument, not finite enumeration.

For \(\lambda=1\), the optimum is \(x_{1,0}=0.707859237041563\ldots\) without measurement noise and \(x_{1,0.2}=0.746564036859439\ldots\) with noise variance \(0.2\). With zero observation noise, the optimal risk is \(0.0241537898655\ldots\), versus \(0.0347654820915\ldots\) at midpoint sampling, a risk reduction of approximately \(30.52\%\).

Reproduction: with Python, NumPy, SciPy and SymPy installed as specified in `requirements.txt`, run `python verify.py`. No external data files are used.

## Relationship to prior work
Folia and Rattray (2017) analyze time aggregation and Kalman inference for linear Ornstein–Uhlenbeck signals and their linear time integrals; the present target is instead the *quadratic* accumulated path energy, and the goal is placement of one noisy observation. Sikolya and Baran (2018) optimize integrated pointwise prediction error and entropy for a stationary complex Ornstein–Uhlenbeck process; this is a different target, initialization and observation model. Nickelsen and Touchette (2022) examine distributions and large deviations of time-integrated Ornstein–Uhlenbeck moments, not one-shot conditional-mean optimal sensing. Palamarchuk (2020) gives asymptotic upper functions for quadratic Ornstein–Uhlenbeck integrals, rather than the claimed exact sensor design; only the abstract was accessible for this comparison.

Classical Gaussian conditioning and the zero-damping Brownian limit are not claimed as new. The proposed contribution is the complete, globally unique, all-damping-and-noise observation-placement law for the quadratic path functional, together with the strict noise monotonicity and the finite interior high-noise limiting time. Earlier equivalent formulations not found in the inspected sources remain a priority risk.

## Limitations
The finding applies only to a zero-start, scalar Ornstein–Uhlenbeck diffusion with known parameters, a unit horizon, one predetermined scalar state observation, and independent homoscedastic Gaussian noise. It does not classify optimal multiple-observation grids, unequal time-dependent noise, stationary random initial states, adaptive measurement decisions, or observation of a non-Gaussian transform. The optimal time is defined by a unique scalar root rather than by an elementary expression at general parameter values. Numerical comparisons support but do not substitute for the continuous proof. Publication novelty remains subject to external specialist review.

## References
- M. M. Folia and M. Rattray, “Trajectory inference and parameter estimation in stochastic models with temporally aggregated data,” *Statistics and Computing*, first published 24 October 2017. https://doi.org/10.1007/s11222-017-9779-x
- K. Sikolya and S. Baran, “On the optimal designs for the prediction of complex Ornstein–Uhlenbeck processes,” first public arXiv version 10 August 2018. https://arxiv.org/abs/1808.03444
- D. Nickelsen and H. Touchette, “Noise correction of large deviations with anomalous scaling,” first public arXiv version 15 February 2022. https://arxiv.org/abs/2202.07348
- E. S. Palamarchuk, “On Upper Functions for Integral Quadratic Functionals Based on Time-Varying Ornstein–Uhlenbeck Process,” published online 22 April 2020. https://doi.org/10.1137/S0040585X97T989799
